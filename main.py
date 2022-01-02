import pandas, sys,os

if len(sys.argv) == 1:
    print("Usage: ", sys.argv[0], "INPUT_CSV_FILE")
    print("Aucun fichier spécifié en argument")
    exit(1)

if not os.path.isfile(sys.argv[1]):
    print("Le fichier", sys.argv[1], "n'existe pas")
    exit(1)

input_file = sys.argv[1]
madataframe = pandas.read_csv(input_file, encoding="cp1252", delimiter=";")
madataframe["payment"] = ""
madataframe.loc[madataframe["label"].str.contains("VIR"), ["payment"]] = 4
madataframe.loc[madataframe["label"].str.contains("CB"), ["payment"]] = 6
madataframe.loc[madataframe["label"].str.contains("CARTE"), ["payment"]] = 6
madataframe.loc[madataframe["label"].str.contains("PRLV SEPA"), ["payment"]] = 11
madataframe["info"] = madataframe["label"]
madataframe = madataframe.drop(columns="dateVal")
madataframe = madataframe.drop(columns="categoryParent")
madataframe = madataframe.drop(columns="accountbalance")
madataframe = madataframe.drop(columns="accountNum")
madataframe = madataframe.drop(columns="accountLabel")
madataframe = madataframe.rename(columns={"dateOp": "date"})
madataframe["memo"] = ""
madataframe["tags"] = ""
madataframe["payee"] = ""
madataframe = madataframe[["date", "payment", "info", "payee", "memo", "amount", "category", "tags"]]
output_file = input_file + "_converted.csv"
madataframe.to_csv(output_file, index=False, quoting=None, sep=";")
print("Fichier converti avec succès!")
exit(0)