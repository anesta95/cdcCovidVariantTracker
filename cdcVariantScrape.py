from tableauscraper import TableauScraper as TS
import pandas as pd

# url = "https://public.tableau.com/views/Variant_Proportions_Plus_Nowcasting/RegionsDashboard?:language=en&:display_count=y&:embed=y&:showVizHome=no"
# ts = TS()
# ts.loads(url)

# ws = ts.getWorksheet("3-Map US Regions")

# rawCDCDF = ws.data

rawCDCDF = pd.read_csv("./3-Map US Regions.csv", header=0)

filteredCDCDF = rawCDCDF.loc[rawCDCDF['Lineage Bin'] == "VOC"].reset_index()

pivotCDCDF = filteredCDCDF.loc[:, ["Hhs Region", "Variant", "Share_pct"]].pivot(
    index = "Hhs Region",
    columns = "Variant",
    values = "Share_pct")

# numericCDCDF = pivotCDCDF.apply(lambda x: pd.to_numeric(x.str.replace('%', '')), axis=0)

numericCDCDF = pivotCDCDF.apply(lambda x: x * 100, axis=0)

numericCDCDF['Value'] = numericCDCDF.sum(axis=1)

pctCDCDF = numericCDCDF.apply(lambda x: round(x).astype(str) + '%')

pctCDCDF['ID'] = pd.to_numeric(pctCDCDF.index)

pctCDCDF['ID'] = pctCDCDF['ID'].apply(int)


cdcVariant = pctCDCDF.sort_values(
    by=['ID']).reset_index()

cdcVariant['ID'] = 'Region ' + cdcVariant['ID'].astype(str)

cdcVariant.drop("Hhs Region",
    axis=1, inplace=True)


cdcVariant.to_csv("cdcVariantData.csv", index=False)


