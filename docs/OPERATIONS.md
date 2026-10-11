# Forecasting and operation / 预报调度流程

[Home](../README.md) · [Model guide](../models/README.md)

1. **Historical state / 历史状态** — Load rainfall, evaporation, stage and release information; establish the reservoir and catchment state at the forecast origin.
2. **Forecast window / 预报时段** — Set the origin and forecast horizon. Interface examples and numerical tables may describe different demonstration windows.
3. **Rainfall / 预报降雨** — Enter areal rainfall by subcatchment and its distribution over forecast time steps.
4. **Outlet controls / 出库控制** — Configure prescribed discharge, prescribed level or rule-based operation. For pre-release, specify the initial state and release schedule explicitly.
5. **Compare / 对比结果** — Inspect inflow, outflow, storage and stage on a common time axis; identify drawdown and subsequent rainfall response.
6. **Save / 保存方案** — Keep input settings and outputs together so the scenario remains identifiable.

![Forecast rainfall input](../figures/forecast-rainfall-input.png)
![Pre-release workflow](../figures/pre-release-workflow.png)

| Item | Pre-release example / 预泄 | Forecast example / 预报 |
|---|---|---|
| Rainfall | 24 mm over 24 h | 100 mm areal forecast rainfall |
| Initial stage | 10.43 m | State at forecast origin |
| Outlet | Spillway release 1 m³/s | Rule-based operation |
| Output | Stage-response plot | 24 hourly comparisons within a described 72-hour window |

The 10.50 m control level shown in the configuration is a historical model setting. Application to another event requires its relevant operating conditions and initial state. This archive documents the case rather than giving a current reservoir operating instruction.

界面图来自原报告及操作手册，用于说明操作方式；通用平台界面不作为塘马某一场洪水的结果。模型工程与报告示例应按各自时间和输入设置识别。
