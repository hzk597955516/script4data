import os
import sys
import urllib.request
import pandas as pd


GPCRs = {'class_A':{'Gonadotrophin-r': 
                        {'GnRH1': ['7BR3']},
                    'Tachykinin':
                        {'NK1': ['6J21', '6E59', '6HLO', '6J20', '6HLL', '6HLP']},
                    'Bradykinin':
                        {'B1': ['7ELB'], 
                         'B2': ['7F20']},
                    'Bile_acid': 
                        {'GPBA': ['7CFM', '7BW0', '7CFN']},
                    'Orphans': 
                        {'GPR52': ['6LI0', '6LI1', '6LI3', '6LI2']},
                    'Melatonin': 
                        {'MT1': ['6PS8', '6ME3', '6ME4', '6ME5', '6ME2', '7DB6'],
                         'MT2': ['6ME7', '6ME9', '6ME8', '6ME6']},
                    'Glycoproteinh':
                        {'LH': ['7FIJ', '7FIG', '7FII', '7FIH']},
                    'Succinate': 
                        {'Succinate': ['6IBB', '6Z10', '6RNK']},
                    'Prostanoid':
                        {'TP': ['6IIU', '6IIV'], 
                         'DP2': ['6D26', '6D27', '7M8W'], 
                         'EP2': ['7CX3', '7CX4', '7CX2'],
                         'EP4': ['5YWY', '7D7M', '5YHL'],
                         'EP3': ['6M9T', '6AK3']},
                    'Ghrelin': 
                        {'Ghrelin': ['7NA8', '7F9Z', '7NA7', '6KO5', '7F9Y']},
                    'Vasopressin_and_oxytocin':
                        {'V2': ['7BB7', '7DW9', '7BB6', '7KH0'], 
                         'OT': ['6TPK']},
                    'Melanocortin':
                        {'MC4': ['6W25', '7AUE']},
                    'Cholecystokinin':
                        {'CCK2': ['7F8V', '7F8W'], 
                         'CCK1': ['7MBX', '7MBY', '7F8U', '7F8Y', '7EZM', '7EZH', '7EZK']},
                    'Formylpeptide':
                        {'FPR2_ALX': ['6LW5', '6OMM']},
                    'Opioid': 
                        {'NOP': ['5DHH', '4EA3', '5DHG'],
                         'miu': ['6DDE', '6DDF', '4DKL', '5C1M'], 
                         'k': ['6VI4', '6B73', '4DJH'],
                         'sigma': ['6PT3', '6PT2', '4RWA', '4RWD', '4EJ4', '4N6H']},
                    'Adrenoceptors':
                        {'alph_2A': ['6KUY', '6KUX'],
                         'alph_2C': ['6KUW'],
                         'alph_2B': ['6K42', '6K41'],
                         'beta_3': ['7DH5'],
                         'beta_2': ['7DHI', '6PS0', '6PS2', '6NI3', '7DHR', '6MXT', '6E67', '6PRZ', '7BZ2', '6PS5', '6PS1', '6PS3',
                                    '6PS4', '6OBA', '6PS6', '6N48', '4LDO', '4GBR', '3NY9', '2R4S', '4LDL', '3KJ6', '5X7D', '5D5B',
                                    '3P0G', '5D6L', '3D4S', '4QKX', '3NYA', '4LDE', '2R4R', '5D5A', '3NY8', '3PDS', '2RH1', '5JQH',
                                    '3SN6'], 
                         'beta_1': ['6IBL', '7BU6', '6H7L', '7B7U', '6TKO', '6H7J', '6H7N', '7BVQ', '7BTS', '7JJO', '6H7M', '5A8E',
                                    '3ZPQ', '4GPO', '2Y01', '2YCZ', '3ZPR', '4BVN', '2YCW', '2Y02', '2YCY', '4AMI', '2VT4', '5F8U',
                                    '2YCX', '2Y03', '2Y04', '2Y00', '4AMJ']},
                    'Neuropeptide_Y': 
                        {'Y2': ['7DDZ'], 
                         'Y1': ['5ZBQ', '5ZBH']},
                    'Unclassified': 
                        {'BILF1': ['7JHJ'],
                         'US28': ['5WB2', '4XT3', '4XT1', '5WB1']},
                    'Lysophospholipid':
                        {'S1P5': ['7EW1'],
                         'S1P3': ['7C4S', '7EW2', '7EW4', '7EW3'],
                         'S1P1': ['3V2W', '3V2Y']},
                    'Opsins': 
                        {'Rhodopsin': ['7MT9', '6OY9', '6QNO', '6OYA', '7MTB', '6FUF', '6PGS', '6PEL', '6PH7', '7MTA', '7MT8', '6NWE', 
                                       '6OFJ', '6I9K', '3CAP', '1U19', '3DQB', '5EN0', '6FKC', '2I36', '6FK9', '3C9L', '3PXO', '3C9M', 
                                       '4A4M', '3AYN', '6FKD', '2X72', '6FKA', '5TE5', '6FKB', '4X1H', '2I37', '6FK8', '5DGY', '5WKT', 
                                       '1F88', '6CMO', '2J4Y', '2HPY', '2ZIY', '4BEY', '5W0P', '2G87', '2I35', '4BEZ', '3PQR', '4WW3', 
                                       '3OAX', '4PXF', '6FK6', '6FK7', '5TE3', '2PED', '3AYM', '4J4Q', '1L9H', '1HZX', '4ZWJ', '1GZM',
                                       '5DYS', '2Z73']},
                    'Proteinase_activated': 
                        {'PAR2': ['5NDZ', '5NJ6', '5NDD'], 
                         'PAR1': ['3VW7']},
                    'Proteinase_activating': 
                        {'PAF': ['5ZKQ', '5ZKP']},
                    'P2Y': 
                        {'P2Y12': ['4PXZ', '4PY0', '4NTJ'],
                         'P2Y1': ['4XNV', '4XNW']},
                    'Orexin':
                        {'OX2': ['6TPG', '6TPN', '6TPJ', '5WS3', '5WQC', '4S0V', '7L1U', '7L1V'], 
                         'OX1': ['6TQ9', '6TP3', '6TP6', '6TOD', '6TOT', '6TP4', '6TOS', '6TQ6', '6T07', '6TQ4', '6TQ7', '6V9S', '4ZJC',
                                 '4ZJ8']},
                    'neurotensin':
                        {'NTS1': ['5T04', '4XES', '4BUO', '3ZEV', '4GRV', '4BWB', '4XEE', '4BV0', '6OSA', '6OS9', '7L0R', '7L0S', '6PWC',
                        '6UP7', '7L0Q', '7L0P']},
                    'acetylcholine':
                        {'m1': ['5CXV', '6ZG4', '6ZG9', '6ZFZ', '6OIJ', '6WJC'],
                         'm2': ['4MQT', '3UON', '4MQS', '5ZK8', '5ZKB', '5ZK3', '5ZKC', '6U1N', '5YC8', '6OIK'],
                         'm3': ['4U15', '4U14', '4DAJ', '4U16', '5ZHP'],
                         'm4': ['5DSG', '6KP6'],
                         'm5': ['6OL9']},
                    'Lysophospholipid': 
                        {'LPA6': ['5XSZ'],
                         'LPA1': ['4Z32', '4Z34', '4Z36']},
                    'Histamine':
                        {'H1': ['3RZE', '7DFL']},
                    'Free_fatty_acid': 
                        {'FFA1': ['5TZY', '4PHU', '5TZR', '5KW2']},
                    'Endothelin':
                        {'ETB': ['5X93', '5GLH', '5XPR', '5GLI', '6LRY', '6IGL', '6K1Q', '6IGK']},
                    'Dopamine': 
                        {'D1': ['7CKZ', '7CRH', '7JOZ', '7JVP', '7LJC', '7JVQ', '7CKW', '7JV5', '7CKX', '7LJD', '7CKY'],
                         'D4': ['5WIV', '5WIU', '6IQL'], 
                         'D3': ['3PBL', '7CMV', '7CMU'],
                         'D2': ['7JVR', '6VMS', '7DFP', '6LUQ', '6CM4']},
                    'Chemokini': 
                        {'CCR7': ['6QZH'], 
                         'CCR6': ['6WWZ'], 
                         'CXCR2': ['6LFO', '6LFL', '6LFM'], 
                         'CXCR4': ['3ODU', '3OE9', '3OE0', '3OE8', '3OE6', '4RWS'], 
                         'CCR9': ['5LWE'],
                         'CCR5': ['5UIW', '4MBS', '6AKY', '7F1R', '7F1S', '6AKX', '6MET', '7O7F', '6MEO', '7F1Q', '7F1T'],
                         'CCR2': ['5T1A', '6GPS', '6GPX']},
                    'Cannabinoid':
                        {'CB2': ['5ZTY', '6PT0', '6KPC', '6KPF'],
                         'CB1': ['5XRA', '5TGZ', '5XR8', '5U09', '6KQI', '6N4B', '6KPG']},
                    'Complement':
                        {'C5a1': ['509H', '6C1R', '6C1Q']},
                    'Leukotriene':
                        {'CysLT2': ['6RZ9', '6RZ7', '6RZ6', '6RZ8'],
                         'CysLT1': ['6RZ4', '6RZ5'],
                         'BLT1': ['5X33', '7K15']},
                    'Angiotensin':
                        {'AT2': ['5UNH', '6JOD', '5UNG', '7C6A', '5XJM', '5UNF'],
                         'AT1': ['4ZUD', '4YAY', '6OS1', '6DO1', '6OS0', '6OS2']},
                    'Apelin': 
                        {'Apelin': ['5VBL', '6KNM']},
                    'Adenosine': 
                        {'A2A': ['5G53', '4UHR', '3VG9', '5IU8', '3UZC', '5IUB', '5K2C', '5N2R', '5OLO', '5VRA', '4EIY', '6AQF', '5OLH', 
                                 '2YDV', '3REY', '5MZJ', '5MZP', '2YDO', '5JTB', '5IUA', '3VGA', '3EML', '5K2B', '3UZA', '6GDG', '5IU4', 
                                 '5WF5', '3QAK', '5OLV', '3PWH', '5NLX', '5OM1', '5WF6', '5K2A', '5OLG', '5UVI', '5UIG', '3RFM', '5NM2', 
                                 '4UG2', '5OLZ', '5NM4', '5OM4', '5K2D', '5IU7', '6LPL', '6MH8', '6ZDV', '6GT3', '7RM5', '6S0Q', '6WQA', 
                                 '6ZDR', '6JZH', '6LPJ', '7ARO', '6S0L', '6PS7', '6LPK'],
                        'A1': ['5UEN', '6D9H', '5N2S', '7LD3', '7LD4']},
                    '5Hydroxytryptamine': 
                        {'5_HT1F': ['7EXD'],
                         '5_HT1A': ['7E2Z', '7E2Y', '7E2X'],
                         '5_HT1D': ['7E32'],
                         '5_HT2A': ['6A93', '6WH4', '6A94', '6WHA', '6WGT'],
                         '5_HT1E': ['7E33'],
                         '5_HT2C': ['6BQH', '6BQG'],
                         '5_HT2B': ['5TUD', '4IB4', '4NC3', '5TVN', '6DRZ', '6DRX', '6DRY', '6DS0'],
                         '5_HT1B': ['6G79', '4IAQ', '5V54', '4IAR', '7C61'],
                         }
                    },
        'Class_B1': {'Corticotropin':
                        {'CRF1': ['6P9X', '6PB0', '4K5Y', '4Z9G'],
                         'CRF2': ['6PB1']},
                    'Calcitonin': 
                        {'CT': ['5UZ7', '6NIY'],
                         'Calcitonin_like': ['6UVA', '6E3Y', '6UUS', '6UUN', '7KNU', '7KNT']},
                    'Glucagon_family': 
                        {'GLP_1': ['6KJV', '7LCI', '7LCJ', '6KK7', '6LN2', '6X18', '7KI1', '7LCK', '7DUQ', '6XOX', '7KI0', '7E14', '5VEW', 
                                   '5VAI', '6B3J', '5VEX', '7RTB', '6KK1', '6X19', '6X1A', '6VCB', '6ORV', '7EVM', '7DUR', '7C2E', '5NX2'],
                         'Glucagon': ['6LMK', '6WHC', '6LML', '6WPW', '5EE7', '5XF1', '5YQZ', '4L6R', '5XEZ'],
                         'Secretin': ['6WI9', '7D3S', '6WZG'],
                         'GHRH': ['7CZ5'],
                         'GLP_2': ['7D68'],
                         'GIP': ['7DTY']},
                    'Parathyroid_h':
                        {'PTH1': ['6NBH', '6NBI', '6FJ3', '6NBF'],
                         'PTH2': ['7F16']},
                    'VIP_and_PACAP':
                        {'PAC1': ['6M1H', '6M1I', '6LPB', '6P9Y'],
                         'VPAC1': ['6VN7']}
                    },
        'Class_B2': {'ADGRG': 
                        {'ADGRG': ['7D76', '7D77']}
                    },
        'Class_C': {'Metabotropic_glutamate': 
                        {'mGlu1': ['7DGD', '7DGE', '4OR2'],
                         'mGlu5': ['6N51', '7P2L', '7FD8', '6N52', '7FD9', '5CGD', '6FFH', '6FFI', '5CGC', '4OO9'],
                         'mGlu4': ['7E9H'], 
                         'mGlu2': ['7MTQ', '7E9G', '7EPD', '7EPF', '7EPA', '7EPE', '7EPB', '7MTR', '7MTS'],
                         'mGlu7': ['7EPC']},
                    'GABAB': 
                        {'GABAB2': ['6WIV', '7EB2', '7CUM', '7CA3', '6VJM', '7CA5', '6UOA', '6UO8', '7C7Q', '7C7S', '6W2X', '6UO9'],
                         'GABAB1': ['6W2Y']}, 
                    'Calcium_sens':
                        {'Cas': ['7DD5', '7M3E', '7DTW', '7E6U', '7E6T', '7M3J', '7DTV', '7M3G', '7DTT', '7M3F', '7DD6', '7DD7', '7DTU']}
                    },
        'Class_D1': {'STE2': 
                        {'STE2': ['7AD3']}
                    },
        'Class_F': {'Frizzled':
                        {'SMO': ['6OT0', '6O3C', '6XBJ', '6XBL', '6XBK', '6XBM', '6D32', '6D35', '4O9R', '4N4W', '4QIN', '4QIM', '5V57', 
                                 '4JKV', '5V56', '5L7I', '5L7D'],
                         'FZD4': ['6BD4'], 
                         'FZD5': ['6WW2'], 
                         'FZD7': ['7EVW']}
                    }
        }


def count(pids):
    if isinstance(pids, list):
        return list(pids)
    else:
        n = []
        for _, value in pids.items():
            n += count(value)
        return n
    

def mkdir(path):
    folder = os.path.exists(path)

    if not folder:                   
        os.makedirs(path)            
        print ("---  new folder...  ---")
        print ("---  OK  ---")

    else:
        print ("---  There is this folder!  ---")

def downloadfasta(PID, path):
    fname = path + '\\' + 'rcsb_pdb_' + PID + '.fasta'
    try:
        if 'rcsb_pdb_' + PID + '.fasta' in os.listdir(path):
            print("---{} already exists !---".format(PID))
            return
        
        f = urllib.request.urlopen("https://www.rcsb.org/fasta/entry/" + PID)
        fname = path + '\\' + 'rcsb_pdb_' + PID + '.fasta'
        with open(fname, "wb") as g:
            g.write(f.read())

    except Exception as e:
        print("---Error occurs when downloading {}---".format(fname))

    print("---{} download completed !---".format(PID))


def down_fastas(PIDs, path):
    mkdir(path)

    for PID in PIDs:
        if len(PID) == 4:
            downloadfasta(PID=PID, path=path)


def down_all(PIDs, root='.\\GPCRs'):
    if isinstance(PIDs, list):
        down_fastas(PIDs, root)
    else:
        for key, values in PIDs.items():
            down_all(values, root + '\\' + key)

    print('---' + root + ' is Ok !---')

def check(s1, s2):
    return 0
if __name__=="__main__":
    # down_all(GPCRs)
    data = pd.read_csv('./all_gpcr_pdb_info.csv')
    other_pids = list(data['pdb_code'])
    down_all(other_pids, '.\\GPCR')