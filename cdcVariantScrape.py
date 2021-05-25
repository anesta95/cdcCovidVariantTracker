#! C:\Users\anesta\.virtualenvs\Verywell_Covid_Variant_Viz-SnP8VGBw\Scripts\python.exe
from tableauscraper import TableauScraper as TS
import pandas as pd

url = "https://public.tableau.com/views/Variant_Proportions_Plus_Nowcasting/RegionsDashboard?:language=en&:display_count=y&:embed=y&:showVizHome=no"

ts = TS()
ts.loads(url)

ws = ts.getWorksheet("3-Map US Regions")

rawCDCDF = ws.data

filteredCDCDF = rawCDCDF.loc[rawCDCDF['Lineage Bin-alias'] == "VOC"].reset_index()

pivotCDCDF = filteredCDCDF.loc[:, ["ATTR(Hhs Region)-alias", "Variant-alias", "ATTR(Share)-alias"]].pivot(
    index = "ATTR(Hhs Region)-alias",
    columns = "Variant-alias",
    values = "ATTR(Share)-alias")

numericCDCDF = pivotCDCDF.apply(lambda x: pd.to_numeric(x))

numericCDCDF['Value'] = numericCDCDF.sum(axis=1)

pctCDCDF = numericCDCDF.apply(lambda x: (round(x * 100, 2)).astype(str) + '%')

pctCDCDF['ID'] = pd.to_numeric(pctCDCDF.index)

cdcVariant = pctCDCDF.sort_values(
    by=['ID']).reset_index()

cdcVariant['ID'] = 'Region ' + cdcVariant['ID'].astype(str)

cdcVariant.drop("ATTR(Hhs Region)-alias",
    axis=1, inplace=True)

cdcVariant.to_csv("cdcVariantData.csv", index=False)


