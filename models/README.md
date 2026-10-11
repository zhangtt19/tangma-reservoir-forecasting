# Native model project / 原始模型工程

[Part 1](tangma-model.zip.001) · [Part 2](tangma-model.zip.002) · [Part 3](tangma-model.zip.003) · [File checksums](manifest.json) · [Input and result excerpts](../data/README.md)

The ZIP contains the original BDS model and APG, GRA and WAP companion files from the saved `20231218有计算结果版` project. Native file bytes are preserved. Opening the project requires a compatible TBM/BDS environment; software is not included.

**The separate HYDRO input series and RESULT output files are excluded.** Only labelled CSV excerpts in `data/` are public. A complete historical rerun also requires its full input series and initial conditions.

压缩包保留原始BDS模型及APG、GRA、WAP配套文件，来自`20231218有计算结果版`工程快照。名称中的“有计算结果版”是原快照名称；本包未附带完整HYDRO输入目录和RESULT结果目录。水文输入和计算结果仅提供[data目录中的片段](../data/README.md)。打开工程需要兼容的TBM/BDS环境，完整历史重算还需要相应输入与初始条件。

## Download and open / 下载与打开

Download all three parts, `manifest.json` and [assemble-model.py](assemble-model.py) into one folder. Run `python assemble-model.py` with Python 3. The script checks each part, reconstructs the original ZIP, verifies its checksum and extracts to `tangma-model/`. It uses the Python standard library only. Existing ZIP files or output folders are not overwritten.

将三个分卷、`manifest.json`和`assemble-model.py`下载到同一个文件夹，在该文件夹运行 `python assemble-model.py`。脚本校验分卷后合并为原始ZIP，再解压到`tangma-model`文件夹；只需Python 3，无额外依赖。已有ZIP或解压目录不会被覆盖。分卷是为适应上传接口大小限制，未删减模型工程内容。
