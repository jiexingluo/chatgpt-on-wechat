|  |  |
| --- | --- |
|  | DAQParent 命名空间 |

类

|  | 类 | 说明 |
| --- | --- | --- |
| 公共类 | [DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm) |  |

接口

|  | 接口 | 说明 |
| --- | --- | --- |
| 公共接口 | [IDAQ\_Instr](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm) |  |


## DAQ 类

|  |  |
| --- | --- |
|  | DAQ 类 |

继承层次

SystemObject
  
  MeasStation  
    DAQParentDAQ

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public class DAQ : MeasStation
```

DAQ 类型公开以下成员。

构造函数

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [DAQ](82f708e3-f7bb-083c-b52c-21ea3c9b6071.htm) | 初始化 DAQ 类的一个新实例 |

[Top](#PageHeader)

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [AbortGeneration](d6a1d244-7778-dec2-d3b5-65a6f2857bb6.htm) |  |
| 公共方法 | [ClearTask](d10d0fff-9ead-b3a4-9002-f7dc8dfbb24f.htm) |  |
| 公共方法 | [ConfigureMultiChannelSineWaveform](42bd9a49-1ca2-f8db-f853-8d6c4d2f0d85.htm) |  |
| 公共方法 | [ConfigurePureToneWaveform](014d253f-5a44-ec7b-a534-f052c1262c0c.htm) |  |
| 公共方法 | [ConfigureSampleClock](69d6757d-a870-50a3-c284-fd2912b4d116.htm) |  |
| 公共方法 | [ConfigureSampleClockHW](42b7f392-7581-7ac7-37fc-35d7fde69877.htm) |  |
| 公共方法 | [ConfigureStartDigitalEdgeTrigger](285404da-a3d1-41c0-551d-f7eb41379489.htm) |  |
| 公共方法 | [Control](620e0c8c-bb70-39e8-6490-c300561f2533.htm) |  |
| 公共方法 | [CreateAIVoltageChannel](485c7046-3e01-f72c-2843-507f0c8e3d99.htm) |  |
| 公共方法 | [CreateAOVoltageChannel](ed839f74-cfee-86aa-25d4-aef3d5a28fe6.htm) |  |
| 公共方法 | [CreateArbWaveform](bc625cac-78e3-5ba0-fa64-7c99cd97e052.htm) |  |
| 公共方法 | [CreateDOChannel](f03e0de7-86d3-9929-7582-29aaab35e4b5.htm) |  |
| 公共方法 | [CreateStandardWaveform](e60d7eec-0819-aecb-38bb-44a5f0447cf9.htm) |  |
| 公共方法 | [CreateTask](9dadcc35-316a-ca6c-9a33-313ac990d468.htm) |  |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 公共方法 | [ExportStartSignal](e7ed5a7a-bdd4-56f1-2618-875b5917c19a.htm) |  |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | [GenerateStandardWaveform](5c0636cc-c418-d0b3-6a4b-f3a72e15139a.htm) |  |
| 公共方法 | [GetAIChannelMaximum](07cebdd4-8eff-7f02-4a0a-bfaba9a4be16.htm) |  |
| 公共方法 | [GetAIChannelMinimum](4d4d6aaf-36b5-41ee-ba68-d63e72ea7ae7.htm) |  |
| 公共方法 | [GetAOChannelMaximum](7b937d9f-b38d-94e4-3801-e4e9dd617104.htm) |  |
| 公共方法 | [GetAOChannelMinimum](1eaeb94b-d409-6ec3-df1d-2d0c8013d578.htm) |  |
| 公共方法 | [GetAutoZeroMode](1be1e716-57c8-b8db-6c31-64fc25895964.htm) |  |
| 公共方法 | [GetDutyCycleHigh](fb7946e8-3146-2a93-4b97-ee23ad7a8ccb.htm) |  |
| 公共方法 | [GetFunctionGenerationStartPhase](50a43ea8-eead-393f-a3c6-07d637c97040.htm) |  |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | [GetOutputIdleBehavior](e8912a65-0e69-841c-7581-d8a0187e34b6.htm) |  |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | [InitiateGeneration](29a5bd98-f16f-d042-3d30-191a3f7f5b2e.htm) |  |
| 公共方法 | [IsTaskDone](06b9d715-0c32-4da0-b52e-71d7894888d3.htm) |  |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [ReadMultiChannelMultiSamples](162dc208-89bd-3c9a-2207-fe8159687c8f.htm) |  |
| 公共方法 | [ReadMultiChannelSingleSample](fec2de1c-a0cc-5396-05fa-08f8cd562b05.htm) |  |
| 公共方法 | [ReadMultiSamples](a6b1a022-9c11-eb57-4c64-727f373090ef.htm) |  |
| 公共方法 | [ReadSingleSample](6643627c-6db7-2999-4425-3479262fa7c8.htm) |  |
| 公共方法 | [ReadWaveform](c076fe14-7fc6-365f-28c7-c39bacd24698.htm) |  |
| 公共方法 | [SetAIChannelMaximum](1ee06323-cd5d-efc1-bf92-2d4c477ef334.htm) |  |
| 公共方法 | [SetAIChannelMinimum](2d5642d9-299b-4131-dbde-ec064d379cab.htm) |  |
| 公共方法 | [SetAICoupling](454bf6fc-e6c5-c4d2-8cc5-c227f8190396.htm) |  |
| 公共方法 | [SetAOChannelMaximum](db91a043-bbaa-ab3b-861c-f090d636b3a0.htm) |  |
| 公共方法 | [SetAOChannelMinimum](1a004dd7-adf5-091c-684b-6d988099186b.htm) |  |
| 公共方法 | [SetAutoZeroMode](71ed3019-ddef-4099-a22f-8f08c9ada109.htm) |  |
| 公共方法 | [SetCommonModeOffset](e1692cb9-dd68-a98b-ead9-d8b5f8e3bb1d.htm) |  |
| 公共方法 | [SetDutyCycleHigh](35176ad9-fa5d-665c-a2e4-1bcaaacd8808.htm) |  |
| 公共方法 | [SetFunctionGenerationStartPhase](cb0f9efd-b900-021a-49e6-302c6e0063ca.htm) |  |
| 公共方法 | [SetOutputIdleBehavior](81602ff1-c23f-d981-02a9-9e326bc035d5.htm) |  |
| 公共方法 | [SetTerminalConfiguration](41c3623c-8869-5e68-c0dd-a4c3b180c8a1.htm) |  |
| 公共方法 | [StartTask](c0aeb19c-d0bc-131a-1057-315b818bf4c2.htm) |  |
| 公共方法 | [StopTask](33339ba5-4158-65ac-cba4-72e01406b94a.htm) |  |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |
| 公共方法 | [WaitForNextSampleClock](31e627aa-5765-c61d-efb2-f00095deb60a.htm) |  |
| 公共方法 | [WriteDigitalLines](fa4a8848-407a-7cf1-40c2-f007963c03fc.htm) |  |
| 公共方法 | [WriteMultiChannelData](741fb880-9d6c-cad8-e742-eaa530000f6b.htm) |  |
| 公共方法 | [WriteSingleChannelData](5bccc0f0-48cf-bc2d-fa9d-2c5c6689c706.htm) |  |

[Top](#PageHeader)

参见

##### 引用

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


### DAQ 构造函数

|  |  |
| --- | --- |
|  | DAQ 构造函数 |

初始化 [DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm) 类的一个新实例

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ()
```

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


### DAQ 方法

|  |  |
| --- | --- |
|  | DAQ 方法 |

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [AbortGeneration](d6a1d244-7778-dec2-d3b5-65a6f2857bb6.htm) |  |
| 公共方法 | [ClearTask](d10d0fff-9ead-b3a4-9002-f7dc8dfbb24f.htm) |  |
| 公共方法 | [ConfigureMultiChannelSineWaveform](42bd9a49-1ca2-f8db-f853-8d6c4d2f0d85.htm) |  |
| 公共方法 | [ConfigurePureToneWaveform](014d253f-5a44-ec7b-a534-f052c1262c0c.htm) |  |
| 公共方法 | [ConfigureSampleClock](69d6757d-a870-50a3-c284-fd2912b4d116.htm) |  |
| 公共方法 | [ConfigureSampleClockHW](42b7f392-7581-7ac7-37fc-35d7fde69877.htm) |  |
| 公共方法 | [ConfigureStartDigitalEdgeTrigger](285404da-a3d1-41c0-551d-f7eb41379489.htm) |  |
| 公共方法 | [Control](620e0c8c-bb70-39e8-6490-c300561f2533.htm) |  |
| 公共方法 | [CreateAIVoltageChannel](485c7046-3e01-f72c-2843-507f0c8e3d99.htm) |  |
| 公共方法 | [CreateAOVoltageChannel](ed839f74-cfee-86aa-25d4-aef3d5a28fe6.htm) |  |
| 公共方法 | [CreateArbWaveform](bc625cac-78e3-5ba0-fa64-7c99cd97e052.htm) |  |
| 公共方法 | [CreateDOChannel](f03e0de7-86d3-9929-7582-29aaab35e4b5.htm) |  |
| 公共方法 | [CreateStandardWaveform](e60d7eec-0819-aecb-38bb-44a5f0447cf9.htm) |  |
| 公共方法 | [CreateTask](9dadcc35-316a-ca6c-9a33-313ac990d468.htm) |  |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 公共方法 | [ExportStartSignal](e7ed5a7a-bdd4-56f1-2618-875b5917c19a.htm) |  |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | [GenerateStandardWaveform](5c0636cc-c418-d0b3-6a4b-f3a72e15139a.htm) |  |
| 公共方法 | [GetAIChannelMaximum](07cebdd4-8eff-7f02-4a0a-bfaba9a4be16.htm) |  |
| 公共方法 | [GetAIChannelMinimum](4d4d6aaf-36b5-41ee-ba68-d63e72ea7ae7.htm) |  |
| 公共方法 | [GetAOChannelMaximum](7b937d9f-b38d-94e4-3801-e4e9dd617104.htm) |  |
| 公共方法 | [GetAOChannelMinimum](1eaeb94b-d409-6ec3-df1d-2d0c8013d578.htm) |  |
| 公共方法 | [GetAutoZeroMode](1be1e716-57c8-b8db-6c31-64fc25895964.htm) |  |
| 公共方法 | [GetDutyCycleHigh](fb7946e8-3146-2a93-4b97-ee23ad7a8ccb.htm) |  |
| 公共方法 | [GetFunctionGenerationStartPhase](50a43ea8-eead-393f-a3c6-07d637c97040.htm) |  |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | [GetOutputIdleBehavior](e8912a65-0e69-841c-7581-d8a0187e34b6.htm) |  |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | [InitiateGeneration](29a5bd98-f16f-d042-3d30-191a3f7f5b2e.htm) |  |
| 公共方法 | [IsTaskDone](06b9d715-0c32-4da0-b52e-71d7894888d3.htm) |  |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [ReadMultiChannelMultiSamples](162dc208-89bd-3c9a-2207-fe8159687c8f.htm) |  |
| 公共方法 | [ReadMultiChannelSingleSample](fec2de1c-a0cc-5396-05fa-08f8cd562b05.htm) |  |
| 公共方法 | [ReadMultiSamples](a6b1a022-9c11-eb57-4c64-727f373090ef.htm) |  |
| 公共方法 | [ReadSingleSample](6643627c-6db7-2999-4425-3479262fa7c8.htm) |  |
| 公共方法 | [ReadWaveform](c076fe14-7fc6-365f-28c7-c39bacd24698.htm) |  |
| 公共方法 | [SetAIChannelMaximum](1ee06323-cd5d-efc1-bf92-2d4c477ef334.htm) |  |
| 公共方法 | [SetAIChannelMinimum](2d5642d9-299b-4131-dbde-ec064d379cab.htm) |  |
| 公共方法 | [SetAICoupling](454bf6fc-e6c5-c4d2-8cc5-c227f8190396.htm) |  |
| 公共方法 | [SetAOChannelMaximum](db91a043-bbaa-ab3b-861c-f090d636b3a0.htm) |  |
| 公共方法 | [SetAOChannelMinimum](1a004dd7-adf5-091c-684b-6d988099186b.htm) |  |
| 公共方法 | [SetAutoZeroMode](71ed3019-ddef-4099-a22f-8f08c9ada109.htm) |  |
| 公共方法 | [SetCommonModeOffset](e1692cb9-dd68-a98b-ead9-d8b5f8e3bb1d.htm) |  |
| 公共方法 | [SetDutyCycleHigh](35176ad9-fa5d-665c-a2e4-1bcaaacd8808.htm) |  |
| 公共方法 | [SetFunctionGenerationStartPhase](cb0f9efd-b900-021a-49e6-302c6e0063ca.htm) |  |
| 公共方法 | [SetOutputIdleBehavior](81602ff1-c23f-d981-02a9-9e326bc035d5.htm) |  |
| 公共方法 | [SetTerminalConfiguration](41c3623c-8869-5e68-c0dd-a4c3b180c8a1.htm) |  |
| 公共方法 | [StartTask](c0aeb19c-d0bc-131a-1057-315b818bf4c2.htm) |  |
| 公共方法 | [StopTask](33339ba5-4158-65ac-cba4-72e01406b94a.htm) |  |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |
| 公共方法 | [WaitForNextSampleClock](31e627aa-5765-c61d-efb2-f00095deb60a.htm) |  |
| 公共方法 | [WriteDigitalLines](fa4a8848-407a-7cf1-40c2-f007963c03fc.htm) |  |
| 公共方法 | [WriteMultiChannelData](741fb880-9d6c-cad8-e742-eaa530000f6b.htm) |  |
| 公共方法 | [WriteSingleChannelData](5bccc0f0-48cf-bc2d-fa9d-2c5c6689c706.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### AbortGeneration 方法

|  |  |
| --- | --- |
|  | DAQAbortGeneration 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ AbortGeneration(
	string Label = ""
)
```

###### 参数

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ClearTask 方法

|  |  |
| --- | --- |
|  | DAQClearTask 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ ClearTask(
	string Label = ""
)
```

###### 参数

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ConfigureMultiChannelSineWaveform 方法

|  |  |
| --- | --- |
|  | DAQConfigureMultiChannelSineWaveform 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ ConfigureMultiChannelSineWaveform(
	double amplitude,
	double dcOffset,
	double frequency,
	string PhaseArray,
	string Label = ""
)
```

###### 参数

amplitude  Double

dcOffset  Double

frequency  Double

PhaseArray  String

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ConfigurePureToneWaveform 方法

|  |  |
| --- | --- |
|  | DAQConfigurePureToneWaveform 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ ConfigurePureToneWaveform(
	string waveformType,
	double amplitude,
	double dcOffset,
	double frequency,
	string Label = ""
)
```

###### 参数

waveformType  String

amplitude  Double

dcOffset  Double

frequency  Double

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ConfigureSampleClock 方法

|  |  |
| --- | --- |
|  | DAQConfigureSampleClock 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ ConfigureSampleClock(
	string source,
	double rate,
	int samplesPerChannel,
	bool continuous = false,
	string Label = ""
)
```

###### 参数

source  String

rate  Double

samplesPerChannel  Int32

continuous  Boolean  (Optional)

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ConfigureSampleClockHW 方法

|  |  |
| --- | --- |
|  | DAQConfigureSampleClockHW 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ ConfigureSampleClockHW(
	double rate,
	string Label = ""
)
```

###### 参数

rate  Double

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ConfigureStartDigitalEdgeTrigger 方法

|  |  |
| --- | --- |
|  | DAQConfigureStartDigitalEdgeTrigger 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ ConfigureStartDigitalEdgeTrigger(
	string source,
	string edgeType,
	string Label = ""
)
```

###### 参数

source  String

edgeType  String

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### Control 方法

|  |  |
| --- | --- |
|  | DAQControl 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ Control(
	string taskAction,
	string Label = ""
)
```

###### 参数

taskAction  String

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### CreateAIVoltageChannel 方法

|  |  |
| --- | --- |
|  | DAQCreateAIVoltageChannel 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ CreateAIVoltageChannel(
	double minimumValue = -5,
	double maximumValue = 5,
	string units = "Volts",
	string Label = ""
)
```

###### 参数

minimumValue  Double  (Optional)

maximumValue  Double  (Optional)

units  String  (Optional)

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### CreateAOVoltageChannel 方法

|  |  |
| --- | --- |
|  | DAQCreateAOVoltageChannel 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ CreateAOVoltageChannel(
	double minimumValue = -5,
	double maximumValue = 5,
	string units = "Volts",
	string Label = ""
)
```

###### 参数

minimumValue  Double  (Optional)

maximumValue  Double  (Optional)

units  String  (Optional)

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### CreateArbWaveform 方法

|  |  |
| --- | --- |
|  | DAQCreateArbWaveform 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ CreateArbWaveform(
	double[] data,
	string Label = ""
)
```

###### 参数

data  Double

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### CreateDOChannel 方法

|  |  |
| --- | --- |
|  | DAQCreateDOChannel 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ CreateDOChannel(
	string lines,
	string nameToAssignToLines,
	int lineGrouping,
	string Label = ""
)
```

###### 参数

lines  String

nameToAssignToLines  String

lineGrouping  Int32

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### CreateStandardWaveform 方法

|  |  |
| --- | --- |
|  | DAQCreateStandardWaveform 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ CreateStandardWaveform(
	string waveformFunction,
	double amplitude,
	double dcOffset,
	double frequency,
	double startPhase,
	string Label = ""
)
```

###### 参数

waveformFunction  String

amplitude  Double

dcOffset  Double

frequency  Double

startPhase  Double

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### CreateTask 方法

|  |  |
| --- | --- |
|  | DAQCreateTask 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ CreateTask(
	string Label = ""
)
```

###### 参数

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ExportStartSignal 方法

|  |  |
| --- | --- |
|  | DAQExportStartSignal 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ ExportStartSignal(
	string outputTerminal,
	string Label = ""
)
```

###### 参数

outputTerminal  String

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### GenerateStandardWaveform 方法

|  |  |
| --- | --- |
|  | DAQGenerateStandardWaveform 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double[]> GenerateStandardWaveform(
	string waveformFunction,
	double amplitude,
	double dcOffset,
	double frequency,
	double startPhase,
	string Label = ""
)
```

###### 参数

waveformFunction  String

amplitude  Double

dcOffset  Double

frequency  Double

startPhase  Double

Label  String  (Optional)

###### 返回值

DictionaryString, Double

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### GetAIChannelMaximum 方法

|  |  |
| --- | --- |
|  | DAQGetAIChannelMaximum 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double[]> GetAIChannelMaximum(
	string Label = ""
)
```

###### 参数

Label  String  (Optional)

###### 返回值

DictionaryString, Double

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### GetAIChannelMinimum 方法

|  |  |
| --- | --- |
|  | DAQGetAIChannelMinimum 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double[]> GetAIChannelMinimum(
	string Label = ""
)
```

###### 参数

Label  String  (Optional)

###### 返回值

DictionaryString, Double

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### GetAOChannelMaximum 方法

|  |  |
| --- | --- |
|  | DAQGetAOChannelMaximum 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double[]> GetAOChannelMaximum(
	string Label = ""
)
```

###### 参数

Label  String  (Optional)

###### 返回值

DictionaryString, Double

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### GetAOChannelMinimum 方法

|  |  |
| --- | --- |
|  | DAQGetAOChannelMinimum 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double[]> GetAOChannelMinimum(
	string Label = ""
)
```

###### 参数

Label  String  (Optional)

###### 返回值

DictionaryString, Double

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### GetAutoZeroMode 方法

|  |  |
| --- | --- |
|  | DAQGetAutoZeroMode 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string[]> GetAutoZeroMode(
	string Label = ""
)
```

###### 参数

Label  String  (Optional)

###### 返回值

DictionaryString, String

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### GetDutyCycleHigh 方法

|  |  |
| --- | --- |
|  | DAQGetDutyCycleHigh 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetDutyCycleHigh(
	string Label = ""
)
```

###### 参数

Label  String  (Optional)

###### 返回值

DictionaryString, Double

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### GetFunctionGenerationStartPhase 方法

|  |  |
| --- | --- |
|  | DAQGetFunctionGenerationStartPhase 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double[]> GetFunctionGenerationStartPhase(
	string Label = ""
)
```

###### 参数

Label  String  (Optional)

###### 返回值

DictionaryString, Double

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### GetOutputIdleBehavior 方法

|  |  |
| --- | --- |
|  | DAQGetOutputIdleBehavior 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string[]> GetOutputIdleBehavior(
	string Label = ""
)
```

###### 参数

Label  String  (Optional)

###### 返回值

DictionaryString, String

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### InitiateGeneration 方法

|  |  |
| --- | --- |
|  | DAQInitiateGeneration 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ InitiateGeneration(
	string Label = ""
)
```

###### 参数

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### IsTaskDone 方法

|  |  |
| --- | --- |
|  | DAQIsTaskDone 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> IsTaskDone(
	string Label = ""
)
```

###### 参数

Label  String  (Optional)

###### 返回值

DictionaryString, Boolean

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ReadMultiChannelMultiSamples 方法

|  |  |
| --- | --- |
|  | DAQReadMultiChannelMultiSamples 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double[]> ReadMultiChannelMultiSamples(
	int sampleNumber,
	double timeout,
	string Label = ""
)
```

###### 参数

sampleNumber  Int32

timeout  Double

Label  String  (Optional)

###### 返回值

DictionaryString, Double

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ReadMultiChannelSingleSample 方法

|  |  |
| --- | --- |
|  | DAQReadMultiChannelSingleSample 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double[]> ReadMultiChannelSingleSample(
	double timeout,
	string Label = ""
)
```

###### 参数

timeout  Double

Label  String  (Optional)

###### 返回值

DictionaryString, Double

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ReadMultiSamples 方法

|  |  |
| --- | --- |
|  | DAQReadMultiSamples 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double[]> ReadMultiSamples(
	int sampleNumber,
	string Label = ""
)
```

###### 参数

sampleNumber  Int32

Label  String  (Optional)

###### 返回值

DictionaryString, Double

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ReadSingleSample 方法

|  |  |
| --- | --- |
|  | DAQReadSingleSample 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> ReadSingleSample(
	string Label = ""
)
```

###### 参数

Label  String  (Optional)

###### 返回值

DictionaryString, Double

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ReadWaveform 方法

|  |  |
| --- | --- |
|  | DAQReadWaveform 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double[]> ReadWaveform(
	int samplesPerChannel,
	string Label = ""
)
```

###### 参数

samplesPerChannel  Int32

Label  String  (Optional)

###### 返回值

DictionaryString, Double

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### SetAIChannelMaximum 方法

|  |  |
| --- | --- |
|  | DAQSetAIChannelMaximum 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ SetAIChannelMaximum(
	double channelMaximum,
	string Label = ""
)
```

###### 参数

channelMaximum  Double

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### SetAIChannelMinimum 方法

|  |  |
| --- | --- |
|  | DAQSetAIChannelMinimum 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ SetAIChannelMinimum(
	double channelMinimum,
	string Label = ""
)
```

###### 参数

channelMinimum  Double

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### SetAICoupling 方法

|  |  |
| --- | --- |
|  | DAQSetAICoupling 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ SetAICoupling(
	string CPLMode,
	string Label = ""
)
```

###### 参数

CPLMode  String

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### SetAOChannelMaximum 方法

|  |  |
| --- | --- |
|  | DAQSetAOChannelMaximum 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ SetAOChannelMaximum(
	double channelMaximum,
	string Label = ""
)
```

###### 参数

channelMaximum  Double

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### SetAOChannelMinimum 方法

|  |  |
| --- | --- |
|  | DAQSetAOChannelMinimum 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ SetAOChannelMinimum(
	double channelMinimum,
	string Label = ""
)
```

###### 参数

channelMinimum  Double

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### SetAutoZeroMode 方法

|  |  |
| --- | --- |
|  | DAQSetAutoZeroMode 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ SetAutoZeroMode(
	string autoZeroMode,
	string Label = ""
)
```

###### 参数

autoZeroMode  String

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### SetCommonModeOffset 方法

|  |  |
| --- | --- |
|  | DAQSetCommonModeOffset 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ SetCommonModeOffset(
	double commonModeOffset,
	string Label = ""
)
```

###### 参数

commonModeOffset  Double

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### SetDutyCycleHigh 方法

|  |  |
| --- | --- |
|  | DAQSetDutyCycleHigh 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ SetDutyCycleHigh(
	double dutyCycleHigh,
	string Label = ""
)
```

###### 参数

dutyCycleHigh  Double

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### SetFunctionGenerationStartPhase 方法

|  |  |
| --- | --- |
|  | DAQSetFunctionGenerationStartPhase 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ SetFunctionGenerationStartPhase(
	double startPhase,
	string Label = ""
)
```

###### 参数

startPhase  Double

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### SetOutputIdleBehavior 方法

|  |  |
| --- | --- |
|  | DAQSetOutputIdleBehavior 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ SetOutputIdleBehavior(
	string behavior,
	string Label = ""
)
```

###### 参数

behavior  String

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### SetTerminalConfiguration 方法

|  |  |
| --- | --- |
|  | DAQSetTerminalConfiguration 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ SetTerminalConfiguration(
	string configuration,
	string Label = ""
)
```

###### 参数

configuration  String

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### StartTask 方法

|  |  |
| --- | --- |
|  | DAQStartTask 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ StartTask(
	string Label = ""
)
```

###### 参数

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### StopTask 方法

|  |  |
| --- | --- |
|  | DAQStopTask 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ StopTask(
	string Label = ""
)
```

###### 参数

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### WaitForNextSampleClock 方法

|  |  |
| --- | --- |
|  | DAQWaitForNextSampleClock 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> WaitForNextSampleClock(
	double timeout,
	string Label = ""
)
```

###### 参数

timeout  Double

Label  String  (Optional)

###### 返回值

DictionaryString, Boolean

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### WriteDigitalLines 方法

|  |  |
| --- | --- |
|  | DAQWriteDigitalLines 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ WriteDigitalLines(
	bool autoStart,
	bool[] writeArray,
	string Label = ""
)
```

###### 参数

autoStart  Boolean

writeArray  Boolean

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### WriteMultiChannelData 方法

|  |  |
| --- | --- |
|  | DAQWriteMultiChannelData 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ WriteMultiChannelData(
	double[,] data,
	string Label = ""
)
```

###### 参数

data  Double

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### WriteSingleChannelData 方法

|  |  |
| --- | --- |
|  | DAQWriteSingleChannelData 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ WriteSingleChannelData(
	double[] data,
	string Label = ""
)
```

###### 参数

data  Double

Label  String  (Optional)

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

参见

###### 引用

[DAQ 类](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


## IDAQ_Instr 接口

|  |  |
| --- | --- |
|  | IDAQ\_Instr 接口 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public interface IDAQ_Instr
```

IDAQ\_Instr 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [AbortGeneration](510ebf74-cb09-d212-2a4a-64b060d4edca.htm) |  |
| 公共方法 | [ClearTask](44b8722a-136f-49db-6be5-7863e7dd9aa6.htm) |  |
| 公共方法 | [Close](3510e391-c0d4-9b66-3e21-a28866241ad7.htm) |  |
| 公共方法 | [ConfigureMultiChannelSineWaveform](ca25afed-ca4d-41ba-9dd3-57ebdee22b7e.htm) |  |
| 公共方法 | [ConfigurePureToneWaveform](9fb8854e-2cca-4339-56fd-4e9c6a4ce192.htm) |  |
| 公共方法 | [ConfigureSampleClock](359b3a8a-7d45-bc38-ac59-cc87ea181257.htm) |  |
| 公共方法 | [ConfigureSampleClockHW](25c62125-9eb4-fe23-7270-a3c91f00ac20.htm) |  |
| 公共方法 | [ConfigureStartDigitalEdgeTrigger](6b682a31-c5a3-8665-eec8-46a9a52406ac.htm) |  |
| 公共方法 | [Control](81320f40-f907-e54f-2e3c-a8123c1a8ef4.htm) |  |
| 公共方法 | [CreateAIVoltageChannel](aa0a6cc1-4962-6dc3-fcab-98d06f5409df.htm) |  |
| 公共方法 | [CreateAOVoltageChannel](40d9b21e-c4be-3e1d-4a5d-72049b17f55a.htm) |  |
| 公共方法 | [CreateArbWaveform](d6e63738-8be2-cb6b-de0b-e74a05685f2e.htm) |  |
| 公共方法 | [CreateDOChannel](b84bf086-f8ac-05ed-9245-6854e35f7263.htm) |  |
| 公共方法 | [CreateStandardWaveform](bdb778fb-bea6-16f1-4d88-6d5afe166656.htm) |  |
| 公共方法 | [CreateTask](940b0339-099d-ea1a-8d53-c089fbc8394f.htm) |  |
| 公共方法 | [ExportStartSignal](ef1650ee-0730-5bfe-42c8-dda95b613a77.htm) |  |
| 公共方法 | [GenerateStandardWaveform](4eb956f5-e031-ac71-9737-012cc5bcaccf.htm) |  |
| 公共方法 | [GetAIChannelMaximum](a436d8b0-d363-dd15-730c-74e7c6994d0e.htm) |  |
| 公共方法 | [GetAIChannelMinimum](261d8c99-7ea1-fb26-f53e-87a95827c70d.htm) |  |
| 公共方法 | [GetAOChannelMaximum](cf1e8dee-c47d-6be1-2b3d-a27b9c3c7cba.htm) |  |
| 公共方法 | [GetAOChannelMinimum](9350206d-37d8-000d-c3e9-bd4278de33fe.htm) |  |
| 公共方法 | [GetAutoZeroMode](ae9255d7-7d23-e0db-391a-9722352a6fc3.htm) |  |
| 公共方法 | [GetDutyCycleHigh](7d236124-169d-8517-d0a2-2efd62fd2b19.htm) |  |
| 公共方法 | [GetFunctionGenerationStartPhase](bb235796-2be8-193e-4002-461770b25257.htm) |  |
| 公共方法 | [GetOutputIdleBehavior](26756c6a-3ee5-ce92-bd94-0c4cd49289a6.htm) |  |
| 公共方法 | [InitiateGeneration](81c6e55a-3b00-b35f-3488-b1228dee2558.htm) |  |
| 公共方法 | [IsTaskDone](03431a96-6f21-269b-645b-5b933afdde05.htm) |  |
| 公共方法 | [ReadMultiChannelMultiSamples](395e052c-9c29-e830-b5b6-f250ca4dc393.htm) |  |
| 公共方法 | [ReadMultiChannelSingleSample](fe055dd1-22b8-efa8-9aa1-2057eeb6e791.htm) |  |
| 公共方法 | [ReadMultiSamples](8f5b9779-4986-9d99-20f3-fabecf9eafca.htm) |  |
| 公共方法 | [ReadSingleSample](721fe9c9-b17e-2bf9-7f48-4e937593cea2.htm) |  |
| 公共方法 | [ReadWaveform](dec08e65-1525-41dc-ad63-511158777811.htm) |  |
| 公共方法 | [Reset](196a8064-6aa5-14db-b152-607f6ea4e55f.htm) |  |
| 公共方法 | [SetAIChannelMaximum](7d4092cc-1672-a648-038c-16ad77f91c45.htm) |  |
| 公共方法 | [SetAIChannelMinimum](90a4cac7-0e9b-715a-69bb-a946603980ba.htm) |  |
| 公共方法 | [SetAICoupling](9f96a006-3548-d02e-d608-5f394fbb8bf4.htm) |  |
| 公共方法 | [SetAOChannelMaximum](0aa716f7-16c5-630a-c5df-688f0ecedaa7.htm) |  |
| 公共方法 | [SetAOChannelMinimum](a8e884f6-c1df-5613-33a2-fe1b0b8d4147.htm) |  |
| 公共方法 | [SetAutoZeroMode](6da844f0-2161-e28b-e9e2-d5c156e5b7fa.htm) |  |
| 公共方法 | [SetCommonModeOffset](d9896d5f-6462-fd08-7728-4509910d531e.htm) |  |
| 公共方法 | [SetDutyCycleHigh](569c83e9-d886-b397-051e-c328ea199e2f.htm) |  |
| 公共方法 | [SetFunctionGenerationStartPhase](7b2974ec-c14c-1977-2226-0799a8d22933.htm) |  |
| 公共方法 | [SetOutputIdleBehavior](d5cb9bd1-f5b2-f258-54cd-788c758f5b1f.htm) |  |
| 公共方法 | [SetTerminalConfiguration](ba9a67d8-4291-5f8d-43d9-3d8add5d2d20.htm) |  |
| 公共方法 | [StartTask](2a547704-f2e9-709a-a2e1-0f5f93036d65.htm) |  |
| 公共方法 | [StopTask](1d0a614b-057b-e049-8015-4ed8007b7ae2.htm) |  |
| 公共方法 | [WaitForNextSampleClock](1004beb4-9820-a828-9a7b-e0c26112158a.htm) |  |
| 公共方法 | [WriteDigitalLines](9ce97b90-1a3b-5814-7dfe-c90857491772.htm) |  |
| 公共方法 | [WriteMultiChannelData](1f85c173-5b3e-1d43-80d8-835f358c9d13.htm) |  |
| 公共方法 | [WriteSingleChannelData](38ac254e-1b82-4db0-5310-f996836c05c7.htm) |  |

[Top](#PageHeader)

参见

##### 引用

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


### IDAQ_Instr 方法

|  |  |
| --- | --- |
|  | IDAQ\_Instr 方法 |

[IDAQ\_Instr](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [AbortGeneration](510ebf74-cb09-d212-2a4a-64b060d4edca.htm) |  |
| 公共方法 | [ClearTask](44b8722a-136f-49db-6be5-7863e7dd9aa6.htm) |  |
| 公共方法 | [Close](3510e391-c0d4-9b66-3e21-a28866241ad7.htm) |  |
| 公共方法 | [ConfigureMultiChannelSineWaveform](ca25afed-ca4d-41ba-9dd3-57ebdee22b7e.htm) |  |
| 公共方法 | [ConfigurePureToneWaveform](9fb8854e-2cca-4339-56fd-4e9c6a4ce192.htm) |  |
| 公共方法 | [ConfigureSampleClock](359b3a8a-7d45-bc38-ac59-cc87ea181257.htm) |  |
| 公共方法 | [ConfigureSampleClockHW](25c62125-9eb4-fe23-7270-a3c91f00ac20.htm) |  |
| 公共方法 | [ConfigureStartDigitalEdgeTrigger](6b682a31-c5a3-8665-eec8-46a9a52406ac.htm) |  |
| 公共方法 | [Control](81320f40-f907-e54f-2e3c-a8123c1a8ef4.htm) |  |
| 公共方法 | [CreateAIVoltageChannel](aa0a6cc1-4962-6dc3-fcab-98d06f5409df.htm) |  |
| 公共方法 | [CreateAOVoltageChannel](40d9b21e-c4be-3e1d-4a5d-72049b17f55a.htm) |  |
| 公共方法 | [CreateArbWaveform](d6e63738-8be2-cb6b-de0b-e74a05685f2e.htm) |  |
| 公共方法 | [CreateDOChannel](b84bf086-f8ac-05ed-9245-6854e35f7263.htm) |  |
| 公共方法 | [CreateStandardWaveform](bdb778fb-bea6-16f1-4d88-6d5afe166656.htm) |  |
| 公共方法 | [CreateTask](940b0339-099d-ea1a-8d53-c089fbc8394f.htm) |  |
| 公共方法 | [ExportStartSignal](ef1650ee-0730-5bfe-42c8-dda95b613a77.htm) |  |
| 公共方法 | [GenerateStandardWaveform](4eb956f5-e031-ac71-9737-012cc5bcaccf.htm) |  |
| 公共方法 | [GetAIChannelMaximum](a436d8b0-d363-dd15-730c-74e7c6994d0e.htm) |  |
| 公共方法 | [GetAIChannelMinimum](261d8c99-7ea1-fb26-f53e-87a95827c70d.htm) |  |
| 公共方法 | [GetAOChannelMaximum](cf1e8dee-c47d-6be1-2b3d-a27b9c3c7cba.htm) |  |
| 公共方法 | [GetAOChannelMinimum](9350206d-37d8-000d-c3e9-bd4278de33fe.htm) |  |
| 公共方法 | [GetAutoZeroMode](ae9255d7-7d23-e0db-391a-9722352a6fc3.htm) |  |
| 公共方法 | [GetDutyCycleHigh](7d236124-169d-8517-d0a2-2efd62fd2b19.htm) |  |
| 公共方法 | [GetFunctionGenerationStartPhase](bb235796-2be8-193e-4002-461770b25257.htm) |  |
| 公共方法 | [GetOutputIdleBehavior](26756c6a-3ee5-ce92-bd94-0c4cd49289a6.htm) |  |
| 公共方法 | [InitiateGeneration](81c6e55a-3b00-b35f-3488-b1228dee2558.htm) |  |
| 公共方法 | [IsTaskDone](03431a96-6f21-269b-645b-5b933afdde05.htm) |  |
| 公共方法 | [ReadMultiChannelMultiSamples](395e052c-9c29-e830-b5b6-f250ca4dc393.htm) |  |
| 公共方法 | [ReadMultiChannelSingleSample](fe055dd1-22b8-efa8-9aa1-2057eeb6e791.htm) |  |
| 公共方法 | [ReadMultiSamples](8f5b9779-4986-9d99-20f3-fabecf9eafca.htm) |  |
| 公共方法 | [ReadSingleSample](721fe9c9-b17e-2bf9-7f48-4e937593cea2.htm) |  |
| 公共方法 | [ReadWaveform](dec08e65-1525-41dc-ad63-511158777811.htm) |  |
| 公共方法 | [Reset](196a8064-6aa5-14db-b152-607f6ea4e55f.htm) |  |
| 公共方法 | [SetAIChannelMaximum](7d4092cc-1672-a648-038c-16ad77f91c45.htm) |  |
| 公共方法 | [SetAIChannelMinimum](90a4cac7-0e9b-715a-69bb-a946603980ba.htm) |  |
| 公共方法 | [SetAICoupling](9f96a006-3548-d02e-d608-5f394fbb8bf4.htm) |  |
| 公共方法 | [SetAOChannelMaximum](0aa716f7-16c5-630a-c5df-688f0ecedaa7.htm) |  |
| 公共方法 | [SetAOChannelMinimum](a8e884f6-c1df-5613-33a2-fe1b0b8d4147.htm) |  |
| 公共方法 | [SetAutoZeroMode](6da844f0-2161-e28b-e9e2-d5c156e5b7fa.htm) |  |
| 公共方法 | [SetCommonModeOffset](d9896d5f-6462-fd08-7728-4509910d531e.htm) |  |
| 公共方法 | [SetDutyCycleHigh](569c83e9-d886-b397-051e-c328ea199e2f.htm) |  |
| 公共方法 | [SetFunctionGenerationStartPhase](7b2974ec-c14c-1977-2226-0799a8d22933.htm) |  |
| 公共方法 | [SetOutputIdleBehavior](d5cb9bd1-f5b2-f258-54cd-788c758f5b1f.htm) |  |
| 公共方法 | [SetTerminalConfiguration](ba9a67d8-4291-5f8d-43d9-3d8add5d2d20.htm) |  |
| 公共方法 | [StartTask](2a547704-f2e9-709a-a2e1-0f5f93036d65.htm) |  |
| 公共方法 | [StopTask](1d0a614b-057b-e049-8015-4ed8007b7ae2.htm) |  |
| 公共方法 | [WaitForNextSampleClock](1004beb4-9820-a828-9a7b-e0c26112158a.htm) |  |
| 公共方法 | [WriteDigitalLines](9ce97b90-1a3b-5814-7dfe-c90857491772.htm) |  |
| 公共方法 | [WriteMultiChannelData](1f85c173-5b3e-1d43-80d8-835f358c9d13.htm) |  |
| 公共方法 | [WriteSingleChannelData](38ac254e-1b82-4db0-5310-f996836c05c7.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### AbortGeneration 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrAbortGeneration 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void AbortGeneration(
	string channelNumber,
	string Label
)
```

###### 参数

channelNumber  String

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ClearTask 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrClearTask 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ClearTask(
	string channelNumber,
	string Label
)
```

###### 参数

channelNumber  String

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### Close 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrClose 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Close()
```

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ConfigureMultiChannelSineWaveform 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrConfigureMultiChannelSineWaveform 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureMultiChannelSineWaveform(
	string channelNumber,
	double amplitude,
	double dcOffset,
	double frequency,
	string PhaseArray,
	string Label
)
```

###### 参数

channelNumber  String

amplitude  Double

dcOffset  Double

frequency  Double

PhaseArray  String

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ConfigurePureToneWaveform 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrConfigurePureToneWaveform 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigurePureToneWaveform(
	string channelNumber,
	string waveformType,
	double amplitude,
	double dcOffset,
	double frequency,
	string Label
)
```

###### 参数

channelNumber  String

waveformType  String

amplitude  Double

dcOffset  Double

frequency  Double

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ConfigureSampleClock 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrConfigureSampleClock 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureSampleClock(
	string channelNumber,
	string source,
	double rate,
	int samplesPerChannel,
	bool continuous = true,
	string Label = ""
)
```

###### 参数

channelNumber  String

source  String

rate  Double

samplesPerChannel  Int32

continuous  Boolean  (Optional)

Label  String  (Optional)

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ConfigureSampleClockHW 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrConfigureSampleClockHW 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureSampleClockHW(
	string channelNumber,
	double rate,
	string Label
)
```

###### 参数

channelNumber  String

rate  Double

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ConfigureStartDigitalEdgeTrigger 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrConfigureStartDigitalEdgeTrigger 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureStartDigitalEdgeTrigger(
	string channelNumber,
	string source,
	string edgeType,
	string Label
)
```

###### 参数

channelNumber  String

source  String

edgeType  String

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### Control 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrControl 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Control(
	string channelNumber,
	string taskAction,
	string Label
)
```

###### 参数

channelNumber  String

taskAction  String

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### CreateAIVoltageChannel 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrCreateAIVoltageChannel 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void CreateAIVoltageChannel(
	string channelNumber,
	double minimumValue = -10,
	double maximumValue = 10,
	string units = "Volts",
	string Label = ""
)
```

###### 参数

channelNumber  String

minimumValue  Double  (Optional)

maximumValue  Double  (Optional)

units  String  (Optional)

Label  String  (Optional)

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### CreateAOVoltageChannel 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrCreateAOVoltageChannel 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void CreateAOVoltageChannel(
	string channelNumber,
	double minimumValue = -10,
	double maximumValue = 10,
	string units = "Volts",
	string Label = ""
)
```

###### 参数

channelNumber  String

minimumValue  Double  (Optional)

maximumValue  Double  (Optional)

units  String  (Optional)

Label  String  (Optional)

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### CreateArbWaveform 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrCreateArbWaveform 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void CreateArbWaveform(
	string channelNumber,
	double[] data,
	string Label
)
```

###### 参数

channelNumber  String

data  Double

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### CreateDOChannel 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrCreateDOChannel 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void CreateDOChannel(
	string channelNumber,
	string lines,
	string nameToAssignToLines,
	int lineGrouping,
	string Label
)
```

###### 参数

channelNumber  String

lines  String

nameToAssignToLines  String

lineGrouping  Int32

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### CreateStandardWaveform 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrCreateStandardWaveform 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void CreateStandardWaveform(
	string channelNumber,
	string waveformFunction,
	double amplitude,
	double dcOffset,
	double frequency,
	double startPhase,
	string Label
)
```

###### 参数

channelNumber  String

waveformFunction  String

amplitude  Double

dcOffset  Double

frequency  Double

startPhase  Double

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### CreateTask 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrCreateTask 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void CreateTask(
	string channelNumber,
	string Label
)
```

###### 参数

channelNumber  String

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ExportStartSignal 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrExportStartSignal 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ExportStartSignal(
	string channelNumber,
	string outputTerminal,
	string Label
)
```

###### 参数

channelNumber  String

outputTerminal  String

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### GenerateStandardWaveform 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrGenerateStandardWaveform 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
Dictionary<string, double[]> GenerateStandardWaveform(
	string channelNumber,
	string waveformFunction,
	double amplitude,
	double dcOffset,
	double frequency,
	double startPhase,
	string Label
)
```

###### 参数

channelNumber  String

waveformFunction  String

amplitude  Double

dcOffset  Double

frequency  Double

startPhase  Double

Label  String

###### 返回值

DictionaryString, Double

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### GetAIChannelMaximum 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrGetAIChannelMaximum 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] GetAIChannelMaximum(
	string channelNumber,
	string Label
)
```

###### 参数

channelNumber  String

Label  String

###### 返回值

Double

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### GetAIChannelMinimum 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrGetAIChannelMinimum 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] GetAIChannelMinimum(
	string channelNumber,
	string Label
)
```

###### 参数

channelNumber  String

Label  String

###### 返回值

Double

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### GetAOChannelMaximum 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrGetAOChannelMaximum 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] GetAOChannelMaximum(
	string channelNumber,
	string Label
)
```

###### 参数

channelNumber  String

Label  String

###### 返回值

Double

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### GetAOChannelMinimum 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrGetAOChannelMinimum 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] GetAOChannelMinimum(
	string channelNumber,
	string Label
)
```

###### 参数

channelNumber  String

Label  String

###### 返回值

Double

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### GetAutoZeroMode 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrGetAutoZeroMode 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string[] GetAutoZeroMode(
	string channelNumber,
	string Label
)
```

###### 参数

channelNumber  String

Label  String

###### 返回值

String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### GetDutyCycleHigh 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrGetDutyCycleHigh 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetDutyCycleHigh(
	string channelNumber,
	string Label
)
```

###### 参数

channelNumber  String

Label  String

###### 返回值

Double

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### GetFunctionGenerationStartPhase 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrGetFunctionGenerationStartPhase 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] GetFunctionGenerationStartPhase(
	string channelNumber,
	string Label
)
```

###### 参数

channelNumber  String

Label  String

###### 返回值

Double

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### GetOutputIdleBehavior 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrGetOutputIdleBehavior 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string[] GetOutputIdleBehavior(
	string channelNumber,
	string Label
)
```

###### 参数

channelNumber  String

Label  String

###### 返回值

String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### InitiateGeneration 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrInitiateGeneration 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void InitiateGeneration(
	string channelNumber,
	string Label
)
```

###### 参数

channelNumber  String

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### IsTaskDone 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrIsTaskDone 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool IsTaskDone(
	string channelNumber,
	string Label
)
```

###### 参数

channelNumber  String

Label  String

###### 返回值

Boolean

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ReadMultiChannelMultiSamples 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrReadMultiChannelMultiSamples 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
Dictionary<string, double[]> ReadMultiChannelMultiSamples(
	string channelNumber,
	int sampleNumber,
	double timeout,
	string Label
)
```

###### 参数

channelNumber  String

sampleNumber  Int32

timeout  Double

Label  String

###### 返回值

DictionaryString, Double

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ReadMultiChannelSingleSample 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrReadMultiChannelSingleSample 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] ReadMultiChannelSingleSample(
	string channelNumber,
	double timeout,
	string Label
)
```

###### 参数

channelNumber  String

timeout  Double

Label  String

###### 返回值

Double

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ReadMultiSamples 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrReadMultiSamples 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
Dictionary<string, double[]> ReadMultiSamples(
	string channelNumber,
	int sampleNumber,
	string Label
)
```

###### 参数

channelNumber  String

sampleNumber  Int32

Label  String

###### 返回值

DictionaryString, Double

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ReadSingleSample 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrReadSingleSample 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double ReadSingleSample(
	string channelNumber,
	string Label
)
```

###### 参数

channelNumber  String

Label  String

###### 返回值

Double

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### ReadWaveform 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrReadWaveform 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
Dictionary<string, double[]> ReadWaveform(
	string channelNumber,
	int samplesPerChannel,
	string Label
)
```

###### 参数

channelNumber  String

samplesPerChannel  Int32

Label  String

###### 返回值

DictionaryString, Double

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### Reset 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrReset 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Reset()
```

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### SetAIChannelMaximum 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrSetAIChannelMaximum 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetAIChannelMaximum(
	string channelNumber,
	double channelMaximum,
	string Label
)
```

###### 参数

channelNumber  String

channelMaximum  Double

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### SetAIChannelMinimum 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrSetAIChannelMinimum 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetAIChannelMinimum(
	string channelNumber,
	double channelMinimum,
	string Label
)
```

###### 参数

channelNumber  String

channelMinimum  Double

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### SetAICoupling 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrSetAICoupling 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetAICoupling(
	string channelNumber,
	string CPLMode,
	string Label
)
```

###### 参数

channelNumber  String

CPLMode  String

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### SetAOChannelMaximum 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrSetAOChannelMaximum 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetAOChannelMaximum(
	string channelNumber,
	double channelMaximum,
	string Label
)
```

###### 参数

channelNumber  String

channelMaximum  Double

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### SetAOChannelMinimum 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrSetAOChannelMinimum 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetAOChannelMinimum(
	string channelNumber,
	double channelMinimum,
	string Label
)
```

###### 参数

channelNumber  String

channelMinimum  Double

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### SetAutoZeroMode 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrSetAutoZeroMode 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetAutoZeroMode(
	string channelNumber,
	string autoZeroMode,
	string Label
)
```

###### 参数

channelNumber  String

autoZeroMode  String

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### SetCommonModeOffset 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrSetCommonModeOffset 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetCommonModeOffset(
	string channelNumber,
	double commonModeOffset,
	string Label
)
```

###### 参数

channelNumber  String

commonModeOffset  Double

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### SetDutyCycleHigh 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrSetDutyCycleHigh 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetDutyCycleHigh(
	string channelNumber,
	double dutyCycleHigh,
	string Label
)
```

###### 参数

channelNumber  String

dutyCycleHigh  Double

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### SetFunctionGenerationStartPhase 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrSetFunctionGenerationStartPhase 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetFunctionGenerationStartPhase(
	string channelNumber,
	double startPhase,
	string Label
)
```

###### 参数

channelNumber  String

startPhase  Double

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### SetOutputIdleBehavior 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrSetOutputIdleBehavior 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetOutputIdleBehavior(
	string channelNumber,
	string behavior,
	string Label
)
```

###### 参数

channelNumber  String

behavior  String

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### SetTerminalConfiguration 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrSetTerminalConfiguration 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetTerminalConfiguration(
	string channelNumber,
	string configuration,
	string Label
)
```

###### 参数

channelNumber  String

configuration  String

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### StartTask 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrStartTask 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void StartTask(
	string channelNumber,
	string Label
)
```

###### 参数

channelNumber  String

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### StopTask 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrStopTask 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void StopTask(
	string channelNumber,
	string Label
)
```

###### 参数

channelNumber  String

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### WaitForNextSampleClock 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrWaitForNextSampleClock 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool WaitForNextSampleClock(
	string channelNumber,
	double timeout,
	string Label
)
```

###### 参数

channelNumber  String

timeout  Double

Label  String

###### 返回值

Boolean

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### WriteDigitalLines 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrWriteDigitalLines 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteDigitalLines(
	string channelNumber,
	bool autoStart,
	bool[] writeArray,
	string Label
)
```

###### 参数

channelNumber  String

autoStart  Boolean

writeArray  Boolean

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### WriteMultiChannelData 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrWriteMultiChannelData 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteMultiChannelData(
	string channelNumber,
	double[,] data,
	string Label
)
```

###### 参数

channelNumber  String

data  Double

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)


#### WriteSingleChannelData 方法

|  |  |
| --- | --- |
|  | IDAQ\_InstrWriteSingleChannelData 方法 |

  
**命名空间：** [DAQParent](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)  
**程序集：** DAQMeasStation (在 DAQMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteSingleChannelData(
	string channelNumber,
	double[] data,
	string Label
)
```

###### 参数

channelNumber  String

data  Double

Label  String

参见

###### 引用

[IDAQ\_Instr 接口](95a999bf-6fe0-fc7a-6979-b26d5e157612.htm)

[DAQParent 命名空间](4d3f6761-be49-c138-d4c7-0b6fe1ac5938.htm)

