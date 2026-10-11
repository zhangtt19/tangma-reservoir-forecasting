# Tangma Reservoir: Inflow Reconstruction, Forecasting and Operations

**A catchment–reservoir modelling case linking sparse observations to rainfall–runoff simulation, reservoir levels and pre-release scenarios.**

[中文](README.zh-CN.md) · [Methods and parameters](docs/METHODS.md) · [Results](docs/RESULTS.md) · [All figures](docs/FIGURES.md) · [Model archive](models/README.md)

![Three subcatchments upstream of Tangma Reservoir](figures/subcatchment-map.png)

## Engineering question

How can reservoir inflow and future water levels be estimated when direct inflow measurements are unavailable? This case combines reservoir levels, stage–storage relationships, outlet records, rainfall and terrain to build a connected hydrological and reservoir model for Tangma Reservoir, Liyang, China.

My work covers hydrological data preparation, inflow reconstruction, catchment delineation, model configuration and calibration, historical comparisons, and forecasting and operation scenarios.

## From observations to decisions

1. Reconstruct historical inflow from changes in reservoir storage and recorded releases.
2. Delineate three subcatchments and calculate areal rainfall using rain-gauge weights.
3. Configure a three-source Xin'anjiang rainfall–runoff model and river routing.
4. Couple catchment inflow to a lumped reservoir water-balance model.
5. Examine inflow and level responses, then apply forecast rainfall and release settings.

| Component | Case configuration |
|---|---|
| Modelled catchment | 39.78 km²; documented area 39.9 km² |
| Subcatchments | 11.84, 15.06 and 12.88 km² |
| Rain gauges | Tangma, Dongmenba, Huoshaoba and Dashankou |
| Historical data period | 2016–2022 |
| Model chain | Three-source Xin'anjiang → Muskingum routing → lumped reservoir |
| Main inputs | Rainfall, evaporation, terrain, reservoir stage, storage curve and outlet information |
| Application | Historical simulation, rainfall forecasting scenarios and pre-release assessment |

## Historical results

![2016 simulated inflow and reconstructed reference](figures/inflow-2016.png)

The original result set includes inflow comparisons for **2016, 2020, 2021 and 2022**, together with selected reservoir-level comparison periods. The reference inflow is reconstructed from the water balance; the plotted reference uses the source workbook's moving average. It is not a directly measured inflow hydrograph.

The comparisons capture seasonal inflow patterns and reveal event- and month-specific differences. The [results page](docs/RESULTS.md) presents selected original table entries and all four years of plots, with their evaluation scope.

## Forecasting and pre-release

![Original pre-release scenario](figures/pre-release-result.png)

A documented pre-release example combines **24 mm rainfall over 24 hours**, initial stage **10.43 m**, and spillway release **1 m³/s**. The original plot shows the simulated drawdown and subsequent response. The [operation guide](docs/OPERATIONS.md) connects forecast timing, rainfall and release settings.

A separate forecasting example reports water-level differences of **0.02–0.09 m for the 24 listed hourly records**. These are case-specific results, not an accuracy guarantee for other events or the full 72-hour scenario horizon.

## Materials

- [Methods, input construction and all 18 parameter settings](docs/METHODS.md)
- [Original results and interpretation](docs/RESULTS.md)
- [Maps, model setup, result plots and operation screenshots](docs/FIGURES.md)
- [CSV tables and data definitions](data/README.md)
- [Native model project and data excerpts](models/README.md)

Study and modelling: **Tianshu Zhang**. Running the native project requires a compatible TBM/BDS modelling environment.

## Data availability / 数据公开范围

The native model project is included. **Hydrological inputs and numerical results are excerpts only**: 1–3 July 2016 rainfall and stage records, 27 June–10 July 2016 daily inflow comparisons, and 24 hourly forecast comparisons. Complete historical input and saved-result archives are excluded. These excerpts illustrate the workflow and do not provide all inputs needed to rerun historical scenarios. See [sample definitions](data/README.md).

提供原始模型工程。**水文输入与数值计算结果仅提供片段**：2016年7月1—3日水位与雨量记录、2016年6月27日—7月10日日入流对比，以及24条逐时预报对比。完整输入和已保存结果归档未公开；片段用于说明数据结构和分析过程，不足以重新运行全部历史情景。
