# Results / 原始结果与解释

[Home](../README.md) · [Gallery](FIGURES.md) · [Data definitions](../data/README.md)

Original figures are retained. Numerical tables and downloadable series are **excerpts only**. 原始成果图保留；数值表格及可下载序列仅为片段。

## Inflow hydrographs / 入流过程

Four original report plots. The reference curve is reconstructed inflow with the plotting workbook's five-record moving average, rather than direct inflow measurements. Original legends are retained.

以下四张为原始成果图，参考线为反推入流的滑动平均序列。原图标题、图例和数值均保留。

### 2016

![2016 inflow](../figures/inflow-2016.png)

### 2020

![2020 inflow](../figures/inflow-2020.png)

### 2021

![2021 inflow](../figures/inflow-2021.png)

### 2022

![2022 inflow](../figures/inflow-2022.png)

## Monthly comparison excerpt / 月尺度对比节选

| Year | May | June | July | August | September |
|---|---:|---:|---:|---:|---:|
| 2016 | 1% | -2% | 16% | 12% | -26% |

These rounded signed differences come from Table 4-6 (2016 excerpt). The workbook aggregates daily discharge by summation, not by monthly mean or peak. Multiplication by the common daily interval converts accumulated discharge into volume, leaving its relative difference unchanged. Values above are transcribed from the report, not a new evaluation.

月表反映累计来水量的相对偏差，而非洪峰误差。不同月份有差异，不能概括为全部月份均在±20%以内。报告与保存的绘图工作簿存在版本差别，例如2016年8月的参考汇总值不同；本页以报告表为准，公开的日序列片段保留工作簿原值，二者不混算。[数据说明](../data/README.md)记录各表出处。

## Event runoff depth excerpts / 事件径流深节选

| Event | Rainfall (mm) | Reconstructed depth (mm) | Simulated depth (mm) | Reported relative error |
|---|---:|---:|---:|---:|
| 20160703 | 102.92 | 122.31 | 54.96 | 55.06% |
| 20170610 | 129.93 | 77.74 | 62.26 | 19.9% |


The event table uses unsigned relative runoff-depth errors. Monthly values use signed differences and a different aggregation window. Antecedent wetness and rainfall concentration are relevant to runoff response. Only two event rows are excerpted here; the full numerical event-results archive is not included.

## Reservoir-level windows / 典型水位过程

These original figures cover selected periods in each year, not every annual stage observation. Reservoir levels reflect both catchment inflow and outlet operation.

### 2016

![2016 reservoir level](../figures/stage-2016.png)

### 2020

![2020 reservoir level](../figures/stage-2020.png)

### 2021

![2021 reservoir level](../figures/stage-2021.png)

### 2022

![2022 reservoir level](../figures/stage-2022.png)

## Pre-release / 预泄

![Original pre-release result](../figures/pre-release-result.png)

Settings: 24 mm rainfall over 24 h, initial stage 10.43 m, spillway discharge 1 m³/s. The plot illustrates drawdown and subsequent rainfall response; it does not compare multiple optimised release schedules.

## Forecasting example / 预报示例

The report describes a 72-hour window from 1 to 4 April 2022, 100 mm areal forecast rainfall and rule-based operation. Its numerical comparison lists only 24 hours, from 01:00 on 1 April to 00:00 on 2 April. Listed observed stages are 10.43–10.44 m, forecasts 10.45–10.53 m and differences 0.02–0.09 m.

[24-hour result excerpt](../data/forecast-results-excerpt-24h.csv). These records support a statement about the listed hours only, rather than 72-hour accuracy across events or a statistical confidence interval.

原报告的72小时预报设置与24小时结果表分别保留其范围。预报与预泄采用不同降雨设置，不应合并为同一个情景。
