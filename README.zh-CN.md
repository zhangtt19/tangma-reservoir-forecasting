# 塘马水库：入流反推、洪水预报与调度模拟

**在缺少直接入库流量观测的条件下，将水文资料、流域产汇流模型和水库调度连接起来。**

[English](README.md) · [方法与参数](docs/METHODS.md) · [成果展示](docs/RESULTS.md) · [全部图件](docs/FIGURES.md) · [工程文件](models/README.md)

![塘马水库上游三个子流域](figures/subcatchment-map.png)

## 研究问题

没有入库流量站，如何建立上游降雨与水库水位之间的联系，并分析预报降雨条件下的水位变化？本项目以溧阳塘马水库为案例，利用水位、库容关系、出库记录、降雨和地形资料，构建流域产汇流与水库水量平衡耦合模型。

我完成的工作包括水文资料整理、入库流量反推、子流域划分、模型配置与率定、历史过程对比，以及预报和调度情景分析。

## 技术路线

1. **重建入流参考序列**：将水位换算为库容，结合时段出库量反推入库流量。
2. **建立空间结构**：依据地形划分三个子流域，按雨量站覆盖情况计算面雨量。
3. **率定上游模型**：配置三水源新安江模型与河道汇流参数，比较模拟入流和反推入流。
4. **耦合水库模型**：将上游来水输入零维水库模型，计算库容与水位变化。
5. **分析运行情景**：设置预报降雨、初始水位与泄流条件，检查水位响应和预泄效果。

| 项目 | 设置 |
|---|---|
| 模型集水面积 | 39.78 km²；工程资料记载面积39.9 km² |
| 子流域 | 竹箦农场11.84、陶庄15.06、来笪村12.88 km² |
| 雨量站 | 塘马、东门坝、火烧坝、大山口 |
| 历史资料 | 2016—2022年 |
| 模型组成 | 三水源新安江模型—马斯京根汇流—零维水库模型 |
| 主要输入 | 降雨、蒸发、地形、水位、库容曲线及出库资料 |

## 历史过程结果

![2016年入库流量对比](figures/inflow-2016.png)

结果包括**2016、2020、2021、2022年入流过程图**及相应年份的典型水位对比时段。入流参考值来自水量平衡反推，图中的参考曲线使用原工作簿的滑动平均处理；水位图则比较记录水位与模拟水位。

这些结果展示了模型对季节性来水过程的刻画，也保留了不同事件和月份的偏差。[成果展示](docs/RESULTS.md)列出四年的全部图件，以及事件径流深和月尺度对比的节选，分别解释其评价对象。

## 预报与预泄

![预泄情景下的水位响应](figures/pre-release-result.png)

原报告展示的一个预泄情景采用：**24小时降雨24 mm、初始水位10.43 m、溢洪闸泄流1 m³/s**。图中可见预泄造成的水位下降及后续变化，形成“预报降雨—入流—出库安排—水位响应”的完整分析链条。

另一个预报示例的**24条逐时记录**中，水位差值为**0.02—0.09 m**。这一范围对应所列时段，不能直接代表所有洪水或整个72小时预报时段的精度。

## 项目材料

- [方法说明与18项参数](docs/METHODS.md)
- [历史结果与工程解释](docs/RESULTS.md)
- [原始地图、成果图及操作界面图集](docs/FIGURES.md)
- [结果数据与字段定义](data/README.md)
- [原始模型工程与数据片段](models/README.md)

研究与建模：**张天舒（Tianshu Zhang）**。工程文件保留原有模型结构，运行需使用兼容的TBM/BDS建模环境。

## Data availability / 数据公开范围

The native model project is included. **Hydrological inputs and numerical results are excerpts only**: 1–3 July 2016 rainfall and stage records, 27 June–10 July 2016 daily inflow comparisons, and 24 hourly forecast comparisons. Complete historical input and saved-result archives are excluded. These excerpts illustrate the workflow and do not provide all inputs needed to rerun historical scenarios. See [sample definitions](data/README.md).

提供原始模型工程。**水文输入与数值计算结果仅提供片段**：2016年7月1—3日水位与雨量记录、2016年6月27日—7月10日日入流对比，以及24条逐时预报对比。完整输入和已保存结果归档未公开；片段用于说明数据结构和分析过程，不足以重新运行全部历史情景。
