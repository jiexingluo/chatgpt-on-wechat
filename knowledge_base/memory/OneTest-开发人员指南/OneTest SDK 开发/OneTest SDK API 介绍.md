|  |  |
| --- | --- |
|  | OneTest SDK API 介绍 |

OneTest SDK API 介绍

这一节主要介绍SDK开发时用到的API


## 1.OneTestSdkClient 构造函数

|  |  |
| --- | --- |
|  | 1.OneTestSdkClient 构造函数 |

OneTestSdkClient 构造函数

* C#

  [复制](# "复制")

  ```
  public OneTestSdkClient();
  ```

  **使用OneTest IDE的配置进行实例化**
* C#

  [复制](# "复制")

  ```
  public OneTestSdkClient(ClientConfig config);
  ```

  **使用参数作为配置进行实例化**


## 2.LoadProject 方法

|  |  |
| --- | --- |
|  | 2.LoadProject 方法 |

LoadProject 方法

C#

[复制](# "复制")

```
public void LoadProject(string projectFile)
```

**加载OneTest项目**

参数：

*projectFile*

    OneTest 项目的完整路径


## 3.GetInstruments 方法

|  |  |
| --- | --- |
|  | 3.GetInstruments 方法 |

GetInstruments 方法

* C#

  [复制](# "复制")

  ```
  public List<Instrument> GetInstruments()
  ```

  **获取项目中所有仪表的信息**


## 4.SetInstrumentAddress 方法

|  |  |
| --- | --- |
|  | 4.SetInstrumentAddress 方法 |

SetInstrumentAddress 方法

* C#

  [复制](# "复制")

  ```
  public bool SetInstrumentAddress(string instName, string address)
  ```

  **设置仪表地址**

  参数：

  *instName*

      仪表名称，通过该名称查找仪表

  *address*

      仪表地址，用来更新仪表地址

  exception: 如果有异常发生会throw OneTestSdkException类型异常


## 5.InitializeInstrument 方法

|  |  |
| --- | --- |
|  | 5.InitializeInstrument 方法 |

InitializeInstrument 方法

* C#

  [复制](# "复制")

  ```
  public void InitializeInstrument()
  ```

  **初始化所有仪器面板配置的仪器**

  exception: 如果有异常发生会throw OneTestSdkException类型异常
* C#

  [复制](# "复制")

  ```
  public void InitializeInstrument(string instrumentLabel)
  ```

  **初始化指定的仪器**

  参数：

  *instrumentLabel*

      OneTest仪器面板上添加的仪器的Label名称

  exception: 如果有异常发生会throw OneTestSdkException类型异常


## 6.CloseInstrument 方法

|  |  |
| --- | --- |
|  | 6.CloseInstrument 方法 |

CloseInstrument 方法

* C#

  [复制](# "复制")

  ```
  public void CloseInstrument()
  ```

  **关闭所有仪器面板配置的仪器**

  exception: 如果有异常发生会throw OneTestSdkException类型异常
* C#

  [复制](# "复制")

  ```
  public void CloseInstrument(string instrumentLabel)
  ```

  **关闭指定的仪器**

  参数：

  *instrumentLabel*

      OneTest仪器面板上添加的仪器的Label名称

  exception: 如果有异常发生会throw OneTestSdkException类型异常


## 7.RunTestMethod 方法

|  |  |
| --- | --- |
|  | 7.RunTestMethod 方法 |

RunTestMethod 方法

* C#

  [复制](# "复制")

  ```
  public async Task RunTestMethod(string testMethodName, int site)
  ```

  **用DebugSuite中设定的值（如果设定过），或者TestMethod的默认值（没有在DebugSuite中设定过）运行某个TestMethod**

  参数：

  *testMethodName*

      要运行的TestMethod的名称

  *site*

      要测试的site（在OneTest Pin Connections面板中已配置）

  exception: 如果有异常发生会throw OneTestSdkException类型异常
* C#

  [复制](# "复制")

  ```
  public async Task RunTestMethod(string testMethodName, int site, Dictionary<string, object> newParameterValues)
  ```

  **用给定的参数新值运行TestMethod**

  参数：

  *testMethodName*

      要运行的TestMethod的名称

  *site*

      要测试的site（在OneTest Pin Connections面板中已配置）

  *newParameterValues*

      要设置新值的参数名值对。key:参数名, value:新值

  exception: 如果有异常发生会throw OneTestSdkException类型异常


## 8.RunTestFlow 方法

|  |  |
| --- | --- |
|  | 8.RunTestFlow 方法 |

RunTestFlow 方法

* C#

  [复制](# "复制")

  ```
  public async Task<string> RunTestFlow(string flowName, int batchSize = 1, int intervalMs = 50)
  ```

  **执行Test Flow**

  参数：

  *flowName*

      TestFlow的名称

  *batchSize*

      UUT执行次数

  *intervalMs*

      批执行间隔时间

  return: Flow任务的唯一ID


## 9.RunTestSuite 方法

|  |  |
| --- | --- |
|  | 9.RunTestSuite 方法 |

RunTestSuite 方法

* C#

  [复制](# "复制")

  ```
  public async Task<string> RunTestSuite(string suiteFullName)
  ```

  **执行TestSuite**

  参数：

  *suiteFullName*

      TestSuite在TestFlow中的位置，由‘.’分隔

  return: Flow任务的唯一ID

  exception: 如果有异常发生会throw OneTestSdkException类型异常
* C#

  [复制](# "复制")

  ```
  public async Task<string> RunTestSuite(string flowName, string suiteName)
  ```

  **执行TestSuite（从flow根节点开始，按深度优先查找）**

  参数：

  *flowName*

      TestFlow名称

  *suiteName*

      TestSuite名称

  return: Flow任务的唯一ID

  exception: 如果有异常发生会throw OneTestSdkException类型异常


## 10.Dispose 方法

|  |  |
| --- | --- |
|  | 10.Dispose 方法 |

Dispose 方法

* C#

  [复制](# "复制")

  ```
  public void Dispose()
  ```

  **释放Engine资源**


## 11.EvaluateResultCallback 委托

|  |  |
| --- | --- |
|  | 11.EvaluateResultCallback 委托 |

EvaluateResultCallback 委托

C#

[复制](# "复制")

```
public Action<MeasurementResult> EvaluateResultCallback { get; set; }
```

**当引擎完成测试任务后，会通过此委托将结果传递给订阅者。**

参数：

*MeasurementResult*

    回调方法的参数，包含测项结果数据。具体结构参考MeasurementResult类的文档。


## 12.GraphResultCallback 委托

|  |  |
| --- | --- |
|  | 12.GraphResultCallback 委托 |

GraphResultCallback 委托

C#

[复制](# "复制")

```
public Action<GraphResult> GraphResultCallback { get; set; }
```

**当引擎完成测试任务后，会通过此委托将结果传递给订阅者。**

参数：

*GraphResult*

    回调方法的参数，包含折线图数据。具体结构参考GraphResult类的文档。


## 13.BatchBinResultCallback 委托

|  |  |
| --- | --- |
|  | 13.BatchBinResultCallback 委托 |

BatchBinResultCallback 委托

C#

[复制](# "复制")

```
public Action<BatchResult> BatchBinResultCallback { get; set; }
```

**当引擎完成测试任务后，会通过此委托将结果传递给订阅者。**

参数：

*BatchResult*

    回调方法的参数，包含一个批次的测试结果数据。具体结构参考BatchResult类的文档。


## 14.TaskFinishedCallback 委托

|  |  |
| --- | --- |
|  | 14.TaskFinishedCallback 委托 |

TaskFinishedCallback 委托

C#

[复制](# "复制")

```
public Action<string> TaskFinishedCallback { get; set; }
```

**当引擎完成测试任务后，会通过此委托将结果传递给订阅者。**

参数：

*string*

    Flow结束时为：Flow execute finished!

    Suite结束时为：Suite execute finished!


## 15.TaskExceptionCallback 委托

|  |  |
| --- | --- |
|  | 15.TaskExceptionCallback 委托 |

TaskExceptionCallback 委托

C#

[复制](# "复制")

```
public Action<TaskExceptionRequest> TaskExceptionCallback { get; set; }
```

**当引擎完成测试任务后，会通过此委托将结果传递给订阅者。**

参数：

*TaskExceptionRequest*

    回调方法的参数，包含测试异常的FlowName和Message


## 16.EngineLogCallback 委托

|  |  |
| --- | --- |
|  | 16.EngineLogCallback 委托 |

EngineLogCallback 委托

C#

[复制](# "复制")

```
public Action<string> EngineLogCallback
```

**引擎记录执行日志时，会通过此委托将结果传递给订阅者。**

参数：

*string*

    日志内容


## 17.TimeMetricLogCallback 委托

|  |  |
| --- | --- |
|  | 17.TimeMetricLogCallback 委托 |

TimeMetricLogCallback 委托

C#

[复制](# "复制")

```
public Action<string> TimeMetricLogCallback
```

**引擎记录Suite执行时间信息日志时，会通过此委托将结果传递给订阅者。**

参数：

*string*

    日志内容


## 18.MeasurementResult 类

|  |  |
| --- | --- |
|  | 18.MeasurementResult 类 |

MeasurementResult 类

属性

| 名称 | 含义 |
| --- | --- |
| Result | 测量结果（Pass/Fail/Done） |
| Site | 进行测试的Site |
| TestSuite | TestFlow中定义的SuiteName |
| TestName | TestMethod中定义的测项名称 |
| TestText | TestMethod中定义的测项 |
| LowLimit | Evaluation Settings中设置的Low Limit |
| HighLimit | Evaluation Settings中设置的High Limit |
| Pin | 测试时设置的Pin |
| MeasuredValue | 测量结果 |
| Unit | Evaluation Settings中设置的Unit |
| SweepParams | Sweep运行时当前参数值 |


## 19.GraphResult 类

|  |  |
| --- | --- |
|  | 19.GraphResult 类 |

GraphResult 类

属性

| 名称 | 含义 |
| --- | --- |
| GraphName | Graph的名称 |
| Append | 图表数据过大时，将数据分布在多个对象中。该属性为true表示图像数据是追加数据。 |
| GraphData | Graph的详细数据，详见GraphData类 |

GraphData 类

属性

| 名称 | 含义 |
| --- | --- |
| GraphType | 1：折线图  2：直方图 |
| GraphLines | 折线图时：列表中包含多条折现的详细数据  直方图时：列表中只包含一个GraphLine对象  详见GraphLine类 |

GraphLine 类

属性

| 名称 | 含义 |
| --- | --- |
| LineName | 图表为折线图时有具体含义：折线的名称 |
| Points | 图表中每个结点的详细数据，详见GraphPoint类 |

GraphPoint 类

属性

| 名称 | 含义 |
| --- | --- |
| XValue | 折线图时：折点的X轴坐标  直方图时：表示该频次的下限值 |
| YValue | 折线图时：折点的Y轴坐标  直方图时：表示该频次的频数值 |
| ZValue | 折线图时：无具体含义  直方图时：表示该频次的上限值 |


## 20.BatchResult 类

|  |  |
| --- | --- |
|  | 20.BatchResult 类 |

BatchResult 类

属性

| 名称 | 含义 |
| --- | --- |
| LoadTick | 开始加载时间（Handler上料开始时间） |
| StartTick | 当前Batch的起始时间点（Master节点的Tick） |
| IndexTime | Handler操作时间，从LoadDevice到BinDevice的总时间减去FlowTime，单位：微秒 |
| ControlTime | Flow运行的控制调度时间，包含通信和UI更新，单位：微秒 |
| TestTime | Batch运行总耗时，从Batch开始到Batch结束的总时间(包含程序调度时间ControlTime），单位：微秒 |
| SuiteTime | 用户的TM执行耗时汇总，单位：微秒 |
| SiteResults | 每个Site的测试结果，详见 SiteDeviceResult 类 |
| ExtInfo | 用户可以传递的其他扩展信息，比如跨Flow的状态或者结果信息 |

SiteDeviceResult 类

属性

| 名称 | 含义 |
| --- | --- |
| SiteId | SiteId |
| CoordX | PH测试时，芯片的X轴坐标 |
| CoordY | PH测试时，芯片的Y轴坐标 |
| DeviceId | 唯一标识，组成规则：BatchId + "&" + site |
| SuiteTime | 用户的TM执行耗时，单位：微秒 |
| GrpcTime | grpc通信耗时，单位：微秒 |
| Result | 测试结果：Done\Pass\Fail\Error |
| BinInfo | 分Bin信息，详见 BinInfo 类 |

BinInfo 类

属性

| 名称 | 含义 |
| --- | --- |
| HardBinNumber | Hard Bin Number |
| HardBinName | Hard Bin 名称 |
| SoftBinNumber | Soft Bin Number |
| SoftBinName | Soft Bin名称 |

