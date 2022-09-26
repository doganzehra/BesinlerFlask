import pandas as pd
import numpy as np
from itertools import permutations
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


def getAprioriResult(hastalikAdi):
    hastalikAdi = hastalikAdi+".csv"
    df = pd.read_csv(hastalikAdi, sep=';', header=None)
    df['Transactions'] = df.values.tolist()
    df['Transactions'] = df['Transactions'].apply(
        lambda x: [i for i in x if str(i) != "nan"])
    transactions = list(df['Transactions'])
    unique_items = [
        item for transaction in transactions for item in transaction]
    unique_item_list = list(set(unique_items))
    rules = list(permutations(unique_item_list, 2))
    encoder = TransactionEncoder().fit(transactions)
    onehot = encoder.transform(transactions)
    onehot = pd.DataFrame(onehot, columns=encoder.columns_)
    onehot['zerdecal_&_domates'] = np.logical_and(
        onehot['zerdecal'], onehot['domates'])
    onehot = onehot.drop('zerdecal_&_domates', axis=1)
    sup_zerdecal_domates = np.logical_and(
        onehot['zerdecal'], onehot['domates']).mean()
    sup_zerdecal = onehot['zerdecal'].mean()
    sup_domates = onehot['domates'].mean()
    conf_zerdecal_to_domates = sup_zerdecal_domates / sup_zerdecal
    lift_zerdecal_to_domates = conf_zerdecal_to_domates/sup_domates
    frequent_itemsets = apriori(
        onehot, min_support=0.0005, max_len=4, use_colnames=True)
    Rules = association_rules(
        frequent_itemsets, metric="support", min_threshold=0.005)
    filtered_rules = Rules[(Rules['antecedent support'] > 0.01) & (
        Rules['support'] > 0.009) & (Rules['lift'] > 1.00)]
    myList = list(zip(filtered_rules.head(20).antecedents,
                      filtered_rules.head(20).consequents))

    return resultsToDict(myList)


def resultsToDict(myList):
    adict = {}
    for value in myList:
        str1 = ""
        str2 = ""
        # traverse in the string
        for ele in list(frozenset(value[0])):
            str1 += ele
        for ele in list(frozenset(value[1])):
            str2 += ele
        adict[str1] = str2
        str1 = ""
        str2 = ""
    return adict
