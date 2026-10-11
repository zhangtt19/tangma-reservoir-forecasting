# Data excerpts / 数据片段

**Hydrological time series and numerical results here are excerpts, not the complete project dataset. 水文输入与计算结果均为片段，并非完整资料。**

| File | Scope and units |
|---|---|
| [Stage input excerpt](stage-input-excerpt-20160701-03.csv) | Tangma Reservoir, 1–3 July 2016, stage in m; source timestamps retained |
| [Rainfall input excerpt](rainfall-input-excerpt-20160701-03.csv) | Dashankou gauge, 1–3 July 2016, recorded amounts in mm; irregular timestamps retained |
| [Inflow result excerpt](inflow-results-excerpt-20160627-0710.csv) | 14 daily records, 27 June–10 July 2016; simulated, reconstructed and moving-average reference flow in m³/s |
| [Forecast result excerpt](forecast-results-excerpt-24h.csv) | 24 hourly records, 1 April 2022 01:00–2 April 2022 00:00; observed/forecast stages and differences in m |
| [Model parameters](model-parameters.csv) | All 18 reported model settings; configuration rather than a time series |
| [Subcatchments](subcatchments.csv) | Three subcatchments and areas in km² |

## Sources and handling / 来源与处理

Stage: `塘马水库2016年水位.txt`. Rainfall: `大山口2016.txt`. Values and timestamps are copied without interpolation, resampling or gap filling. Rainfall amounts at source timestamps are not inferred hourly intensities. Missing timestamps are not assigned zero rainfall. Local source time is retained without timezone conversion. Stage uses the original project datum.

水位与降雨保留原始时间戳和数值，没有插值、补零或重采样。不规则雨量记录不能直接当作等间隔雨强；缺少记录不自动代表无雨。水位保留工程原高程基准。

Inflow: `流量率定-画图.xlsx`, sheet `16`, columns A (date), B (simulation), C (reconstructed reference), F (cached moving-average reference). The moving average is copied from the workbook and can depend on records outside the excerpt. Blank cells remain missing; reconstructed inflow is not direct discharge measurement. No metrics are calculated from this short window.

Forecast: V4 report's 24-row forecast comparison table, within its described 72-hour scenario. This excerpt does not establish accuracy for the unlisted 48 hours or other events. Model configuration CSVs are transcribed from the V4 report.

The input excerpts, daily historical comparison and forecast example have distinct time windows and purposes; they are not a single ready-to-run input/output pair. Full historical input and saved output files are excluded. Compatible modelling software and complete scenario inputs are needed for full reruns.

输入片段、日入流对比与预报示例属于不同时间范围，不能拼接为同一次模拟。这里提供数据结构和成果阅读示例，不提供历史重算所需的全部序列。
