# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 23:20:34 2021

@author: danie
 
in questo programma prenso program02 e modifico il controllo debito

"""



def ex1(acn1, acn2, acn3, imd_acn1, imd_acn2, init_amount, transact_log):
# =============================================================================
# CONTO è un registro che inizializza gli utenti e le i rispettivi conti
# =============================================================================
    conto = {acn1: init_amount, acn2: init_amount, acn3: init_amount, imd_acn1: 0, imd_acn2:0} 
    
# =============================================================================
# DEBITI è un registro nel quale verranno accumulati i debiti degli utenti nei 
# confronti degli intermediari                                                                                                      
# =============================================================================
    registro_debiti = {imd_acn1:{acn1:0, acn2:0, acn3:0}, imd_acn2: {acn1:0, acn2:0, acn3:0}}
    
    # per ogni transazione in transazioni                 
    for transazione in transact_log:                                           
        mittente = transazione[0][0]
        destinatario = transazione[0][1]
        importo = transazione[1]
        percentualePerIntermediario = int(importo * (transazione[3] / 100))
        # se intermediario1 è nella transazione
        if imd_acn1 in transazione:
            # esegui l'operazione                                                               
            operazione(imd_acn1, conto, mittente, destinatario, importo, percentualePerIntermediario, registro_debiti)
            controlloDebito(registro_debiti, conto, mittente, imd_acn1, imd_acn2)
            controlloDebito(registro_debiti, conto, destinatario, imd_acn1, imd_acn2)
            continue
        # altrimenti intermediario2
        else:
            #esegui l'operazione
            operazione(imd_acn2, conto, mittente, destinatario, importo, percentualePerIntermediario, registro_debiti)     
            controlloDebito(registro_debiti, conto, mittente, imd_acn2, imd_acn1)
            controlloDebito(registro_debiti, conto, destinatario, imd_acn1, imd_acn2)
            continue
    
    return [int(conto[acn1]), int(conto[acn2]), int(conto[acn3])], [int(conto[imd_acn1]), int(conto[imd_acn2])], [list(registro_debiti[imd_acn1].values()), list(registro_debiti[imd_acn2].values())]



def operazione(intermediarioA, conto, mittente, destinatario, importo, percentualePerIntermediario, registro_debiti):
    
    # intermediarioA è il principare intermediario chiamato ad effettuare la transazione
    # se il mittente può pagare la percentuale e l'importo
    if conto[mittente] >= (percentualePerIntermediario + importo):
        # aggiorno il conto dellìintermediario aggiungendo la percentuale che gli spetta
        conto[intermediarioA] += (percentualePerIntermediario)
        # sottraggo al mittente gli importi che deve pagare
        conto[mittente] -= (percentualePerIntermediario + importo)
        # aggiungo al destinatario l'importo da trasferire
        conto[destinatario] += importo
        return
    # se il mittente non può pagare la transazione 
    else: 
        # questo controllo è ridondante eliminalo appena puoi
        # se il mittente ha i fondi necessari per pagare la percentuale intermediario
        if conto[mittente] >=  percentualePerIntermediario:
            # aggiorno il conto dell'intermediario con la percentuale 
            conto[intermediarioA] += percentualePerIntermediario
            # sottraggo al mittente SOLO la percentuale 
            conto[mittente] -= percentualePerIntermediario 
            return
        # se il mittente NON può pagare nemmeno la percentuale 
        else:
            # passo tutti i fondi del mittente all'intermediario
            conto[intermediarioA] += conto[mittente]
            # azzero il conto del mittente
            registro_debiti[intermediarioA][mittente] = conto[mittente] - percentualePerIntermediario
            # registro il debito del mittente 
            conto[mittente] -= conto[mittente]
            return
    

    


def controlloDebito(debito, conto, utente , intermediario1, intermediario2):    
    # nessun debito
    a1 = debito[intermediario1][utente]     # valore debito utente intermediario1
    b1 = debito[intermediario2][utente]     # valore debito utente intermediario2
    c1 = debito[intermediario1]             # conto debito intermediario1
    d1 = debito[intermediario2]             # conto debito intermediario2
    # se non ci sono debiti
    if (a1 == 0 ) and (b1 == 0):        # se conto sta a 0 non continuare
        return
    elif conto[utente] == 0:
        return
    # controllo se ha debiti con entrambi
    elif (a1 < 0)==True and (b1 < 0)== True:
        # se si controllo con chi è maggiore
        operazioneDebito(c1, d1, utente, intermediario1, intermediario2, conto)
        return
    # debito solo con intermediario1
    elif (a1 < 0 ) and (b1 == 0 ):
        # se può estinguerlo tutto il debito
        if conto[utente] > abs(a1):
            conto[utente] += debito[intermediario1][utente]
            conto[intermediario1] += abs(debito[intermediario1][utente])
            debito[intermediario1][utente] -= debito[intermediario1][utente]
        else:
            debito[intermediario1][utente] += conto[utente]
            conto[intermediario1] += conto[utente]
            conto[utente] -= conto[utente]
    # debito solo con intermediario2
    elif (b1 < 0 ) and (a1 == 0 ) :
        if conto[utente] >= abs(b1):
            conto[utente] += debito[intermediario2][utente]
            conto[intermediario2] += abs(debito[intermediario2][utente])
            debito[intermediario2][utente] -= debito[intermediario2][utente]
        else:
            debito[intermediario2][utente] += conto[utente]
            conto[intermediario2] += conto[utente]
            conto[utente] -= conto[utente]
    # controllo il debitore
    else:
        return
        
        


def operazioneDebito(debitoIntermediario1, debitoIntermediario2, utente, intermediario1, intermediario2, conto):
    # controllo su chi effettuo il recupero del debito
    # il debitointermediario1 è maggiore 
    if debitoIntermediario1[utente] < debitoIntermediario2[utente]:
        # se il mittente ha fondi a sufficienza per estinguere il debito 
        if abs(debitoIntermediario1[utente]) < conto[utente]:
            # aggiorna conto dell'intermediario
            conto[intermediario1] += abs(debitoIntermediario1[utente])
            # detraggo il debito dal conto del mittente
            conto[utente] += debitoIntermediario1[utente]
            # azzero il debito del mittente
            debitoIntermediario1[utente] -= debitoIntermediario1[utente]  
            # controlo se con i soldi che avanzano al mittente posso pagare una parte del debito con l'altro intermediario
            if conto[utente] > 0 and conto[utente] >= abs(debitoIntermediario2[utente]):
                conto[intermediario2] += abs(debitoIntermediario2[utente])
                conto[utente] += debitoIntermediario2[utente]
                debitoIntermediario2[utente] -= debitoIntermediario2[utente]
            else:
                conto[intermediario2] += abs(debitoIntermediario2[utente])
                debitoIntermediario2[utente] += conto[utente]
                conto[utente] -= conto[utente]    
        # se i fondi del mittente non bastano li azzero e mando tutto al debito  
        else:
            conto[intermediario1] += abs(debitoIntermediario1[utente])
            debitoIntermediario1[utente] += conto[utente]
            conto[utente] -= conto[utente]    
    # il deditointermediario2 è maggiore   
    else:
        # se il mittente ha fondi a sufficienza per estinguere il debito 
        if abs(debitoIntermediario2[utente]) <= conto[utente]:
            # aggiorna conto dell'intermediario
            conto[intermediario2] += abs(debitoIntermediario2[utente])
            # detraggo il debito dal conto del mittente
            conto[utente] += debitoIntermediario2[utente]
            # azzero il debito del mittente
            debitoIntermediario2[utente] -= debitoIntermediario2[utente]  
            # controlo se con i soldi che avanzano al mittente posso pagare una parte del debito con l'altro intermediario
            if conto[utente] > 0 and conto[utente] >= abs(debitoIntermediario1[utente]):
                conto[intermediario1] += abs(debitoIntermediario1[utente])
                conto[utente] += debitoIntermediario1[utente]
                debitoIntermediario1[utente] -= debitoIntermediario1[utente]
            else:
                conto[intermediario1] += abs(debitoIntermediario1[utente])
                debitoIntermediario1[utente] += conto[utente]
                conto[utente] -= conto[utente]    
        # se i fondi del mittente non bastano li azzero e mando tutto al debito  
        else:
            conto[intermediario2] += abs(debitoIntermediario2[utente])
            debitoIntermediario2[utente] += conto[utente]
            conto[utente] -= conto[utente]
           

        
    


if __name__ == '__main__':
    # Insert your own tests here
    
    acn1 = 0xA1
    acn2 = 0xD0
    acn3 = 0x52F
    imd_acn1 = 0x108
    imd_acn2 = 0x2A9
    init_amount = 2000
    transact_log = \
            [((acn1, acn2), 4000, imd_acn1,100),
             ((acn2, acn1), 5000, imd_acn1,100),
             ((acn3, acn2), 6000, imd_acn1,50)
             ]
    ciao_ciao = ex1(acn1,acn2,acn3,imd_acn1,imd_acn2,init_amount,transact_log)    
    
    print(ciao_ciao)
    pass

