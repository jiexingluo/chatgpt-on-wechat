|  |  |
| --- | --- |
|  | Guwave.OneTest.TestMethod 命名空间 |

类

|  | 类 | 说明 |
| --- | --- | --- |
| 公共类 | [DialogResult](853d1712-49b1-bd6a-0ebb-f7783b5975a3.htm) |  |
| 公共类 | [InputGroupParamAttribute](cce82ed5-f9cd-2fee-ea69-2e9cebef8a2c.htm) |  |
| 公共类 | [InputParamAttribute](b8a6b68c-b60b-2702-a248-5e92a3479efe.htm) |  |
| 公共类 | [PartVariables](c281af04-b2cd-2012-8377-2634a3da8931.htm) |  |
| 公共类 | [ProgramVariables](44493283-e635-f7bf-6080-ef8f86b3f1a2.htm) |  |
| 公共类 | [SemiContext](421aec95-4c88-392e-653b-28511d2c5421.htm) | 仪表操作接口上下文 |
| 公共类 | [TestBinResult](c05768d0-3a5a-71cc-9d5f-0d0f16602f5f.htm) |  |
| 公共类 | [TestMethod](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm) | C#类型TestMethod基类，用户添加C#类型的TestMethod必须集成此类 |

接口

|  | 接口 | 说明 |
| --- | --- | --- |
| 公共接口 | [FunctionalTestDescriptor](dc3cf586-a6b2-712e-28e1-51c40cc39fa1.htm) | 基于功能的测项定义 |
| 公共接口 | [IFileAccessor](dc5e402a-56da-a9ac-1101-94bfb5c693dd.htm) | 用户在TM中可以记录自定义的数据信息 |
| 公共接口 | [IFrontDialog](967e7930-ec11-55ba-71d5-ba173c681598.htm) |  |
| 公共接口 | [IHist](68ea8fb9-b1dc-07d4-eb20-70e4ac475178.htm) | 直方图显示和导出接口 |
| 公共接口 | [IInstrumentAccessor](8365c067-d962-ccb8-21df-9617210b236d.htm) | 仪表访问器 |
| 公共接口 | [IPinmapAccessor](c31b9fa6-009d-3188-6deb-bca1d67c7cc7.htm) | Pin连接信息访问器 |
| 公共接口 | [IPlot](36365182-b589-2e22-ed58-95684d8fb7d6.htm) | 折线图显示和导出接口 |
| 公共接口 | [IRawData](61e036ef-d223-3b58-9ca2-b89e8fea7254.htm) |  |
| 公共接口 | [IRegisterAccessor](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm) | Register访问器 |
| 公共接口 | [ISwitchAccessor](f4adcf92-99fb-8004-0cf6-b59040e967eb.htm) | 继电器操作接口 |
| 公共接口 | [ITestMethod](c4400014-a326-7727-d895-39228f0667f3.htm) |  |
| 公共接口 | [IVariableAccessor](6e6124cd-87b1-6191-bf37-5a6153dcae9c.htm) |  |
| 公共接口 | [ParametricTestDescriptor](3889512c-1f25-5aea-bfc4-901b516e0e52.htm) | 基于参数的测项定义 |

枚举

|  | 枚举 | 说明 |
| --- | --- | --- |
| 公共枚举 | [DataType](4da48b7d-9aa8-b509-34a2-0e424ff543c9.htm) |  |
| 公共枚举 | [InstrumentType](07ed3860-185c-858d-e20a-a0cffa6b13d2.htm) |  |
| 公共枚举 | [LogLevel](aaec65d4-7cb4-f48d-80f6-03bb853b8d2b.htm) |  |
| 公共枚举 | [NumberBase](050f54bd-af30-c1e9-4a9e-123e9fa0664d.htm) | 整数进制枚举类 |
| 公共枚举 | [PinType](4f676645-359f-b1e1-862d-e363d7ea1ee8.htm) |  |
| 公共枚举 | [ScalingFactor](d86ddfe9-c36a-ccd6-5f24-8403d81b3783.htm) |  |


## DataType 枚举

|  |  |
| --- | --- |
|  | DataType 枚举 |

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public enum DataType
```

成员

| 成员名称 | 值 | 说明 |
| --- | --- | --- |
| String | 0 |  |
| Int | 1 |  |
| Double | 2 |  |
| Long | 3 |  |
| Ulong | 4 |  |
| Bool | 5 |  |

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## DialogResult 类

|  |  |
| --- | --- |
|  | DialogResult 类 |

继承层次

SystemObject
  
  Guwave.OneTest.TestMethodDialogResult

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public class DialogResult
```

DialogResult 类型公开以下成员。

构造函数

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [DialogResult](27ddc17f-56d3-276c-2826-515209ad7776.htm) | 初始化 DialogResult 类的一个新实例 |

[Top](#PageHeader)

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [ButtonKey](7a2b1eb7-8e08-baed-2acd-6a9ca2412dea.htm) |  |
| 公共属性 | [InputData](1c584787-507b-fd84-e675-60adfddba81e.htm) |  |

[Top](#PageHeader)

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |

[Top](#PageHeader)

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### DialogResult 构造函数

|  |  |
| --- | --- |
|  | DialogResult 构造函数 |

初始化 [DialogResult](853d1712-49b1-bd6a-0ebb-f7783b5975a3.htm) 类的一个新实例

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DialogResult()
```

参见

###### 引用

[DialogResult 类](853d1712-49b1-bd6a-0ebb-f7783b5975a3.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### DialogResult 属性

|  |  |
| --- | --- |
|  | DialogResult 属性 |

[DialogResult](853d1712-49b1-bd6a-0ebb-f7783b5975a3.htm) 类型公开以下成员。

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [ButtonKey](7a2b1eb7-8e08-baed-2acd-6a9ca2412dea.htm) |  |
| 公共属性 | [InputData](1c584787-507b-fd84-e675-60adfddba81e.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[DialogResult 类](853d1712-49b1-bd6a-0ebb-f7783b5975a3.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### ButtonKey 属性

|  |  |
| --- | --- |
|  | DialogResultButtonKey 属性 |

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string ButtonKey { get; set; }
```

###### 属性值

String

参见

###### 引用

[DialogResult 类](853d1712-49b1-bd6a-0ebb-f7783b5975a3.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### InputData 属性

|  |  |
| --- | --- |
|  | DialogResultInputData 属性 |

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> InputData { get; set; }
```

###### 属性值

DictionaryString, String

参见

###### 引用

[DialogResult 类](853d1712-49b1-bd6a-0ebb-f7783b5975a3.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### DialogResult 方法

|  |  |
| --- | --- |
|  | DialogResult 方法 |

[DialogResult](853d1712-49b1-bd6a-0ebb-f7783b5975a3.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |

[Top](#PageHeader)

参见

###### 引用

[DialogResult 类](853d1712-49b1-bd6a-0ebb-f7783b5975a3.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## FunctionalTestDescriptor 接口

|  |  |
| --- | --- |
|  | FunctionalTestDescriptor 接口 |

基于功能的测项定义

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public interface FunctionalTestDescriptor
```

FunctionalTestDescriptor 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Concat](c4b4d562-bd14-49aa-6d98-4827557ed93c.htm) | 修改或新增Evaluation设置 |
| 公共方法 | [Evaluate(Boolean)](c62c4ebe-10cb-99ab-edbc-f6d4db1a5e78.htm) | 对测量值进行evaluate，结果将在界面和report体现 |
| 公共方法 | [Evaluate(DictionaryString, Boolean)](9c42f565-cead-8be8-fa0f-a66f7586f457.htm) | 对测量值进行evaluate，结果将在界面和report体现 |
| 公共方法 | [GetSubEvaluater](d17b8e6b-8064-8dcd-a20f-bf72a75c9d42.htm) | 获取当前Evaluation子级Evaluation |
| 公共方法 | [Publish(Boolean)](c430e232-f246-0cbd-f31f-234588c573c9.htm) | 对测量值进行Publish，结果将在界面和report体现, 不影响分Bin |
| 公共方法 | [Publish(DictionaryString, Boolean)](4491f354-df30-5dae-e705-0f2b7314152a.htm) | 对测量值进行Publish，结果将在界面和report体现, 不影响分Bin |

[Top](#PageHeader)

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### FunctionalTestDescriptor 方法

|  |  |
| --- | --- |
|  | FunctionalTestDescriptor 方法 |

[FunctionalTestDescriptor](dc3cf586-a6b2-712e-28e1-51c40cc39fa1.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Concat](c4b4d562-bd14-49aa-6d98-4827557ed93c.htm) | 修改或新增Evaluation设置 |
| 公共方法 | [Evaluate(Boolean)](c62c4ebe-10cb-99ab-edbc-f6d4db1a5e78.htm) | 对测量值进行evaluate，结果将在界面和report体现 |
| 公共方法 | [Evaluate(DictionaryString, Boolean)](9c42f565-cead-8be8-fa0f-a66f7586f457.htm) | 对测量值进行evaluate，结果将在界面和report体现 |
| 公共方法 | [GetSubEvaluater](d17b8e6b-8064-8dcd-a20f-bf72a75c9d42.htm) | 获取当前Evaluation子级Evaluation |
| 公共方法 | [Publish(Boolean)](c430e232-f246-0cbd-f31f-234588c573c9.htm) | 对测量值进行Publish，结果将在界面和report体现, 不影响分Bin |
| 公共方法 | [Publish(DictionaryString, Boolean)](4491f354-df30-5dae-e705-0f2b7314152a.htm) | 对测量值进行Publish，结果将在界面和report体现, 不影响分Bin |

[Top](#PageHeader)

参见

###### 引用

[FunctionalTestDescriptor 接口](dc3cf586-a6b2-712e-28e1-51c40cc39fa1.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Concat 方法

|  |  |
| --- | --- |
|  | FunctionalTestDescriptorConcat 方法 |

修改或新增Evaluation设置

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Concat(
	uint testNumber,
	string testName,
	string testText,
	int softBin = 2147483647,
	string outputVariable = ""
)
```

###### 参数

testNumber  UInt32
:   要设置的Test Number

testName  String
:   要设置的Test Name

testText  String
:   要设置的Test Text

softBin  Int32  (Optional)
:   要设置的SoftBin Number，可选参数

outputVariable  String  (Optional)
:   要设置的Output Variable，可选参数

参见

###### 引用

[FunctionalTestDescriptor 接口](dc3cf586-a6b2-712e-28e1-51c40cc39fa1.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Evaluate 方法

|  |  |
| --- | --- |
|  | FunctionalTestDescriptorEvaluate 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Evaluate(Boolean)](c62c4ebe-10cb-99ab-edbc-f6d4db1a5e78.htm) | 对测量值进行evaluate，结果将在界面和report体现 |
| 公共方法 | [Evaluate(DictionaryString, Boolean)](9c42f565-cead-8be8-fa0f-a66f7586f457.htm) | 对测量值进行evaluate，结果将在界面和report体现 |

[Top](#PageHeader)

参见

###### 引用

[FunctionalTestDescriptor 接口](dc3cf586-a6b2-712e-28e1-51c40cc39fa1.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Evaluate(Boolean) 方法

|  |  |
| --- | --- |
|  | FunctionalTestDescriptorEvaluate(Boolean) 方法 |

对测量值进行evaluate，结果将在界面和report体现

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Evaluate(
	bool result
)
```

###### 参数

result  Boolean
:   测量值,一般情况下此数值由meastation测量方法返回

参见

###### 引用

[FunctionalTestDescriptor 接口](dc3cf586-a6b2-712e-28e1-51c40cc39fa1.htm)

[Evaluate 重载](0c4b90c7-7551-ad1a-1195-f6f04dfab113.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Evaluate(Dictionary&lt;String, Boolean&gt;) 方法

|  |  |
| --- | --- |
|  | FunctionalTestDescriptorEvaluate(DictionaryString, Boolean) 方法 |

对测量值进行evaluate，结果将在界面和report体现

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Evaluate(
	Dictionary<string, bool> resultDict
)
```

###### 参数

resultDict  DictionaryString, Boolean
:   字典作为输入参数,其中key表示的是引脚,value表示测量值,一般情况下此数值由meastation测量方法返回

参见

###### 引用

[FunctionalTestDescriptor 接口](dc3cf586-a6b2-712e-28e1-51c40cc39fa1.htm)

[Evaluate 重载](0c4b90c7-7551-ad1a-1195-f6f04dfab113.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetSubEvaluater 方法

|  |  |
| --- | --- |
|  | FunctionalTestDescriptorGetSubEvaluater 方法 |

获取当前Evaluation子级Evaluation

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
FunctionalTestDescriptor GetSubEvaluater(
	string subName
)
```

###### 参数

subName  String
:   子级Evaluation的Name，横杠后面的部分

###### 返回值

[FunctionalTestDescriptor](dc3cf586-a6b2-712e-28e1-51c40cc39fa1.htm)  
子级Evaluater

参见

###### 引用

[FunctionalTestDescriptor 接口](dc3cf586-a6b2-712e-28e1-51c40cc39fa1.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Publish 方法

|  |  |
| --- | --- |
|  | FunctionalTestDescriptorPublish 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Publish(Boolean)](c430e232-f246-0cbd-f31f-234588c573c9.htm) | 对测量值进行Publish，结果将在界面和report体现, 不影响分Bin |
| 公共方法 | [Publish(DictionaryString, Boolean)](4491f354-df30-5dae-e705-0f2b7314152a.htm) | 对测量值进行Publish，结果将在界面和report体现, 不影响分Bin |

[Top](#PageHeader)

参见

###### 引用

[FunctionalTestDescriptor 接口](dc3cf586-a6b2-712e-28e1-51c40cc39fa1.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Publish(Boolean) 方法

|  |  |
| --- | --- |
|  | FunctionalTestDescriptorPublish(Boolean) 方法 |

对测量值进行Publish，结果将在界面和report体现, 不影响分Bin

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Publish(
	bool result
)
```

###### 参数

result  Boolean
:   测量值,一般情况下此数值由meastation测量方法返回

参见

###### 引用

[FunctionalTestDescriptor 接口](dc3cf586-a6b2-712e-28e1-51c40cc39fa1.htm)

[Publish 重载](c60d4363-3d56-f8aa-b637-57e9a1b06891.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Publish(Dictionary&lt;String, Boolean&gt;) 方法

|  |  |
| --- | --- |
|  | FunctionalTestDescriptorPublish(DictionaryString, Boolean) 方法 |

对测量值进行Publish，结果将在界面和report体现, 不影响分Bin

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Publish(
	Dictionary<string, bool> resultDict
)
```

###### 参数

resultDict  DictionaryString, Boolean
:   字典作为输入参数,其中key表示的是引脚,value表示测量值,一般情况下此数值由meastation测量方法返回

参见

###### 引用

[FunctionalTestDescriptor 接口](dc3cf586-a6b2-712e-28e1-51c40cc39fa1.htm)

[Publish 重载](c60d4363-3d56-f8aa-b637-57e9a1b06891.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## IFileAccessor 接口

|  |  |
| --- | --- |
|  | IFileAccessor 接口 |

用户在TM中可以记录自定义的数据信息

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public interface IFileAccessor
```

IFileAccessor 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [WriteFileToProjectPath(String, Byte, Boolean)](50976971-82e8-05a4-799c-4f02ee40859e.htm) | 以覆盖模式将字节数据直接写入项目目录下的指定文件中 |
| 公共方法 | [WriteFileToProjectPath(String, String, Boolean)](a063a399-f662-fdfc-6c9e-5636fd7852ef.htm) | 以覆盖模式将文本数据直接写入项目目录下的指定文件中 |
| 公共方法 | [WriteLine](bcbd1310-7cb5-2062-0d81-16dcb9170138.htm) | 向全局文件以追加模式写入一行文本（每次Debug产生一个新的文件） |

[Top](#PageHeader)

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### IFileAccessor 方法

|  |  |
| --- | --- |
|  | IFileAccessor 方法 |

[IFileAccessor](dc5e402a-56da-a9ac-1101-94bfb5c693dd.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [WriteFileToProjectPath(String, Byte, Boolean)](50976971-82e8-05a4-799c-4f02ee40859e.htm) | 以覆盖模式将字节数据直接写入项目目录下的指定文件中 |
| 公共方法 | [WriteFileToProjectPath(String, String, Boolean)](a063a399-f662-fdfc-6c9e-5636fd7852ef.htm) | 以覆盖模式将文本数据直接写入项目目录下的指定文件中 |
| 公共方法 | [WriteLine](bcbd1310-7cb5-2062-0d81-16dcb9170138.htm) | 向全局文件以追加模式写入一行文本（每次Debug产生一个新的文件） |

[Top](#PageHeader)

参见

###### 引用

[IFileAccessor 接口](dc5e402a-56da-a9ac-1101-94bfb5c693dd.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### WriteFileToProjectPath 方法

|  |  |
| --- | --- |
|  | IFileAccessorWriteFileToProjectPath 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [WriteFileToProjectPath(String, Byte, Boolean)](50976971-82e8-05a4-799c-4f02ee40859e.htm) | 以覆盖模式将字节数据直接写入项目目录下的指定文件中 |
| 公共方法 | [WriteFileToProjectPath(String, String, Boolean)](a063a399-f662-fdfc-6c9e-5636fd7852ef.htm) | 以覆盖模式将文本数据直接写入项目目录下的指定文件中 |

[Top](#PageHeader)

参见

###### 引用

[IFileAccessor 接口](dc5e402a-56da-a9ac-1101-94bfb5c693dd.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### WriteFileToProjectPath(String, Byte[], Boolean) 方法

|  |  |
| --- | --- |
|  | IFileAccessorWriteFileToProjectPath(String, Byte, Boolean) 方法 |

以覆盖模式将字节数据直接写入项目目录下的指定文件中

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteFileToProjectPath(
	string relativePath,
	byte[] bytes,
	bool wait = false
)
```

###### 参数

relativePath  String
:   文件相等路径名称

bytes  Byte
:   数据内容字节数组

wait  Boolean  (Optional)
:   是否等待文件上传完成

参见

###### 引用

[IFileAccessor 接口](dc5e402a-56da-a9ac-1101-94bfb5c693dd.htm)

[WriteFileToProjectPath 重载](be3526fa-c5fe-f5b7-2a2e-de0f3457e8f5.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### WriteFileToProjectPath(String, String, Boolean) 方法

|  |  |
| --- | --- |
|  | IFileAccessorWriteFileToProjectPath(String, String, Boolean) 方法 |

以覆盖模式将文本数据直接写入项目目录下的指定文件中

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteFileToProjectPath(
	string relativePath,
	string text,
	bool wait = false
)
```

###### 参数

relativePath  String
:   文件相等路径名称

text  String
:   文本数据内容

wait  Boolean  (Optional)
:   是否等待文件上传完成

参见

###### 引用

[IFileAccessor 接口](dc5e402a-56da-a9ac-1101-94bfb5c693dd.htm)

[WriteFileToProjectPath 重载](be3526fa-c5fe-f5b7-2a2e-de0f3457e8f5.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### WriteLine 方法

|  |  |
| --- | --- |
|  | IFileAccessorWriteLine 方法 |

向全局文件以追加模式写入一行文本（每次Debug产生一个新的文件）

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteLine(
	string lineContent
)
```

###### 参数

lineContent  String

参见

###### 引用

[IFileAccessor 接口](dc5e402a-56da-a9ac-1101-94bfb5c693dd.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## IFrontDialog 接口

|  |  |
| --- | --- |
|  | IFrontDialog 接口 |

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public interface IFrontDialog
```

IFrontDialog 类型公开以下成员。

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [Description](20ee1050-3bc3-4ddb-8878-da23708afced.htm) | 在Dialog内部显示的描述信息 |
| 公共属性 | [DialogTitle](74335628-5b6f-16f9-248d-df2d018df98a.htm) | Dialog的标题 |

[Top](#PageHeader)

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [AddButton](03f7c0af-32ee-99fc-2bbc-ca407e065408.htm) | 给Dialog添加Button，默认只有一个OK按钮 |
| 公共方法 | [AddCheckGroup](57065d86-958c-2edd-4b83-69b0fabc9551.htm) | 给Dialog添加复选框组表单 |
| 公共方法 | [AddInputForm](cc91f3a4-5160-f83c-c8d3-8cf0b9d00c30.htm) | 给Dialog添加文本输入表单 |
| 公共方法 | [AddNumberSelect](18480e49-2e23-deb9-90c6-3f0d61703133.htm) | 给Dialog添加数字选择表单 |
| 公共方法 | [AddRadioGroup](fe40703c-728a-da78-f663-a2e1075fd01c.htm) | 给Dialog添加单选按钮组表单 |
| 公共方法 | [AddSelectForm](a32fe868-376e-e3d4-11e4-bea7b40d10fe.htm) | 给Dialog添加下来选择表单 |
| 公共方法 | [ClearForms](a82f13c3-bc94-ef5d-a302-c1776b42fa4b.htm) | 清除已经添加的Form表单 |
| 公共方法 | [RemoveButton](f9db861b-9a4d-55d6-4e15-00409e0ebbc7.htm) | 删除已经添加的Button |
| 公共方法 | [RemoveForm](31ef2860-1c04-3ad9-d2a6-182c57868eb8.htm) | 删除已经添加的表单 |
| 公共方法 | [Show](588d788b-6263-c6a6-9b90-b6d95b422858.htm) | 显示对话框 |
| 公共方法 | [ShowForResult](a6dfe9b2-5799-cfd4-8630-4777ca05a1f9.htm) | 显示对话框并获取用户输入结果 |

[Top](#PageHeader)

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### IFrontDialog 属性

|  |  |
| --- | --- |
|  | IFrontDialog 属性 |

[IFrontDialog](967e7930-ec11-55ba-71d5-ba173c681598.htm) 类型公开以下成员。

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [Description](20ee1050-3bc3-4ddb-8878-da23708afced.htm) | 在Dialog内部显示的描述信息 |
| 公共属性 | [DialogTitle](74335628-5b6f-16f9-248d-df2d018df98a.htm) | Dialog的标题 |

[Top](#PageHeader)

参见

###### 引用

[IFrontDialog 接口](967e7930-ec11-55ba-71d5-ba173c681598.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Description 属性

|  |  |
| --- | --- |
|  | IFrontDialogDescription 属性 |

在Dialog内部显示的描述信息

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string Description { get; set; }
```

###### 属性值

String

参见

###### 引用

[IFrontDialog 接口](967e7930-ec11-55ba-71d5-ba173c681598.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### DialogTitle 属性

|  |  |
| --- | --- |
|  | IFrontDialogDialogTitle 属性 |

Dialog的标题

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string DialogTitle { get; set; }
```

###### 属性值

String

参见

###### 引用

[IFrontDialog 接口](967e7930-ec11-55ba-71d5-ba173c681598.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### IFrontDialog 方法

|  |  |
| --- | --- |
|  | IFrontDialog 方法 |

[IFrontDialog](967e7930-ec11-55ba-71d5-ba173c681598.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [AddButton](03f7c0af-32ee-99fc-2bbc-ca407e065408.htm) | 给Dialog添加Button，默认只有一个OK按钮 |
| 公共方法 | [AddCheckGroup](57065d86-958c-2edd-4b83-69b0fabc9551.htm) | 给Dialog添加复选框组表单 |
| 公共方法 | [AddInputForm](cc91f3a4-5160-f83c-c8d3-8cf0b9d00c30.htm) | 给Dialog添加文本输入表单 |
| 公共方法 | [AddNumberSelect](18480e49-2e23-deb9-90c6-3f0d61703133.htm) | 给Dialog添加数字选择表单 |
| 公共方法 | [AddRadioGroup](fe40703c-728a-da78-f663-a2e1075fd01c.htm) | 给Dialog添加单选按钮组表单 |
| 公共方法 | [AddSelectForm](a32fe868-376e-e3d4-11e4-bea7b40d10fe.htm) | 给Dialog添加下来选择表单 |
| 公共方法 | [ClearForms](a82f13c3-bc94-ef5d-a302-c1776b42fa4b.htm) | 清除已经添加的Form表单 |
| 公共方法 | [RemoveButton](f9db861b-9a4d-55d6-4e15-00409e0ebbc7.htm) | 删除已经添加的Button |
| 公共方法 | [RemoveForm](31ef2860-1c04-3ad9-d2a6-182c57868eb8.htm) | 删除已经添加的表单 |
| 公共方法 | [Show](588d788b-6263-c6a6-9b90-b6d95b422858.htm) | 显示对话框 |
| 公共方法 | [ShowForResult](a6dfe9b2-5799-cfd4-8630-4777ca05a1f9.htm) | 显示对话框并获取用户输入结果 |

[Top](#PageHeader)

参见

###### 引用

[IFrontDialog 接口](967e7930-ec11-55ba-71d5-ba173c681598.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### AddButton 方法

|  |  |
| --- | --- |
|  | IFrontDialogAddButton 方法 |

给Dialog添加Button，默认只有一个OK按钮

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void AddButton(
	string btnKey,
	string text
)
```

###### 参数

btnKey  String
:   按钮的唯一标识

text  String
:   按钮显示文本

参见

###### 引用

[IFrontDialog 接口](967e7930-ec11-55ba-71d5-ba173c681598.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### AddCheckGroup 方法

|  |  |
| --- | --- |
|  | IFrontDialogAddCheckGroup 方法 |

给Dialog添加复选框组表单

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void AddCheckGroup(
	string paramKey,
	string paramName,
	List<string> itemList,
	string defaultValue = "",
	bool canEmpty = false
)
```

###### 参数

paramKey  String
:   获取结果的键值

paramName  String
:   输入框前的显示信息

itemList  ListString
:   可选项

defaultValue  String  (Optional)
:   默认值，必现在可选项内

canEmpty  Boolean  (Optional)
:   是否可以全不选

参见

###### 引用

[IFrontDialog 接口](967e7930-ec11-55ba-71d5-ba173c681598.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### AddInputForm 方法

|  |  |
| --- | --- |
|  | IFrontDialogAddInputForm 方法 |

给Dialog添加文本输入表单

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void AddInputForm(
	string paramKey,
	string paramName,
	Object defaultValue = null,
	bool canEmpty = false,
	string placeHolder = "",
	string unit = "",
	int textLimit = 0,
	string regExpression = "",
	DataType dataType = DataType.String
)
```

###### 参数

paramKey  String
:   获取结果的键值

paramName  String
:   输入框前的显示信息

defaultValue  Object  (Optional)
:   默认值

canEmpty  Boolean  (Optional)
:   可否为空

placeHolder  String  (Optional)
:   文本为空时输入框内的提示信息(PlaceHolder)

unit  String  (Optional)
:   显示单位

textLimit  Int32  (Optional)
:   输入文本的长度限制

regExpression  String  (Optional)
:   输入文本的合法性校验正则表达式

dataType  [DataType](4da48b7d-9aa8-b509-34a2-0e424ff543c9.htm)  (Optional)
:   需要输入的数据类型

参见

###### 引用

[IFrontDialog 接口](967e7930-ec11-55ba-71d5-ba173c681598.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### AddNumberSelect 方法

|  |  |
| --- | --- |
|  | IFrontDialogAddNumberSelect 方法 |

给Dialog添加数字选择表单

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void AddNumberSelect(
	string paramKey,
	string paramName,
	int defaultValue = 1,
	string unit = ""
)
```

###### 参数

paramKey  String
:   获取结果的键值

paramName  String
:   输入框前的显示信息

defaultValue  Int32  (Optional)
:   默认值

unit  String  (Optional)

参见

###### 引用

[IFrontDialog 接口](967e7930-ec11-55ba-71d5-ba173c681598.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### AddRadioGroup 方法

|  |  |
| --- | --- |
|  | IFrontDialogAddRadioGroup 方法 |

给Dialog添加单选按钮组表单

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void AddRadioGroup(
	string paramKey,
	string paramName,
	List<string> itemList,
	string defaultValue = ""
)
```

###### 参数

paramKey  String
:   获取结果的键值

paramName  String
:   输入框前的显示信息

itemList  ListString
:   可选项

defaultValue  String  (Optional)
:   默认值，必现在可选项内

参见

###### 引用

[IFrontDialog 接口](967e7930-ec11-55ba-71d5-ba173c681598.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### AddSelectForm 方法

|  |  |
| --- | --- |
|  | IFrontDialogAddSelectForm 方法 |

给Dialog添加下来选择表单

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void AddSelectForm(
	string paramKey,
	string paramName,
	List<string> itemList,
	string defaultValue = "",
	string unit = ""
)
```

###### 参数

paramKey  String
:   获取结果的键值

paramName  String
:   输入框前的显示信息

itemList  ListString
:   可选项，如果值和显示信息不同，可将显示信息和真实值用冒号拼接，如 男:1,女:0

defaultValue  String  (Optional)
:   默认值，必现在可选项内

unit  String  (Optional)
:   显示单位

参见

###### 引用

[IFrontDialog 接口](967e7930-ec11-55ba-71d5-ba173c681598.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### ClearForms 方法

|  |  |
| --- | --- |
|  | IFrontDialogClearForms 方法 |

清除已经添加的Form表单

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ClearForms()
```

参见

###### 引用

[IFrontDialog 接口](967e7930-ec11-55ba-71d5-ba173c681598.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### RemoveButton 方法

|  |  |
| --- | --- |
|  | IFrontDialogRemoveButton 方法 |

删除已经添加的Button

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void RemoveButton(
	string btnKey
)
```

###### 参数

btnKey  String
:   按钮的唯一标识

参见

###### 引用

[IFrontDialog 接口](967e7930-ec11-55ba-71d5-ba173c681598.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### RemoveForm 方法

|  |  |
| --- | --- |
|  | IFrontDialogRemoveForm 方法 |

删除已经添加的表单

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void RemoveForm(
	string paramKey
)
```

###### 参数

paramKey  String

参见

###### 引用

[IFrontDialog 接口](967e7930-ec11-55ba-71d5-ba173c681598.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Show 方法

|  |  |
| --- | --- |
|  | IFrontDialogShow 方法 |

显示对话框

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Show()
```

参见

###### 引用

[IFrontDialog 接口](967e7930-ec11-55ba-71d5-ba173c681598.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### ShowForResult 方法

|  |  |
| --- | --- |
|  | IFrontDialogShowForResult 方法 |

显示对话框并获取用户输入结果

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
DialogResult ShowForResult()
```

###### 返回值

[DialogResult](853d1712-49b1-bd6a-0ebb-f7783b5975a3.htm)

参见

###### 引用

[IFrontDialog 接口](967e7930-ec11-55ba-71d5-ba173c681598.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## IHist 接口

|  |  |
| --- | --- |
|  | IHist 接口 |

直方图显示和导出接口

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public interface IHist
```

IHist 类型公开以下成员。

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [GraphName](70052821-2f69-f69b-4416-239531e36f76.htm) | 图表名称 |

[Top](#PageHeader)

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Display(Double)](f38b441c-672e-a6a0-bd8b-3ca9f7ea3069.htm) | 显示数据类型为double[]的直方图 |
| 公共方法 | [Display(ListDouble)](7e1ca670-a760-c9dd-aec4-09e53f214715.htm) | 显示数据类型为List的直方图 |
| 公共方法 | [Display(Double, Int32)](ddd33812-83d4-b4af-c566-1be67e129b16.htm) | 显示数据类型为double[]的直方图,且自定义组别数 |
| 公共方法 | [Display(ListDouble, Int32)](6b6d3625-6ece-99c3-ac56-0cec5586f67f.htm) | 显示数据类型为List的直方图,且自定义组别数 |
| 公共方法 | [SaveToImage(String, Int32, Int32)](d9ea41e6-beb8-af6b-07a9-9f47301155b0.htm) | 将前一次Display的图导出到本地文件 |
| 公共方法 | [SaveToImage(Double, String, Int32, Int32, Int32)](a3f6662b-883b-8cd0-57b0-0982419a4767.htm) | 将指定数据表示的图导出到本地文件 |
| 公共方法 | [SaveToImage(ListDouble, String, Int32, Int32, Int32)](8fa87414-8309-0dcc-c0a7-4c561dbec92a.htm) | 将指定数据表示的图导出到本地文件 |

[Top](#PageHeader)

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### IHist 属性

|  |  |
| --- | --- |
|  | IHist 属性 |

[IHist](68ea8fb9-b1dc-07d4-eb20-70e4ac475178.htm) 类型公开以下成员。

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [GraphName](70052821-2f69-f69b-4416-239531e36f76.htm) | 图表名称 |

[Top](#PageHeader)

参见

###### 引用

[IHist 接口](68ea8fb9-b1dc-07d4-eb20-70e4ac475178.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GraphName 属性

|  |  |
| --- | --- |
|  | IHistGraphName 属性 |

图表名称

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GraphName { get; set; }
```

###### 属性值

String

参见

###### 引用

[IHist 接口](68ea8fb9-b1dc-07d4-eb20-70e4ac475178.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### IHist 方法

|  |  |
| --- | --- |
|  | IHist 方法 |

[IHist](68ea8fb9-b1dc-07d4-eb20-70e4ac475178.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Display(Double)](f38b441c-672e-a6a0-bd8b-3ca9f7ea3069.htm) | 显示数据类型为double[]的直方图 |
| 公共方法 | [Display(ListDouble)](7e1ca670-a760-c9dd-aec4-09e53f214715.htm) | 显示数据类型为List的直方图 |
| 公共方法 | [Display(Double, Int32)](ddd33812-83d4-b4af-c566-1be67e129b16.htm) | 显示数据类型为double[]的直方图,且自定义组别数 |
| 公共方法 | [Display(ListDouble, Int32)](6b6d3625-6ece-99c3-ac56-0cec5586f67f.htm) | 显示数据类型为List的直方图,且自定义组别数 |
| 公共方法 | [SaveToImage(String, Int32, Int32)](d9ea41e6-beb8-af6b-07a9-9f47301155b0.htm) | 将前一次Display的图导出到本地文件 |
| 公共方法 | [SaveToImage(Double, String, Int32, Int32, Int32)](a3f6662b-883b-8cd0-57b0-0982419a4767.htm) | 将指定数据表示的图导出到本地文件 |
| 公共方法 | [SaveToImage(ListDouble, String, Int32, Int32, Int32)](8fa87414-8309-0dcc-c0a7-4c561dbec92a.htm) | 将指定数据表示的图导出到本地文件 |

[Top](#PageHeader)

参见

###### 引用

[IHist 接口](68ea8fb9-b1dc-07d4-eb20-70e4ac475178.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Display 方法

|  |  |
| --- | --- |
|  | IHistDisplay 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Display(Double)](f38b441c-672e-a6a0-bd8b-3ca9f7ea3069.htm) | 显示数据类型为double[]的直方图 |
| 公共方法 | [Display(ListDouble)](7e1ca670-a760-c9dd-aec4-09e53f214715.htm) | 显示数据类型为List的直方图 |
| 公共方法 | [Display(Double, Int32)](ddd33812-83d4-b4af-c566-1be67e129b16.htm) | 显示数据类型为double[]的直方图,且自定义组别数 |
| 公共方法 | [Display(ListDouble, Int32)](6b6d3625-6ece-99c3-ac56-0cec5586f67f.htm) | 显示数据类型为List的直方图,且自定义组别数 |

[Top](#PageHeader)

参见

###### 引用

[IHist 接口](68ea8fb9-b1dc-07d4-eb20-70e4ac475178.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Display(Double[]) 方法

|  |  |
| --- | --- |
|  | IHistDisplay(Double) 方法 |

显示数据类型为double[]的直方图

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Display(
	double[] yData
)
```

###### 参数

yData  Double
:   直方图数据,默认组别数为y的个数

参见

###### 引用

[IHist 接口](68ea8fb9-b1dc-07d4-eb20-70e4ac475178.htm)

[Display 重载](e96743e1-76cc-eef5-5179-eb3eb9890374.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Display(List&lt;Double&gt;) 方法

|  |  |
| --- | --- |
|  | IHistDisplay(ListDouble) 方法 |

显示数据类型为List的直方图

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Display(
	List<double> yData
)
```

###### 参数

yData  ListDouble
:   直方图数据,默认组别数为y的个数

参见

###### 引用

[IHist 接口](68ea8fb9-b1dc-07d4-eb20-70e4ac475178.htm)

[Display 重载](e96743e1-76cc-eef5-5179-eb3eb9890374.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Display(Double[], Int32) 方法

|  |  |
| --- | --- |
|  | IHistDisplay(Double, Int32) 方法 |

显示数据类型为double[]的直方图,且自定义组别数

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Display(
	double[] yData,
	int nbins
)
```

###### 参数

yData  Double
:   直方图数据

nbins  Int32
:   表示会将数据从最小值到最大值平均分为nbins个组别

参见

###### 引用

[IHist 接口](68ea8fb9-b1dc-07d4-eb20-70e4ac475178.htm)

[Display 重载](e96743e1-76cc-eef5-5179-eb3eb9890374.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Display(List&lt;Double&gt;, Int32) 方法

|  |  |
| --- | --- |
|  | IHistDisplay(ListDouble, Int32) 方法 |

显示数据类型为List的直方图,且自定义组别数

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Display(
	List<double> yData,
	int nbins
)
```

###### 参数

yData  ListDouble
:   直方图数据

nbins  Int32
:   表示会将数据从最小值到最大值平均分为nbins个组别

参见

###### 引用

[IHist 接口](68ea8fb9-b1dc-07d4-eb20-70e4ac475178.htm)

[Display 重载](e96743e1-76cc-eef5-5179-eb3eb9890374.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### SaveToImage 方法

|  |  |
| --- | --- |
|  | IHistSaveToImage 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [SaveToImage(String, Int32, Int32)](d9ea41e6-beb8-af6b-07a9-9f47301155b0.htm) | 将前一次Display的图导出到本地文件 |
| 公共方法 | [SaveToImage(Double, String, Int32, Int32, Int32)](a3f6662b-883b-8cd0-57b0-0982419a4767.htm) | 将指定数据表示的图导出到本地文件 |
| 公共方法 | [SaveToImage(ListDouble, String, Int32, Int32, Int32)](8fa87414-8309-0dcc-c0a7-4c561dbec92a.htm) | 将指定数据表示的图导出到本地文件 |

[Top](#PageHeader)

参见

###### 引用

[IHist 接口](68ea8fb9-b1dc-07d4-eb20-70e4ac475178.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### SaveToImage(String, Int32, Int32) 方法

|  |  |
| --- | --- |
|  | IHistSaveToImage(String, Int32, Int32) 方法 |

将前一次Display的图导出到本地文件

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SaveToImage(
	string filePath,
	int width = 800,
	int height = 600
)
```

###### 参数

filePath  String

width  Int32  (Optional)

height  Int32  (Optional)

参见

###### 引用

[IHist 接口](68ea8fb9-b1dc-07d4-eb20-70e4ac475178.htm)

[SaveToImage 重载](335ecd45-f9e4-394b-a3dd-a2576fa76e50.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### SaveToImage(Double[], String, Int32, Int32, Int32) 方法

|  |  |
| --- | --- |
|  | IHistSaveToImage(Double, String, Int32, Int32, Int32) 方法 |

将指定数据表示的图导出到本地文件

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SaveToImage(
	double[] yData,
	string filePath,
	int nbins,
	int width = 800,
	int height = 600
)
```

###### 参数

yData  Double
:   Y轴数据

filePath  String
:   项目Result目录的相对路径

nbins  Int32
:   表示会将数据从最小值到最大值平均分为nbins个组别

width  Int32  (Optional)
:   导出图片的像素宽度

height  Int32  (Optional)
:   导出图片的像素高度

参见

###### 引用

[IHist 接口](68ea8fb9-b1dc-07d4-eb20-70e4ac475178.htm)

[SaveToImage 重载](335ecd45-f9e4-394b-a3dd-a2576fa76e50.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### SaveToImage(List&lt;Double&gt;, String, Int32, Int32, Int32) 方法

|  |  |
| --- | --- |
|  | IHistSaveToImage(ListDouble, String, Int32, Int32, Int32) 方法 |

将指定数据表示的图导出到本地文件

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SaveToImage(
	List<double> yData,
	string filePath,
	int nbins,
	int width = 800,
	int height = 600
)
```

###### 参数

yData  ListDouble
:   Y轴数据

filePath  String
:   项目Result目录的相对路径

nbins  Int32
:   表示会将数据从最小值到最大值平均分为nbins个组别

width  Int32  (Optional)
:   导出图片的像素宽度

height  Int32  (Optional)
:   导出图片的像素高度

参见

###### 引用

[IHist 接口](68ea8fb9-b1dc-07d4-eb20-70e4ac475178.htm)

[SaveToImage 重载](335ecd45-f9e4-394b-a3dd-a2576fa76e50.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## IInstrumentAccessor 接口

|  |  |
| --- | --- |
|  | IInstrumentAccessor 接口 |

仪表访问器

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public interface IInstrumentAccessor
```

IInstrumentAccessor 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [CloseByModel](fec984ae-0a04-7a5a-15aa-b86940e2259d.htm) | 关闭(断开)同型号的仪表连接 |
| 公共方法 | [CloseByName](50133906-123b-e554-7388-007a09d98ee0.htm) | 关闭(断开)仪表连接 |
| 公共方法 | [GetPresetValue](2e709d9c-c378-fdac-a1db-88b7f1135313.htm) | 获取Preset的值 |
| 公共方法 | [InitialByModel](4d9d2f35-f2a8-5dac-2376-dde10b6a0eef.htm) | 初始化连接同型号的所有仪表 |
| 公共方法 | [InitialByName](0ce5fd9e-3069-90ce-966e-d500a8853a68.htm) | 初始化仪表连接 |
| 公共方法 | [SetPresetValue](e7e22414-eae5-5dee-79ef-20c9a8d7156a.htm) | 更新Preset的值 |

[Top](#PageHeader)

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### IInstrumentAccessor 方法

|  |  |
| --- | --- |
|  | IInstrumentAccessor 方法 |

[IInstrumentAccessor](8365c067-d962-ccb8-21df-9617210b236d.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [CloseByModel](fec984ae-0a04-7a5a-15aa-b86940e2259d.htm) | 关闭(断开)同型号的仪表连接 |
| 公共方法 | [CloseByName](50133906-123b-e554-7388-007a09d98ee0.htm) | 关闭(断开)仪表连接 |
| 公共方法 | [GetPresetValue](2e709d9c-c378-fdac-a1db-88b7f1135313.htm) | 获取Preset的值 |
| 公共方法 | [InitialByModel](4d9d2f35-f2a8-5dac-2376-dde10b6a0eef.htm) | 初始化连接同型号的所有仪表 |
| 公共方法 | [InitialByName](0ce5fd9e-3069-90ce-966e-d500a8853a68.htm) | 初始化仪表连接 |
| 公共方法 | [SetPresetValue](e7e22414-eae5-5dee-79ef-20c9a8d7156a.htm) | 更新Preset的值 |

[Top](#PageHeader)

参见

###### 引用

[IInstrumentAccessor 接口](8365c067-d962-ccb8-21df-9617210b236d.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### CloseByModel 方法

|  |  |
| --- | --- |
|  | IInstrumentAccessorCloseByModel 方法 |

关闭(断开)同型号的仪表连接

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void CloseByModel(
	string modelName
)
```

###### 参数

modelName  String
:   仪表型号

参见

###### 引用

[IInstrumentAccessor 接口](8365c067-d962-ccb8-21df-9617210b236d.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### CloseByName 方法

|  |  |
| --- | --- |
|  | IInstrumentAccessorCloseByName 方法 |

关闭(断开)仪表连接

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void CloseByName(
	string instrumentName
)
```

###### 参数

instrumentName  String
:   仪表名称

参见

###### 引用

[IInstrumentAccessor 接口](8365c067-d962-ccb8-21df-9617210b236d.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetPresetValue 方法

|  |  |
| --- | --- |
|  | IInstrumentAccessorGetPresetValue 方法 |

获取Preset的值

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
Object GetPresetValue(
	string presetName,
	string paramKey
)
```

###### 参数

presetName  String

paramKey  String

###### 返回值

Object

参见

###### 引用

[IInstrumentAccessor 接口](8365c067-d962-ccb8-21df-9617210b236d.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### InitialByModel 方法

|  |  |
| --- | --- |
|  | IInstrumentAccessorInitialByModel 方法 |

初始化连接同型号的所有仪表

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void InitialByModel(
	string modelName
)
```

###### 参数

modelName  String
:   仪表型号

参见

###### 引用

[IInstrumentAccessor 接口](8365c067-d962-ccb8-21df-9617210b236d.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### InitialByName 方法

|  |  |
| --- | --- |
|  | IInstrumentAccessorInitialByName 方法 |

初始化仪表连接

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void InitialByName(
	string instrumentName
)
```

###### 参数

instrumentName  String
:   仪表名称

参见

###### 引用

[IInstrumentAccessor 接口](8365c067-d962-ccb8-21df-9617210b236d.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### SetPresetValue 方法

|  |  |
| --- | --- |
|  | IInstrumentAccessorSetPresetValue 方法 |

更新Preset的值

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPresetValue(
	string presetName,
	string paramKey,
	Object value
)
```

###### 参数

presetName  String

paramKey  String

value  Object

参见

###### 引用

[IInstrumentAccessor 接口](8365c067-d962-ccb8-21df-9617210b236d.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## InputGroupParamAttribute 类

|  |  |
| --- | --- |
|  | InputGroupParamAttribute 类 |

继承层次

SystemObject
  
  SystemAttribute  
    Guwave.OneTest.TestMethodInputGroupParamAttribute

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public class InputGroupParamAttribute : Attribute
```

InputGroupParamAttribute 类型公开以下成员。

构造函数

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [InputGroupParamAttribute](616fa2f8-7a2d-8b7e-be5a-fec712591266.htm) | 初始化 InputGroupParamAttribute 类的一个新实例 |

[Top](#PageHeader)

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [CanDebug](b2ecb643-b3fe-5ece-d421-67dd57b50b32.htm) | 参数是否可调试 |
| 公共属性 | [DataType](c0668484-7773-3195-5e88-a286f9e0bce3.htm) |  |
| 公共属性 | [DefaultValue](98d76fc7-5c88-c113-d35f-5f32a6fd5ad9.htm) | 参数默认值 |
| 公共属性 | [Description](c5972bf2-78ce-9757-d69b-8aa802eb13c5.htm) | 参数描述信息 |
| 公共属性 | [GroupRely](33452a80-c603-92a1-a738-9bda17d8f311.htm) | 参数组依赖 如果为true，当前组内同级及子级参数都会依赖RelyParam，子级的依赖关系将被覆盖 |
| 公共属性 | [Name](dfa5d90d-1187-92f2-7f31-1e22f97488df.htm) | 参数名称 |
| 公共属性 | [OptionValue](1d92fc2d-2836-2047-c4e0-b140505fc55d.htm) | 参数的可选值数组，数组元素以逗号分割 |
| 公共属性 | [RelyParam](d193403f-4075-9ae7-e977-927c2f6c6ccd.htm) | 依赖参数 当依赖参数的取值等于RelyValue时，该属性才显示 |
| 公共属性 | [RelyValue](23959e6b-0edd-3ad4-b452-114a1f24e62a.htm) | 依赖值 当依赖参数的取值等于RelyValue时，该属性才显示 |
| 公共属性 | TypeId | When implemented in a derived class, gets a unique identifier for this Attribute. (继承自 Attribute。) |

[Top](#PageHeader)

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | Equals | Returns a value that indicates whether this instance is equal to a specified object. (继承自 Attribute。) |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | GetHashCode | Returns the hash code for this instance. (继承自 Attribute。) |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | IsDefaultAttribute | When overridden in a derived class, indicates whether the value of this instance is the default value for the derived class. (继承自 Attribute。) |
| 公共方法 | Match | When overridden in a derived class, returns a value that indicates whether this instance equals a specified object. (继承自 Attribute。) |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |

[Top](#PageHeader)

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### InputGroupParamAttribute 构造函数

|  |  |
| --- | --- |
|  | InputGroupParamAttribute 构造函数 |

初始化 [InputGroupParamAttribute](cce82ed5-f9cd-2fee-ea69-2e9cebef8a2c.htm) 类的一个新实例

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public InputGroupParamAttribute(
	string name
)
```

###### 参数

name  String

参见

###### 引用

[InputGroupParamAttribute 类](cce82ed5-f9cd-2fee-ea69-2e9cebef8a2c.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### InputGroupParamAttribute 属性

|  |  |
| --- | --- |
|  | InputGroupParamAttribute 属性 |

[InputGroupParamAttribute](cce82ed5-f9cd-2fee-ea69-2e9cebef8a2c.htm) 类型公开以下成员。

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [CanDebug](b2ecb643-b3fe-5ece-d421-67dd57b50b32.htm) | 参数是否可调试 |
| 公共属性 | [DataType](c0668484-7773-3195-5e88-a286f9e0bce3.htm) |  |
| 公共属性 | [DefaultValue](98d76fc7-5c88-c113-d35f-5f32a6fd5ad9.htm) | 参数默认值 |
| 公共属性 | [Description](c5972bf2-78ce-9757-d69b-8aa802eb13c5.htm) | 参数描述信息 |
| 公共属性 | [GroupRely](33452a80-c603-92a1-a738-9bda17d8f311.htm) | 参数组依赖 如果为true，当前组内同级及子级参数都会依赖RelyParam，子级的依赖关系将被覆盖 |
| 公共属性 | [Name](dfa5d90d-1187-92f2-7f31-1e22f97488df.htm) | 参数名称 |
| 公共属性 | [OptionValue](1d92fc2d-2836-2047-c4e0-b140505fc55d.htm) | 参数的可选值数组，数组元素以逗号分割 |
| 公共属性 | [RelyParam](d193403f-4075-9ae7-e977-927c2f6c6ccd.htm) | 依赖参数 当依赖参数的取值等于RelyValue时，该属性才显示 |
| 公共属性 | [RelyValue](23959e6b-0edd-3ad4-b452-114a1f24e62a.htm) | 依赖值 当依赖参数的取值等于RelyValue时，该属性才显示 |
| 公共属性 | TypeId | When implemented in a derived class, gets a unique identifier for this Attribute. (继承自 Attribute。) |

[Top](#PageHeader)

参见

###### 引用

[InputGroupParamAttribute 类](cce82ed5-f9cd-2fee-ea69-2e9cebef8a2c.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### CanDebug 属性

|  |  |
| --- | --- |
|  | InputGroupParamAttributeCanDebug 属性 |

参数是否可调试

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public bool CanDebug { get; set; }
```

###### 属性值

Boolean

参见

###### 引用

[InputGroupParamAttribute 类](cce82ed5-f9cd-2fee-ea69-2e9cebef8a2c.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### DataType 属性

|  |  |
| --- | --- |
|  | InputGroupParamAttributeDataType 属性 |

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string DataType { get; set; }
```

###### 属性值

String

参见

###### 引用

[InputGroupParamAttribute 类](cce82ed5-f9cd-2fee-ea69-2e9cebef8a2c.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### DefaultValue 属性

|  |  |
| --- | --- |
|  | InputGroupParamAttributeDefaultValue 属性 |

参数默认值

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Object DefaultValue { get; set; }
```

###### 属性值

Object

参见

###### 引用

[InputGroupParamAttribute 类](cce82ed5-f9cd-2fee-ea69-2e9cebef8a2c.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Description 属性

|  |  |
| --- | --- |
|  | InputGroupParamAttributeDescription 属性 |

参数描述信息

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string Description { get; set; }
```

###### 属性值

String

参见

###### 引用

[InputGroupParamAttribute 类](cce82ed5-f9cd-2fee-ea69-2e9cebef8a2c.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GroupRely 属性

|  |  |
| --- | --- |
|  | InputGroupParamAttributeGroupRely 属性 |

参数组依赖
如果为true，当前组内同级及子级参数都会依赖RelyParam，子级的依赖关系将被覆盖

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public bool GroupRely { get; set; }
```

###### 属性值

Boolean

参见

###### 引用

[InputGroupParamAttribute 类](cce82ed5-f9cd-2fee-ea69-2e9cebef8a2c.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Name 属性

|  |  |
| --- | --- |
|  | InputGroupParamAttributeName 属性 |

参数名称

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string Name { get; set; }
```

###### 属性值

String

参见

###### 引用

[InputGroupParamAttribute 类](cce82ed5-f9cd-2fee-ea69-2e9cebef8a2c.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### OptionValue 属性

|  |  |
| --- | --- |
|  | InputGroupParamAttributeOptionValue 属性 |

参数的可选值数组，数组元素以逗号分割

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string OptionValue { get; set; }
```

###### 属性值

String

参见

###### 引用

[InputGroupParamAttribute 类](cce82ed5-f9cd-2fee-ea69-2e9cebef8a2c.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### RelyParam 属性

|  |  |
| --- | --- |
|  | InputGroupParamAttributeRelyParam 属性 |

依赖参数
当依赖参数的取值等于RelyValue时，该属性才显示

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string RelyParam { get; set; }
```

###### 属性值

String

参见

###### 引用

[InputGroupParamAttribute 类](cce82ed5-f9cd-2fee-ea69-2e9cebef8a2c.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### RelyValue 属性

|  |  |
| --- | --- |
|  | InputGroupParamAttributeRelyValue 属性 |

依赖值
当依赖参数的取值等于RelyValue时，该属性才显示

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string RelyValue { get; set; }
```

###### 属性值

String

参见

###### 引用

[InputGroupParamAttribute 类](cce82ed5-f9cd-2fee-ea69-2e9cebef8a2c.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### InputGroupParamAttribute 方法

|  |  |
| --- | --- |
|  | InputGroupParamAttribute 方法 |

[InputGroupParamAttribute](cce82ed5-f9cd-2fee-ea69-2e9cebef8a2c.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | Equals | Returns a value that indicates whether this instance is equal to a specified object. (继承自 Attribute。) |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | GetHashCode | Returns the hash code for this instance. (继承自 Attribute。) |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | IsDefaultAttribute | When overridden in a derived class, indicates whether the value of this instance is the default value for the derived class. (继承自 Attribute。) |
| 公共方法 | Match | When overridden in a derived class, returns a value that indicates whether this instance equals a specified object. (继承自 Attribute。) |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |

[Top](#PageHeader)

参见

###### 引用

[InputGroupParamAttribute 类](cce82ed5-f9cd-2fee-ea69-2e9cebef8a2c.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## InputParamAttribute 类

|  |  |
| --- | --- |
|  | InputParamAttribute 类 |

继承层次

SystemObject
  
  SystemAttribute  
    Guwave.OneTest.TestMethodInputParamAttribute

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public class InputParamAttribute : Attribute
```

InputParamAttribute 类型公开以下成员。

构造函数

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [InputParamAttribute](5bc134f7-3c6c-392d-0ef5-b42abcd7e70b.htm) | 初始化 InputParamAttribute 类的一个新实例 |

[Top](#PageHeader)

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [CanDebug](72422108-cc1d-e84f-851a-63962015054c.htm) | 参数是否可调试 |
| 公共属性 | [DefaultValue](769cdfe2-9af1-573c-309f-c69305f5cb4b.htm) | 参数默认值 |
| 公共属性 | [Description](ae28f04a-b106-d662-7a7e-85049b6f02b6.htm) | 参数描述信息 |
| 公共属性 | [Name](0331b36a-61e4-6878-8b37-fb6bc2afbdc9.htm) | 参数名称 |
| 公共属性 | [OptionValue](93f2c238-85dc-e7fb-bb49-8ffee0dfdaa3.htm) | 参数的可选值数组，数组元素以逗号分割 |
| 公共属性 | [RelyParam](deefadf0-c644-d3e3-f788-45406be6e094.htm) | 依赖参数 当依赖参数的取值等于RelyValue时，该属性才显示 |
| 公共属性 | [RelyValue](9579e5e8-973a-e470-ed6d-dccb326e8420.htm) | 依赖值 当依赖参数的取值等于RelyValue时，该属性才显示 |
| 公共属性 | TypeId | When implemented in a derived class, gets a unique identifier for this Attribute. (继承自 Attribute。) |

[Top](#PageHeader)

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | Equals | Returns a value that indicates whether this instance is equal to a specified object. (继承自 Attribute。) |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | GetHashCode | Returns the hash code for this instance. (继承自 Attribute。) |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | IsDefaultAttribute | When overridden in a derived class, indicates whether the value of this instance is the default value for the derived class. (继承自 Attribute。) |
| 公共方法 | Match | When overridden in a derived class, returns a value that indicates whether this instance equals a specified object. (继承自 Attribute。) |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |

[Top](#PageHeader)

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### InputParamAttribute 构造函数

|  |  |
| --- | --- |
|  | InputParamAttribute 构造函数 |

初始化 [InputParamAttribute](b8a6b68c-b60b-2702-a248-5e92a3479efe.htm) 类的一个新实例

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public InputParamAttribute()
```

参见

###### 引用

[InputParamAttribute 类](b8a6b68c-b60b-2702-a248-5e92a3479efe.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### InputParamAttribute 属性

|  |  |
| --- | --- |
|  | InputParamAttribute 属性 |

[InputParamAttribute](b8a6b68c-b60b-2702-a248-5e92a3479efe.htm) 类型公开以下成员。

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [CanDebug](72422108-cc1d-e84f-851a-63962015054c.htm) | 参数是否可调试 |
| 公共属性 | [DefaultValue](769cdfe2-9af1-573c-309f-c69305f5cb4b.htm) | 参数默认值 |
| 公共属性 | [Description](ae28f04a-b106-d662-7a7e-85049b6f02b6.htm) | 参数描述信息 |
| 公共属性 | [Name](0331b36a-61e4-6878-8b37-fb6bc2afbdc9.htm) | 参数名称 |
| 公共属性 | [OptionValue](93f2c238-85dc-e7fb-bb49-8ffee0dfdaa3.htm) | 参数的可选值数组，数组元素以逗号分割 |
| 公共属性 | [RelyParam](deefadf0-c644-d3e3-f788-45406be6e094.htm) | 依赖参数 当依赖参数的取值等于RelyValue时，该属性才显示 |
| 公共属性 | [RelyValue](9579e5e8-973a-e470-ed6d-dccb326e8420.htm) | 依赖值 当依赖参数的取值等于RelyValue时，该属性才显示 |
| 公共属性 | TypeId | When implemented in a derived class, gets a unique identifier for this Attribute. (继承自 Attribute。) |

[Top](#PageHeader)

参见

###### 引用

[InputParamAttribute 类](b8a6b68c-b60b-2702-a248-5e92a3479efe.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### CanDebug 属性

|  |  |
| --- | --- |
|  | InputParamAttributeCanDebug 属性 |

参数是否可调试

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public bool CanDebug { get; set; }
```

###### 属性值

Boolean

参见

###### 引用

[InputParamAttribute 类](b8a6b68c-b60b-2702-a248-5e92a3479efe.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### DefaultValue 属性

|  |  |
| --- | --- |
|  | InputParamAttributeDefaultValue 属性 |

参数默认值

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Object DefaultValue { get; set; }
```

###### 属性值

Object

参见

###### 引用

[InputParamAttribute 类](b8a6b68c-b60b-2702-a248-5e92a3479efe.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Description 属性

|  |  |
| --- | --- |
|  | InputParamAttributeDescription 属性 |

参数描述信息

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string Description { get; set; }
```

###### 属性值

String

参见

###### 引用

[InputParamAttribute 类](b8a6b68c-b60b-2702-a248-5e92a3479efe.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Name 属性

|  |  |
| --- | --- |
|  | InputParamAttributeName 属性 |

参数名称

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string Name { get; set; }
```

###### 属性值

String

参见

###### 引用

[InputParamAttribute 类](b8a6b68c-b60b-2702-a248-5e92a3479efe.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### OptionValue 属性

|  |  |
| --- | --- |
|  | InputParamAttributeOptionValue 属性 |

参数的可选值数组，数组元素以逗号分割

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string OptionValue { get; set; }
```

###### 属性值

String

参见

###### 引用

[InputParamAttribute 类](b8a6b68c-b60b-2702-a248-5e92a3479efe.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### RelyParam 属性

|  |  |
| --- | --- |
|  | InputParamAttributeRelyParam 属性 |

依赖参数
当依赖参数的取值等于RelyValue时，该属性才显示

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string RelyParam { get; set; }
```

###### 属性值

String

参见

###### 引用

[InputParamAttribute 类](b8a6b68c-b60b-2702-a248-5e92a3479efe.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### RelyValue 属性

|  |  |
| --- | --- |
|  | InputParamAttributeRelyValue 属性 |

依赖值
当依赖参数的取值等于RelyValue时，该属性才显示

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string RelyValue { get; set; }
```

###### 属性值

String

参见

###### 引用

[InputParamAttribute 类](b8a6b68c-b60b-2702-a248-5e92a3479efe.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### InputParamAttribute 方法

|  |  |
| --- | --- |
|  | InputParamAttribute 方法 |

[InputParamAttribute](b8a6b68c-b60b-2702-a248-5e92a3479efe.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | Equals | Returns a value that indicates whether this instance is equal to a specified object. (继承自 Attribute。) |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | GetHashCode | Returns the hash code for this instance. (继承自 Attribute。) |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | IsDefaultAttribute | When overridden in a derived class, indicates whether the value of this instance is the default value for the derived class. (继承自 Attribute。) |
| 公共方法 | Match | When overridden in a derived class, returns a value that indicates whether this instance equals a specified object. (继承自 Attribute。) |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |

[Top](#PageHeader)

参见

###### 引用

[InputParamAttribute 类](b8a6b68c-b60b-2702-a248-5e92a3479efe.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## InstrumentType 枚举

|  |  |
| --- | --- |
|  | InstrumentType 枚举 |

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public enum InstrumentType
```

成员

| 成员名称 | 值 | 说明 |
| --- | --- | --- |
| AP | 0 |  |
| BusAdapter | 1 |  |
| Counter | 2 |  |
| DCVI | 3 |  |
| Digital | 4 |  |
| Dmm | 5 |  |
| Eload | 6 |  |
| Fgen | 7 |  |
| HID | 8 |  |
| PNA | 9 |  |
| RFSA | 10 |  |
| RFSG | 11 |  |
| Scope | 12 |  |
| Serial | 13 |  |
| SpecAn | 14 |  |
| Switch | 15 |  |
| Sync | 16 |  |
| Thermal | 17 |  |
| PowerMeter | 18 |  |
| Converter | 19 |  |
| Visa | 20 |  |

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## IPinmapAccessor 接口

|  |  |
| --- | --- |
|  | IPinmapAccessor 接口 |

Pin连接信息访问器

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public interface IPinmapAccessor
```

IPinmapAccessor 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Channel2Pin](a5246913-4302-9e83-5f9a-d2a810f02ef7.htm) | 通过仪表Name和Channel编号获取所连接的Pin列表 |
| 公共方法 | [FilterPins(InstrumentType)](96703226-d8ef-bce1-c108-69b6c0009672.htm) | 仅根据仪器类型过滤并返回引脚列表。 |
| 公共方法 | [FilterPins(String)](04627ce8-0d38-824f-d905-b18aaa6f642d.htm) | 仅根据仪器类型过滤并返回引脚列表。 |
| 公共方法 | [FilterPins(String, InstrumentType)](cb3bc946-b23f-c108-ad85-97f389386250.htm) | 根据pin或pinGroup名称以及仪器类型过滤并返回引脚列表 |
| 公共方法 | [FilterPins(String, String)](4c784dfa-999e-96b8-0598-3f3b22a43f6b.htm) | 根据pin或pinGroup名称以及仪器类型过滤并返回引脚列表 |
| 公共方法 | [GetAllPinGroups](731200bd-ec5d-f1f8-cfae-282871d59221.htm) | 获取所有的PinGroup |
| 公共方法 | [GetAllPins](9f3b10ce-32b3-9fdc-f3e8-32200cbd22d4.htm) | 获取所有的Pin信息 |
| 公共方法 | [GetInstrumentName](8bc7622a-91e2-0e7c-a162-3bdad68a6f77.htm) | 获取指定引脚类型的pin和site所连接的仪表名称 |
| 公共方法 | [GetPinList(String)](c2f861c3-391e-d336-77fd-292b9527020c.htm) | 获取pin或pinGroup的引脚名称列表。 |
| 公共方法 | [GetPinList(String, PinType)](212dc89f-dab8-7179-5b92-035143af1c53.htm) | 获取指定引脚类型的pin或pin group的引脚名称列表。 |
| 公共方法 | [GetPinList(String, String)](588af7ee-e0e9-4484-cd05-8099b3d24771.htm) | 获取指定引脚类型的pin或pin group的引脚名称列表。 |
| 公共方法 | [GetPins](3fb4524c-6187-0960-d2a5-cd58664a1ee8.htm) | 通过名称获取Pin Group所有的Pin |
| 公共方法 | [Pin2Channel](379dbc59-4abd-1114-321c-c80b714780ea.htm) | 通过Pin获取所连接仪表的Channel |
| 公共方法 | [Pin2Route](23f2d2e3-d3ea-a129-41e7-ddf56d53bf1b.htm) | 通过Pin获取连接的Switch Route |
| 公共方法 | [Route2Connection](facc8d0a-7bd0-72c2-77bb-a19dee271944.htm) | 通过Route Name获取Route的连接通路 |

[Top](#PageHeader)

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### IPinmapAccessor 方法

|  |  |
| --- | --- |
|  | IPinmapAccessor 方法 |

[IPinmapAccessor](c31b9fa6-009d-3188-6deb-bca1d67c7cc7.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Channel2Pin](a5246913-4302-9e83-5f9a-d2a810f02ef7.htm) | 通过仪表Name和Channel编号获取所连接的Pin列表 |
| 公共方法 | [FilterPins(InstrumentType)](96703226-d8ef-bce1-c108-69b6c0009672.htm) | 仅根据仪器类型过滤并返回引脚列表。 |
| 公共方法 | [FilterPins(String)](04627ce8-0d38-824f-d905-b18aaa6f642d.htm) | 仅根据仪器类型过滤并返回引脚列表。 |
| 公共方法 | [FilterPins(String, InstrumentType)](cb3bc946-b23f-c108-ad85-97f389386250.htm) | 根据pin或pinGroup名称以及仪器类型过滤并返回引脚列表 |
| 公共方法 | [FilterPins(String, String)](4c784dfa-999e-96b8-0598-3f3b22a43f6b.htm) | 根据pin或pinGroup名称以及仪器类型过滤并返回引脚列表 |
| 公共方法 | [GetAllPinGroups](731200bd-ec5d-f1f8-cfae-282871d59221.htm) | 获取所有的PinGroup |
| 公共方法 | [GetAllPins](9f3b10ce-32b3-9fdc-f3e8-32200cbd22d4.htm) | 获取所有的Pin信息 |
| 公共方法 | [GetInstrumentName](8bc7622a-91e2-0e7c-a162-3bdad68a6f77.htm) | 获取指定引脚类型的pin和site所连接的仪表名称 |
| 公共方法 | [GetPinList(String)](c2f861c3-391e-d336-77fd-292b9527020c.htm) | 获取pin或pinGroup的引脚名称列表。 |
| 公共方法 | [GetPinList(String, PinType)](212dc89f-dab8-7179-5b92-035143af1c53.htm) | 获取指定引脚类型的pin或pin group的引脚名称列表。 |
| 公共方法 | [GetPinList(String, String)](588af7ee-e0e9-4484-cd05-8099b3d24771.htm) | 获取指定引脚类型的pin或pin group的引脚名称列表。 |
| 公共方法 | [GetPins](3fb4524c-6187-0960-d2a5-cd58664a1ee8.htm) | 通过名称获取Pin Group所有的Pin |
| 公共方法 | [Pin2Channel](379dbc59-4abd-1114-321c-c80b714780ea.htm) | 通过Pin获取所连接仪表的Channel |
| 公共方法 | [Pin2Route](23f2d2e3-d3ea-a129-41e7-ddf56d53bf1b.htm) | 通过Pin获取连接的Switch Route |
| 公共方法 | [Route2Connection](facc8d0a-7bd0-72c2-77bb-a19dee271944.htm) | 通过Route Name获取Route的连接通路 |

[Top](#PageHeader)

参见

###### 引用

[IPinmapAccessor 接口](c31b9fa6-009d-3188-6deb-bca1d67c7cc7.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Channel2Pin 方法

|  |  |
| --- | --- |
|  | IPinmapAccessorChannel2Pin 方法 |

通过仪表Name和Channel编号获取所连接的Pin列表

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
List<string> Channel2Pin(
	string instrumentName,
	string channel
)
```

###### 参数

instrumentName  String

channel  String

###### 返回值

ListString

参见

###### 引用

[IPinmapAccessor 接口](c31b9fa6-009d-3188-6deb-bca1d67c7cc7.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### FilterPins 方法

|  |  |
| --- | --- |
|  | IPinmapAccessorFilterPins 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [FilterPins(InstrumentType)](96703226-d8ef-bce1-c108-69b6c0009672.htm) | 仅根据仪器类型过滤并返回引脚列表。 |
| 公共方法 | [FilterPins(String)](04627ce8-0d38-824f-d905-b18aaa6f642d.htm) | 仅根据仪器类型过滤并返回引脚列表。 |
| 公共方法 | [FilterPins(String, InstrumentType)](cb3bc946-b23f-c108-ad85-97f389386250.htm) | 根据pin或pinGroup名称以及仪器类型过滤并返回引脚列表 |
| 公共方法 | [FilterPins(String, String)](4c784dfa-999e-96b8-0598-3f3b22a43f6b.htm) | 根据pin或pinGroup名称以及仪器类型过滤并返回引脚列表 |

[Top](#PageHeader)

参见

###### 引用

[IPinmapAccessor 接口](c31b9fa6-009d-3188-6deb-bca1d67c7cc7.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### FilterPins(InstrumentType) 方法

|  |  |
| --- | --- |
|  | IPinmapAccessorFilterPins(InstrumentType) 方法 |

仅根据仪器类型过滤并返回引脚列表。

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
List<string> FilterPins(
	InstrumentType instrumentType
)
```

###### 参数

instrumentType  [InstrumentType](07ed3860-185c-858d-e20a-a0cffa6b13d2.htm)
:   仪器类型

###### 返回值

ListString  
指定仪器类型的所有单个Pin的集合

参见

###### 引用

[IPinmapAccessor 接口](c31b9fa6-009d-3188-6deb-bca1d67c7cc7.htm)

[FilterPins 重载](15e3280b-2f5d-f95e-8aff-6829eba9768b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### FilterPins(String) 方法

|  |  |
| --- | --- |
|  | IPinmapAccessorFilterPins(String) 方法 |

仅根据仪器类型过滤并返回引脚列表。

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
List<string> FilterPins(
	string instrumentType
)
```

###### 参数

instrumentType  String
:   仪器类型

###### 返回值

ListString  
指定仪器类型的所有单个Pin的集合

参见

###### 引用

[IPinmapAccessor 接口](c31b9fa6-009d-3188-6deb-bca1d67c7cc7.htm)

[FilterPins 重载](15e3280b-2f5d-f95e-8aff-6829eba9768b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### FilterPins(String, InstrumentType) 方法

|  |  |
| --- | --- |
|  | IPinmapAccessorFilterPins(String, InstrumentType) 方法 |

根据pin或pinGroup名称以及仪器类型过滤并返回引脚列表

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
List<string> FilterPins(
	string pinString,
	InstrumentType instrumentType
)
```

###### 参数

pinString  String
:   pin或pinGroup名称

instrumentType  [InstrumentType](07ed3860-185c-858d-e20a-a0cffa6b13d2.htm)
:   仪器类型

###### 返回值

ListString  
指定仪器类型的所有单个Pin的集合

参见

###### 引用

[IPinmapAccessor 接口](c31b9fa6-009d-3188-6deb-bca1d67c7cc7.htm)

[FilterPins 重载](15e3280b-2f5d-f95e-8aff-6829eba9768b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### FilterPins(String, String) 方法

|  |  |
| --- | --- |
|  | IPinmapAccessorFilterPins(String, String) 方法 |

根据pin或pinGroup名称以及仪器类型过滤并返回引脚列表

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
List<string> FilterPins(
	string pinString,
	string instrumentType
)
```

###### 参数

pinString  String
:   pin或pinGroup名称

instrumentType  String
:   仪器类型

###### 返回值

ListString  
指定仪器类型的所有单个Pin的集合

参见

###### 引用

[IPinmapAccessor 接口](c31b9fa6-009d-3188-6deb-bca1d67c7cc7.htm)

[FilterPins 重载](15e3280b-2f5d-f95e-8aff-6829eba9768b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetAllPinGroups 方法

|  |  |
| --- | --- |
|  | IPinmapAccessorGetAllPinGroups 方法 |

获取所有的PinGroup

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
List<string> GetAllPinGroups()
```

###### 返回值

ListString

参见

###### 引用

[IPinmapAccessor 接口](c31b9fa6-009d-3188-6deb-bca1d67c7cc7.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetAllPins 方法

|  |  |
| --- | --- |
|  | IPinmapAccessorGetAllPins 方法 |

获取所有的Pin信息

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
List<string> GetAllPins()
```

###### 返回值

ListString

参见

###### 引用

[IPinmapAccessor 接口](c31b9fa6-009d-3188-6deb-bca1d67c7cc7.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetInstrumentName 方法

|  |  |
| --- | --- |
|  | IPinmapAccessorGetInstrumentName 方法 |

获取指定引脚类型的pin和site所连接的仪表名称

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetInstrumentName(
	string pinName
)
```

###### 参数

pinName  String

###### 返回值

String  
仪表名称(界面添加时输入的Name)

参见

###### 引用

[IPinmapAccessor 接口](c31b9fa6-009d-3188-6deb-bca1d67c7cc7.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetPinList 方法

|  |  |
| --- | --- |
|  | IPinmapAccessorGetPinList 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [GetPinList(String)](c2f861c3-391e-d336-77fd-292b9527020c.htm) | 获取pin或pinGroup的引脚名称列表。 |
| 公共方法 | [GetPinList(String, PinType)](212dc89f-dab8-7179-5b92-035143af1c53.htm) | 获取指定引脚类型的pin或pin group的引脚名称列表。 |
| 公共方法 | [GetPinList(String, String)](588af7ee-e0e9-4484-cd05-8099b3d24771.htm) | 获取指定引脚类型的pin或pin group的引脚名称列表。 |

[Top](#PageHeader)

参见

###### 引用

[IPinmapAccessor 接口](c31b9fa6-009d-3188-6deb-bca1d67c7cc7.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### GetPinList(String) 方法

|  |  |
| --- | --- |
|  | IPinmapAccessorGetPinList(String) 方法 |

获取pin或pinGroup的引脚名称列表。

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
List<string> GetPinList(
	string pinString
)
```

###### 参数

pinString  String
:   pin或pin Group名称

###### 返回值

ListString  
所有单个Pin的集合

参见

###### 引用

[IPinmapAccessor 接口](c31b9fa6-009d-3188-6deb-bca1d67c7cc7.htm)

[GetPinList 重载](409c919c-6d05-a56f-47fb-5b2fdb2ba9d6.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### GetPinList(String, PinType) 方法

|  |  |
| --- | --- |
|  | IPinmapAccessorGetPinList(String, PinType) 方法 |

获取指定引脚类型的pin或pin group的引脚名称列表。

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
List<string> GetPinList(
	string pinString,
	PinType pinType
)
```

###### 参数

pinString  String
:   pin或pin Group名称

pinType  [PinType](4f676645-359f-b1e1-862d-e363d7ea1ee8.htm)
:   引脚类型

###### 返回值

ListString  
指定引脚类型的所有单个Pin的集合

参见

###### 引用

[IPinmapAccessor 接口](c31b9fa6-009d-3188-6deb-bca1d67c7cc7.htm)

[GetPinList 重载](409c919c-6d05-a56f-47fb-5b2fdb2ba9d6.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### GetPinList(String, String) 方法

|  |  |
| --- | --- |
|  | IPinmapAccessorGetPinList(String, String) 方法 |

获取指定引脚类型的pin或pin group的引脚名称列表。

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
List<string> GetPinList(
	string pinString,
	string pinType
)
```

###### 参数

pinString  String
:   pin或pin Group名称

pinType  String
:   引脚类型, 可选值："DutPin", "SystemPin"

###### 返回值

ListString  
指定引脚类型的所有单个Pin的集合

参见

###### 引用

[IPinmapAccessor 接口](c31b9fa6-009d-3188-6deb-bca1d67c7cc7.htm)

[GetPinList 重载](409c919c-6d05-a56f-47fb-5b2fdb2ba9d6.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetPins 方法

|  |  |
| --- | --- |
|  | IPinmapAccessorGetPins 方法 |

通过名称获取Pin Group所有的Pin

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
List<string> GetPins(
	string pinGroupName
)
```

###### 参数

pinGroupName  String

###### 返回值

ListString

参见

###### 引用

[IPinmapAccessor 接口](c31b9fa6-009d-3188-6deb-bca1d67c7cc7.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Pin2Channel 方法

|  |  |
| --- | --- |
|  | IPinmapAccessorPin2Channel 方法 |

通过Pin获取所连接仪表的Channel

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string Pin2Channel(
	string pinName
)
```

###### 参数

pinName  String

###### 返回值

String

参见

###### 引用

[IPinmapAccessor 接口](c31b9fa6-009d-3188-6deb-bca1d67c7cc7.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Pin2Route 方法

|  |  |
| --- | --- |
|  | IPinmapAccessorPin2Route 方法 |

通过Pin获取连接的Switch Route

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string Pin2Route(
	string pinName
)
```

###### 参数

pinName  String

###### 返回值

String

参见

###### 引用

[IPinmapAccessor 接口](c31b9fa6-009d-3188-6deb-bca1d67c7cc7.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Route2Connection 方法

|  |  |
| --- | --- |
|  | IPinmapAccessorRoute2Connection 方法 |

通过Route Name获取Route的连接通路

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
List<string[]> Route2Connection(
	string routeName
)
```

###### 参数

routeName  String

###### 返回值

ListString

参见

###### 引用

[IPinmapAccessor 接口](c31b9fa6-009d-3188-6deb-bca1d67c7cc7.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## IPlot 接口

|  |  |
| --- | --- |
|  | IPlot 接口 |

折线图显示和导出接口

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public interface IPlot
```

IPlot 类型公开以下成员。

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [GraphName](1af27e7c-f014-8c90-e6a3-81b63227585b.htm) | 图表名称 |

[Top](#PageHeader)

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [AddCursor](ec3c3e17-7b09-2779-2151-456b94ade1b3.htm) | 向图表添加一个Cursor标记 |
| 公共方法 | [AddCursorToLine](28246ac1-a6d9-4ae8-2bce-46512ee67967.htm) | 向图表中的曲线添加一个Cursor标记 |
| 公共方法 | [AddLine(Double, String)](03276ea6-efe4-426c-3cf8-22c3d0265f5a.htm) | 用于向同一张图表中添加多条曲线,添加后需要调用MultiLineDisplay()方法方可实际生效 |
| 公共方法 | [AddLine(ListDouble, String)](3dd5d013-b8c8-c393-6fc3-41806d220755.htm) | 用于向同一张图表中添加多条曲线,添加后需要调用MultiLineDisplay()方法方可实际生效 |
| 公共方法 | [AppendDataToLine(String, ListDouble)](55dc419b-d397-380b-a4ab-263abee94e74.htm) | 向图表添加一条曲线图 |
| 公共方法 | [AppendDataToLine(String, Double)](ba912abe-1eee-a52f-2bfb-e5f107428f64.htm) | 向图表添加一条曲线图 |
| 公共方法 | [Display(Double)](fd242efa-2eb1-22f4-d372-9bb9f862e656.htm) | 显示图形并自定义类型为double[,]的XY轴数据 |
| 公共方法 | [Display(Double, DictionaryString, Double)](e6864d23-3d40-846c-5a22-9d66b4ef6c65.htm) | 同时显示多条曲线, 共用X轴 |
| 公共方法 | [Display(ListDouble, DictionaryString, ListDouble)](c7fd5b9e-3bf9-4a33-fd27-f672d7ccc4f5.htm) | 同时显示多条曲线, 共用X轴 |
| 公共方法 | [Display(Double, String, String)](be0f108b-c9b5-4f94-f406-3ab160cda1c1.htm) | 显示图形并自定义类型为double[]的Y轴数据,Y轴的名称和单位 |
| 公共方法 | [Display(ListDouble, String, String)](f1ae74e3-6ee0-c898-e6fa-27a4fbe39fee.htm) | 显示图形并自定义类型为List的Y轴数据,Y轴的名称和单位 |
| 公共方法 | [Display(Double, String, String, String, String)](5327f0c6-0171-0310-6141-c877b88716d5.htm) | 显示图形并自定义类型为double[,]的XY轴数据,X轴Y轴的名称和单位 |
| 公共方法 | [Display(Double, Double, String, String, String, String)](b02c64e3-c911-910a-c24c-0ed561f8398a.htm) | 显示图形并自定义类型为Trace的XY轴数据,X轴Y轴的名称和单位 |
| 公共方法 | [Display(ListDouble, ListDouble, String, String, String, String)](2496df47-f95d-e652-d641-789eb26d7c66.htm) | 显示图形并自定义类型为List的XY轴数据,X轴Y轴的名称和单位 |
| 公共方法 | [MultiLineDisplay](70f144d5-68ea-e320-1a07-1982c910d620.htm) | 在Add多条Line后,调用MultiLineDisplay显示多条曲线 |
| 公共方法 | [SaveToImage(String, Int32, Int32)](05013979-dfbf-9ed2-b7d6-2d5b9269f0ed.htm) | 将前一次Display的图或者通过AddLine添加的图导出到本地文件 |
| 公共方法 | [SaveToImage(Double, Double, String, Int32, Int32)](d9c6a54a-1561-2a98-a884-d1a35d465c87.htm) | 将指定数据表示的图导出到本地文件 |
| 公共方法 | [SaveToImage(ListDouble, DictionaryString, ListDouble, String, Int32, Int32)](73911071-1a9f-bb5b-d780-1fa65253f0eb.htm) | 将指定数据表示的图导出到本地文件，显示多条曲线, 共用X轴 |
| 公共方法 | [SaveToImage(ListDouble, ListDouble, String, Int32, Int32)](6ebf7521-8968-936b-09aa-87000c78bcf2.htm) | 将指定数据表示的图导出到本地文件 |

[Top](#PageHeader)

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### IPlot 属性

|  |  |
| --- | --- |
|  | IPlot 属性 |

[IPlot](36365182-b589-2e22-ed58-95684d8fb7d6.htm) 类型公开以下成员。

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [GraphName](1af27e7c-f014-8c90-e6a3-81b63227585b.htm) | 图表名称 |

[Top](#PageHeader)

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GraphName 属性

|  |  |
| --- | --- |
|  | IPlotGraphName 属性 |

图表名称

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GraphName { get; set; }
```

###### 属性值

String

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### IPlot 方法

|  |  |
| --- | --- |
|  | IPlot 方法 |

[IPlot](36365182-b589-2e22-ed58-95684d8fb7d6.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [AddCursor](ec3c3e17-7b09-2779-2151-456b94ade1b3.htm) | 向图表添加一个Cursor标记 |
| 公共方法 | [AddCursorToLine](28246ac1-a6d9-4ae8-2bce-46512ee67967.htm) | 向图表中的曲线添加一个Cursor标记 |
| 公共方法 | [AddLine(Double, String)](03276ea6-efe4-426c-3cf8-22c3d0265f5a.htm) | 用于向同一张图表中添加多条曲线,添加后需要调用MultiLineDisplay()方法方可实际生效 |
| 公共方法 | [AddLine(ListDouble, String)](3dd5d013-b8c8-c393-6fc3-41806d220755.htm) | 用于向同一张图表中添加多条曲线,添加后需要调用MultiLineDisplay()方法方可实际生效 |
| 公共方法 | [AppendDataToLine(String, ListDouble)](55dc419b-d397-380b-a4ab-263abee94e74.htm) | 向图表添加一条曲线图 |
| 公共方法 | [AppendDataToLine(String, Double)](ba912abe-1eee-a52f-2bfb-e5f107428f64.htm) | 向图表添加一条曲线图 |
| 公共方法 | [Display(Double)](fd242efa-2eb1-22f4-d372-9bb9f862e656.htm) | 显示图形并自定义类型为double[,]的XY轴数据 |
| 公共方法 | [Display(Double, DictionaryString, Double)](e6864d23-3d40-846c-5a22-9d66b4ef6c65.htm) | 同时显示多条曲线, 共用X轴 |
| 公共方法 | [Display(ListDouble, DictionaryString, ListDouble)](c7fd5b9e-3bf9-4a33-fd27-f672d7ccc4f5.htm) | 同时显示多条曲线, 共用X轴 |
| 公共方法 | [Display(Double, String, String)](be0f108b-c9b5-4f94-f406-3ab160cda1c1.htm) | 显示图形并自定义类型为double[]的Y轴数据,Y轴的名称和单位 |
| 公共方法 | [Display(ListDouble, String, String)](f1ae74e3-6ee0-c898-e6fa-27a4fbe39fee.htm) | 显示图形并自定义类型为List的Y轴数据,Y轴的名称和单位 |
| 公共方法 | [Display(Double, String, String, String, String)](5327f0c6-0171-0310-6141-c877b88716d5.htm) | 显示图形并自定义类型为double[,]的XY轴数据,X轴Y轴的名称和单位 |
| 公共方法 | [Display(Double, Double, String, String, String, String)](b02c64e3-c911-910a-c24c-0ed561f8398a.htm) | 显示图形并自定义类型为Trace的XY轴数据,X轴Y轴的名称和单位 |
| 公共方法 | [Display(ListDouble, ListDouble, String, String, String, String)](2496df47-f95d-e652-d641-789eb26d7c66.htm) | 显示图形并自定义类型为List的XY轴数据,X轴Y轴的名称和单位 |
| 公共方法 | [MultiLineDisplay](70f144d5-68ea-e320-1a07-1982c910d620.htm) | 在Add多条Line后,调用MultiLineDisplay显示多条曲线 |
| 公共方法 | [SaveToImage(String, Int32, Int32)](05013979-dfbf-9ed2-b7d6-2d5b9269f0ed.htm) | 将前一次Display的图或者通过AddLine添加的图导出到本地文件 |
| 公共方法 | [SaveToImage(Double, Double, String, Int32, Int32)](d9c6a54a-1561-2a98-a884-d1a35d465c87.htm) | 将指定数据表示的图导出到本地文件 |
| 公共方法 | [SaveToImage(ListDouble, DictionaryString, ListDouble, String, Int32, Int32)](73911071-1a9f-bb5b-d780-1fa65253f0eb.htm) | 将指定数据表示的图导出到本地文件，显示多条曲线, 共用X轴 |
| 公共方法 | [SaveToImage(ListDouble, ListDouble, String, Int32, Int32)](6ebf7521-8968-936b-09aa-87000c78bcf2.htm) | 将指定数据表示的图导出到本地文件 |

[Top](#PageHeader)

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### AddCursor 方法

|  |  |
| --- | --- |
|  | IPlotAddCursor 方法 |

向图表添加一个Cursor标记

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void AddCursor(
	double xValue,
	double yValue,
	string cursorName = "",
	bool xVisible = true,
	bool yVisible = true,
	string cursorColor = "#596BFF"
)
```

###### 参数

xValue  Double
:   X坐标

yValue  Double
:   Y坐标

cursorName  String  (Optional)
:   标记名称

xVisible  Boolean  (Optional)
:   是否显示与X轴平行的参考线

yVisible  Boolean  (Optional)
:   是否显示与Y轴平行的参考线

cursorColor  String  (Optional)
:   标记颜色

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### AddCursorToLine 方法

|  |  |
| --- | --- |
|  | IPlotAddCursorToLine 方法 |

向图表中的曲线添加一个Cursor标记

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void AddCursorToLine(
	string lineName,
	double xValue,
	double yValue,
	string cursorName = "",
	bool xVisible = true,
	bool yVisible = true,
	string cursorColor = "#596BFF"
)
```

###### 参数

lineName  String
:   曲线名称

xValue  Double
:   X坐标

yValue  Double
:   Y坐标

cursorName  String  (Optional)
:   标记名称

xVisible  Boolean  (Optional)
:   是否显示与X轴平行的参考线

yVisible  Boolean  (Optional)
:   是否显示与Y轴平行的参考线

cursorColor  String  (Optional)
:   标记颜色

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### AddLine 方法

|  |  |
| --- | --- |
|  | IPlotAddLine 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [AddLine(Double, String)](03276ea6-efe4-426c-3cf8-22c3d0265f5a.htm) | 用于向同一张图表中添加多条曲线,添加后需要调用MultiLineDisplay()方法方可实际生效 |
| 公共方法 | [AddLine(ListDouble, String)](3dd5d013-b8c8-c393-6fc3-41806d220755.htm) | 用于向同一张图表中添加多条曲线,添加后需要调用MultiLineDisplay()方法方可实际生效 |

[Top](#PageHeader)

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### AddLine(Double[], String) 方法

|  |  |
| --- | --- |
|  | IPlotAddLine(Double, String) 方法 |

用于向同一张图表中添加多条曲线,添加后需要调用MultiLineDisplay()方法方可实际生效

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void AddLine(
	double[] yData,
	string lineName = "Null"
)
```

###### 参数

yData  Double
:   曲线数据

lineName  String  (Optional)
:   曲线名称

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[AddLine 重载](a4a1d297-dafb-180d-97f0-6daaf395a8ef.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### AddLine(List&lt;Double&gt;, String) 方法

|  |  |
| --- | --- |
|  | IPlotAddLine(ListDouble, String) 方法 |

用于向同一张图表中添加多条曲线,添加后需要调用MultiLineDisplay()方法方可实际生效

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void AddLine(
	List<double> yData,
	string lineName = "Null"
)
```

###### 参数

yData  ListDouble
:   曲线数据

lineName  String  (Optional)
:   曲线名称

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[AddLine 重载](a4a1d297-dafb-180d-97f0-6daaf395a8ef.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### AppendDataToLine 方法

|  |  |
| --- | --- |
|  | IPlotAppendDataToLine 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [AppendDataToLine(String, ListDouble)](55dc419b-d397-380b-a4ab-263abee94e74.htm) | 向图表添加一条曲线图 |
| 公共方法 | [AppendDataToLine(String, Double)](ba912abe-1eee-a52f-2bfb-e5f107428f64.htm) | 向图表添加一条曲线图 |

[Top](#PageHeader)

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### AppendDataToLine(String, List&lt;Double&gt;) 方法

|  |  |
| --- | --- |
|  | IPlotAppendDataToLine(String, ListDouble) 方法 |

向图表添加一条曲线图

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void AppendDataToLine(
	string lineName,
	List<double> yData
)
```

###### 参数

lineName  String
:   曲线名称

yData  ListDouble
:   Y轴数据

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[AppendDataToLine 重载](c4a5f6c2-6e56-f4e1-6111-49099656b747.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### AppendDataToLine(String, Double[]) 方法

|  |  |
| --- | --- |
|  | IPlotAppendDataToLine(String, Double) 方法 |

向图表添加一条曲线图

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void AppendDataToLine(
	string lineName,
	double[] yData
)
```

###### 参数

lineName  String
:   曲线名称

yData  Double
:   Y轴数据

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[AppendDataToLine 重载](c4a5f6c2-6e56-f4e1-6111-49099656b747.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Display 方法

|  |  |
| --- | --- |
|  | IPlotDisplay 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Display(Double)](fd242efa-2eb1-22f4-d372-9bb9f862e656.htm) | 显示图形并自定义类型为double[,]的XY轴数据 |
| 公共方法 | [Display(Double, DictionaryString, Double)](e6864d23-3d40-846c-5a22-9d66b4ef6c65.htm) | 同时显示多条曲线, 共用X轴 |
| 公共方法 | [Display(ListDouble, DictionaryString, ListDouble)](c7fd5b9e-3bf9-4a33-fd27-f672d7ccc4f5.htm) | 同时显示多条曲线, 共用X轴 |
| 公共方法 | [Display(Double, String, String)](be0f108b-c9b5-4f94-f406-3ab160cda1c1.htm) | 显示图形并自定义类型为double[]的Y轴数据,Y轴的名称和单位 |
| 公共方法 | [Display(ListDouble, String, String)](f1ae74e3-6ee0-c898-e6fa-27a4fbe39fee.htm) | 显示图形并自定义类型为List的Y轴数据,Y轴的名称和单位 |
| 公共方法 | [Display(Double, String, String, String, String)](5327f0c6-0171-0310-6141-c877b88716d5.htm) | 显示图形并自定义类型为double[,]的XY轴数据,X轴Y轴的名称和单位 |
| 公共方法 | [Display(Double, Double, String, String, String, String)](b02c64e3-c911-910a-c24c-0ed561f8398a.htm) | 显示图形并自定义类型为Trace的XY轴数据,X轴Y轴的名称和单位 |
| 公共方法 | [Display(ListDouble, ListDouble, String, String, String, String)](2496df47-f95d-e652-d641-789eb26d7c66.htm) | 显示图形并自定义类型为List的XY轴数据,X轴Y轴的名称和单位 |

[Top](#PageHeader)

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Display(Double[,]) 方法

|  |  |
| --- | --- |
|  | IPlotDisplay(Double) 方法 |

显示图形并自定义类型为double[,]的XY轴数据

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Display(
	double[,] xyData
)
```

###### 参数

xyData  Double
:   XY轴数据点

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[Display 重载](f49ef64a-c09c-3e65-5119-fd958cfa4a19.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Display(Double[], Dictionary&lt;String, Double[]&gt;) 方法

|  |  |
| --- | --- |
|  | IPlotDisplay(Double, DictionaryString, Double) 方法 |

同时显示多条曲线, 共用X轴

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Display(
	double[] xData,
	Dictionary<string, double[]> yData
)
```

###### 参数

xData  Double
:   X轴数据

yData  DictionaryString, Double
:   多条曲线的Y轴数据

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[Display 重载](f49ef64a-c09c-3e65-5119-fd958cfa4a19.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Display(List&lt;Double&gt;, Dictionary&lt;String, List&lt;Double&gt;&gt;) 方法

|  |  |
| --- | --- |
|  | IPlotDisplay(ListDouble, DictionaryString, ListDouble) 方法 |

同时显示多条曲线, 共用X轴

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Display(
	List<double> xData,
	Dictionary<string, List<double>> yData
)
```

###### 参数

xData  ListDouble
:   X轴数据

yData  DictionaryString, ListDouble
:   多条曲线的Y轴数据

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[Display 重载](f49ef64a-c09c-3e65-5119-fd958cfa4a19.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Display(Double[], String, String) 方法

|  |  |
| --- | --- |
|  | IPlotDisplay(Double, String, String) 方法 |

显示图形并自定义类型为double[]的Y轴数据,Y轴的名称和单位

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Display(
	double[] yData,
	string yName = "",
	string yUnit = ""
)
```

###### 参数

yData  Double
:   Y轴数据

yName  String  (Optional)
:   Y轴名称

yUnit  String  (Optional)
:   Y轴单位

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[Display 重载](f49ef64a-c09c-3e65-5119-fd958cfa4a19.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Display(List&lt;Double&gt;, String, String) 方法

|  |  |
| --- | --- |
|  | IPlotDisplay(ListDouble, String, String) 方法 |

显示图形并自定义类型为List的Y轴数据,Y轴的名称和单位

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Display(
	List<double> yData,
	string yName = "",
	string yUnit = ""
)
```

###### 参数

yData  ListDouble
:   Y轴数据

yName  String  (Optional)
:   Y轴名称

yUnit  String  (Optional)
:   Y轴单位

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[Display 重载](f49ef64a-c09c-3e65-5119-fd958cfa4a19.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Display(Double[,], String, String, String, String) 方法

|  |  |
| --- | --- |
|  | IPlotDisplay(Double, String, String, String, String) 方法 |

显示图形并自定义类型为double[,]的XY轴数据,X轴Y轴的名称和单位

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Display(
	double[,] xyData,
	string xName,
	string yName,
	string xUnit = "",
	string yUnit = ""
)
```

###### 参数

xyData  Double
:   XY轴数据点

xName  String
:   X轴名称

yName  String
:   Y轴名称

xUnit  String  (Optional)
:   X轴单位

yUnit  String  (Optional)
:   Y轴单位

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[Display 重载](f49ef64a-c09c-3e65-5119-fd958cfa4a19.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Display(Double[], Double[], String, String, String, String) 方法

|  |  |
| --- | --- |
|  | IPlotDisplay(Double, Double, String, String, String, String) 方法 |

显示图形并自定义类型为Trace的XY轴数据,X轴Y轴的名称和单位

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Display(
	double[] xData,
	double[] yData,
	string xName = "",
	string yName = "",
	string xUnit = "",
	string yUnit = ""
)
```

###### 参数

xData  Double
:   X轴数据

yData  Double
:   Y轴数据

xName  String  (Optional)
:   X轴名称

yName  String  (Optional)
:   Y轴名称

xUnit  String  (Optional)
:   X轴单位

yUnit  String  (Optional)
:   Y轴单位

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[Display 重载](f49ef64a-c09c-3e65-5119-fd958cfa4a19.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Display(List&lt;Double&gt;, List&lt;Double&gt;, String, String, String, String) 方法

|  |  |
| --- | --- |
|  | IPlotDisplay(ListDouble, ListDouble, String, String, String, String) 方法 |

显示图形并自定义类型为List的XY轴数据,X轴Y轴的名称和单位

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Display(
	List<double> xData,
	List<double> yData,
	string xName = "",
	string yName = "",
	string xUnit = "",
	string yUnit = ""
)
```

###### 参数

xData  ListDouble
:   X轴数据

yData  ListDouble
:   Y轴数据

xName  String  (Optional)
:   X轴名称

yName  String  (Optional)
:   Y轴名称

xUnit  String  (Optional)
:   X轴单位

yUnit  String  (Optional)
:   Y轴单位

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[Display 重载](f49ef64a-c09c-3e65-5119-fd958cfa4a19.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### MultiLineDisplay 方法

|  |  |
| --- | --- |
|  | IPlotMultiLineDisplay 方法 |

在Add多条Line后,调用MultiLineDisplay显示多条曲线

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void MultiLineDisplay(
	string xName = "X",
	string yName = "Y",
	string xUnit = "",
	string yUnit = ""
)
```

###### 参数

xName  String  (Optional)
:   X轴名称

yName  String  (Optional)
:   Y轴名称

xUnit  String  (Optional)
:   X轴单位

yUnit  String  (Optional)
:   Y轴单位

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### SaveToImage 方法

|  |  |
| --- | --- |
|  | IPlotSaveToImage 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [SaveToImage(String, Int32, Int32)](05013979-dfbf-9ed2-b7d6-2d5b9269f0ed.htm) | 将前一次Display的图或者通过AddLine添加的图导出到本地文件 |
| 公共方法 | [SaveToImage(Double, Double, String, Int32, Int32)](d9c6a54a-1561-2a98-a884-d1a35d465c87.htm) | 将指定数据表示的图导出到本地文件 |
| 公共方法 | [SaveToImage(ListDouble, DictionaryString, ListDouble, String, Int32, Int32)](73911071-1a9f-bb5b-d780-1fa65253f0eb.htm) | 将指定数据表示的图导出到本地文件，显示多条曲线, 共用X轴 |
| 公共方法 | [SaveToImage(ListDouble, ListDouble, String, Int32, Int32)](6ebf7521-8968-936b-09aa-87000c78bcf2.htm) | 将指定数据表示的图导出到本地文件 |

[Top](#PageHeader)

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### SaveToImage(String, Int32, Int32) 方法

|  |  |
| --- | --- |
|  | IPlotSaveToImage(String, Int32, Int32) 方法 |

将前一次Display的图或者通过AddLine添加的图导出到本地文件

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SaveToImage(
	string filePath,
	int width = 800,
	int height = 600
)
```

###### 参数

filePath  String
:   项目Result目录的相对路径

width  Int32  (Optional)
:   导出图片的像素宽度

height  Int32  (Optional)
:   导出图片的像素高度

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[SaveToImage 重载](06916f98-afb5-b167-8542-47be3d984574.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### SaveToImage(Double[], Double[], String, Int32, Int32) 方法

|  |  |
| --- | --- |
|  | IPlotSaveToImage(Double, Double, String, Int32, Int32) 方法 |

将指定数据表示的图导出到本地文件

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SaveToImage(
	double[] xData,
	double[] yData,
	string filePath,
	int width = 800,
	int height = 600
)
```

###### 参数

xData  Double
:   X轴数据

yData  Double
:   Y轴数据

filePath  String
:   项目Result目录的相对路径

width  Int32  (Optional)
:   导出图片的像素宽度

height  Int32  (Optional)
:   导出图片的像素高度

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[SaveToImage 重载](06916f98-afb5-b167-8542-47be3d984574.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### SaveToImage(List&lt;Double&gt;, Dictionary&lt;String, List&lt;Double&gt;&gt;, String, Int32, Int32) 方法

|  |  |
| --- | --- |
|  | IPlotSaveToImage(ListDouble, DictionaryString, ListDouble, String, Int32, Int32) 方法 |

将指定数据表示的图导出到本地文件，显示多条曲线, 共用X轴

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SaveToImage(
	List<double> xData,
	Dictionary<string, List<double>> yData,
	string filePath,
	int width = 800,
	int height = 600
)
```

###### 参数

xData  ListDouble
:   X轴数据

yData  DictionaryString, ListDouble
:   多条曲线的Y轴数据

filePath  String
:   项目Result目录的相对路径

width  Int32  (Optional)
:   导出图片的像素宽度

height  Int32  (Optional)
:   导出图片的像素高度

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[SaveToImage 重载](06916f98-afb5-b167-8542-47be3d984574.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### SaveToImage(List&lt;Double&gt;, List&lt;Double&gt;, String, Int32, Int32) 方法

|  |  |
| --- | --- |
|  | IPlotSaveToImage(ListDouble, ListDouble, String, Int32, Int32) 方法 |

将指定数据表示的图导出到本地文件

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SaveToImage(
	List<double> xData,
	List<double> yData,
	string filePath,
	int width = 800,
	int height = 600
)
```

###### 参数

xData  ListDouble
:   X轴数据

yData  ListDouble
:   Y轴数据

filePath  String
:   项目Result目录的相对路径

width  Int32  (Optional)
:   导出图片的像素宽度

height  Int32  (Optional)
:   导出图片的像素高度

参见

###### 引用

[IPlot 接口](36365182-b589-2e22-ed58-95684d8fb7d6.htm)

[SaveToImage 重载](06916f98-afb5-b167-8542-47be3d984574.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## IRawData 接口

|  |  |
| --- | --- |
|  | IRawData 接口 |

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public interface IRawData
```

IRawData 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [AddCondition](fee95215-8ffa-819a-f986-d6e1b09071c3.htm) | 添加测试条件(参数) |
| 公共方法 | [AddTestData](20b270b1-ad38-27c8-ce4d-d16e04eb760e.htm) | 添加原始波形数据 |
| 公共方法 | [AddTestFile](f6935956-34e8-7fab-70d4-c1071afaf756.htm) | 添加原始数据文件 |
| 公共方法 | [SetRawData](22b85f05-be0c-29a7-f2bc-685a37522f61.htm) | 设置RawData名称，一般使用TestText |

[Top](#PageHeader)

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### IRawData 方法

|  |  |
| --- | --- |
|  | IRawData 方法 |

[IRawData](61e036ef-d223-3b58-9ca2-b89e8fea7254.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [AddCondition](fee95215-8ffa-819a-f986-d6e1b09071c3.htm) | 添加测试条件(参数) |
| 公共方法 | [AddTestData](20b270b1-ad38-27c8-ce4d-d16e04eb760e.htm) | 添加原始波形数据 |
| 公共方法 | [AddTestFile](f6935956-34e8-7fab-70d4-c1071afaf756.htm) | 添加原始数据文件 |
| 公共方法 | [SetRawData](22b85f05-be0c-29a7-f2bc-685a37522f61.htm) | 设置RawData名称，一般使用TestText |

[Top](#PageHeader)

参见

###### 引用

[IRawData 接口](61e036ef-d223-3b58-9ca2-b89e8fea7254.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### AddCondition 方法

|  |  |
| --- | --- |
|  | IRawDataAddCondition 方法 |

添加测试条件(参数)

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void AddCondition(
	string paramName,
	Object value
)
```

###### 参数

paramName  String
:   参数名称需要带TestSuite名称，格式：TestSuiteName:InputParamName

value  Object
:   参数值

参见

###### 引用

[IRawData 接口](61e036ef-d223-3b58-9ca2-b89e8fea7254.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### AddTestData 方法

|  |  |
| --- | --- |
|  | IRawDataAddTestData 方法 |

添加原始波形数据

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void AddTestData(
	string lineName,
	double[,] waveData
)
```

###### 参数

lineName  String
:   X轴名称

waveData  Double
:   波形数据

参见

###### 引用

[IRawData 接口](61e036ef-d223-3b58-9ca2-b89e8fea7254.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### AddTestFile 方法

|  |  |
| --- | --- |
|  | IRawDataAddTestFile 方法 |

添加原始数据文件

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void AddTestFile(
	string rawFile
)
```

###### 参数

rawFile  String
:   绝对路径文件名或者项目下以CustomFiles开始的相对路径

参见

###### 引用

[IRawData 接口](61e036ef-d223-3b58-9ca2-b89e8fea7254.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### SetRawData 方法

|  |  |
| --- | --- |
|  | IRawDataSetRawData 方法 |

设置RawData名称，一般使用TestText

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetRawData(
	string rawName
)
```

###### 参数

rawName  String

参见

###### 引用

[IRawData 接口](61e036ef-d223-3b58-9ca2-b89e8fea7254.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## IRegisterAccessor 接口

|  |  |
| --- | --- |
|  | IRegisterAccessor 接口 |

Register访问器

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public interface IRegisterAccessor
```

IRegisterAccessor 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [ApplyAllRegisterGroups](ff0fd18a-106c-11d0-d759-0888c04c78e9.htm) | Apply所有寄存器组,对寄存器组中的只读寄存器进行读操作,对只写寄存器进行写操作,对于可读可写的寄存器先写后读 更新SingleRegister界面的ReadBackValue、Value和Mask，更新RegisterGroup界面的ReadBackValue Mask取内存(也是界面设置的)中的值 |
| 公共方法 | [ApplyRegisterGroup(String)](b3878276-b8ca-88fa-42fd-938b7325c39e.htm) | Apply单个寄存器组,对寄存器组中的只读寄存器进行读操作,对只写寄存器进行写寄存器,对于可读可写的寄存器先写后读 更新SingleRegister界面的ReadBackValue、Value和Mask，更新RegisterGroup界面的ReadBackValue Mask取内存(也是界面设置的)中的值 |
| 公共方法 | [ApplyRegisterGroup(String, UInt64)](586f69cb-44e6-dd82-25d3-3cb12cc3ece7.htm) | Apply单个寄存器组,对寄存器组中的只读寄存器进行读操作,对只写寄存器进行写寄存器,对于可读可写的寄存器先写后读 更新SingleRegister界面的ReadBackValue、Value和Mask，更新RegisterGroup界面的ReadBackValue Mask取所有可写字段对应的Mask |
| 公共方法 | [ApplyRegisterGroup(String, Int32, UInt64)](9afa8e88-8ea1-a33e-8ea6-6b0264da4457.htm) | Apply单个寄存器组,对寄存器组中的只读寄存器进行读操作,对只写寄存器进行写寄存器,对于可读可写的寄存器先写后读,传入索引不得超出界面索引范围 更新SingleRegister界面的ReadBackValue、Value和Mask，更新RegisterGroup界面的ReadBackValue Mask取所有可写字段对应的Mask |
| 公共方法 | [CheckSingleRegister(String)](15ab388f-353d-8757-2e8b-7168ec492326.htm) | 对Module内的所有寄存器先写后读，比较值是否一样 更新SingleRegister界面Value和ReadBackValue和Mask |
| 公共方法 | [CheckSingleRegister(String, UInt64)](9873697a-6e46-df29-6bb4-6355f8bf4f23.htm) | 对寄存器先写后读，比较值是否一样 更新SingleRegister界面Value和ReadBackValue和Mask |
| 公共方法 | [CheckSingleRegister(UInt64, UInt64)](92b2c8b6-319c-e303-75bd-df962a8ff251.htm) | 对寄存器先写后读，比较值是否一样 更新SingleRegister界面Value和ReadBackValue和Mask Mask为所有可写字段为1其他字段为0的值 |
| 公共方法 | [CheckSingleRegister(String, String, UInt64)](9819a986-28c2-17f0-f3d2-5d0e9647278f.htm) | 对寄存器先写后读，比较值是否一样 更新SingleRegister界面Value和ReadBackValue和Mask |
| 公共方法 | [CheckSingleRegister(String, String, UInt64)](6245c91c-0fbb-092a-4af0-640df47031a3.htm) | 对寄存器先写后读，比较值是否一样 更新SingleRegister界面Value、ReadBackValue和Mask |
| 公共方法 | [CheckSingleRegister(String, UInt64, UInt64)](a275a13f-d3fb-9e78-99ba-333f4ab8ee42.htm) | 对寄存器先写后读，比较值是否一样 更新SingleRegister界面Value和ReadBackValue和Mask |
| 公共方法 | [Command](a95f74e2-0959-8c5f-eb07-ac2dc9bf0a45.htm) | 执行Register Command脚本 |
| 公共方法 | [GetAllFieldNameInRegister](219d4309-8c47-445d-86e4-e9a02a576401.htm) | 通过寄存器名字获取该寄存器中的所有Field名称 |
| 公共方法 | [GetAllRegisterGroups](2648e750-e741-f9bd-9fdd-5e985b8c1bb2.htm) | 获取所有寄存器组的名称 |
| 公共方法 | [GetAllRegisters](92ad7d7b-f6f1-5b0c-2d8f-f38f0e4e40c3.htm) | 获取所有寄存器的名称 |
| 公共方法 | [GetFieldLocation](dd68bf04-7505-5d4d-cdd5-3535d26f944a.htm) | 通过字段名称获取字段地址 |
| 公共方法 | [GetFieldName](9c8a18f8-5a70-0984-9cdd-5730252de090.htm) | 通过字段地址获取字段名称 |
| 公共方法 | [GetGroupRegisters](4475e1e6-4730-0130-2eeb-a14e0205eb57.htm) | 通过寄存器组名字获取该寄存器组中的所有寄存器名称 |
| 公共方法 | [GetRegisterAddress](cb084b8b-3fd0-175c-bf44-2575b5ba1557.htm) | 通过RegisterName获取RegisterAddress |
| 公共方法 | [GetRegisterField](8ae05d04-c059-f543-3a93-9724f56202e4.htm) | 读单个寄存器指定位段值 |
| 公共方法 | [GetRegisterFieldInGroup](d26acd30-3153-289a-a640-a138865c273f.htm) | 通过寄存器名字获取field列表 不涉及界面更新 |
| 公共方法 | [GetRegisterName](302ed699-a0a4-c0d2-5b16-f35e2eed58f0.htm) | 通过address获取RegisterName |
| 公共方法 | [GetRegisterValue](112d72d4-90e3-881e-16a9-76d5dd3342eb.htm) | 通过RegisterName获取RegisterValue |
| 公共方法 | [GetRegisterValueInGroup](d48f347c-2c19-2935-d6de-8e0c5f0263db.htm) | 获取寄存器组中寄存器的值 不涉及界面更新 |
| 公共方法 | [GlobalModifyModulePreset](bb2d05fb-6a69-269c-ab98-43c422137270.htm) | 全局修改Module的Preset设置 更新界面配置，生命周期为本次Flow运行 |
| 公共方法 | [GlobalResetRegistertoDefaultValue](c3dff3a4-7467-765d-1f9f-0e9c362cc7c1.htm) | 全局将寄存器的值重置回defaultvalue，同时其Fields也保持与Default值同步; 本次Flow运行期间生效，更新SingleRegister界面的Value和Mask字段 |
| 公共方法 | [GlobalSetRegisterField](1eba9bdc-d5bb-8625-7688-7043ed34dea1.htm) | 全局设置寄存器位段值 本次Flow运行期间生效，不更新界面 |
| 公共方法 | [GlobalSetRegisterValueInGroup(String, String, UInt64, Int32)](d19d143d-ad17-ca67-477f-db3e07435dbf.htm) | 全局设置寄存器组中寄存器的值 更新RegisterGroup界面的Value值，本次Flow运行周期内生效 |
| 公共方法 | [GlobalSetRegisterValueInGroup(String, String, String, UInt64, Int32)](07122762-15ee-fb1f-4525-81e3d8612632.htm) | 全局设置寄存器组中寄存器位段的值 更新RegisterGroup界面的Value值，本次Flow运行周期内生效 |
| 公共方法 | [GlobalSetRegisterValueInGroup(String, String, String, UInt64, Int32)](c60931e6-2513-2624-7993-887dec60df7b.htm) | 全局设置寄存器组中寄存器位段的值 更新RegisterGroup界面的Value值，本次Flow运行周期内生效 |
| 公共方法 | [GlobalSetSingleRegister](2bd70c2f-bb31-adef-b563-9c202c10a066.htm) | 全局设置寄存器值， 本次Flow运行期间生效，不更新界面 |
| 公共方法 | [ModifyModulePreset](a88bc198-645c-a4b8-0e7a-ff4970dcfdea.htm) | 修改Module的Preset设置 当前TestSuite生效，不影响下一个TestSuite运行 |
| 公共方法 | [ReadRegisterByModule](7aa2734a-b9c5-cbfc-a1b5-7ee92800af42.htm) | 读单个寄存器 更新SingleRegister界面ReadBackValue |
| 公共方法 | [ReadRegisterGroup](3a4baca9-9d9a-1aa5-f79e-9c4cc63ff55e.htm) | 读寄存器组 更新SingleRegister界面的ReadBackValue和RegisterGroup界面的ReadBackValue |
| 公共方法 | [ReadSingleRegister(String)](351c94ea-6a09-2c53-2a47-70b5a0f37ade.htm) | 读单个寄存器 更新SingleRegister界面ReadBackValue |
| 公共方法 | [ReadSingleRegister(UInt64)](a77f6c9e-5e20-48fa-976a-af29023fb2ed.htm) | 读单个寄存器 更新SingleRegister界面ReadBackValue |
| 公共方法 | [ReadSingleRegister(String, String)](86c9fdf9-2a0f-2e7b-c491-ef7573e8a07d.htm) | 读单个寄存器 更新SingleRegister界面ReadBackValue |
| 公共方法 | [ResetRegistertoDefaultValue](4a7b5de3-39d1-8bea-2938-528598b39a8c.htm) | 将寄存器的值重置回defaultvalue，同时其Fields也保持与Default值同步; 只在当前TestSuite内生效，不更新界面 |
| 公共方法 | [SetRegisterField](c7a7888d-9b0e-ea8c-08e4-495766d876d4.htm) | 设置寄存器位段值 只在当前TestSuite内生效，不更新界面 |
| 公共方法 | [SetRegisterValueInGroup(String, String, UInt64, Int32)](1b8c42ad-eaeb-5731-ed3e-ecbba9e88de3.htm) | 设置寄存器组中寄存器的值 不更新任何界面 |
| 公共方法 | [SetRegisterValueInGroup(String, String, String, UInt64, Int32)](03c2e1dd-3c95-cf02-5d2c-fb7df8195bf5.htm) | 设置寄存器组中寄存器位段的值 不更新任何界面 |
| 公共方法 | [SetRegisterValueInGroup(String, String, String, UInt64, Int32)](abc21a5d-1c27-3067-8e68-ef98f527181e.htm) | 设置寄存器组中寄存器位段的值 不更新任何界面 |
| 公共方法 | [SetSingleRegister](2ac10ccf-5600-af6e-2815-3ba98850de60.htm) | 设置寄存器值 只在当前TestSuite内生效，不更新界面 |
| 公共方法 | [VerifyRegisterGroup](e6546f2d-9681-beb6-9e19-53cc516ff1ce.htm) | 验证寄存器组 更新SingleRegister界面的ReadBackValue、Value和Mask，更新RegisterGroup界面的ReadBackValue Mask取内存(也是界面设置的)中的值 |
| 公共方法 | [WriteRegisterByModule](b5c8fb0a-ddae-2ead-b964-c67fa9a08282.htm) | 写单个寄存器 更新SingleRegister界面Value和Mask |
| 公共方法 | [WriteRegisterGroup(String)](f480f332-a9f3-33c2-d3ff-d05d464e8d37.htm) | 写寄存器组 更新SingleRegister界面的Value和Mask Mask取内存(也是界面设置的)中的值 |
| 公共方法 | [WriteRegisterGroup(String, UInt64)](6ebecdc6-0272-ef90-b8e5-396b139b999d.htm) | 写寄存器组 更新SingleRegister界面的Value和Mask Mask取所有可写字段对应的Mask |
| 公共方法 | [WriteSingleRegister(String, Boolean)](e9e5fdef-c44c-93f6-87b5-e724d0e597f1.htm) | 写单个寄存器 更新SingleRegister界面Value和Mask Mask取内存(也是界面设置的)中的值 |
| 公共方法 | [WriteSingleRegister(String, String, UInt64)](a5ce85dd-d5eb-d29d-9cf3-56ad53b4ad50.htm) | 写单个寄存器 更新SingleRegister界面Value和Mask |
| 公共方法 | [WriteSingleRegister(String, UInt64, Boolean)](80f24806-7445-187e-da9a-2cfcc03ed76d.htm) | 写单个寄存器 更新SingleRegister界面Value和Mask Mask取所有可写字段对应的Mask |
| 公共方法 | [WriteSingleRegister(String, UInt64, UInt64)](3beb2f8a-70e2-1421-2685-8f8a62303d85.htm) | 写单个寄存器 更新SingleRegister界面Value和Mask |
| 公共方法 | [WriteSingleRegister(UInt64, UInt64, Boolean)](106b9788-c043-34cd-6149-8a5fd08209ab.htm) | 写单个寄存器 更新SingleRegister界面Value和Mask Mask取所有可写字段对应的Mask |

[Top](#PageHeader)

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### IRegisterAccessor 方法

|  |  |
| --- | --- |
|  | IRegisterAccessor 方法 |

[IRegisterAccessor](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [ApplyAllRegisterGroups](ff0fd18a-106c-11d0-d759-0888c04c78e9.htm) | Apply所有寄存器组,对寄存器组中的只读寄存器进行读操作,对只写寄存器进行写操作,对于可读可写的寄存器先写后读 更新SingleRegister界面的ReadBackValue、Value和Mask，更新RegisterGroup界面的ReadBackValue Mask取内存(也是界面设置的)中的值 |
| 公共方法 | [ApplyRegisterGroup(String)](b3878276-b8ca-88fa-42fd-938b7325c39e.htm) | Apply单个寄存器组,对寄存器组中的只读寄存器进行读操作,对只写寄存器进行写寄存器,对于可读可写的寄存器先写后读 更新SingleRegister界面的ReadBackValue、Value和Mask，更新RegisterGroup界面的ReadBackValue Mask取内存(也是界面设置的)中的值 |
| 公共方法 | [ApplyRegisterGroup(String, UInt64)](586f69cb-44e6-dd82-25d3-3cb12cc3ece7.htm) | Apply单个寄存器组,对寄存器组中的只读寄存器进行读操作,对只写寄存器进行写寄存器,对于可读可写的寄存器先写后读 更新SingleRegister界面的ReadBackValue、Value和Mask，更新RegisterGroup界面的ReadBackValue Mask取所有可写字段对应的Mask |
| 公共方法 | [ApplyRegisterGroup(String, Int32, UInt64)](9afa8e88-8ea1-a33e-8ea6-6b0264da4457.htm) | Apply单个寄存器组,对寄存器组中的只读寄存器进行读操作,对只写寄存器进行写寄存器,对于可读可写的寄存器先写后读,传入索引不得超出界面索引范围 更新SingleRegister界面的ReadBackValue、Value和Mask，更新RegisterGroup界面的ReadBackValue Mask取所有可写字段对应的Mask |
| 公共方法 | [CheckSingleRegister(String)](15ab388f-353d-8757-2e8b-7168ec492326.htm) | 对Module内的所有寄存器先写后读，比较值是否一样 更新SingleRegister界面Value和ReadBackValue和Mask |
| 公共方法 | [CheckSingleRegister(String, UInt64)](9873697a-6e46-df29-6bb4-6355f8bf4f23.htm) | 对寄存器先写后读，比较值是否一样 更新SingleRegister界面Value和ReadBackValue和Mask |
| 公共方法 | [CheckSingleRegister(UInt64, UInt64)](92b2c8b6-319c-e303-75bd-df962a8ff251.htm) | 对寄存器先写后读，比较值是否一样 更新SingleRegister界面Value和ReadBackValue和Mask Mask为所有可写字段为1其他字段为0的值 |
| 公共方法 | [CheckSingleRegister(String, String, UInt64)](9819a986-28c2-17f0-f3d2-5d0e9647278f.htm) | 对寄存器先写后读，比较值是否一样 更新SingleRegister界面Value和ReadBackValue和Mask |
| 公共方法 | [CheckSingleRegister(String, String, UInt64)](6245c91c-0fbb-092a-4af0-640df47031a3.htm) | 对寄存器先写后读，比较值是否一样 更新SingleRegister界面Value、ReadBackValue和Mask |
| 公共方法 | [CheckSingleRegister(String, UInt64, UInt64)](a275a13f-d3fb-9e78-99ba-333f4ab8ee42.htm) | 对寄存器先写后读，比较值是否一样 更新SingleRegister界面Value和ReadBackValue和Mask |
| 公共方法 | [Command](a95f74e2-0959-8c5f-eb07-ac2dc9bf0a45.htm) | 执行Register Command脚本 |
| 公共方法 | [GetAllFieldNameInRegister](219d4309-8c47-445d-86e4-e9a02a576401.htm) | 通过寄存器名字获取该寄存器中的所有Field名称 |
| 公共方法 | [GetAllRegisterGroups](2648e750-e741-f9bd-9fdd-5e985b8c1bb2.htm) | 获取所有寄存器组的名称 |
| 公共方法 | [GetAllRegisters](92ad7d7b-f6f1-5b0c-2d8f-f38f0e4e40c3.htm) | 获取所有寄存器的名称 |
| 公共方法 | [GetFieldLocation](dd68bf04-7505-5d4d-cdd5-3535d26f944a.htm) | 通过字段名称获取字段地址 |
| 公共方法 | [GetFieldName](9c8a18f8-5a70-0984-9cdd-5730252de090.htm) | 通过字段地址获取字段名称 |
| 公共方法 | [GetGroupRegisters](4475e1e6-4730-0130-2eeb-a14e0205eb57.htm) | 通过寄存器组名字获取该寄存器组中的所有寄存器名称 |
| 公共方法 | [GetRegisterAddress](cb084b8b-3fd0-175c-bf44-2575b5ba1557.htm) | 通过RegisterName获取RegisterAddress |
| 公共方法 | [GetRegisterField](8ae05d04-c059-f543-3a93-9724f56202e4.htm) | 读单个寄存器指定位段值 |
| 公共方法 | [GetRegisterFieldInGroup](d26acd30-3153-289a-a640-a138865c273f.htm) | 通过寄存器名字获取field列表 不涉及界面更新 |
| 公共方法 | [GetRegisterName](302ed699-a0a4-c0d2-5b16-f35e2eed58f0.htm) | 通过address获取RegisterName |
| 公共方法 | [GetRegisterValue](112d72d4-90e3-881e-16a9-76d5dd3342eb.htm) | 通过RegisterName获取RegisterValue |
| 公共方法 | [GetRegisterValueInGroup](d48f347c-2c19-2935-d6de-8e0c5f0263db.htm) | 获取寄存器组中寄存器的值 不涉及界面更新 |
| 公共方法 | [GlobalModifyModulePreset](bb2d05fb-6a69-269c-ab98-43c422137270.htm) | 全局修改Module的Preset设置 更新界面配置，生命周期为本次Flow运行 |
| 公共方法 | [GlobalResetRegistertoDefaultValue](c3dff3a4-7467-765d-1f9f-0e9c362cc7c1.htm) | 全局将寄存器的值重置回defaultvalue，同时其Fields也保持与Default值同步; 本次Flow运行期间生效，更新SingleRegister界面的Value和Mask字段 |
| 公共方法 | [GlobalSetRegisterField](1eba9bdc-d5bb-8625-7688-7043ed34dea1.htm) | 全局设置寄存器位段值 本次Flow运行期间生效，不更新界面 |
| 公共方法 | [GlobalSetRegisterValueInGroup(String, String, UInt64, Int32)](d19d143d-ad17-ca67-477f-db3e07435dbf.htm) | 全局设置寄存器组中寄存器的值 更新RegisterGroup界面的Value值，本次Flow运行周期内生效 |
| 公共方法 | [GlobalSetRegisterValueInGroup(String, String, String, UInt64, Int32)](07122762-15ee-fb1f-4525-81e3d8612632.htm) | 全局设置寄存器组中寄存器位段的值 更新RegisterGroup界面的Value值，本次Flow运行周期内生效 |
| 公共方法 | [GlobalSetRegisterValueInGroup(String, String, String, UInt64, Int32)](c60931e6-2513-2624-7993-887dec60df7b.htm) | 全局设置寄存器组中寄存器位段的值 更新RegisterGroup界面的Value值，本次Flow运行周期内生效 |
| 公共方法 | [GlobalSetSingleRegister](2bd70c2f-bb31-adef-b563-9c202c10a066.htm) | 全局设置寄存器值， 本次Flow运行期间生效，不更新界面 |
| 公共方法 | [ModifyModulePreset](a88bc198-645c-a4b8-0e7a-ff4970dcfdea.htm) | 修改Module的Preset设置 当前TestSuite生效，不影响下一个TestSuite运行 |
| 公共方法 | [ReadRegisterByModule](7aa2734a-b9c5-cbfc-a1b5-7ee92800af42.htm) | 读单个寄存器 更新SingleRegister界面ReadBackValue |
| 公共方法 | [ReadRegisterGroup](3a4baca9-9d9a-1aa5-f79e-9c4cc63ff55e.htm) | 读寄存器组 更新SingleRegister界面的ReadBackValue和RegisterGroup界面的ReadBackValue |
| 公共方法 | [ReadSingleRegister(String)](351c94ea-6a09-2c53-2a47-70b5a0f37ade.htm) | 读单个寄存器 更新SingleRegister界面ReadBackValue |
| 公共方法 | [ReadSingleRegister(UInt64)](a77f6c9e-5e20-48fa-976a-af29023fb2ed.htm) | 读单个寄存器 更新SingleRegister界面ReadBackValue |
| 公共方法 | [ReadSingleRegister(String, String)](86c9fdf9-2a0f-2e7b-c491-ef7573e8a07d.htm) | 读单个寄存器 更新SingleRegister界面ReadBackValue |
| 公共方法 | [ResetRegistertoDefaultValue](4a7b5de3-39d1-8bea-2938-528598b39a8c.htm) | 将寄存器的值重置回defaultvalue，同时其Fields也保持与Default值同步; 只在当前TestSuite内生效，不更新界面 |
| 公共方法 | [SetRegisterField](c7a7888d-9b0e-ea8c-08e4-495766d876d4.htm) | 设置寄存器位段值 只在当前TestSuite内生效，不更新界面 |
| 公共方法 | [SetRegisterValueInGroup(String, String, UInt64, Int32)](1b8c42ad-eaeb-5731-ed3e-ecbba9e88de3.htm) | 设置寄存器组中寄存器的值 不更新任何界面 |
| 公共方法 | [SetRegisterValueInGroup(String, String, String, UInt64, Int32)](03c2e1dd-3c95-cf02-5d2c-fb7df8195bf5.htm) | 设置寄存器组中寄存器位段的值 不更新任何界面 |
| 公共方法 | [SetRegisterValueInGroup(String, String, String, UInt64, Int32)](abc21a5d-1c27-3067-8e68-ef98f527181e.htm) | 设置寄存器组中寄存器位段的值 不更新任何界面 |
| 公共方法 | [SetSingleRegister](2ac10ccf-5600-af6e-2815-3ba98850de60.htm) | 设置寄存器值 只在当前TestSuite内生效，不更新界面 |
| 公共方法 | [VerifyRegisterGroup](e6546f2d-9681-beb6-9e19-53cc516ff1ce.htm) | 验证寄存器组 更新SingleRegister界面的ReadBackValue、Value和Mask，更新RegisterGroup界面的ReadBackValue Mask取内存(也是界面设置的)中的值 |
| 公共方法 | [WriteRegisterByModule](b5c8fb0a-ddae-2ead-b964-c67fa9a08282.htm) | 写单个寄存器 更新SingleRegister界面Value和Mask |
| 公共方法 | [WriteRegisterGroup(String)](f480f332-a9f3-33c2-d3ff-d05d464e8d37.htm) | 写寄存器组 更新SingleRegister界面的Value和Mask Mask取内存(也是界面设置的)中的值 |
| 公共方法 | [WriteRegisterGroup(String, UInt64)](6ebecdc6-0272-ef90-b8e5-396b139b999d.htm) | 写寄存器组 更新SingleRegister界面的Value和Mask Mask取所有可写字段对应的Mask |
| 公共方法 | [WriteSingleRegister(String, Boolean)](e9e5fdef-c44c-93f6-87b5-e724d0e597f1.htm) | 写单个寄存器 更新SingleRegister界面Value和Mask Mask取内存(也是界面设置的)中的值 |
| 公共方法 | [WriteSingleRegister(String, String, UInt64)](a5ce85dd-d5eb-d29d-9cf3-56ad53b4ad50.htm) | 写单个寄存器 更新SingleRegister界面Value和Mask |
| 公共方法 | [WriteSingleRegister(String, UInt64, Boolean)](80f24806-7445-187e-da9a-2cfcc03ed76d.htm) | 写单个寄存器 更新SingleRegister界面Value和Mask Mask取所有可写字段对应的Mask |
| 公共方法 | [WriteSingleRegister(String, UInt64, UInt64)](3beb2f8a-70e2-1421-2685-8f8a62303d85.htm) | 写单个寄存器 更新SingleRegister界面Value和Mask |
| 公共方法 | [WriteSingleRegister(UInt64, UInt64, Boolean)](106b9788-c043-34cd-6149-8a5fd08209ab.htm) | 写单个寄存器 更新SingleRegister界面Value和Mask Mask取所有可写字段对应的Mask |

[Top](#PageHeader)

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### ApplyAllRegisterGroups 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorApplyAllRegisterGroups 方法 |

Apply所有寄存器组,对寄存器组中的只读寄存器进行读操作,对只写寄存器进行写操作,对于可读可写的寄存器先写后读
更新SingleRegister界面的ReadBackValue、Value和Mask，更新RegisterGroup界面的ReadBackValue
Mask取内存(也是界面设置的)中的值

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
Dictionary<string, Dictionary<ulong, ulong>> ApplyAllRegisterGroups()
```

###### 返回值

DictionaryString, DictionaryUInt64, UInt64  
返回一个字典，其中key为寄存器组的名称，value也为字典，其中key为寄存器地址，value为寄存器的值

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### ApplyRegisterGroup 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorApplyRegisterGroup 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [ApplyRegisterGroup(String)](b3878276-b8ca-88fa-42fd-938b7325c39e.htm) | Apply单个寄存器组,对寄存器组中的只读寄存器进行读操作,对只写寄存器进行写寄存器,对于可读可写的寄存器先写后读 更新SingleRegister界面的ReadBackValue、Value和Mask，更新RegisterGroup界面的ReadBackValue Mask取内存(也是界面设置的)中的值 |
| 公共方法 | [ApplyRegisterGroup(String, UInt64)](586f69cb-44e6-dd82-25d3-3cb12cc3ece7.htm) | Apply单个寄存器组,对寄存器组中的只读寄存器进行读操作,对只写寄存器进行写寄存器,对于可读可写的寄存器先写后读 更新SingleRegister界面的ReadBackValue、Value和Mask，更新RegisterGroup界面的ReadBackValue Mask取所有可写字段对应的Mask |
| 公共方法 | [ApplyRegisterGroup(String, Int32, UInt64)](9afa8e88-8ea1-a33e-8ea6-6b0264da4457.htm) | Apply单个寄存器组,对寄存器组中的只读寄存器进行读操作,对只写寄存器进行写寄存器,对于可读可写的寄存器先写后读,传入索引不得超出界面索引范围 更新SingleRegister界面的ReadBackValue、Value和Mask，更新RegisterGroup界面的ReadBackValue Mask取所有可写字段对应的Mask |

[Top](#PageHeader)

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### ApplyRegisterGroup(String) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorApplyRegisterGroup(String) 方法 |

Apply单个寄存器组,对寄存器组中的只读寄存器进行读操作,对只写寄存器进行写寄存器,对于可读可写的寄存器先写后读
更新SingleRegister界面的ReadBackValue、Value和Mask，更新RegisterGroup界面的ReadBackValue
Mask取内存(也是界面设置的)中的值

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
Dictionary<ulong, ulong> ApplyRegisterGroup(
	string groupName
)
```

###### 参数

groupName  String
:   寄存器组名称

###### 返回值

DictionaryUInt64, UInt64  
返回一个字典，其中key为寄存器地址，value为寄存器的值

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[ApplyRegisterGroup 重载](6b62629f-af72-0378-97ad-1d1fd30a103f.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### ApplyRegisterGroup(String, UInt64[]) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorApplyRegisterGroup(String, UInt64) 方法 |

Apply单个寄存器组,对寄存器组中的只读寄存器进行读操作,对只写寄存器进行写寄存器,对于可读可写的寄存器先写后读
更新SingleRegister界面的ReadBackValue、Value和Mask，更新RegisterGroup界面的ReadBackValue
Mask取所有可写字段对应的Mask

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
Dictionary<ulong, ulong> ApplyRegisterGroup(
	string groupName,
	ulong[] registerValues
)
```

###### 参数

groupName  String
:   寄存器组名称

registerValues  UInt64
:   按顺序写入到每一个特定寄存器的值

###### 返回值

DictionaryUInt64, UInt64  
返回一个字典，其中key为寄存器地址，value为读到的寄存器的值

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[ApplyRegisterGroup 重载](6b62629f-af72-0378-97ad-1d1fd30a103f.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### ApplyRegisterGroup(String, Int32[], UInt64[]) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorApplyRegisterGroup(String, Int32, UInt64) 方法 |

Apply单个寄存器组,对寄存器组中的只读寄存器进行读操作,对只写寄存器进行写寄存器,对于可读可写的寄存器先写后读,传入索引不得超出界面索引范围
更新SingleRegister界面的ReadBackValue、Value和Mask，更新RegisterGroup界面的ReadBackValue
Mask取所有可写字段对应的Mask

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
Dictionary<ulong, ulong> ApplyRegisterGroup(
	string groupName,
	int[] registerIndexesInGroup,
	ulong[] registerValues
)
```

###### 参数

groupName  String
:   寄存器组名称

registerIndexesInGroup  Int32
:   界面上寄存器在寄存器组中的索引

registerValues  UInt64
:   按顺序写入到每一个特定寄存器的值

###### 返回值

DictionaryUInt64, UInt64  
返回一个字典，其中key为寄存器地址，value为读到的寄存器的值

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[ApplyRegisterGroup 重载](6b62629f-af72-0378-97ad-1d1fd30a103f.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### CheckSingleRegister 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorCheckSingleRegister 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [CheckSingleRegister(String)](15ab388f-353d-8757-2e8b-7168ec492326.htm) | 对Module内的所有寄存器先写后读，比较值是否一样 更新SingleRegister界面Value和ReadBackValue和Mask |
| 公共方法 | [CheckSingleRegister(String, UInt64)](9873697a-6e46-df29-6bb4-6355f8bf4f23.htm) | 对寄存器先写后读，比较值是否一样 更新SingleRegister界面Value和ReadBackValue和Mask |
| 公共方法 | [CheckSingleRegister(UInt64, UInt64)](92b2c8b6-319c-e303-75bd-df962a8ff251.htm) | 对寄存器先写后读，比较值是否一样 更新SingleRegister界面Value和ReadBackValue和Mask Mask为所有可写字段为1其他字段为0的值 |
| 公共方法 | [CheckSingleRegister(String, String, UInt64)](9819a986-28c2-17f0-f3d2-5d0e9647278f.htm) | 对寄存器先写后读，比较值是否一样 更新SingleRegister界面Value和ReadBackValue和Mask |
| 公共方法 | [CheckSingleRegister(String, String, UInt64)](6245c91c-0fbb-092a-4af0-640df47031a3.htm) | 对寄存器先写后读，比较值是否一样 更新SingleRegister界面Value、ReadBackValue和Mask |
| 公共方法 | [CheckSingleRegister(String, UInt64, UInt64)](a275a13f-d3fb-9e78-99ba-333f4ab8ee42.htm) | 对寄存器先写后读，比较值是否一样 更新SingleRegister界面Value和ReadBackValue和Mask |

[Top](#PageHeader)

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### CheckSingleRegister(String) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorCheckSingleRegister(String) 方法 |

对Module内的所有寄存器先写后读，比较值是否一样
更新SingleRegister界面Value和ReadBackValue和Mask

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
Dictionary<string, bool> CheckSingleRegister(
	string moduleName
)
```

###### 参数

moduleName  String
:   寄存器模块名称

###### 返回值

DictionaryString, Boolean  
检查结果

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[CheckSingleRegister 重载](0df97fbe-6e1b-845c-2e8e-c7239b61e35a.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### CheckSingleRegister(String, UInt64) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorCheckSingleRegister(String, UInt64) 方法 |

对寄存器先写后读，比较值是否一样
更新SingleRegister界面Value和ReadBackValue和Mask

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool CheckSingleRegister(
	string registerName,
	ulong value
)
```

###### 参数

registerName  String
:   寄存器名称

value  UInt64
:   寄存器值

###### 返回值

Boolean  
检查结果

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[CheckSingleRegister 重载](0df97fbe-6e1b-845c-2e8e-c7239b61e35a.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### CheckSingleRegister(UInt64, UInt64) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorCheckSingleRegister(UInt64, UInt64) 方法 |

对寄存器先写后读，比较值是否一样
更新SingleRegister界面Value和ReadBackValue和Mask
Mask为所有可写字段为1其他字段为0的值

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool CheckSingleRegister(
	ulong address,
	ulong value
)
```

###### 参数

address  UInt64
:   寄存器地址

value  UInt64
:   寄存器值

###### 返回值

Boolean  
检查结果

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[CheckSingleRegister 重载](0df97fbe-6e1b-845c-2e8e-c7239b61e35a.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### CheckSingleRegister(String, String, UInt64) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorCheckSingleRegister(String, String, UInt64) 方法 |

对寄存器先写后读，比较值是否一样
更新SingleRegister界面Value和ReadBackValue和Mask

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool CheckSingleRegister(
	string moduleName,
	string registerName,
	ulong value
)
```

###### 参数

moduleName  String
:   寄存器模块名称

registerName  String
:   寄存器名称

value  UInt64
:   寄存器值

###### 返回值

Boolean  
检查结果

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[CheckSingleRegister 重载](0df97fbe-6e1b-845c-2e8e-c7239b61e35a.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### CheckSingleRegister(String, String[], UInt64[]) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorCheckSingleRegister(String, String, UInt64) 方法 |

对寄存器先写后读，比较值是否一样
更新SingleRegister界面Value、ReadBackValue和Mask

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
Dictionary<string, bool> CheckSingleRegister(
	string registerName,
	string[] fieldNames,
	ulong[] fieldValues
)
```

###### 参数

registerName  String
:   寄存器名称

fieldNames  String
:   寄存器位段名称数组

fieldValues  UInt64
:   寄存器位段写入值数组

###### 返回值

DictionaryString, Boolean  
检查结果

异常

| 异常 | 条件 |
| --- | --- |
| ArgumentNullException |  |
| ArgumentException |  |
| NotSupportedException |  |

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[CheckSingleRegister 重载](0df97fbe-6e1b-845c-2e8e-c7239b61e35a.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### CheckSingleRegister(String, UInt64, UInt64) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorCheckSingleRegister(String, UInt64, UInt64) 方法 |

对寄存器先写后读，比较值是否一样
更新SingleRegister界面Value和ReadBackValue和Mask

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool CheckSingleRegister(
	string moduleName,
	ulong address,
	ulong value
)
```

###### 参数

moduleName  String
:   寄存器模块名称

address  UInt64
:   寄存器地址

value  UInt64
:   寄存器值

###### 返回值

Boolean

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[CheckSingleRegister 重载](0df97fbe-6e1b-845c-2e8e-c7239b61e35a.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Command 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorCommand 方法 |

执行Register Command脚本

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string Command(
	string commandName
)
```

###### 参数

commandName  String
:   已保存的脚本名称

###### 返回值

String  
执行结果输出

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetAllFieldNameInRegister 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorGetAllFieldNameInRegister 方法 |

通过寄存器名字获取该寄存器中的所有Field名称

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string[] GetAllFieldNameInRegister(
	string registerName
)
```

###### 参数

registerName  String
:   寄存器名称

###### 返回值

String  
返回一个Array类型，寄存器Field集合

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetAllRegisterGroups 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorGetAllRegisterGroups 方法 |

获取所有寄存器组的名称

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string[] GetAllRegisterGroups()
```

###### 返回值

String  
返回一个Array类型，寄存器组名称集合

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetAllRegisters 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorGetAllRegisters 方法 |

获取所有寄存器的名称

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string[] GetAllRegisters()
```

###### 返回值

String  
返回一个Array类型，寄存器名称集合

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetFieldLocation 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorGetFieldLocation 方法 |

通过字段名称获取字段地址

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetFieldLocation(
	string registerName,
	string fieldName
)
```

###### 参数

registerName  String

fieldName  String

###### 返回值

String

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetFieldName 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorGetFieldName 方法 |

通过字段地址获取字段名称

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetFieldName(
	string registerName,
	string fieldLocation
)
```

###### 参数

registerName  String

fieldLocation  String

###### 返回值

String

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetGroupRegisters 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorGetGroupRegisters 方法 |

通过寄存器组名字获取该寄存器组中的所有寄存器名称

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string[] GetGroupRegisters(
	string groupName
)
```

###### 参数

groupName  String
:   寄存器组名称

###### 返回值

String  
返回一个Array类型，寄存器名称集合

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetRegisterAddress 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorGetRegisterAddress 方法 |

通过RegisterName获取RegisterAddress

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
ulong GetRegisterAddress(
	string registerName
)
```

###### 参数

registerName  String

###### 返回值

UInt64

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetRegisterField 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorGetRegisterField 方法 |

读单个寄存器指定位段值

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
ulong[] GetRegisterField(
	string registerName,
	string[] fieldNames
)
```

###### 参数

registerName  String
:   寄存器名称

fieldNames  String
:   寄存器位段名称数组

###### 返回值

UInt64  
指定的寄存器位段值

异常

| 异常 | 条件 |
| --- | --- |
| ArgumentNullException |  |
| ArgumentException |  |
| NotSupportedException |  |

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetRegisterFieldInGroup 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorGetRegisterFieldInGroup 方法 |

通过寄存器名字获取field列表
不涉及界面更新

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
List<Dictionary<string, ulong>> GetRegisterFieldInGroup(
	string groupName,
	string registerName,
	int registerIndex = -1
)
```

###### 参数

groupName  String
:   寄存器组名称

registerName  String
:   寄存器名称

registerIndex  Int32  (Optional)
:   寄存器序列值

###### 返回值

ListDictionaryString, UInt64  
返回一个List类型，寄存器位段列表

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetRegisterName 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorGetRegisterName 方法 |

通过address获取RegisterName

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetRegisterName(
	ulong address
)
```

###### 参数

address  UInt64

###### 返回值

String

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetRegisterValue 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorGetRegisterValue 方法 |

通过RegisterName获取RegisterValue

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
ulong GetRegisterValue(
	string registerName
)
```

###### 参数

registerName  String

###### 返回值

UInt64

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetRegisterValueInGroup 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorGetRegisterValueInGroup 方法 |

获取寄存器组中寄存器的值
不涉及界面更新

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
ulong GetRegisterValueInGroup(
	string groupName,
	string registerName,
	int indexInGroup = -1
)
```

###### 参数

groupName  String
:   寄存器组名称

registerName  String
:   寄存器名称

indexInGroup  Int32  (Optional)
:   寄存器序列值

###### 返回值

UInt64

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GlobalModifyModulePreset 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorGlobalModifyModulePreset 方法 |

全局修改Module的Preset设置
更新界面配置，生命周期为本次Flow运行

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void GlobalModifyModulePreset(
	string moduleName,
	string instrumentName,
	string presetName
)
```

###### 参数

moduleName  String

instrumentName  String

presetName  String

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GlobalResetRegistertoDefaultValue 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorGlobalResetRegistertoDefaultValue 方法 |

全局将寄存器的值重置回defaultvalue，同时其Fields也保持与Default值同步;
本次Flow运行期间生效，更新SingleRegister界面的Value和Mask字段

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void GlobalResetRegistertoDefaultValue(
	string registerName
)
```

###### 参数

registerName  String
:   寄存器名称

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GlobalSetRegisterField 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorGlobalSetRegisterField 方法 |

全局设置寄存器位段值
本次Flow运行期间生效，不更新界面

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void GlobalSetRegisterField(
	string registerName,
	string[] fieldNames,
	ulong[] fieldValues
)
```

###### 参数

registerName  String
:   寄存器名称

fieldNames  String
:   寄存器位段名称数组

fieldValues  UInt64
:   寄存器位段写入值数组

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GlobalSetRegisterValueInGroup 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorGlobalSetRegisterValueInGroup 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [GlobalSetRegisterValueInGroup(String, String, UInt64, Int32)](d19d143d-ad17-ca67-477f-db3e07435dbf.htm) | 全局设置寄存器组中寄存器的值 更新RegisterGroup界面的Value值，本次Flow运行周期内生效 |
| 公共方法 | [GlobalSetRegisterValueInGroup(String, String, String, UInt64, Int32)](07122762-15ee-fb1f-4525-81e3d8612632.htm) | 全局设置寄存器组中寄存器位段的值 更新RegisterGroup界面的Value值，本次Flow运行周期内生效 |
| 公共方法 | [GlobalSetRegisterValueInGroup(String, String, String, UInt64, Int32)](c60931e6-2513-2624-7993-887dec60df7b.htm) | 全局设置寄存器组中寄存器位段的值 更新RegisterGroup界面的Value值，本次Flow运行周期内生效 |

[Top](#PageHeader)

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### GlobalSetRegisterValueInGroup(String, String, UInt64, Int32) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorGlobalSetRegisterValueInGroup(String, String, UInt64, Int32) 方法 |

全局设置寄存器组中寄存器的值
更新RegisterGroup界面的Value值，本次Flow运行周期内生效

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void GlobalSetRegisterValueInGroup(
	string groupName,
	string registerName,
	ulong registerValue,
	int indexInGroup = -1
)
```

###### 参数

groupName  String
:   寄存器组名称

registerName  String
:   寄存器名称

registerValue  UInt64
:   寄存器值

indexInGroup  Int32  (Optional)
:   寄存器序列值

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[GlobalSetRegisterValueInGroup 重载](f6b342ff-a4c6-5985-edf6-33c57e2ae2f9.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### GlobalSetRegisterValueInGroup(String, String, String, UInt64, Int32) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorGlobalSetRegisterValueInGroup(String, String, String, UInt64, Int32) 方法 |

全局设置寄存器组中寄存器位段的值
更新RegisterGroup界面的Value值，本次Flow运行周期内生效

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void GlobalSetRegisterValueInGroup(
	string groupName,
	string registerName,
	string fieldName,
	ulong fieldValue,
	int indexInGroup = -1
)
```

###### 参数

groupName  String
:   寄存器组名称

registerName  String
:   寄存器名称

fieldName  String
:   位段名称

fieldValue  UInt64
:   位段值

indexInGroup  Int32  (Optional)
:   寄存器序列值

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[GlobalSetRegisterValueInGroup 重载](f6b342ff-a4c6-5985-edf6-33c57e2ae2f9.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### GlobalSetRegisterValueInGroup(String, String, String[], UInt64[], Int32) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorGlobalSetRegisterValueInGroup(String, String, String, UInt64, Int32) 方法 |

全局设置寄存器组中寄存器位段的值
更新RegisterGroup界面的Value值，本次Flow运行周期内生效

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void GlobalSetRegisterValueInGroup(
	string groupName,
	string registerName,
	string[] fieldNames,
	ulong[] fieldValues,
	int indexInGroup = -1
)
```

###### 参数

groupName  String
:   寄存器组名称

registerName  String
:   寄存器名称

fieldNames  String
:   位段名称数组

fieldValues  UInt64
:   位段值数组

indexInGroup  Int32  (Optional)
:   寄存器序列值

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[GlobalSetRegisterValueInGroup 重载](f6b342ff-a4c6-5985-edf6-33c57e2ae2f9.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GlobalSetSingleRegister 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorGlobalSetSingleRegister 方法 |

全局设置寄存器值，
本次Flow运行期间生效，不更新界面

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void GlobalSetSingleRegister(
	string registerName,
	ulong value
)
```

###### 参数

registerName  String
:   寄存器名称

value  UInt64
:   寄存器写入值

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### ModifyModulePreset 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorModifyModulePreset 方法 |

修改Module的Preset设置
当前TestSuite生效，不影响下一个TestSuite运行

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ModifyModulePreset(
	string moduleName,
	string instrumentName,
	string presetName
)
```

###### 参数

moduleName  String

instrumentName  String

presetName  String

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### ReadRegisterByModule 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorReadRegisterByModule 方法 |

读单个寄存器
更新SingleRegister界面ReadBackValue

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
ulong ReadRegisterByModule(
	string moduleName,
	ulong address
)
```

###### 参数

moduleName  String
:   寄存器中存在的Module

address  UInt64
:   寄存器地址,可以是不存在的地址

###### 返回值

UInt64  
指定的寄存器值

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### ReadRegisterGroup 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorReadRegisterGroup 方法 |

读寄存器组
更新SingleRegister界面的ReadBackValue和RegisterGroup界面的ReadBackValue

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
Dictionary<ulong, ulong> ReadRegisterGroup(
	string groupName
)
```

###### 参数

groupName  String
:   寄存器组名称

###### 返回值

DictionaryUInt64, UInt64

异常

| 异常 | 条件 |
| --- | --- |
| Exception |  |

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### ReadSingleRegister 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorReadSingleRegister 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [ReadSingleRegister(String)](351c94ea-6a09-2c53-2a47-70b5a0f37ade.htm) | 读单个寄存器 更新SingleRegister界面ReadBackValue |
| 公共方法 | [ReadSingleRegister(UInt64)](a77f6c9e-5e20-48fa-976a-af29023fb2ed.htm) | 读单个寄存器 更新SingleRegister界面ReadBackValue |
| 公共方法 | [ReadSingleRegister(String, String)](86c9fdf9-2a0f-2e7b-c491-ef7573e8a07d.htm) | 读单个寄存器 更新SingleRegister界面ReadBackValue |

[Top](#PageHeader)

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### ReadSingleRegister(String) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorReadSingleRegister(String) 方法 |

读单个寄存器
更新SingleRegister界面ReadBackValue

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
ulong ReadSingleRegister(
	string registerName
)
```

###### 参数

registerName  String
:   寄存器名称

###### 返回值

UInt64  
指定的寄存器值

异常

| 异常 | 条件 |
| --- | --- |
| ArgumentException |  |

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[ReadSingleRegister 重载](2368754a-bf07-dddc-2e32-7c82a392e92f.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### ReadSingleRegister(UInt64) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorReadSingleRegister(UInt64) 方法 |

读单个寄存器
更新SingleRegister界面ReadBackValue

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
ulong ReadSingleRegister(
	ulong address
)
```

###### 参数

address  UInt64
:   寄存器地址

###### 返回值

UInt64  
指定的寄存器值

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[ReadSingleRegister 重载](2368754a-bf07-dddc-2e32-7c82a392e92f.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### ReadSingleRegister(String, String[]) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorReadSingleRegister(String, String) 方法 |

读单个寄存器
更新SingleRegister界面ReadBackValue

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
ulong[] ReadSingleRegister(
	string registerName,
	string[] fieldNames
)
```

###### 参数

registerName  String
:   寄存器名称

fieldNames  String
:   寄存器位段名称数组

###### 返回值

UInt64  
指定的寄存器位段值

异常

| 异常 | 条件 |
| --- | --- |
| ArgumentNullException |  |
| ArgumentException |  |
| NotSupportedException |  |

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[ReadSingleRegister 重载](2368754a-bf07-dddc-2e32-7c82a392e92f.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### ResetRegistertoDefaultValue 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorResetRegistertoDefaultValue 方法 |

将寄存器的值重置回defaultvalue，同时其Fields也保持与Default值同步;
只在当前TestSuite内生效，不更新界面

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ResetRegistertoDefaultValue(
	string registerName
)
```

###### 参数

registerName  String
:   寄存器名称

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### SetRegisterField 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorSetRegisterField 方法 |

设置寄存器位段值
只在当前TestSuite内生效，不更新界面

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetRegisterField(
	string registerName,
	string[] fieldNames,
	ulong[] fieldValues
)
```

###### 参数

registerName  String
:   寄存器名称

fieldNames  String
:   寄存器位段名称数组

fieldValues  UInt64
:   寄存器位段写入值数组

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### SetRegisterValueInGroup 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorSetRegisterValueInGroup 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [SetRegisterValueInGroup(String, String, UInt64, Int32)](1b8c42ad-eaeb-5731-ed3e-ecbba9e88de3.htm) | 设置寄存器组中寄存器的值 不更新任何界面 |
| 公共方法 | [SetRegisterValueInGroup(String, String, String, UInt64, Int32)](03c2e1dd-3c95-cf02-5d2c-fb7df8195bf5.htm) | 设置寄存器组中寄存器位段的值 不更新任何界面 |
| 公共方法 | [SetRegisterValueInGroup(String, String, String, UInt64, Int32)](abc21a5d-1c27-3067-8e68-ef98f527181e.htm) | 设置寄存器组中寄存器位段的值 不更新任何界面 |

[Top](#PageHeader)

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### SetRegisterValueInGroup(String, String, UInt64, Int32) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorSetRegisterValueInGroup(String, String, UInt64, Int32) 方法 |

设置寄存器组中寄存器的值
不更新任何界面

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetRegisterValueInGroup(
	string groupName,
	string registerName,
	ulong registerValue,
	int indexInGroup = -1
)
```

###### 参数

groupName  String
:   寄存器组名称

registerName  String
:   寄存器名称

registerValue  UInt64
:   寄存器值

indexInGroup  Int32  (Optional)
:   寄存器序列值

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[SetRegisterValueInGroup 重载](1c0033e7-4f4d-1084-6504-8a658ee6b367.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### SetRegisterValueInGroup(String, String, String, UInt64, Int32) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorSetRegisterValueInGroup(String, String, String, UInt64, Int32) 方法 |

设置寄存器组中寄存器位段的值
不更新任何界面

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetRegisterValueInGroup(
	string groupName,
	string registerName,
	string fieldName,
	ulong fieldValue,
	int indexInGroup = -1
)
```

###### 参数

groupName  String
:   寄存器组名称

registerName  String
:   寄存器名称

fieldName  String
:   位段名称

fieldValue  UInt64
:   位段值

indexInGroup  Int32  (Optional)
:   寄存器序列值

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[SetRegisterValueInGroup 重载](1c0033e7-4f4d-1084-6504-8a658ee6b367.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### SetRegisterValueInGroup(String, String, String[], UInt64[], Int32) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorSetRegisterValueInGroup(String, String, String, UInt64, Int32) 方法 |

设置寄存器组中寄存器位段的值
不更新任何界面

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetRegisterValueInGroup(
	string groupName,
	string registerName,
	string[] fieldNames,
	ulong[] fieldValues,
	int indexInGroup = -1
)
```

###### 参数

groupName  String
:   寄存器组名称

registerName  String
:   寄存器名称

fieldNames  String
:   位段名称数组

fieldValues  UInt64
:   位段值数组

indexInGroup  Int32  (Optional)
:   寄存器序列值

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[SetRegisterValueInGroup 重载](1c0033e7-4f4d-1084-6504-8a658ee6b367.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### SetSingleRegister 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorSetSingleRegister 方法 |

设置寄存器值
只在当前TestSuite内生效，不更新界面

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSingleRegister(
	string registerName,
	ulong value
)
```

###### 参数

registerName  String
:   寄存器名称

value  UInt64
:   寄存器写入值

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### VerifyRegisterGroup 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorVerifyRegisterGroup 方法 |

验证寄存器组
更新SingleRegister界面的ReadBackValue、Value和Mask，更新RegisterGroup界面的ReadBackValue
Mask取内存(也是界面设置的)中的值

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
Dictionary<ulong, bool> VerifyRegisterGroup(
	string groupName
)
```

###### 参数

groupName  String
:   寄存器组名称

###### 返回值

DictionaryUInt64, Boolean

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### WriteRegisterByModule 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorWriteRegisterByModule 方法 |

写单个寄存器
更新SingleRegister界面Value和Mask

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteRegisterByModule(
	string moduleName,
	ulong address,
	ulong value,
	ulong valueMask = 18446744073709551615
)
```

###### 参数

moduleName  String
:   寄存器模块名称

address  UInt64
:   寄存器地址,可以是不存在的地址

value  UInt64
:   寄存器写入值

valueMask  UInt64  (Optional)
:   寄存器写入值掩码, 如果不加将和下面一个接口重复

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### WriteRegisterGroup 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorWriteRegisterGroup 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [WriteRegisterGroup(String)](f480f332-a9f3-33c2-d3ff-d05d464e8d37.htm) | 写寄存器组 更新SingleRegister界面的Value和Mask Mask取内存(也是界面设置的)中的值 |
| 公共方法 | [WriteRegisterGroup(String, UInt64)](6ebecdc6-0272-ef90-b8e5-396b139b999d.htm) | 写寄存器组 更新SingleRegister界面的Value和Mask Mask取所有可写字段对应的Mask |

[Top](#PageHeader)

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### WriteRegisterGroup(String) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorWriteRegisterGroup(String) 方法 |

写寄存器组
更新SingleRegister界面的Value和Mask
Mask取内存(也是界面设置的)中的值

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteRegisterGroup(
	string groupName
)
```

###### 参数

groupName  String
:   寄存器组名称

异常

| 异常 | 条件 |
| --- | --- |
| Exception |  |

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[WriteRegisterGroup 重载](0c6aaab9-9041-b8b6-02bc-a6b0f2ef42c5.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### WriteRegisterGroup(String, UInt64[]) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorWriteRegisterGroup(String, UInt64) 方法 |

写寄存器组
更新SingleRegister界面的Value和Mask
Mask取所有可写字段对应的Mask

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteRegisterGroup(
	string groupName,
	ulong[] registerValues
)
```

###### 参数

groupName  String
:   寄存器组名称

registerValues  UInt64
:   寄存器组写入值数组

异常

| 异常 | 条件 |
| --- | --- |
| ArgumentException |  |
| Exception |  |

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[WriteRegisterGroup 重载](0c6aaab9-9041-b8b6-02bc-a6b0f2ef42c5.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### WriteSingleRegister 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorWriteSingleRegister 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [WriteSingleRegister(String, Boolean)](e9e5fdef-c44c-93f6-87b5-e724d0e597f1.htm) | 写单个寄存器 更新SingleRegister界面Value和Mask Mask取内存(也是界面设置的)中的值 |
| 公共方法 | [WriteSingleRegister(String, String, UInt64)](a5ce85dd-d5eb-d29d-9cf3-56ad53b4ad50.htm) | 写单个寄存器 更新SingleRegister界面Value和Mask |
| 公共方法 | [WriteSingleRegister(String, UInt64, Boolean)](80f24806-7445-187e-da9a-2cfcc03ed76d.htm) | 写单个寄存器 更新SingleRegister界面Value和Mask Mask取所有可写字段对应的Mask |
| 公共方法 | [WriteSingleRegister(String, UInt64, UInt64)](3beb2f8a-70e2-1421-2685-8f8a62303d85.htm) | 写单个寄存器 更新SingleRegister界面Value和Mask |
| 公共方法 | [WriteSingleRegister(UInt64, UInt64, Boolean)](106b9788-c043-34cd-6149-8a5fd08209ab.htm) | 写单个寄存器 更新SingleRegister界面Value和Mask Mask取所有可写字段对应的Mask |

[Top](#PageHeader)

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### WriteSingleRegister(String, Boolean) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorWriteSingleRegister(String, Boolean) 方法 |

写单个寄存器
更新SingleRegister界面Value和Mask
Mask取内存(也是界面设置的)中的值

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteSingleRegister(
	string registerName,
	bool forcedWriteOnly = false
)
```

###### 参数

registerName  String
:   寄存器名称

forcedWriteOnly  Boolean  (Optional)
:   是否force写入(即使有Field是RO，直接按照指定Value写入)可选，默认false

异常

| 异常 | 条件 |
| --- | --- |
| ArgumentException |  |

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[WriteSingleRegister 重载](139e5832-634d-67da-13ca-d79787cc9591.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### WriteSingleRegister(String, String[], UInt64[]) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorWriteSingleRegister(String, String, UInt64) 方法 |

写单个寄存器
更新SingleRegister界面Value和Mask

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteSingleRegister(
	string registerName,
	string[] fieldNames,
	ulong[] fieldValues
)
```

###### 参数

registerName  String
:   寄存器名称

fieldNames  String
:   寄存器位段名称数组

fieldValues  UInt64
:   寄存器位段写入值数组

异常

| 异常 | 条件 |
| --- | --- |
| ArgumentException |  |

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[WriteSingleRegister 重载](139e5832-634d-67da-13ca-d79787cc9591.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### WriteSingleRegister(String, UInt64, Boolean) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorWriteSingleRegister(String, UInt64, Boolean) 方法 |

写单个寄存器
更新SingleRegister界面Value和Mask
Mask取所有可写字段对应的Mask

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteSingleRegister(
	string registerName,
	ulong value,
	bool forcedWriteOnly = false
)
```

###### 参数

registerName  String
:   寄存器名称

value  UInt64
:   寄存器写入值

forcedWriteOnly  Boolean  (Optional)
:   是否force写入(即使有Field是RO，直接按照指定Value写入)可选，默认false

异常

| 异常 | 条件 |
| --- | --- |
| ArgumentException |  |

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[WriteSingleRegister 重载](139e5832-634d-67da-13ca-d79787cc9591.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### WriteSingleRegister(String, UInt64, UInt64) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorWriteSingleRegister(String, UInt64, UInt64) 方法 |

写单个寄存器
更新SingleRegister界面Value和Mask

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteSingleRegister(
	string registerName,
	ulong value,
	ulong valueMask
)
```

###### 参数

registerName  String
:   寄存器名称

value  UInt64
:   寄存器写入值

valueMask  UInt64
:   寄存器写入值掩码

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[WriteSingleRegister 重载](139e5832-634d-67da-13ca-d79787cc9591.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### WriteSingleRegister(UInt64, UInt64, Boolean) 方法

|  |  |
| --- | --- |
|  | IRegisterAccessorWriteSingleRegister(UInt64, UInt64, Boolean) 方法 |

写单个寄存器
更新SingleRegister界面Value和Mask
Mask取所有可写字段对应的Mask

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteSingleRegister(
	ulong address,
	ulong value,
	bool forcedWriteOnly = false
)
```

###### 参数

address  UInt64
:   寄存器地址

value  UInt64
:   寄存器写入值

forcedWriteOnly  Boolean  (Optional)
:   是否force写入(即使有Field是RO，直接按照指定Value写入)可选，默认false

参见

###### 引用

[IRegisterAccessor 接口](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

[WriteSingleRegister 重载](139e5832-634d-67da-13ca-d79787cc9591.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## ISwitchAccessor 接口

|  |  |
| --- | --- |
|  | ISwitchAccessor 接口 |

继电器操作接口

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public interface ISwitchAccessor
```

ISwitchAccessor 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Apply](2d96db60-13b1-fb43-7874-85558009208f.htm) | 根据switchRouteName对Group中的Connect进行操作，按照编辑的顺序进行连接和断开的操作 |
| 公共方法 | [Connect](46148fee-9bba-0e63-da26-b5eb8fe2a855.htm) | 根据switchRouteName连接Switch，只连接其中标记为Connect的Path |
| 公共方法 | [Disconnect](2325e648-86fe-c479-d6bb-29ba0f563d5d.htm) | 根据switchRouteName断开Switch连接，只断开其中标记为Disconnect的Path |
| 公共方法 | [DisconnectAll](6b276f2b-e3bd-2a11-a4e0-ce6aefdd4e75.htm) | 断开所有连接 |
| 公共方法 | [DisconnectByInstrument](3548c99f-8119-6614-3442-06aaadfd515e.htm) | 断开某个仪表的所有Path连接 |
| 公共方法 | [Revert](0897d59f-4b7d-a0a9-6e3c-0b52e46f46c6.htm) | 调用Apply后，按照连接的倒序进行反向操作操作(Connect改为Disconnect，Disconnect改为Connect) |
| 公共方法 | [Status](df949ef9-bac0-14c8-6f5b-981f41917f16.htm) | 根据switchRouteName返回switch状态 |

[Top](#PageHeader)

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### ISwitchAccessor 方法

|  |  |
| --- | --- |
|  | ISwitchAccessor 方法 |

[ISwitchAccessor](f4adcf92-99fb-8004-0cf6-b59040e967eb.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Apply](2d96db60-13b1-fb43-7874-85558009208f.htm) | 根据switchRouteName对Group中的Connect进行操作，按照编辑的顺序进行连接和断开的操作 |
| 公共方法 | [Connect](46148fee-9bba-0e63-da26-b5eb8fe2a855.htm) | 根据switchRouteName连接Switch，只连接其中标记为Connect的Path |
| 公共方法 | [Disconnect](2325e648-86fe-c479-d6bb-29ba0f563d5d.htm) | 根据switchRouteName断开Switch连接，只断开其中标记为Disconnect的Path |
| 公共方法 | [DisconnectAll](6b276f2b-e3bd-2a11-a4e0-ce6aefdd4e75.htm) | 断开所有连接 |
| 公共方法 | [DisconnectByInstrument](3548c99f-8119-6614-3442-06aaadfd515e.htm) | 断开某个仪表的所有Path连接 |
| 公共方法 | [Revert](0897d59f-4b7d-a0a9-6e3c-0b52e46f46c6.htm) | 调用Apply后，按照连接的倒序进行反向操作操作(Connect改为Disconnect，Disconnect改为Connect) |
| 公共方法 | [Status](df949ef9-bac0-14c8-6f5b-981f41917f16.htm) | 根据switchRouteName返回switch状态 |

[Top](#PageHeader)

参见

###### 引用

[ISwitchAccessor 接口](f4adcf92-99fb-8004-0cf6-b59040e967eb.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Apply 方法

|  |  |
| --- | --- |
|  | ISwitchAccessorApply 方法 |

根据switchRouteName对Group中的Connect进行操作，按照编辑的顺序进行连接和断开的操作

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Apply(
	string switchRouteName,
	bool parallel = false
)
```

###### 参数

switchRouteName  String
:   switchPathGroup名称

parallel  Boolean  (Optional)
:   是否并行执行

参见

###### 引用

[ISwitchAccessor 接口](f4adcf92-99fb-8004-0cf6-b59040e967eb.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Connect 方法

|  |  |
| --- | --- |
|  | ISwitchAccessorConnect 方法 |

根据switchRouteName连接Switch，只连接其中标记为Connect的Path

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Connect(
	string switchRouteName,
	bool parallel = false
)
```

###### 参数

switchRouteName  String
:   switchPathGroup名称

parallel  Boolean  (Optional)
:   是否并行执行

参见

###### 引用

[ISwitchAccessor 接口](f4adcf92-99fb-8004-0cf6-b59040e967eb.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Disconnect 方法

|  |  |
| --- | --- |
|  | ISwitchAccessorDisconnect 方法 |

根据switchRouteName断开Switch连接，只断开其中标记为Disconnect的Path

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Disconnect(
	string switchRouteName,
	bool parallel = false
)
```

###### 参数

switchRouteName  String
:   switchPathGroup名称

parallel  Boolean  (Optional)
:   是否并行执行

参见

###### 引用

[ISwitchAccessor 接口](f4adcf92-99fb-8004-0cf6-b59040e967eb.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### DisconnectAll 方法

|  |  |
| --- | --- |
|  | ISwitchAccessorDisconnectAll 方法 |

断开所有连接

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void DisconnectAll(
	bool parallel = false
)
```

###### 参数

parallel  Boolean  (Optional)
:   是否并行执行

参见

###### 引用

[ISwitchAccessor 接口](f4adcf92-99fb-8004-0cf6-b59040e967eb.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### DisconnectByInstrument 方法

|  |  |
| --- | --- |
|  | ISwitchAccessorDisconnectByInstrument 方法 |

断开某个仪表的所有Path连接

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void DisconnectByInstrument(
	string instrumentName,
	bool parallel = false
)
```

###### 参数

instrumentName  String
:   仪表名称

parallel  Boolean  (Optional)
:   是否并行执行

参见

###### 引用

[ISwitchAccessor 接口](f4adcf92-99fb-8004-0cf6-b59040e967eb.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Revert 方法

|  |  |
| --- | --- |
|  | ISwitchAccessorRevert 方法 |

调用Apply后，按照连接的倒序进行反向操作操作(Connect改为Disconnect，Disconnect改为Connect)

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Revert(
	string switchRouteName,
	bool parallel = false
)
```

###### 参数

switchRouteName  String
:   switchPathGroup名称

parallel  Boolean  (Optional)
:   是否并行执行

参见

###### 引用

[ISwitchAccessor 接口](f4adcf92-99fb-8004-0cf6-b59040e967eb.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Status 方法

|  |  |
| --- | --- |
|  | ISwitchAccessorStatus 方法 |

根据switchRouteName返回switch状态

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
Dictionary<string, Dictionary<string, SwitchStatus>> Status(
	string switchRouteName
)
```

###### 参数

switchRouteName  String
:   switchPathGroup名称

###### 返回值

DictionaryString, DictionaryString, SwitchStatus  
dictionary的集合，key是instrument name, value是dicitionary的集合，value的key是 path name, value的value是switch status

参见

###### 引用

[ISwitchAccessor 接口](f4adcf92-99fb-8004-0cf6-b59040e967eb.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## ITestMethod 接口

|  |  |
| --- | --- |
|  | ITestMethod 接口 |

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public interface ITestMethod
```

ITestMethod 类型公开以下成员。

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [SemiContext](423234cf-e1d6-9cf3-bfc0-5afc5eedf9ef.htm) | 测试执行上下文 每个Site在Flow测试周期内有唯一的SemiContext |
| 公共属性 | [TestMethodName](051c7331-6df0-9291-3df9-18c7e7e42f89.htm) | TestMethod名称 |

[Top](#PageHeader)

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Execute](1463c7a6-ef51-6c85-08f7-058c4b4b5997.htm) | TestSuite的Execute |
| 公共方法 | [GetInputParameters](ece165ba-2647-4d37-e487-6566d19fc819.htm) | 获取当前运行状态下所有开放参数的实时值 |
| 公共方法 | [Initialize](965f13d3-7d40-cc8a-1719-52f893fc75a1.htm) | TM初始化方法，在Debug或者Flow任务启动前运行一次 用户TM可以重写此方法，但要调用基类的此方法 |
| 公共方法 | [OnParameterChange](757bbf16-fb3f-5911-38d6-1d01a77f2182.htm) | 当运行中修改了TestSuite的Configuration，则会触发此事件 如果有需要，用户可以在TM中重写此方法 |
| 公共方法 | [PostExecute](d0944ef8-3071-76c6-935a-7e01a360b8cd.htm) | 每次执行TestSuite的Execute方法之后会执行此方法 如果有需要，用户可以在TM中重写此方法 |
| 公共方法 | [PreExecute](2e53cd21-0d75-910e-4ce7-0fceb0eac326.htm) | 每次执行TestSuite的Execute方法之前会执行此方法 如果有需要，用户可以在TM中重写此方法 |

[Top](#PageHeader)

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### ITestMethod 属性

|  |  |
| --- | --- |
|  | ITestMethod 属性 |

[ITestMethod](c4400014-a326-7727-d895-39228f0667f3.htm) 类型公开以下成员。

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [SemiContext](423234cf-e1d6-9cf3-bfc0-5afc5eedf9ef.htm) | 测试执行上下文 每个Site在Flow测试周期内有唯一的SemiContext |
| 公共属性 | [TestMethodName](051c7331-6df0-9291-3df9-18c7e7e42f89.htm) | TestMethod名称 |

[Top](#PageHeader)

参见

###### 引用

[ITestMethod 接口](c4400014-a326-7727-d895-39228f0667f3.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### SemiContext 属性

|  |  |
| --- | --- |
|  | ITestMethodSemiContext 属性 |

测试执行上下文
每个Site在Flow测试周期内有唯一的SemiContext

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
SemiContext SemiContext { get; }
```

###### 属性值

[SemiContext](421aec95-4c88-392e-653b-28511d2c5421.htm)

参见

###### 引用

[ITestMethod 接口](c4400014-a326-7727-d895-39228f0667f3.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### TestMethodName 属性

|  |  |
| --- | --- |
|  | ITestMethodTestMethodName 属性 |

TestMethod名称

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string TestMethodName { get; }
```

###### 属性值

String

参见

###### 引用

[ITestMethod 接口](c4400014-a326-7727-d895-39228f0667f3.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### ITestMethod 方法

|  |  |
| --- | --- |
|  | ITestMethod 方法 |

[ITestMethod](c4400014-a326-7727-d895-39228f0667f3.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Execute](1463c7a6-ef51-6c85-08f7-058c4b4b5997.htm) | TestSuite的Execute |
| 公共方法 | [GetInputParameters](ece165ba-2647-4d37-e487-6566d19fc819.htm) | 获取当前运行状态下所有开放参数的实时值 |
| 公共方法 | [Initialize](965f13d3-7d40-cc8a-1719-52f893fc75a1.htm) | TM初始化方法，在Debug或者Flow任务启动前运行一次 用户TM可以重写此方法，但要调用基类的此方法 |
| 公共方法 | [OnParameterChange](757bbf16-fb3f-5911-38d6-1d01a77f2182.htm) | 当运行中修改了TestSuite的Configuration，则会触发此事件 如果有需要，用户可以在TM中重写此方法 |
| 公共方法 | [PostExecute](d0944ef8-3071-76c6-935a-7e01a360b8cd.htm) | 每次执行TestSuite的Execute方法之后会执行此方法 如果有需要，用户可以在TM中重写此方法 |
| 公共方法 | [PreExecute](2e53cd21-0d75-910e-4ce7-0fceb0eac326.htm) | 每次执行TestSuite的Execute方法之前会执行此方法 如果有需要，用户可以在TM中重写此方法 |

[Top](#PageHeader)

参见

###### 引用

[ITestMethod 接口](c4400014-a326-7727-d895-39228f0667f3.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Execute 方法

|  |  |
| --- | --- |
|  | ITestMethodExecute 方法 |

TestSuite的Execute

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Execute()
```

参见

###### 引用

[ITestMethod 接口](c4400014-a326-7727-d895-39228f0667f3.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetInputParameters 方法

|  |  |
| --- | --- |
|  | ITestMethodGetInputParameters 方法 |

获取当前运行状态下所有开放参数的实时值

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
Dictionary<string, Object> GetInputParameters()
```

###### 返回值

DictionaryString, Object

参见

###### 引用

[ITestMethod 接口](c4400014-a326-7727-d895-39228f0667f3.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Initialize 方法

|  |  |
| --- | --- |
|  | ITestMethodInitialize 方法 |

TM初始化方法，在Debug或者Flow任务启动前运行一次
用户TM可以重写此方法，但要调用基类的此方法

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Initialize(
	SemiContext semiContext
)
```

###### 参数

semiContext  [SemiContext](421aec95-4c88-392e-653b-28511d2c5421.htm)

参见

###### 引用

[ITestMethod 接口](c4400014-a326-7727-d895-39228f0667f3.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### OnParameterChange 方法

|  |  |
| --- | --- |
|  | ITestMethodOnParameterChange 方法 |

当运行中修改了TestSuite的Configuration，则会触发此事件
如果有需要，用户可以在TM中重写此方法

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void OnParameterChange()
```

参见

###### 引用

[ITestMethod 接口](c4400014-a326-7727-d895-39228f0667f3.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### PostExecute 方法

|  |  |
| --- | --- |
|  | ITestMethodPostExecute 方法 |

每次执行TestSuite的Execute方法之后会执行此方法
如果有需要，用户可以在TM中重写此方法

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void PostExecute()
```

参见

###### 引用

[ITestMethod 接口](c4400014-a326-7727-d895-39228f0667f3.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### PreExecute 方法

|  |  |
| --- | --- |
|  | ITestMethodPreExecute 方法 |

每次执行TestSuite的Execute方法之前会执行此方法
如果有需要，用户可以在TM中重写此方法

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void PreExecute()
```

参见

###### 引用

[ITestMethod 接口](c4400014-a326-7727-d895-39228f0667f3.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## IVariableAccessor 接口

|  |  |
| --- | --- |
|  | IVariableAccessor 接口 |

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public interface IVariableAccessor
```

IVariableAccessor 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Get(String)](10e60d7e-354c-d0b0-6f4c-ad9d39d612ed.htm) | 获取某个全局变量的值（TestMethod中使用）（非泛型版本） |
| 公共方法 | [GetT(String)](5615bcdb-9ffe-5df1-425b-8df9f75d6fa0.htm) | 获取某个全局变量的值（TestMethod中使用）（泛型版本） |
| 公共方法 | [SetT](6e04f3ed-2f98-399d-b78a-cb405c4eb130.htm) | 设置某个全局变量的值（TestMethod中使用） |
| 公共方法 | [SetVariable](0335d8ee-7211-3820-fdcf-e671c91e9abf.htm) | 根据名字设置某个variable（oi中使用） |

[Top](#PageHeader)

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### IVariableAccessor 方法

|  |  |
| --- | --- |
|  | IVariableAccessor 方法 |

[IVariableAccessor](6e6124cd-87b1-6191-bf37-5a6153dcae9c.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Get(String)](10e60d7e-354c-d0b0-6f4c-ad9d39d612ed.htm) | 获取某个全局变量的值（TestMethod中使用）（非泛型版本） |
| 公共方法 | [GetT(String)](5615bcdb-9ffe-5df1-425b-8df9f75d6fa0.htm) | 获取某个全局变量的值（TestMethod中使用）（泛型版本） |
| 公共方法 | [SetT](6e04f3ed-2f98-399d-b78a-cb405c4eb130.htm) | 设置某个全局变量的值（TestMethod中使用） |
| 公共方法 | [SetVariable](0335d8ee-7211-3820-fdcf-e671c91e9abf.htm) | 根据名字设置某个variable（oi中使用） |

[Top](#PageHeader)

参见

###### 引用

[IVariableAccessor 接口](6e6124cd-87b1-6191-bf37-5a6153dcae9c.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Get 方法

|  |  |
| --- | --- |
|  | IVariableAccessorGet 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Get(String)](10e60d7e-354c-d0b0-6f4c-ad9d39d612ed.htm) | 获取某个全局变量的值（TestMethod中使用）（非泛型版本） |
| 公共方法 | [GetT(String)](5615bcdb-9ffe-5df1-425b-8df9f75d6fa0.htm) | 获取某个全局变量的值（TestMethod中使用）（泛型版本） |

[Top](#PageHeader)

参见

###### 引用

[IVariableAccessor 接口](6e6124cd-87b1-6191-bf37-5a6153dcae9c.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Get(String) 方法

|  |  |
| --- | --- |
|  | IVariableAccessorGet(String) 方法 |

获取某个全局变量的值（TestMethod中使用）（非泛型版本）

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
Object Get(
	string variableName
)
```

###### 参数

variableName  String
:   全局变量的名称

###### 返回值

Object  
全局变量的值

参见

###### 引用

[IVariableAccessor 接口](6e6124cd-87b1-6191-bf37-5a6153dcae9c.htm)

[Get 重载](932bc1ea-1adb-b4c9-3b8a-067d71bc3448.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Get&lt;T&gt;(String) 方法

|  |  |
| --- | --- |
|  | IVariableAccessorGetT(String) 方法 |

获取某个全局变量的值（TestMethod中使用）（泛型版本）

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
T Get<T>(
	string variableName
)
```

###### 参数

variableName  String
:   全局变量的名称

###### 类型参数

T
:   全局变量的类型

###### 返回值

T  
全局变量的值

参见

###### 引用

[IVariableAccessor 接口](6e6124cd-87b1-6191-bf37-5a6153dcae9c.htm)

[Get 重载](932bc1ea-1adb-b4c9-3b8a-067d71bc3448.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Set&lt;T&gt; 方法

|  |  |
| --- | --- |
|  | IVariableAccessorSetT 方法 |

设置某个全局变量的值（TestMethod中使用）

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Set<T>(
	string variableName,
	T variable
)
```

###### 参数

variableName  String
:   全局变量的名称

variable  T
:   全局变量的设置值

###### 类型参数

T
:   全局变量的类型

参见

###### 引用

[IVariableAccessor 接口](6e6124cd-87b1-6191-bf37-5a6153dcae9c.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### SetVariable 方法

|  |  |
| --- | --- |
|  | IVariableAccessorSetVariable 方法 |

根据名字设置某个variable（oi中使用）

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetVariable(
	string variableName,
	Object value,
	bool isEditable = true
)
```

###### 参数

variableName  String
:   全局变量的名称

value  Object
:   全局变量的设置值

isEditable  Boolean  (Optional)

参见

###### 引用

[IVariableAccessor 接口](6e6124cd-87b1-6191-bf37-5a6153dcae9c.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## LogLevel 枚举

|  |  |
| --- | --- |
|  | LogLevel 枚举 |

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public enum LogLevel
```

成员

| 成员名称 | 值 | 说明 |
| --- | --- | --- |
| Debug | 0 |  |
| Info | 1 |  |
| Warn | 2 |  |
| Error | 3 |  |

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## NumberBase 枚举

|  |  |
| --- | --- |
|  | NumberBase 枚举 |

整数进制枚举类

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public enum NumberBase
```

成员

| 成员名称 | 值 | 说明 |
| --- | --- | --- |
| Binary | 2 |  |
| Decimal | 10 |  |
| Hexadecimal | 16 |  |

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## ParametricTestDescriptor 接口

|  |  |
| --- | --- |
|  | ParametricTestDescriptor 接口 |

基于参数的测项定义

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public interface ParametricTestDescriptor
```

ParametricTestDescriptor 类型公开以下成员。

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [CanSkipEval](41532041-7ae9-d829-355c-84164efc4cfb.htm) | Low or High limits are not defined |
| 公共属性 | [HighLimit](7ecf1879-ec58-8644-703c-6581338ae223.htm) | 获取当前Evaluation的HighLimit |
| 公共属性 | [IsLimitNotDefined](7aab5b40-5c7c-e5e2-54ce-43755d1338a5.htm) | 获取当前Evaluation是否设置了Limit的值 |
| 公共属性 | [LowLimit](d9c4555a-58c2-cb16-8948-2356324a3b63.htm) | 获取当前Evaluation的LowLimit |
| 公共属性 | [Scaling](73ac5db8-abeb-46ee-8ffd-ce588c3f41d9.htm) | 获取当前Evaluation的Scaling |
| 公共属性 | [Unit](1d00685c-9dad-c688-718d-1e837fb634a7.htm) | 获取当前Evaluate的值的单位 |

[Top](#PageHeader)

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Concat](38675d6b-1a81-49c2-921a-1c2ae08903de.htm) | 修改或新增Evaluation设置 |
| 公共方法 | [Evaluate(DictionaryString, Double)](bf2604ce-352a-64fa-e227-67fda5062207.htm) | 对测量值进行evaluate，结果将在界面和report体现 |
| 公共方法 | [Evaluate(DictionaryString, String)](9861eb65-cb6b-8523-151c-13f1fb8732f9.htm) | 对测量值进行evaluate，结果将在界面和report体现 |
| 公共方法 | [Evaluate(Double)](2cce93a1-5e01-59a2-b7d6-5b685ea904b6.htm) | 对测量值进行evaluate，结果将在界面和report体现 |
| 公共方法 | [Evaluate(String)](d2f31f61-32fe-3285-4df1-23395a4e06aa.htm) | 对测量值进行evaluate，结果将在界面和report体现 |
| 公共方法 | [Evaluate(DictionaryString, UInt64, NumberBase)](53edc006-983f-dd1c-d8a9-6b5118c8c27d.htm) | 对测量值进行evaluate，结果将在界面和report体现 |
| 公共方法 | [Evaluate(UInt64, NumberBase)](dff9b706-e4f4-1ff7-a035-2ac171d2cd64.htm) | 对测量值进行evaluate，结果将在界面和report体现 |
| 公共方法 | [GetSubEvaluater](f1630a40-074e-1c9e-0569-87aa935045d6.htm) | 获取当前Evaluation子级Evaluation |
| 公共方法 | [Publish(DictionaryString, Double)](4e63421f-5150-21a6-4b56-3c77af3e4ebd.htm) | 对测量值进行Publish，结果将在界面和report体现，不影响分Bin |
| 公共方法 | [Publish(DictionaryString, String)](cc2c45fd-8fc4-9bd9-6e8a-5cdcfdbfccec.htm) | 对测量值进行Publish，结果将在界面和report体现，不影响分Bin |
| 公共方法 | [Publish(Double)](b7b3e8a7-63d7-1057-d1d6-157206b48f5c.htm) | 对测量值进行Publish，结果将在界面和report体现，不影响分Bin |
| 公共方法 | [Publish(String)](17de001b-53ec-214d-fbf8-9b838887759b.htm) | 对测量值进行Publish，结果将在界面和report体现，不影响分Bin |
| 公共方法 | [Publish(DictionaryString, UInt64, NumberBase)](b0133fc9-4d97-7f00-5ae2-b37594de210b.htm) | 对测量值进行evaluate，结果将在界面和report体现，不影响分Bin |
| 公共方法 | [Publish(UInt64, NumberBase)](49cb84db-4d61-09c2-dad2-5b204777bac5.htm) | 对测量值进行Publish，结果将在界面和report体现，不影响分Bin |
| 公共方法 | [SetHighLimit](5aaf1e84-86eb-2675-bc98-7dbb2337c78e.htm) | 设置当前Evaluation的HighLimit值 设置父节点，子节点自动生效，设置子节点则只影响自身 |
| 公共方法 | [SetLowLimit](0433fc4b-736a-f8ed-50ff-1a0657d07d23.htm) | 设置当前Evaluation的LowLimit值 设置父节点，子节点自动生效，设置子节点则只影响自身 |

[Top](#PageHeader)

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### ParametricTestDescriptor 属性

|  |  |
| --- | --- |
|  | ParametricTestDescriptor 属性 |

[ParametricTestDescriptor](3889512c-1f25-5aea-bfc4-901b516e0e52.htm) 类型公开以下成员。

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [CanSkipEval](41532041-7ae9-d829-355c-84164efc4cfb.htm) | Low or High limits are not defined |
| 公共属性 | [HighLimit](7ecf1879-ec58-8644-703c-6581338ae223.htm) | 获取当前Evaluation的HighLimit |
| 公共属性 | [IsLimitNotDefined](7aab5b40-5c7c-e5e2-54ce-43755d1338a5.htm) | 获取当前Evaluation是否设置了Limit的值 |
| 公共属性 | [LowLimit](d9c4555a-58c2-cb16-8948-2356324a3b63.htm) | 获取当前Evaluation的LowLimit |
| 公共属性 | [Scaling](73ac5db8-abeb-46ee-8ffd-ce588c3f41d9.htm) | 获取当前Evaluation的Scaling |
| 公共属性 | [Unit](1d00685c-9dad-c688-718d-1e837fb634a7.htm) | 获取当前Evaluate的值的单位 |

[Top](#PageHeader)

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### CanSkipEval 属性

|  |  |
| --- | --- |
|  | ParametricTestDescriptorCanSkipEval 属性 |

Low or High limits are not defined

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool CanSkipEval { get; }
```

###### 属性值

Boolean

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### HighLimit 属性

|  |  |
| --- | --- |
|  | ParametricTestDescriptorHighLimit 属性 |

获取当前Evaluation的HighLimit

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double HighLimit { get; }
```

###### 属性值

Double

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### IsLimitNotDefined 属性

|  |  |
| --- | --- |
|  | ParametricTestDescriptorIsLimitNotDefined 属性 |

获取当前Evaluation是否设置了Limit的值

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool IsLimitNotDefined { get; }
```

###### 属性值

Boolean

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### LowLimit 属性

|  |  |
| --- | --- |
|  | ParametricTestDescriptorLowLimit 属性 |

获取当前Evaluation的LowLimit

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double LowLimit { get; }
```

###### 属性值

Double

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Scaling 属性

|  |  |
| --- | --- |
|  | ParametricTestDescriptorScaling 属性 |

获取当前Evaluation的Scaling

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double Scaling { get; }
```

###### 属性值

Double

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Unit 属性

|  |  |
| --- | --- |
|  | ParametricTestDescriptorUnit 属性 |

获取当前Evaluate的值的单位

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string Unit { get; }
```

###### 属性值

String

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### ParametricTestDescriptor 方法

|  |  |
| --- | --- |
|  | ParametricTestDescriptor 方法 |

[ParametricTestDescriptor](3889512c-1f25-5aea-bfc4-901b516e0e52.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Concat](38675d6b-1a81-49c2-921a-1c2ae08903de.htm) | 修改或新增Evaluation设置 |
| 公共方法 | [Evaluate(DictionaryString, Double)](bf2604ce-352a-64fa-e227-67fda5062207.htm) | 对测量值进行evaluate，结果将在界面和report体现 |
| 公共方法 | [Evaluate(DictionaryString, String)](9861eb65-cb6b-8523-151c-13f1fb8732f9.htm) | 对测量值进行evaluate，结果将在界面和report体现 |
| 公共方法 | [Evaluate(Double)](2cce93a1-5e01-59a2-b7d6-5b685ea904b6.htm) | 对测量值进行evaluate，结果将在界面和report体现 |
| 公共方法 | [Evaluate(String)](d2f31f61-32fe-3285-4df1-23395a4e06aa.htm) | 对测量值进行evaluate，结果将在界面和report体现 |
| 公共方法 | [Evaluate(DictionaryString, UInt64, NumberBase)](53edc006-983f-dd1c-d8a9-6b5118c8c27d.htm) | 对测量值进行evaluate，结果将在界面和report体现 |
| 公共方法 | [Evaluate(UInt64, NumberBase)](dff9b706-e4f4-1ff7-a035-2ac171d2cd64.htm) | 对测量值进行evaluate，结果将在界面和report体现 |
| 公共方法 | [GetSubEvaluater](f1630a40-074e-1c9e-0569-87aa935045d6.htm) | 获取当前Evaluation子级Evaluation |
| 公共方法 | [Publish(DictionaryString, Double)](4e63421f-5150-21a6-4b56-3c77af3e4ebd.htm) | 对测量值进行Publish，结果将在界面和report体现，不影响分Bin |
| 公共方法 | [Publish(DictionaryString, String)](cc2c45fd-8fc4-9bd9-6e8a-5cdcfdbfccec.htm) | 对测量值进行Publish，结果将在界面和report体现，不影响分Bin |
| 公共方法 | [Publish(Double)](b7b3e8a7-63d7-1057-d1d6-157206b48f5c.htm) | 对测量值进行Publish，结果将在界面和report体现，不影响分Bin |
| 公共方法 | [Publish(String)](17de001b-53ec-214d-fbf8-9b838887759b.htm) | 对测量值进行Publish，结果将在界面和report体现，不影响分Bin |
| 公共方法 | [Publish(DictionaryString, UInt64, NumberBase)](b0133fc9-4d97-7f00-5ae2-b37594de210b.htm) | 对测量值进行evaluate，结果将在界面和report体现，不影响分Bin |
| 公共方法 | [Publish(UInt64, NumberBase)](49cb84db-4d61-09c2-dad2-5b204777bac5.htm) | 对测量值进行Publish，结果将在界面和report体现，不影响分Bin |
| 公共方法 | [SetHighLimit](5aaf1e84-86eb-2675-bc98-7dbb2337c78e.htm) | 设置当前Evaluation的HighLimit值 设置父节点，子节点自动生效，设置子节点则只影响自身 |
| 公共方法 | [SetLowLimit](0433fc4b-736a-f8ed-50ff-1a0657d07d23.htm) | 设置当前Evaluation的LowLimit值 设置父节点，子节点自动生效，设置子节点则只影响自身 |

[Top](#PageHeader)

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Concat 方法

|  |  |
| --- | --- |
|  | ParametricTestDescriptorConcat 方法 |

修改或新增Evaluation设置

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Concat(
	uint testNumber,
	string testName,
	string testText,
	int softBin = 2147483647,
	double lowLimit = NaN,
	double highLimit = NaN,
	ScalingFactor scalingFactor = ScalingFactor.NaN,
	string unit = null,
	string outputVariable = ""
)
```

###### 参数

testNumber  UInt32
:   要设置的Test Number

testName  String
:   要设置的Test Name

testText  String
:   要设置的Test Text

softBin  Int32  (Optional)
:   要设置的SoftBin Number，可选参数

lowLimit  Double  (Optional)
:   要设置的LowLimit，可选参数

highLimit  Double  (Optional)
:   要设置的HighLimit，可选参数

scalingFactor  [ScalingFactor](d86ddfe9-c36a-ccd6-5f24-8403d81b3783.htm)  (Optional)
:   要设置的Scaling Factor，可选参数

unit  String  (Optional)
:   要设置的Unit，可选参数

outputVariable  String  (Optional)
:   要设置的Output Variable，可选参数

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Evaluate 方法

|  |  |
| --- | --- |
|  | ParametricTestDescriptorEvaluate 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Evaluate(DictionaryString, Double)](bf2604ce-352a-64fa-e227-67fda5062207.htm) | 对测量值进行evaluate，结果将在界面和report体现 |
| 公共方法 | [Evaluate(DictionaryString, String)](9861eb65-cb6b-8523-151c-13f1fb8732f9.htm) | 对测量值进行evaluate，结果将在界面和report体现 |
| 公共方法 | [Evaluate(Double)](2cce93a1-5e01-59a2-b7d6-5b685ea904b6.htm) | 对测量值进行evaluate，结果将在界面和report体现 |
| 公共方法 | [Evaluate(String)](d2f31f61-32fe-3285-4df1-23395a4e06aa.htm) | 对测量值进行evaluate，结果将在界面和report体现 |
| 公共方法 | [Evaluate(DictionaryString, UInt64, NumberBase)](53edc006-983f-dd1c-d8a9-6b5118c8c27d.htm) | 对测量值进行evaluate，结果将在界面和report体现 |
| 公共方法 | [Evaluate(UInt64, NumberBase)](dff9b706-e4f4-1ff7-a035-2ac171d2cd64.htm) | 对测量值进行evaluate，结果将在界面和report体现 |

[Top](#PageHeader)

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Evaluate(Dictionary&lt;String, Double&gt;) 方法

|  |  |
| --- | --- |
|  | ParametricTestDescriptorEvaluate(DictionaryString, Double) 方法 |

对测量值进行evaluate，结果将在界面和report体现

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
Dictionary<string, bool> Evaluate(
	Dictionary<string, double> namedResults
)
```

###### 参数

namedResults  DictionaryString, Double
:   测量值,一般情况下此数值由meastation测量方法返回

###### 返回值

DictionaryString, Boolean

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Evaluate 重载](b715078f-1e10-7b13-0c30-c56d9cc4481f.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Evaluate(Dictionary&lt;String, String&gt;) 方法

|  |  |
| --- | --- |
|  | ParametricTestDescriptorEvaluate(DictionaryString, String) 方法 |

对测量值进行evaluate，结果将在界面和report体现

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
Dictionary<string, bool> Evaluate(
	Dictionary<string, string> namedResults
)
```

###### 参数

namedResults  DictionaryString, String
:   测量值,一般情况下此数值由meastation测量方法返回

###### 返回值

DictionaryString, Boolean  
Evaluation的结果

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Evaluate 重载](b715078f-1e10-7b13-0c30-c56d9cc4481f.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Evaluate(Double) 方法

|  |  |
| --- | --- |
|  | ParametricTestDescriptorEvaluate(Double) 方法 |

对测量值进行evaluate，结果将在界面和report体现

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool Evaluate(
	double result
)
```

###### 参数

result  Double
:   测量值,一般情况下此数值由meastation测量方法返回

###### 返回值

Boolean  
Evaluation的结果

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Evaluate 重载](b715078f-1e10-7b13-0c30-c56d9cc4481f.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Evaluate(String) 方法

|  |  |
| --- | --- |
|  | ParametricTestDescriptorEvaluate(String) 方法 |

对测量值进行evaluate，结果将在界面和report体现

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool Evaluate(
	string result
)
```

###### 参数

result  String
:   测量值,一般情况下此数值由meastation测量方法返回

###### 返回值

Boolean  
Evaluation的结果

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Evaluate 重载](b715078f-1e10-7b13-0c30-c56d9cc4481f.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Evaluate(Dictionary&lt;String, UInt64&gt;, NumberBase) 方法

|  |  |
| --- | --- |
|  | ParametricTestDescriptorEvaluate(DictionaryString, UInt64, NumberBase) 方法 |

对测量值进行evaluate，结果将在界面和report体现

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
Dictionary<string, bool> Evaluate(
	Dictionary<string, ulong> namedResults,
	NumberBase numBase = NumberBase.Decimal
)
```

###### 参数

namedResults  DictionaryString, UInt64
:   测量值,一般情况下此数值由meastation测量方法返回

numBase  [NumberBase](050f54bd-af30-c1e9-4a9e-123e9fa0664d.htm)  (Optional)
:   输出数字进制，默认十进制

###### 返回值

DictionaryString, Boolean  
Evaluation的结果

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Evaluate 重载](b715078f-1e10-7b13-0c30-c56d9cc4481f.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Evaluate(UInt64, NumberBase) 方法

|  |  |
| --- | --- |
|  | ParametricTestDescriptorEvaluate(UInt64, NumberBase) 方法 |

对测量值进行evaluate，结果将在界面和report体现

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool Evaluate(
	ulong result,
	NumberBase numBase = NumberBase.Decimal
)
```

###### 参数

result  UInt64
:   测量值,一般情况下此数值由meastation测量方法返回

numBase  [NumberBase](050f54bd-af30-c1e9-4a9e-123e9fa0664d.htm)  (Optional)
:   输出数字进制，默认十进制

###### 返回值

Boolean  
Evaluation的结果

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Evaluate 重载](b715078f-1e10-7b13-0c30-c56d9cc4481f.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetSubEvaluater 方法

|  |  |
| --- | --- |
|  | ParametricTestDescriptorGetSubEvaluater 方法 |

获取当前Evaluation子级Evaluation

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
ParametricTestDescriptor GetSubEvaluater(
	string subName
)
```

###### 参数

subName  String
:   子级Evaluation的Name，横杠后面的部分

###### 返回值

[ParametricTestDescriptor](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)  
子级Evaluater

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Publish 方法

|  |  |
| --- | --- |
|  | ParametricTestDescriptorPublish 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Publish(DictionaryString, Double)](4e63421f-5150-21a6-4b56-3c77af3e4ebd.htm) | 对测量值进行Publish，结果将在界面和report体现，不影响分Bin |
| 公共方法 | [Publish(DictionaryString, String)](cc2c45fd-8fc4-9bd9-6e8a-5cdcfdbfccec.htm) | 对测量值进行Publish，结果将在界面和report体现，不影响分Bin |
| 公共方法 | [Publish(Double)](b7b3e8a7-63d7-1057-d1d6-157206b48f5c.htm) | 对测量值进行Publish，结果将在界面和report体现，不影响分Bin |
| 公共方法 | [Publish(String)](17de001b-53ec-214d-fbf8-9b838887759b.htm) | 对测量值进行Publish，结果将在界面和report体现，不影响分Bin |
| 公共方法 | [Publish(DictionaryString, UInt64, NumberBase)](b0133fc9-4d97-7f00-5ae2-b37594de210b.htm) | 对测量值进行evaluate，结果将在界面和report体现，不影响分Bin |
| 公共方法 | [Publish(UInt64, NumberBase)](49cb84db-4d61-09c2-dad2-5b204777bac5.htm) | 对测量值进行Publish，结果将在界面和report体现，不影响分Bin |

[Top](#PageHeader)

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Publish(Dictionary&lt;String, Double&gt;) 方法

|  |  |
| --- | --- |
|  | ParametricTestDescriptorPublish(DictionaryString, Double) 方法 |

对测量值进行Publish，结果将在界面和report体现，不影响分Bin

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Publish(
	Dictionary<string, double> namedResults
)
```

###### 参数

namedResults  DictionaryString, Double
:   测量值,一般情况下此数值由meastation测量方法返回

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Publish 重载](2121759c-80f4-6e7c-e978-77fec894573c.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Publish(Dictionary&lt;String, String&gt;) 方法

|  |  |
| --- | --- |
|  | ParametricTestDescriptorPublish(DictionaryString, String) 方法 |

对测量值进行Publish，结果将在界面和report体现，不影响分Bin

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Publish(
	Dictionary<string, string> namedResults
)
```

###### 参数

namedResults  DictionaryString, String
:   测量值,一般情况下此数值由meastation测量方法返回

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Publish 重载](2121759c-80f4-6e7c-e978-77fec894573c.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Publish(Double) 方法

|  |  |
| --- | --- |
|  | ParametricTestDescriptorPublish(Double) 方法 |

对测量值进行Publish，结果将在界面和report体现，不影响分Bin

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Publish(
	double result
)
```

###### 参数

result  Double
:   测量值,一般情况下此数值由meastation测量方法返回

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Publish 重载](2121759c-80f4-6e7c-e978-77fec894573c.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Publish(String) 方法

|  |  |
| --- | --- |
|  | ParametricTestDescriptorPublish(String) 方法 |

对测量值进行Publish，结果将在界面和report体现，不影响分Bin

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Publish(
	string result
)
```

###### 参数

result  String
:   测量值,一般情况下此数值由meastation测量方法返回

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Publish 重载](2121759c-80f4-6e7c-e978-77fec894573c.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Publish(Dictionary&lt;String, UInt64&gt;, NumberBase) 方法

|  |  |
| --- | --- |
|  | ParametricTestDescriptorPublish(DictionaryString, UInt64, NumberBase) 方法 |

对测量值进行evaluate，结果将在界面和report体现，不影响分Bin

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Publish(
	Dictionary<string, ulong> namedResults,
	NumberBase numBase = NumberBase.Decimal
)
```

###### 参数

namedResults  DictionaryString, UInt64
:   测量值,一般情况下此数值由meastation测量方法返回

numBase  [NumberBase](050f54bd-af30-c1e9-4a9e-123e9fa0664d.htm)  (Optional)
:   输出数字进制，默认十进制

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Publish 重载](2121759c-80f4-6e7c-e978-77fec894573c.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Publish(UInt64, NumberBase) 方法

|  |  |
| --- | --- |
|  | ParametricTestDescriptorPublish(UInt64, NumberBase) 方法 |

对测量值进行Publish，结果将在界面和report体现，不影响分Bin

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Publish(
	ulong result,
	NumberBase numBase = NumberBase.Decimal
)
```

###### 参数

result  UInt64
:   测量值,一般情况下此数值由meastation测量方法返回

numBase  [NumberBase](050f54bd-af30-c1e9-4a9e-123e9fa0664d.htm)  (Optional)
:   输出数字进制，默认十进制

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Publish 重载](2121759c-80f4-6e7c-e978-77fec894573c.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### SetHighLimit 方法

|  |  |
| --- | --- |
|  | ParametricTestDescriptorSetHighLimit 方法 |

设置当前Evaluation的HighLimit值
设置父节点，子节点自动生效，设置子节点则只影响自身

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetHighLimit(
	double highLimit
)
```

###### 参数

highLimit  Double
:   要设置的值

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### SetLowLimit 方法

|  |  |
| --- | --- |
|  | ParametricTestDescriptorSetLowLimit 方法 |

设置当前Evaluation的LowLimit值
设置父节点，子节点自动生效，设置子节点则只影响自身

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetLowLimit(
	double lowLimit
)
```

###### 参数

lowLimit  Double
:   要设置的值

参见

###### 引用

[ParametricTestDescriptor 接口](3889512c-1f25-5aea-bfc4-901b516e0e52.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## PartVariables 类

|  |  |
| --- | --- |
|  | PartVariables 类 |

继承层次

SystemObject
  
  Guwave.OneTest.TestMethodPartVariables

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public class PartVariables
```

PartVariables 类型公开以下成员。

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [BatchNo](3d1b7206-41c5-dd7c-6735-da397b4ab011.htm) | 获取本次启动任务以来执行批次的编号 |
| 公共属性 | [BinResult](60054fa2-ca9d-5985-1c18-cad000e88351.htm) | **已过时。**  获取执行到当前为止的测试结果包含：Site,Status,SoftBin,HardBin |
| 公共属性 | [DeviceNo](2a209e9d-bd95-3aa9-76e8-842bca6ca227.htm) | 获取本次启动任务以来当前Device从1开始的编号 |
| 公共属性 | [PartID](48817e9e-34a3-e949-d1c4-c81b79e1b324.htm) | Part级别的变量：PartID |
| 公共属性 | [XCoord](dae51e34-d921-2da1-1697-e235e3cdeb64.htm) | Device在Wafer上的横坐标 |
| 公共属性 | [YCoord](9dda36d8-cf03-d671-8db0-ff8f1b06bec5.htm) | Device在Wafer上的纵坐标 |

[Top](#PageHeader)

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | [GetVariable](48478c2a-c55a-dcf2-3ad0-5a4a79c403ac.htm) |  |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [SetVariable](2e0dcdd1-eb32-38c2-b5ee-00244296c0df.htm) |  |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |

[Top](#PageHeader)

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### PartVariables 属性

|  |  |
| --- | --- |
|  | PartVariables 属性 |

[PartVariables](c281af04-b2cd-2012-8377-2634a3da8931.htm) 类型公开以下成员。

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [BatchNo](3d1b7206-41c5-dd7c-6735-da397b4ab011.htm) | 获取本次启动任务以来执行批次的编号 |
| 公共属性 | [BinResult](60054fa2-ca9d-5985-1c18-cad000e88351.htm) | **已过时。**   获取执行到当前为止的测试结果包含：Site,Status,SoftBin,HardBin |
| 公共属性 | [DeviceNo](2a209e9d-bd95-3aa9-76e8-842bca6ca227.htm) | 获取本次启动任务以来当前Device从1开始的编号 |
| 公共属性 | [PartID](48817e9e-34a3-e949-d1c4-c81b79e1b324.htm) | Part级别的变量：PartID |
| 公共属性 | [XCoord](dae51e34-d921-2da1-1697-e235e3cdeb64.htm) | Device在Wafer上的横坐标 |
| 公共属性 | [YCoord](9dda36d8-cf03-d671-8db0-ff8f1b06bec5.htm) | Device在Wafer上的纵坐标 |

[Top](#PageHeader)

参见

###### 引用

[PartVariables 类](c281af04-b2cd-2012-8377-2634a3da8931.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### BatchNo 属性

|  |  |
| --- | --- |
|  | PartVariablesBatchNo 属性 |

获取本次启动任务以来执行批次的编号

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public int BatchNo { get; }
```

###### 属性值

Int32

参见

###### 引用

[PartVariables 类](c281af04-b2cd-2012-8377-2634a3da8931.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### BinResult 属性

|  |  |
| --- | --- |
|  | PartVariablesBinResult 属性 |

**注意：此 API 现在已过时。**

获取执行到当前为止的测试结果包含：Site,Status,SoftBin,HardBin

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
[ObsoleteAttribute("该API已过时，将在未来版本中移除，请使用Semicontext.DeviceAccessor.GetCurrentBinResult代替。")]
public TestBinResult BinResult { get; }
```

###### 属性值

[TestBinResult](c05768d0-3a5a-71cc-9d5f-0d0f16602f5f.htm)

参见

###### 引用

[PartVariables 类](c281af04-b2cd-2012-8377-2634a3da8931.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### DeviceNo 属性

|  |  |
| --- | --- |
|  | PartVariablesDeviceNo 属性 |

获取本次启动任务以来当前Device从1开始的编号

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public int DeviceNo { get; }
```

###### 属性值

Int32

参见

###### 引用

[PartVariables 类](c281af04-b2cd-2012-8377-2634a3da8931.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### PartID 属性

|  |  |
| --- | --- |
|  | PartVariablesPartID 属性 |

Part级别的变量：PartID

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string PartID { get; set; }
```

###### 属性值

String

参见

###### 引用

[PartVariables 类](c281af04-b2cd-2012-8377-2634a3da8931.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### XCoord 属性

|  |  |
| --- | --- |
|  | PartVariablesXCoord 属性 |

Device在Wafer上的横坐标

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public short XCoord { get; set; }
```

###### 属性值

Int16

参见

###### 引用

[PartVariables 类](c281af04-b2cd-2012-8377-2634a3da8931.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### YCoord 属性

|  |  |
| --- | --- |
|  | PartVariablesYCoord 属性 |

Device在Wafer上的纵坐标

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public short YCoord { get; set; }
```

###### 属性值

Int16

参见

###### 引用

[PartVariables 类](c281af04-b2cd-2012-8377-2634a3da8931.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### PartVariables 方法

|  |  |
| --- | --- |
|  | PartVariables 方法 |

[PartVariables](c281af04-b2cd-2012-8377-2634a3da8931.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | [GetVariable](48478c2a-c55a-dcf2-3ad0-5a4a79c403ac.htm) |  |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [SetVariable](2e0dcdd1-eb32-38c2-b5ee-00244296c0df.htm) |  |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |

[Top](#PageHeader)

参见

###### 引用

[PartVariables 类](c281af04-b2cd-2012-8377-2634a3da8931.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetVariable 方法

|  |  |
| --- | --- |
|  | PartVariablesGetVariable 方法 |

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string GetVariable(
	string varName
)
```

###### 参数

varName  String

###### 返回值

String

参见

###### 引用

[PartVariables 类](c281af04-b2cd-2012-8377-2634a3da8931.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### SetVariable 方法

|  |  |
| --- | --- |
|  | PartVariablesSetVariable 方法 |

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public void SetVariable(
	string varName,
	string varValue
)
```

###### 参数

varName  String

varValue  String

参见

###### 引用

[PartVariables 类](c281af04-b2cd-2012-8377-2634a3da8931.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## PinType 枚举

|  |  |
| --- | --- |
|  | PinType 枚举 |

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public enum PinType
```

成员

| 成员名称 | 值 | 说明 |
| --- | --- | --- |
| DutPin | 0 |  |
| SystemPin | 1 |  |
| All | 2 |  |

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## ProgramVariables 类

|  |  |
| --- | --- |
|  | ProgramVariables 类 |

继承层次

SystemObject
  
  Guwave.OneTest.TestMethodProgramVariables

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public class ProgramVariables
```

ProgramVariables 类型公开以下成员。

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [\_variableChangedAction](eb9216a0-bf07-63a6-aeb5-de35177d7cb5.htm) |  |
| 公共属性 | [DeviceName](67a486c5-3c50-300a-a86a-80855d81cce6.htm) | 获取Test ProgramName级别的变量：DeviceName |
| 公共属性 | [LotID](639c70f3-2c9d-d1dd-3549-64f35efcbdc8.htm) | 获取Test ProgramName级别的变量：LotID |
| 公共属性 | [OperatorName](0c8f095c-3756-74e3-1b52-a86d83644e78.htm) | 获取Test ProgramName级别的变量：OperatorName |
| 公共属性 | [Process](8d06787e-0f7a-693e-7e45-1b6edf4c995b.htm) | 获取Test ProgramName级别的变量：Process |
| 公共属性 | [Temperature](e6a73896-875e-9cd4-2450-976e55f97b5a.htm) | 获取Test ProgramName级别的变量：Temperature |
| 公共属性 | [TestCode](54e9963b-6a10-ee62-4cc6-dd82c3d550b5.htm) | 获取Test ProgramName级别的变量：TestCode |
| 公共属性 | [TestProgramName](a8c7da40-51d4-9b0c-369b-7789dd400464.htm) | 获取Test ProgramName级别的变量：TestProgramName |

[Top](#PageHeader)

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | [GetVariable](b706f9ad-b174-9f13-cf02-8983323e1162.htm) | 获取TestProgram级别的变量 |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [SetVariable](400ad44d-dc87-3eeb-fdfb-4f60a934e318.htm) | 设置TestProgram级别的变量，不存在时自动新增 |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |

[Top](#PageHeader)

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### ProgramVariables 属性

|  |  |
| --- | --- |
|  | ProgramVariables 属性 |

[ProgramVariables](44493283-e635-f7bf-6080-ef8f86b3f1a2.htm) 类型公开以下成员。

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [\_variableChangedAction](eb9216a0-bf07-63a6-aeb5-de35177d7cb5.htm) |  |
| 公共属性 | [DeviceName](67a486c5-3c50-300a-a86a-80855d81cce6.htm) | 获取Test ProgramName级别的变量：DeviceName |
| 公共属性 | [LotID](639c70f3-2c9d-d1dd-3549-64f35efcbdc8.htm) | 获取Test ProgramName级别的变量：LotID |
| 公共属性 | [OperatorName](0c8f095c-3756-74e3-1b52-a86d83644e78.htm) | 获取Test ProgramName级别的变量：OperatorName |
| 公共属性 | [Process](8d06787e-0f7a-693e-7e45-1b6edf4c995b.htm) | 获取Test ProgramName级别的变量：Process |
| 公共属性 | [Temperature](e6a73896-875e-9cd4-2450-976e55f97b5a.htm) | 获取Test ProgramName级别的变量：Temperature |
| 公共属性 | [TestCode](54e9963b-6a10-ee62-4cc6-dd82c3d550b5.htm) | 获取Test ProgramName级别的变量：TestCode |
| 公共属性 | [TestProgramName](a8c7da40-51d4-9b0c-369b-7789dd400464.htm) | 获取Test ProgramName级别的变量：TestProgramName |

[Top](#PageHeader)

参见

###### 引用

[ProgramVariables 类](44493283-e635-f7bf-6080-ef8f86b3f1a2.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### _variableChangedAction 属性

|  |  |
| --- | --- |
|  | ProgramVariables\_variableChangedAction 属性 |

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Action<VariableChangeEvent> _variableChangedAction { get; set; }
```

###### 属性值

ActionVariableChangeEvent

参见

###### 引用

[ProgramVariables 类](44493283-e635-f7bf-6080-ef8f86b3f1a2.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### DeviceName 属性

|  |  |
| --- | --- |
|  | ProgramVariablesDeviceName 属性 |

获取Test ProgramName级别的变量：DeviceName

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string DeviceName { get; set; }
```

###### 属性值

String

参见

###### 引用

[ProgramVariables 类](44493283-e635-f7bf-6080-ef8f86b3f1a2.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### LotID 属性

|  |  |
| --- | --- |
|  | ProgramVariablesLotID 属性 |

获取Test ProgramName级别的变量：LotID

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string LotID { get; set; }
```

###### 属性值

String

参见

###### 引用

[ProgramVariables 类](44493283-e635-f7bf-6080-ef8f86b3f1a2.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### OperatorName 属性

|  |  |
| --- | --- |
|  | ProgramVariablesOperatorName 属性 |

获取Test ProgramName级别的变量：OperatorName

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string OperatorName { get; set; }
```

###### 属性值

String

参见

###### 引用

[ProgramVariables 类](44493283-e635-f7bf-6080-ef8f86b3f1a2.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Process 属性

|  |  |
| --- | --- |
|  | ProgramVariablesProcess 属性 |

获取Test ProgramName级别的变量：Process

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string Process { get; set; }
```

###### 属性值

String

参见

###### 引用

[ProgramVariables 类](44493283-e635-f7bf-6080-ef8f86b3f1a2.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Temperature 属性

|  |  |
| --- | --- |
|  | ProgramVariablesTemperature 属性 |

获取Test ProgramName级别的变量：Temperature

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string Temperature { get; set; }
```

###### 属性值

String

参见

###### 引用

[ProgramVariables 类](44493283-e635-f7bf-6080-ef8f86b3f1a2.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### TestCode 属性

|  |  |
| --- | --- |
|  | ProgramVariablesTestCode 属性 |

获取Test ProgramName级别的变量：TestCode

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string TestCode { get; set; }
```

###### 属性值

String

参见

###### 引用

[ProgramVariables 类](44493283-e635-f7bf-6080-ef8f86b3f1a2.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### TestProgramName 属性

|  |  |
| --- | --- |
|  | ProgramVariablesTestProgramName 属性 |

获取Test ProgramName级别的变量：TestProgramName

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string TestProgramName { get; set; }
```

###### 属性值

String

参见

###### 引用

[ProgramVariables 类](44493283-e635-f7bf-6080-ef8f86b3f1a2.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### ProgramVariables 方法

|  |  |
| --- | --- |
|  | ProgramVariables 方法 |

[ProgramVariables](44493283-e635-f7bf-6080-ef8f86b3f1a2.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | [GetVariable](b706f9ad-b174-9f13-cf02-8983323e1162.htm) | 获取TestProgram级别的变量 |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [SetVariable](400ad44d-dc87-3eeb-fdfb-4f60a934e318.htm) | 设置TestProgram级别的变量，不存在时自动新增 |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |

[Top](#PageHeader)

参见

###### 引用

[ProgramVariables 类](44493283-e635-f7bf-6080-ef8f86b3f1a2.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetVariable 方法

|  |  |
| --- | --- |
|  | ProgramVariablesGetVariable 方法 |

获取TestProgram级别的变量

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string GetVariable(
	string varName
)
```

###### 参数

varName  String

###### 返回值

String

参见

###### 引用

[ProgramVariables 类](44493283-e635-f7bf-6080-ef8f86b3f1a2.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### SetVariable 方法

|  |  |
| --- | --- |
|  | ProgramVariablesSetVariable 方法 |

设置TestProgram级别的变量，不存在时自动新增

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public void SetVariable(
	string varName,
	string varValue
)
```

###### 参数

varName  String

varValue  String

参见

###### 引用

[ProgramVariables 类](44493283-e635-f7bf-6080-ef8f86b3f1a2.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## ScalingFactor 枚举

|  |  |
| --- | --- |
|  | ScalingFactor 枚举 |

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public enum ScalingFactor
```

成员

| 成员名称 | 值 | 说明 |
| --- | --- | --- |
| FEMTO | 0 |  |
| PICO | 1 |  |
| NANO | 2 |  |
| MICRO | 3 |  |
| MILLI | 4 |  |
| PERCENT | 5 |  |
| EMPTY | 6 |  |
| KILO | 7 |  |
| MEGA | 8 |  |
| GIGA | 9 |  |
| TERA | 10 |  |
| NaN | 11 |  |

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## SemiContext 类

|  |  |
| --- | --- |
|  | SemiContext 类 |

仪表操作接口上下文

继承层次

SystemObject
  
  Guwave.OneTest.TestMethodSemiContext

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public class SemiContext
```

SemiContext 类型公开以下成员。

构造函数

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [SemiContext](5cf37b0b-1e12-cac4-ef8e-4d920ecb9e8a.htm) | SemiContext只能在系统内部初始化，TM中不可以创建新实例 |

[Top](#PageHeader)

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [CurrentSite](7b971fc1-a862-2275-35ca-cb2fe451975f.htm) | 当前线程所处理的Site编号 |
| 公共属性 | [DeviceAccessor](1041d5f1-d337-7b77-16fb-b534b11412df.htm) | 当前Site分Bin指定操作接口,直接修改当前Site ExecutionHolder的bin结果, 与Evaluate方法同优先级 |
| 公共属性 | [ErrorFlag](59ed677d-334d-a3dd-ecad-715100599238.htm) | 用于记录当前Site执行过程中的错误信息(当然也可以是别的信息)，实现信息在Flow内跨TestMethod传递 |
| 公共属性 | [ExecuteMode](b2950f55-8ea8-9e27-bbc2-4a94d167c093.htm) | 是否是Debug模式，Debug模式会打印TimeMetric信息，同时会输出Plot等图表 |
| 公共属性 | [FileAccessor](9ad750ef-a4b9-0c96-5437-4cffa3924b42.htm) | 文件访问接口,与TestMethod内的FileAccessor是同一个实例，可使用任意一个 |
| 公共属性 | [InstrumentAccessor](5ce8d206-090e-926d-7b86-3c8f01d3f5dd.htm) | 仪器仪表操作接口,与TestMethod内的InstrumentAccessor是同一个实例，可使用任意一个 |
| 公共属性 | [Part](049d96e7-fc73-c414-8aff-fb6b05fcbe17.htm) | Part级别的变量获取和设置接口 |
| 公共属性 | [PinmapAccessor](3ca49381-1cdd-ea9e-f123-8167f8df4c8b.htm) | Pin/PinGroup和连接配置访问接口,与TestMethod内的PinmapAccessor是同一个实例，可使用任意一个 |
| 公共属性 | [ProjectClientPath](89b2c02c-6b3a-bba3-ddaf-de681956ad40.htm) | 项目在IDE环境上的物理路径 |
| 公共属性 | [ProjectRemotePath](3675913d-722b-66c8-781a-16c9c29e9309.htm) | 项目在Engine上的缓存目录 此路径的父级目录可以在Engine安装目录下config/engineConfig.xml修改 |
| 公共属性 | [RegisterAccessor](0ec3ef7a-d32d-a8f7-2e82-c93c7d8e780c.htm) | 寄存器访问接口,与TestMethod内的RegisterAccessor是同一个实例，可使用任意一个 |
| 公共属性 | [SwitchAccessor](907b669b-4b37-4b32-019e-f2da6d9d1122.htm) | Switch访问接口,与TestMethod内的SwitchAccessor是同一个实例，可使用任意一个 |
| 公共属性 | [TestProgram](6ec0c2a5-0d74-70fc-fc74-862329c566c9.htm) | TestProgram级别的变量获取和设置接口 |
| 公共属性 | [VariableAccessor](a6f160a7-11ee-dbb7-f066-fb4ba510add0.htm) | 变量访问接口,与TestMethod内的VariableAccessor是同一个实例，可使用任意一个 |

[Top](#PageHeader)

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [AP](32f574c9-3c93-eac5-1d93-bfb95b1700b6.htm) | 根据输入的 Pin获取 AP 类仪器的操作对象 |
| 公共方法 | [BERT](bc7082fd-6a90-22a1-4ee8-eb6aec3dd8a7.htm) | 根据输入的 Pin获取 BERT 类仪器的操作对象 |
| 公共方法 | [Converter](82f53ff6-ef4a-051d-553d-2d31a6f450ff.htm) | 根据输入的 Pin获取 Converter 类仪器的操作对象 |
| 公共方法 | [Counter](bab6fcba-44a0-6321-c183-4ae728bb5f2c.htm) | 根据输入的 Pin获取 Counter 类仪器的操作对象 |
| 公共方法 | [DAQ](599943ce-888d-0201-3d9c-11844012da09.htm) | 根据输入的 Pin获取 DAQ 类仪器的操作对象 |
| 公共方法 | [DCA](cfc2e029-b29c-df22-0f74-ad1cc16d2f2f.htm) | 根据输入的 Pin获取 DCA 类仪器的操作对象 |
| 公共方法 | [DCVI](f899aec9-d7c7-119e-55f7-ee0316dda49f.htm) | 根据输入的 Pin获取 DCVI 类仪器的操作对象 |
| 公共方法 | [Digital](bd55b73e-0d85-cb1c-b998-b15871ac1cd5.htm) | 根据输入的 Pin获取 Digital 类仪器的操作对象 |
| 公共方法 | [Dmm](bc52222b-4501-765f-5a90-8ed393124914.htm) | 根据输入的 Pin获取 Dmm 类仪器的操作对象 |
| 公共方法 | [Eload](e105e2b9-fdb7-6076-3ca9-67f245c20948.htm) | 根据输入的 Pin获取 Eload 类仪器的操作对象 |
| 公共方法 | [ENA](29d51a0c-18ca-599f-8b35-869652672e98.htm) | 根据输入的 Pin获取 ENA 类仪器的操作对象 |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 公共方法 | [Fgen](7828868f-c1fd-2c25-acd5-4d25cd4faf5c.htm) | 根据输入的 Pin获取 Fgen 类仪器的操作对象 |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | [GetMeasureStationT](b318e874-2e27-85c2-f61b-557f3e096c07.htm) | 根据输入的 Pin获取自定义仪器的操作对象 |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | [HID](67d7631a-ab84-6efb-3f3d-f9d337843f4f.htm) | 根据输入的 Pin获取 HID 类仪器的操作对象 |
| 公共方法 | [LCRMeter](a564026c-7188-da9a-1106-162971114075.htm) | 根据输入的 Pin获取 LCRMeter 类仪器的操作对象 |
| 公共方法 | [Log(Object)](7ca538c6-ee2d-8d37-b768-35f471a1a389.htm) | 向Output.Engine输出通道中打印日志 |
| 公共方法 | [Log(LogLevel, Object)](87b28270-9ea2-791e-42f8-6f8c99a1b28b.htm) | 向Output.Engine输出通道中打印日志 |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [PipeInvoke](5b7738b0-b2e8-134f-b3af-a054d327a21c.htm) | 根据输入的 Pin获取 PipeInvoke 类仪器的操作对象 |
| 公共方法 | [PNA](cea7d544-3980-9f69-589c-7747c9b5114a.htm) | 根据输入的 Pin获取 PNA 类仪器的操作对象 |
| 公共方法 | [Power](f8c587da-4e8b-4be8-09ad-d1f3327287c0.htm) | 根据输入的 Pin获取 Power 类仪器的操作对象 |
| 公共方法 | [PowerMeter](5c5da2d3-6f6c-becd-998c-3a095bd24f19.htm) | 根据输入的 Pin获取 PowerMeter 类仪器的操作对象 |
| 公共方法 | [RFSA](3db77564-dd6f-2884-7616-254222b769fb.htm) | 根据输入的 Pin获取 RFSA 类仪器的操作对象 |
| 公共方法 | [RFSG](d11697fd-52f6-8e21-a583-e6620b32ddc8.htm) | 根据输入的 Pin获取 RFSG 类仪器的操作对象 |
| 公共方法 | [Scope](5345d5ce-458f-9610-bafc-4afdc2474cff.htm) | 根据输入的 Pin获取 Scope 类仪器的操作对象 |
| 公共方法 | [Serial](3b5b0e77-2cf6-2d3c-bfa5-b0e30ef47320.htm) | 根据输入的 Pin获取 Serial 类仪器的操作对象 |
| 公共方法 | [SerialChamber](c4c77f7f-3ddd-4f83-da9d-2e999559a369.htm) | 根据输入的 Pin获取 SerialChamber 类仪器的操作对象 |
| 公共方法 | [SpDigital](074ab21f-13eb-14eb-9d20-fc64cec58531.htm) | 根据输入的 Pin获取 SpDigital 类仪器的操作对象 |
| 公共方法 | [SpecAn](3f6f133b-7114-8d11-6402-e06d8c53c5af.htm) | 根据输入的 Pin获取 SpecAn 类仪器的操作对象 |
| 公共方法 | [Switch](b7c4cdbe-db68-5abb-cb91-0dd876cd4a7a.htm) | 根据输入的 Pin获取 Switch 类仪器的操作对象 |
| 公共方法 | [Sync](8a11daf5-ad27-45de-0bc2-ad94933131ae.htm) | 根据输入的 Pin获取 Sync 类仪器的操作对象 |
| 公共方法 | [Thermal](a5be2f9e-b105-7dbd-f5d0-15d633b2ff39.htm) | 根据输入的 Pin获取 Thermal 类仪器的操作对象 |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |
| 公共方法 | [Visa](b3d1aea3-b67a-9451-5c89-69b1a7c96484.htm) | 根据输入的 Pin获取 Visa 类仪器的操作对象 |

[Top](#PageHeader)

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### SemiContext 构造函数

|  |  |
| --- | --- |
|  | SemiContext 构造函数 |

SemiContext只能在系统内部初始化，TM中不可以创建新实例

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public SemiContext(
	int siteId,
	RunMode runMode,
	string clientPath,
	string remotePath,
	IRegisterAccessor regAccessor,
	IVariableAccessor varAccessor,
	ISwitchAccessor switchAccessor,
	IPinmapAccessor pinAccessor,
	IFileAccessor fileAccessor,
	IInstrumentAccessor instAccessor,
	IDeviceAccessor deviceAccessor
)
```

###### 参数

siteId  Int32

runMode  RunMode

clientPath  String

remotePath  String

regAccessor  [IRegisterAccessor](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

varAccessor  [IVariableAccessor](6e6124cd-87b1-6191-bf37-5a6153dcae9c.htm)

switchAccessor  [ISwitchAccessor](f4adcf92-99fb-8004-0cf6-b59040e967eb.htm)

pinAccessor  [IPinmapAccessor](c31b9fa6-009d-3188-6deb-bca1d67c7cc7.htm)

fileAccessor  [IFileAccessor](dc5e402a-56da-a9ac-1101-94bfb5c693dd.htm)

instAccessor  [IInstrumentAccessor](8365c067-d962-ccb8-21df-9617210b236d.htm)

deviceAccessor  [IDeviceAccessor](77da62e2-6cb3-e081-28ce-33c245f4add3.htm)

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### SemiContext 属性

|  |  |
| --- | --- |
|  | SemiContext 属性 |

[SemiContext](421aec95-4c88-392e-653b-28511d2c5421.htm) 类型公开以下成员。

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [CurrentSite](7b971fc1-a862-2275-35ca-cb2fe451975f.htm) | 当前线程所处理的Site编号 |
| 公共属性 | [DeviceAccessor](1041d5f1-d337-7b77-16fb-b534b11412df.htm) | 当前Site分Bin指定操作接口,直接修改当前Site ExecutionHolder的bin结果, 与Evaluate方法同优先级 |
| 公共属性 | [ErrorFlag](59ed677d-334d-a3dd-ecad-715100599238.htm) | 用于记录当前Site执行过程中的错误信息(当然也可以是别的信息)，实现信息在Flow内跨TestMethod传递 |
| 公共属性 | [ExecuteMode](b2950f55-8ea8-9e27-bbc2-4a94d167c093.htm) | 是否是Debug模式，Debug模式会打印TimeMetric信息，同时会输出Plot等图表 |
| 公共属性 | [FileAccessor](9ad750ef-a4b9-0c96-5437-4cffa3924b42.htm) | 文件访问接口,与TestMethod内的FileAccessor是同一个实例，可使用任意一个 |
| 公共属性 | [InstrumentAccessor](5ce8d206-090e-926d-7b86-3c8f01d3f5dd.htm) | 仪器仪表操作接口,与TestMethod内的InstrumentAccessor是同一个实例，可使用任意一个 |
| 公共属性 | [Part](049d96e7-fc73-c414-8aff-fb6b05fcbe17.htm) | Part级别的变量获取和设置接口 |
| 公共属性 | [PinmapAccessor](3ca49381-1cdd-ea9e-f123-8167f8df4c8b.htm) | Pin/PinGroup和连接配置访问接口,与TestMethod内的PinmapAccessor是同一个实例，可使用任意一个 |
| 公共属性 | [ProjectClientPath](89b2c02c-6b3a-bba3-ddaf-de681956ad40.htm) | 项目在IDE环境上的物理路径 |
| 公共属性 | [ProjectRemotePath](3675913d-722b-66c8-781a-16c9c29e9309.htm) | 项目在Engine上的缓存目录 此路径的父级目录可以在Engine安装目录下config/engineConfig.xml修改 |
| 公共属性 | [RegisterAccessor](0ec3ef7a-d32d-a8f7-2e82-c93c7d8e780c.htm) | 寄存器访问接口,与TestMethod内的RegisterAccessor是同一个实例，可使用任意一个 |
| 公共属性 | [SwitchAccessor](907b669b-4b37-4b32-019e-f2da6d9d1122.htm) | Switch访问接口,与TestMethod内的SwitchAccessor是同一个实例，可使用任意一个 |
| 公共属性 | [TestProgram](6ec0c2a5-0d74-70fc-fc74-862329c566c9.htm) | TestProgram级别的变量获取和设置接口 |
| 公共属性 | [VariableAccessor](a6f160a7-11ee-dbb7-f066-fb4ba510add0.htm) | 变量访问接口,与TestMethod内的VariableAccessor是同一个实例，可使用任意一个 |

[Top](#PageHeader)

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### CurrentSite 属性

|  |  |
| --- | --- |
|  | SemiContextCurrentSite 属性 |

当前线程所处理的Site编号

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public int CurrentSite { get; }
```

###### 属性值

Int32

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### DeviceAccessor 属性

|  |  |
| --- | --- |
|  | SemiContextDeviceAccessor 属性 |

当前Site分Bin指定操作接口,直接修改当前Site ExecutionHolder的bin结果, 与Evaluate方法同优先级

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public IDeviceAccessor DeviceAccessor { get; }
```

###### 属性值

[IDeviceAccessor](77da62e2-6cb3-e081-28ce-33c245f4add3.htm)

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### ErrorFlag 属性

|  |  |
| --- | --- |
|  | SemiContextErrorFlag 属性 |

用于记录当前Site执行过程中的错误信息(当然也可以是别的信息)，实现信息在Flow内跨TestMethod传递

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string ErrorFlag { get; set; }
```

###### 属性值

String

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### ExecuteMode 属性

|  |  |
| --- | --- |
|  | SemiContextExecuteMode 属性 |

是否是Debug模式，Debug模式会打印TimeMetric信息，同时会输出Plot等图表

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public RunMode ExecuteMode { get; }
```

###### 属性值

RunMode

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### FileAccessor 属性

|  |  |
| --- | --- |
|  | SemiContextFileAccessor 属性 |

文件访问接口,与TestMethod内的FileAccessor是同一个实例，可使用任意一个

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public IFileAccessor FileAccessor { get; }
```

###### 属性值

[IFileAccessor](dc5e402a-56da-a9ac-1101-94bfb5c693dd.htm)

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### InstrumentAccessor 属性

|  |  |
| --- | --- |
|  | SemiContextInstrumentAccessor 属性 |

仪器仪表操作接口,与TestMethod内的InstrumentAccessor是同一个实例，可使用任意一个

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public IInstrumentAccessor InstrumentAccessor { get; }
```

###### 属性值

[IInstrumentAccessor](8365c067-d962-ccb8-21df-9617210b236d.htm)

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Part 属性

|  |  |
| --- | --- |
|  | SemiContextPart 属性 |

Part级别的变量获取和设置接口

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public PartVariables Part { get; }
```

###### 属性值

[PartVariables](c281af04-b2cd-2012-8377-2634a3da8931.htm)

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### PinmapAccessor 属性

|  |  |
| --- | --- |
|  | SemiContextPinmapAccessor 属性 |

Pin/PinGroup和连接配置访问接口,与TestMethod内的PinmapAccessor是同一个实例，可使用任意一个

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public IPinmapAccessor PinmapAccessor { get; }
```

###### 属性值

[IPinmapAccessor](c31b9fa6-009d-3188-6deb-bca1d67c7cc7.htm)

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### ProjectClientPath 属性

|  |  |
| --- | --- |
|  | SemiContextProjectClientPath 属性 |

项目在IDE环境上的物理路径

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string ProjectClientPath { get; }
```

###### 属性值

String

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### ProjectRemotePath 属性

|  |  |
| --- | --- |
|  | SemiContextProjectRemotePath 属性 |

项目在Engine上的缓存目录
此路径的父级目录可以在Engine安装目录下config/engineConfig.xml修改

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string ProjectRemotePath { get; }
```

###### 属性值

String

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### RegisterAccessor 属性

|  |  |
| --- | --- |
|  | SemiContextRegisterAccessor 属性 |

寄存器访问接口,与TestMethod内的RegisterAccessor是同一个实例，可使用任意一个

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public IRegisterAccessor RegisterAccessor { get; }
```

###### 属性值

[IRegisterAccessor](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### SwitchAccessor 属性

|  |  |
| --- | --- |
|  | SemiContextSwitchAccessor 属性 |

Switch访问接口,与TestMethod内的SwitchAccessor是同一个实例，可使用任意一个

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public ISwitchAccessor SwitchAccessor { get; }
```

###### 属性值

[ISwitchAccessor](f4adcf92-99fb-8004-0cf6-b59040e967eb.htm)

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### TestProgram 属性

|  |  |
| --- | --- |
|  | SemiContextTestProgram 属性 |

TestProgram级别的变量获取和设置接口

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public ProgramVariables TestProgram { get; }
```

###### 属性值

[ProgramVariables](44493283-e635-f7bf-6080-ef8f86b3f1a2.htm)

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### VariableAccessor 属性

|  |  |
| --- | --- |
|  | SemiContextVariableAccessor 属性 |

变量访问接口,与TestMethod内的VariableAccessor是同一个实例，可使用任意一个

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public IVariableAccessor VariableAccessor { get; }
```

###### 属性值

[IVariableAccessor](6e6124cd-87b1-6191-bf37-5a6153dcae9c.htm)

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### SemiContext 方法

|  |  |
| --- | --- |
|  | SemiContext 方法 |

[SemiContext](421aec95-4c88-392e-653b-28511d2c5421.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [AP](32f574c9-3c93-eac5-1d93-bfb95b1700b6.htm) | 根据输入的 Pin获取 AP 类仪器的操作对象 |
| 公共方法 | [BERT](bc7082fd-6a90-22a1-4ee8-eb6aec3dd8a7.htm) | 根据输入的 Pin获取 BERT 类仪器的操作对象 |
| 公共方法 | [Converter](82f53ff6-ef4a-051d-553d-2d31a6f450ff.htm) | 根据输入的 Pin获取 Converter 类仪器的操作对象 |
| 公共方法 | [Counter](bab6fcba-44a0-6321-c183-4ae728bb5f2c.htm) | 根据输入的 Pin获取 Counter 类仪器的操作对象 |
| 公共方法 | [DAQ](599943ce-888d-0201-3d9c-11844012da09.htm) | 根据输入的 Pin获取 DAQ 类仪器的操作对象 |
| 公共方法 | [DCA](cfc2e029-b29c-df22-0f74-ad1cc16d2f2f.htm) | 根据输入的 Pin获取 DCA 类仪器的操作对象 |
| 公共方法 | [DCVI](f899aec9-d7c7-119e-55f7-ee0316dda49f.htm) | 根据输入的 Pin获取 DCVI 类仪器的操作对象 |
| 公共方法 | [Digital](bd55b73e-0d85-cb1c-b998-b15871ac1cd5.htm) | 根据输入的 Pin获取 Digital 类仪器的操作对象 |
| 公共方法 | [Dmm](bc52222b-4501-765f-5a90-8ed393124914.htm) | 根据输入的 Pin获取 Dmm 类仪器的操作对象 |
| 公共方法 | [Eload](e105e2b9-fdb7-6076-3ca9-67f245c20948.htm) | 根据输入的 Pin获取 Eload 类仪器的操作对象 |
| 公共方法 | [ENA](29d51a0c-18ca-599f-8b35-869652672e98.htm) | 根据输入的 Pin获取 ENA 类仪器的操作对象 |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 公共方法 | [Fgen](7828868f-c1fd-2c25-acd5-4d25cd4faf5c.htm) | 根据输入的 Pin获取 Fgen 类仪器的操作对象 |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | [GetMeasureStationT](b318e874-2e27-85c2-f61b-557f3e096c07.htm) | 根据输入的 Pin获取自定义仪器的操作对象 |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | [HID](67d7631a-ab84-6efb-3f3d-f9d337843f4f.htm) | 根据输入的 Pin获取 HID 类仪器的操作对象 |
| 公共方法 | [LCRMeter](a564026c-7188-da9a-1106-162971114075.htm) | 根据输入的 Pin获取 LCRMeter 类仪器的操作对象 |
| 公共方法 | [Log(Object)](7ca538c6-ee2d-8d37-b768-35f471a1a389.htm) | 向Output.Engine输出通道中打印日志 |
| 公共方法 | [Log(LogLevel, Object)](87b28270-9ea2-791e-42f8-6f8c99a1b28b.htm) | 向Output.Engine输出通道中打印日志 |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [PipeInvoke](5b7738b0-b2e8-134f-b3af-a054d327a21c.htm) | 根据输入的 Pin获取 PipeInvoke 类仪器的操作对象 |
| 公共方法 | [PNA](cea7d544-3980-9f69-589c-7747c9b5114a.htm) | 根据输入的 Pin获取 PNA 类仪器的操作对象 |
| 公共方法 | [Power](f8c587da-4e8b-4be8-09ad-d1f3327287c0.htm) | 根据输入的 Pin获取 Power 类仪器的操作对象 |
| 公共方法 | [PowerMeter](5c5da2d3-6f6c-becd-998c-3a095bd24f19.htm) | 根据输入的 Pin获取 PowerMeter 类仪器的操作对象 |
| 公共方法 | [RFSA](3db77564-dd6f-2884-7616-254222b769fb.htm) | 根据输入的 Pin获取 RFSA 类仪器的操作对象 |
| 公共方法 | [RFSG](d11697fd-52f6-8e21-a583-e6620b32ddc8.htm) | 根据输入的 Pin获取 RFSG 类仪器的操作对象 |
| 公共方法 | [Scope](5345d5ce-458f-9610-bafc-4afdc2474cff.htm) | 根据输入的 Pin获取 Scope 类仪器的操作对象 |
| 公共方法 | [Serial](3b5b0e77-2cf6-2d3c-bfa5-b0e30ef47320.htm) | 根据输入的 Pin获取 Serial 类仪器的操作对象 |
| 公共方法 | [SerialChamber](c4c77f7f-3ddd-4f83-da9d-2e999559a369.htm) | 根据输入的 Pin获取 SerialChamber 类仪器的操作对象 |
| 公共方法 | [SpDigital](074ab21f-13eb-14eb-9d20-fc64cec58531.htm) | 根据输入的 Pin获取 SpDigital 类仪器的操作对象 |
| 公共方法 | [SpecAn](3f6f133b-7114-8d11-6402-e06d8c53c5af.htm) | 根据输入的 Pin获取 SpecAn 类仪器的操作对象 |
| 公共方法 | [Switch](b7c4cdbe-db68-5abb-cb91-0dd876cd4a7a.htm) | 根据输入的 Pin获取 Switch 类仪器的操作对象 |
| 公共方法 | [Sync](8a11daf5-ad27-45de-0bc2-ad94933131ae.htm) | 根据输入的 Pin获取 Sync 类仪器的操作对象 |
| 公共方法 | [Thermal](a5be2f9e-b105-7dbd-f5d0-15d633b2ff39.htm) | 根据输入的 Pin获取 Thermal 类仪器的操作对象 |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |
| 公共方法 | [Visa](b3d1aea3-b67a-9451-5c89-69b1a7c96484.htm) | 根据输入的 Pin获取 Visa 类仪器的操作对象 |

[Top](#PageHeader)

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### AP 方法

|  |  |
| --- | --- |
|  | SemiContextAP 方法 |

根据输入的 Pin获取 AP 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public AP AP(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[AP](aa3ed330-2cf9-c2ac-3179-08ccfc938c9e.htm)  
AP 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### BERT 方法

|  |  |
| --- | --- |
|  | SemiContextBERT 方法 |

根据输入的 Pin获取 BERT 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public BERT BERT(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[BERT](0763e887-9796-2b60-1ddc-6f18dc9245b3.htm)  
BERT 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Converter 方法

|  |  |
| --- | --- |
|  | SemiContextConverter 方法 |

根据输入的 Pin获取 Converter 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Converter Converter(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[Converter](406ef1dc-666f-fa06-d8d0-4b0b71cd8907.htm)  
Converter 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Counter 方法

|  |  |
| --- | --- |
|  | SemiContextCounter 方法 |

根据输入的 Pin获取 Counter 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Counter Counter(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[Counter](0fc6b786-5bf0-1e3b-5b4a-7c689d325715.htm)  
Counter 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### DAQ 方法

|  |  |
| --- | --- |
|  | SemiContextDAQ 方法 |

根据输入的 Pin获取 DAQ 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DAQ DAQ(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[DAQ](b9f831ec-9cad-45b0-7222-1ad4f062a2c8.htm)  
DAQ 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### DCA 方法

|  |  |
| --- | --- |
|  | SemiContextDCA 方法 |

根据输入的 Pin获取 DCA 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCA DCA(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[DCA](2d57d3b6-4517-2777-895f-a57196dbf307.htm)  
DCA 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### DCVI 方法

|  |  |
| --- | --- |
|  | SemiContextDCVI 方法 |

根据输入的 Pin获取 DCVI 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI DCVI(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
DCVI 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Digital 方法

|  |  |
| --- | --- |
|  | SemiContextDigital 方法 |

根据输入的 Pin获取 Digital 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital Digital(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Digital 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Dmm 方法

|  |  |
| --- | --- |
|  | SemiContextDmm 方法 |

根据输入的 Pin获取 Dmm 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm Dmm(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Dmm 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Eload 方法

|  |  |
| --- | --- |
|  | SemiContextEload 方法 |

根据输入的 Pin获取 Eload 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Eload Eload(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[Eload](be53d32e-a542-874a-c04b-81f977459ec6.htm)  
Eload 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### ENA 方法

|  |  |
| --- | --- |
|  | SemiContextENA 方法 |

根据输入的 Pin获取 ENA 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public ENA ENA(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[ENA](fb1515f8-1b1c-e935-a29d-fde2493edc8e.htm)  
ENA 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Fgen 方法

|  |  |
| --- | --- |
|  | SemiContextFgen 方法 |

根据输入的 Pin获取 Fgen 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen Fgen(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Fgen 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetMeasureStation&lt;T&gt; 方法

|  |  |
| --- | --- |
|  | SemiContextGetMeasureStationT 方法 |

根据输入的 Pin获取自定义仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public T GetMeasureStation<T>(
	string pinString
)
where T : new(), MeasStation
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 类型参数

T

###### 返回值

T  
自定义仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### HID 方法

|  |  |
| --- | --- |
|  | SemiContextHID 方法 |

根据输入的 Pin获取 HID 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public HID HID(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[HID](a0cc3449-3897-c501-18e3-2809809aec7a.htm)  
HID 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### LCRMeter 方法

|  |  |
| --- | --- |
|  | SemiContextLCRMeter 方法 |

根据输入的 Pin获取 LCRMeter 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public LCRMeter LCRMeter(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[LCRMeter](ef7abadb-af0a-eeef-d696-45cdb731978d.htm)  
LCRMeter 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Log 方法

|  |  |
| --- | --- |
|  | SemiContextLog 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Log(Object)](7ca538c6-ee2d-8d37-b768-35f471a1a389.htm) | 向Output.Engine输出通道中打印日志 |
| 公共方法 | [Log(LogLevel, Object)](87b28270-9ea2-791e-42f8-6f8c99a1b28b.htm) | 向Output.Engine输出通道中打印日志 |

[Top](#PageHeader)

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Log(Object[]) 方法

|  |  |
| --- | --- |
|  | SemiContextLog(Object) 方法 |

向Output.Engine输出通道中打印日志

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public void Log(
	params Object[] msg
)
```

###### 参数

msg  Object

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Log 重载](163c9322-e057-33e2-4dda-03aaf6bebc6e.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Log(LogLevel, Object[]) 方法

|  |  |
| --- | --- |
|  | SemiContextLog(LogLevel, Object) 方法 |

向Output.Engine输出通道中打印日志

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public void Log(
	LogLevel level,
	params Object[] msg
)
```

###### 参数

level  [LogLevel](aaec65d4-7cb4-f48d-80f6-03bb853b8d2b.htm)

msg  Object

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Log 重载](163c9322-e057-33e2-4dda-03aaf6bebc6e.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### PipeInvoke 方法

|  |  |
| --- | --- |
|  | SemiContextPipeInvoke 方法 |

根据输入的 Pin获取 PipeInvoke 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public PipeInvoke PipeInvoke(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

PipeInvoke  
Power 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### PNA 方法

|  |  |
| --- | --- |
|  | SemiContextPNA 方法 |

根据输入的 Pin获取 PNA 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public PNA PNA(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[PNA](58380131-0ebb-302c-87ba-e7831cfd4224.htm)  
PNA 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Power 方法

|  |  |
| --- | --- |
|  | SemiContextPower 方法 |

根据输入的 Pin获取 Power 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Power Power(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

Power  
Power 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### PowerMeter 方法

|  |  |
| --- | --- |
|  | SemiContextPowerMeter 方法 |

根据输入的 Pin获取 PowerMeter 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public PowerMeter PowerMeter(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[PowerMeter](278e6738-f659-458e-aed8-5005701a6a85.htm)  
PowerMeter 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### RFSA 方法

|  |  |
| --- | --- |
|  | SemiContextRFSA 方法 |

根据输入的 Pin获取 RFSA 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public RFSA RFSA(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[RFSA](f1973016-6e93-710c-c1a9-1c924ffb692c.htm)  
RFSA 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### RFSG 方法

|  |  |
| --- | --- |
|  | SemiContextRFSG 方法 |

根据输入的 Pin获取 RFSG 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public RFSG RFSG(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[RFSG](f2f0f7e6-04f5-15b2-3d08-89e2e6ad7dba.htm)  
RFSG 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Scope 方法

|  |  |
| --- | --- |
|  | SemiContextScope 方法 |

根据输入的 Pin获取 Scope 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Scope Scope(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[Scope](9bb822ec-b57c-5075-7b11-c53eb488fd08.htm)  
Scope 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Serial 方法

|  |  |
| --- | --- |
|  | SemiContextSerial 方法 |

根据输入的 Pin获取 Serial 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Serial Serial(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[Serial](ac5c38b4-efd1-2405-d14f-e33d45245709.htm)  
Serial 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### SerialChamber 方法

|  |  |
| --- | --- |
|  | SemiContextSerialChamber 方法 |

根据输入的 Pin获取 SerialChamber 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public SerialChamber SerialChamber(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[SerialChamber](e6ca99bc-ea35-a9a5-05df-4d615e8874a5.htm)  
SerialChamber 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### SpDigital 方法

|  |  |
| --- | --- |
|  | SemiContextSpDigital 方法 |

根据输入的 Pin获取 SpDigital 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public SpDigital SpDigital(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[SpDigital](2c6d2847-491a-b16e-4a95-7aaa01a7d678.htm)  
SpDigital 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### SpecAn 方法

|  |  |
| --- | --- |
|  | SemiContextSpecAn 方法 |

根据输入的 Pin获取 SpecAn 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public SpecAn SpecAn(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[SpecAn](98ee1762-8764-818d-098f-90c91d17d0de.htm)  
SpecAn 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Switch 方法

|  |  |
| --- | --- |
|  | SemiContextSwitch 方法 |

根据输入的 Pin获取 Switch 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Switch Switch(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[Switch](3690c03c-74e6-7072-c3c7-f9d985b5803a.htm)  
Switch 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Sync 方法

|  |  |
| --- | --- |
|  | SemiContextSync 方法 |

根据输入的 Pin获取 Sync 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Sync Sync(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[Sync](1db79bd8-f2d5-4a18-7d91-289c1cbaf127.htm)  
Sync 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Thermal 方法

|  |  |
| --- | --- |
|  | SemiContextThermal 方法 |

根据输入的 Pin获取 Thermal 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Thermal Thermal(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[Thermal](4fff860f-e3f3-dc25-6b3a-395ca999d188.htm)  
Thermal 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Visa 方法

|  |  |
| --- | --- |
|  | SemiContextVisa 方法 |

根据输入的 Pin获取 Visa 类仪器的操作对象

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Visa Visa(
	string pinString
)
```

###### 参数

pinString  String
:   想要操作的 Pin，Pins 或 PinGroup，多个时用逗号连接

###### 返回值

[Visa](b2f57cdd-a54a-e5f4-a0e4-13aa42796180.htm)  
Visa 仪器操作对象

参见

###### 引用

[SemiContext 类](421aec95-4c88-392e-653b-28511d2c5421.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## TestBinResult 类

|  |  |
| --- | --- |
|  | TestBinResult 类 |

继承层次

SystemObject
  
  Guwave.OneTest.TestMethodTestBinResult

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public class TestBinResult
```

TestBinResult 类型公开以下成员。

构造函数

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [TestBinResult](1dcc78f7-4727-08b0-2b95-6fdd200ca9a0.htm) | 初始化 TestBinResult 类的一个新实例 |

[Top](#PageHeader)

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [HardBin](1f5d8055-1439-e22a-8bad-86b8dda19335.htm) |  |
| 公共属性 | [Site](40e9ea19-6018-3c85-f7a8-2b738e35f977.htm) |  |
| 公共属性 | [SoftBin](45f2b3bf-1003-a7c9-8637-7c9e77e2c2c1.htm) |  |
| 公共属性 | [Status](d442eaea-1cc2-74fb-ebcc-fd9e0d221add.htm) |  |

[Top](#PageHeader)

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |

[Top](#PageHeader)

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### TestBinResult 构造函数

|  |  |
| --- | --- |
|  | TestBinResult 构造函数 |

初始化 [TestBinResult](c05768d0-3a5a-71cc-9d5f-0d0f16602f5f.htm) 类的一个新实例

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public TestBinResult()
```

参见

###### 引用

[TestBinResult 类](c05768d0-3a5a-71cc-9d5f-0d0f16602f5f.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### TestBinResult 属性

|  |  |
| --- | --- |
|  | TestBinResult 属性 |

[TestBinResult](c05768d0-3a5a-71cc-9d5f-0d0f16602f5f.htm) 类型公开以下成员。

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [HardBin](1f5d8055-1439-e22a-8bad-86b8dda19335.htm) |  |
| 公共属性 | [Site](40e9ea19-6018-3c85-f7a8-2b738e35f977.htm) |  |
| 公共属性 | [SoftBin](45f2b3bf-1003-a7c9-8637-7c9e77e2c2c1.htm) |  |
| 公共属性 | [Status](d442eaea-1cc2-74fb-ebcc-fd9e0d221add.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[TestBinResult 类](c05768d0-3a5a-71cc-9d5f-0d0f16602f5f.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### HardBin 属性

|  |  |
| --- | --- |
|  | TestBinResultHardBin 属性 |

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public int HardBin { get; set; }
```

###### 属性值

Int32

参见

###### 引用

[TestBinResult 类](c05768d0-3a5a-71cc-9d5f-0d0f16602f5f.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Site 属性

|  |  |
| --- | --- |
|  | TestBinResultSite 属性 |

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public uint Site { get; set; }
```

###### 属性值

UInt32

参见

###### 引用

[TestBinResult 类](c05768d0-3a5a-71cc-9d5f-0d0f16602f5f.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### SoftBin 属性

|  |  |
| --- | --- |
|  | TestBinResultSoftBin 属性 |

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public int SoftBin { get; set; }
```

###### 属性值

Int32

参见

###### 引用

[TestBinResult 类](c05768d0-3a5a-71cc-9d5f-0d0f16602f5f.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Status 属性

|  |  |
| --- | --- |
|  | TestBinResultStatus 属性 |

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public bool Status { get; set; }
```

###### 属性值

Boolean

参见

###### 引用

[TestBinResult 类](c05768d0-3a5a-71cc-9d5f-0d0f16602f5f.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### TestBinResult 方法

|  |  |
| --- | --- |
|  | TestBinResult 方法 |

[TestBinResult](c05768d0-3a5a-71cc-9d5f-0d0f16602f5f.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |

[Top](#PageHeader)

参见

###### 引用

[TestBinResult 类](c05768d0-3a5a-71cc-9d5f-0d0f16602f5f.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


## TestMethod 类

|  |  |
| --- | --- |
|  | TestMethod 类 |

C#类型TestMethod基类，用户添加C#类型的TestMethod必须集成此类

继承层次

SystemObject
  
  Guwave.OneTest.TestMethodTestMethod

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public abstract class TestMethod : ITestMethod
```

TestMethod 类型公开以下成员。

构造函数

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [TestMethod](066b7e74-7add-e904-fbd7-dac705fa11ea.htm) | 构造函数 如果用户自己在一个TestMethod中初始化另一个TestMethod，调用此构造函数后，必须还有调用Initialize方法 |

[Top](#PageHeader)

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [DeviceAccessor](9dff777c-e82a-4ba2-03b1-b6556e9c56f4.htm) | 当前Site分Bin指定操作接口,直接修改当前Site ExecutionHolder的bin结果, 与Evaluate方法同优先级 |
| 公共属性 | [FileAccessor](c3396395-3634-56ce-2606-240101897c35.htm) | 文件访问接口, 与SemiContext内的FileAccessor是同一个实例，可使用任意一个 |
| 公共属性 | [InputGroupParams](8dac7ebb-7f3b-6c5e-ffe5-98d71ef9eb99.htm) | 当前TestMethod对界面暴露的分组参数列表 |
| 公共属性 | [InputParams](2013e083-9071-933a-9276-f91826e73ca0.htm) | 当前TestMethod对界面暴露的普通参数列表 |
| 公共属性 | [PinmapAccessor](43391c0d-f5b3-4461-47ba-c15f3bcc3f5e.htm) | Pin/PinGroup和连接配置访问接口, 与SemiContext内的PinmapAccessor是同一个实例，可使用任意一个 |
| 公共属性 | [RegisterAccessor](7dea5150-79b9-9ce7-75aa-4c414044576d.htm) | 寄存器访问接口, 与SemiContext内的RegisterAccessor是同一个实例，可使用任意一个 |
| 公共属性 | [SemiContext](35dcafbb-2741-4376-a973-316afde34de8.htm) | SemiContext上下文 |
| 公共属性 | [SwitchAccessor](fa4e01c3-07c0-42b9-9a1f-71ab6d1524dc.htm) | Switch访问接口, 与SemiContext内的SwitchAccessor是同一个实例，可使用任意一个 |
| 公共属性 | [TestMethodName](56fd2e49-c53c-3829-c43b-8d56217bd88f.htm) | TestMethod名称 |
| 公共属性 | [VariableAccessor](b1f74749-59f8-305f-0373-e595b79a1f43.htm) | 变量访问接口, 与SemiContext内的VariableAccessor是同一个实例，可使用任意一个 |

[Top](#PageHeader)

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [DebugPrint](fd4f3c15-ecd3-e248-e98a-9d2d1179b1a6.htm) | 向报告(CharCSV)中打印Debug信息 |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 公共方法 | [Execute](ce5680a9-cf97-a1d1-6cc3-a5c65b73aae4.htm) | TestSuite的Execute |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | [GetInputParameters](505eb21e-a265-538d-f530-766569f700e0.htm) | 获取当前运行状态下所有开放参数的实时值 |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | [Initialize](a58acdbb-63b7-961b-b029-9536436fc4fe.htm) | TM初始化方法，在Debug或者Flow任务启动前运行一次 用户TM可以重写此方法，但要调用基类的此方法 |
| 公共方法 | [Log(Object)](81d524a4-be33-3724-1301-6f2978e9d8af.htm) | 向Output.Engine输出通道中打印日志 |
| 公共方法 | [Log(LogLevel, Object)](b01435ba-ba3d-1954-bb43-281b08ea8f93.htm) | 向Output.Engine输出通道中打印日志 |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [OnParameterChange](a611b411-df12-ff80-cbc0-48cc01370369.htm) | 当运行中修改了TestSuite的Configuration，则会触发此事件 如果有需要，用户可以在TM中重写此方法 |
| 公共方法 | [PostExecute](b73c3eea-09aa-3fd5-2144-29ff970868d6.htm) | 每次执行TestSuite的Execute方法之后会执行此方法 如果有需要，用户可以在TM中重写此方法 |
| 公共方法 | [PreExecute](3bdfa9d1-d679-eab6-5214-6837846eb02b.htm) | 每次执行TestSuite的Execute方法之前会执行此方法 如果有需要，用户可以在TM中重写此方法 |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |

[Top](#PageHeader)

参见

##### 引用

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### TestMethod 构造函数

|  |  |
| --- | --- |
|  | TestMethod 构造函数 |

构造函数
如果用户自己在一个TestMethod中初始化另一个TestMethod，调用此构造函数后，必须还有调用Initialize方法

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public TestMethod()
```

参见

###### 引用

[TestMethod 类](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### TestMethod 属性

|  |  |
| --- | --- |
|  | TestMethod 属性 |

[TestMethod](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm) 类型公开以下成员。

属性

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共属性 | [DeviceAccessor](9dff777c-e82a-4ba2-03b1-b6556e9c56f4.htm) | 当前Site分Bin指定操作接口,直接修改当前Site ExecutionHolder的bin结果, 与Evaluate方法同优先级 |
| 公共属性 | [FileAccessor](c3396395-3634-56ce-2606-240101897c35.htm) | 文件访问接口, 与SemiContext内的FileAccessor是同一个实例，可使用任意一个 |
| 公共属性 | [InputGroupParams](8dac7ebb-7f3b-6c5e-ffe5-98d71ef9eb99.htm) | 当前TestMethod对界面暴露的分组参数列表 |
| 公共属性 | [InputParams](2013e083-9071-933a-9276-f91826e73ca0.htm) | 当前TestMethod对界面暴露的普通参数列表 |
| 公共属性 | [PinmapAccessor](43391c0d-f5b3-4461-47ba-c15f3bcc3f5e.htm) | Pin/PinGroup和连接配置访问接口, 与SemiContext内的PinmapAccessor是同一个实例，可使用任意一个 |
| 公共属性 | [RegisterAccessor](7dea5150-79b9-9ce7-75aa-4c414044576d.htm) | 寄存器访问接口, 与SemiContext内的RegisterAccessor是同一个实例，可使用任意一个 |
| 公共属性 | [SemiContext](35dcafbb-2741-4376-a973-316afde34de8.htm) | SemiContext上下文 |
| 公共属性 | [SwitchAccessor](fa4e01c3-07c0-42b9-9a1f-71ab6d1524dc.htm) | Switch访问接口, 与SemiContext内的SwitchAccessor是同一个实例，可使用任意一个 |
| 公共属性 | [TestMethodName](56fd2e49-c53c-3829-c43b-8d56217bd88f.htm) | TestMethod名称 |
| 公共属性 | [VariableAccessor](b1f74749-59f8-305f-0373-e595b79a1f43.htm) | 变量访问接口, 与SemiContext内的VariableAccessor是同一个实例，可使用任意一个 |

[Top](#PageHeader)

参见

###### 引用

[TestMethod 类](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### DeviceAccessor 属性

|  |  |
| --- | --- |
|  | TestMethodDeviceAccessor 属性 |

当前Site分Bin指定操作接口,直接修改当前Site ExecutionHolder的bin结果, 与Evaluate方法同优先级

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public IDeviceAccessor DeviceAccessor { get; }
```

###### 属性值

[IDeviceAccessor](77da62e2-6cb3-e081-28ce-33c245f4add3.htm)

参见

###### 引用

[TestMethod 类](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### FileAccessor 属性

|  |  |
| --- | --- |
|  | TestMethodFileAccessor 属性 |

文件访问接口, 与SemiContext内的FileAccessor是同一个实例，可使用任意一个

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public IFileAccessor FileAccessor { get; }
```

###### 属性值

[IFileAccessor](dc5e402a-56da-a9ac-1101-94bfb5c693dd.htm)

参见

###### 引用

[TestMethod 类](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### InputGroupParams 属性

|  |  |
| --- | --- |
|  | TestMethodInputGroupParams 属性 |

当前TestMethod对界面暴露的分组参数列表

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public List<InputGroupParamAttribute> InputGroupParams { get; }
```

###### 属性值

List[InputGroupParamAttribute](cce82ed5-f9cd-2fee-ea69-2e9cebef8a2c.htm)

参见

###### 引用

[TestMethod 类](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### InputParams 属性

|  |  |
| --- | --- |
|  | TestMethodInputParams 属性 |

当前TestMethod对界面暴露的普通参数列表

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public List<InputParamAttribute> InputParams { get; }
```

###### 属性值

List[InputParamAttribute](b8a6b68c-b60b-2702-a248-5e92a3479efe.htm)

参见

###### 引用

[TestMethod 类](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### PinmapAccessor 属性

|  |  |
| --- | --- |
|  | TestMethodPinmapAccessor 属性 |

Pin/PinGroup和连接配置访问接口, 与SemiContext内的PinmapAccessor是同一个实例，可使用任意一个

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public IPinmapAccessor PinmapAccessor { get; }
```

###### 属性值

[IPinmapAccessor](c31b9fa6-009d-3188-6deb-bca1d67c7cc7.htm)

参见

###### 引用

[TestMethod 类](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### RegisterAccessor 属性

|  |  |
| --- | --- |
|  | TestMethodRegisterAccessor 属性 |

寄存器访问接口, 与SemiContext内的RegisterAccessor是同一个实例，可使用任意一个

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public IRegisterAccessor RegisterAccessor { get; }
```

###### 属性值

[IRegisterAccessor](c1d7847e-be65-d71a-2a6b-299baa8b9f0b.htm)

参见

###### 引用

[TestMethod 类](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### SemiContext 属性

|  |  |
| --- | --- |
|  | TestMethodSemiContext 属性 |

SemiContext上下文

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public SemiContext SemiContext { get; }
```

###### 属性值

[SemiContext](421aec95-4c88-392e-653b-28511d2c5421.htm)

###### 实现

[ITestMethodSemiContext](423234cf-e1d6-9cf3-bfc0-5afc5eedf9ef.htm)

参见

###### 引用

[TestMethod 类](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### SwitchAccessor 属性

|  |  |
| --- | --- |
|  | TestMethodSwitchAccessor 属性 |

Switch访问接口, 与SemiContext内的SwitchAccessor是同一个实例，可使用任意一个

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public ISwitchAccessor SwitchAccessor { get; }
```

###### 属性值

[ISwitchAccessor](f4adcf92-99fb-8004-0cf6-b59040e967eb.htm)

参见

###### 引用

[TestMethod 类](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### TestMethodName 属性

|  |  |
| --- | --- |
|  | TestMethodTestMethodName 属性 |

TestMethod名称

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string TestMethodName { get; }
```

###### 属性值

String

###### 实现

[ITestMethodTestMethodName](051c7331-6df0-9291-3df9-18c7e7e42f89.htm)

参见

###### 引用

[TestMethod 类](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### VariableAccessor 属性

|  |  |
| --- | --- |
|  | TestMethodVariableAccessor 属性 |

变量访问接口, 与SemiContext内的VariableAccessor是同一个实例，可使用任意一个

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public IVariableAccessor VariableAccessor { get; }
```

###### 属性值

[IVariableAccessor](6e6124cd-87b1-6191-bf37-5a6153dcae9c.htm)

参见

###### 引用

[TestMethod 类](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


### TestMethod 方法

|  |  |
| --- | --- |
|  | TestMethod 方法 |

[TestMethod](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [DebugPrint](fd4f3c15-ecd3-e248-e98a-9d2d1179b1a6.htm) | 向报告(CharCSV)中打印Debug信息 |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 公共方法 | [Execute](ce5680a9-cf97-a1d1-6cc3-a5c65b73aae4.htm) | TestSuite的Execute |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | [GetInputParameters](505eb21e-a265-538d-f530-766569f700e0.htm) | 获取当前运行状态下所有开放参数的实时值 |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | [Initialize](a58acdbb-63b7-961b-b029-9536436fc4fe.htm) | TM初始化方法，在Debug或者Flow任务启动前运行一次 用户TM可以重写此方法，但要调用基类的此方法 |
| 公共方法 | [Log(Object)](81d524a4-be33-3724-1301-6f2978e9d8af.htm) | 向Output.Engine输出通道中打印日志 |
| 公共方法 | [Log(LogLevel, Object)](b01435ba-ba3d-1954-bb43-281b08ea8f93.htm) | 向Output.Engine输出通道中打印日志 |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [OnParameterChange](a611b411-df12-ff80-cbc0-48cc01370369.htm) | 当运行中修改了TestSuite的Configuration，则会触发此事件 如果有需要，用户可以在TM中重写此方法 |
| 公共方法 | [PostExecute](b73c3eea-09aa-3fd5-2144-29ff970868d6.htm) | 每次执行TestSuite的Execute方法之后会执行此方法 如果有需要，用户可以在TM中重写此方法 |
| 公共方法 | [PreExecute](3bdfa9d1-d679-eab6-5214-6837846eb02b.htm) | 每次执行TestSuite的Execute方法之前会执行此方法 如果有需要，用户可以在TM中重写此方法 |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |

[Top](#PageHeader)

参见

###### 引用

[TestMethod 类](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### DebugPrint 方法

|  |  |
| --- | --- |
|  | TestMethodDebugPrint 方法 |

向报告(CharCSV)中打印Debug信息

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public void DebugPrint(
	string info
)
```

###### 参数

info  String

参见

###### 引用

[TestMethod 类](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Execute 方法

|  |  |
| --- | --- |
|  | TestMethodExecute 方法 |

TestSuite的Execute

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public abstract void Execute()
```

###### 实现

[ITestMethodExecute](1463c7a6-ef51-6c85-08f7-058c4b4b5997.htm)

参见

###### 引用

[TestMethod 类](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### GetInputParameters 方法

|  |  |
| --- | --- |
|  | TestMethodGetInputParameters 方法 |

获取当前运行状态下所有开放参数的实时值

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, Object> GetInputParameters()
```

###### 返回值

DictionaryString, Object  

###### 实现

[ITestMethodGetInputParameters](ece165ba-2647-4d37-e487-6566d19fc819.htm)

参见

###### 引用

[TestMethod 类](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Initialize 方法

|  |  |
| --- | --- |
|  | TestMethodInitialize 方法 |

TM初始化方法，在Debug或者Flow任务启动前运行一次
用户TM可以重写此方法，但要调用基类的此方法

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public virtual void Initialize(
	SemiContext semiContext
)
```

###### 参数

semiContext  [SemiContext](421aec95-4c88-392e-653b-28511d2c5421.htm)

###### 实现

[ITestMethodInitialize(SemiContext)](965f13d3-7d40-cc8a-1719-52f893fc75a1.htm)

参见

###### 引用

[TestMethod 类](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### Log 方法

|  |  |
| --- | --- |
|  | TestMethodLog 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Log(Object)](81d524a4-be33-3724-1301-6f2978e9d8af.htm) | 向Output.Engine输出通道中打印日志 |
| 公共方法 | [Log(LogLevel, Object)](b01435ba-ba3d-1954-bb43-281b08ea8f93.htm) | 向Output.Engine输出通道中打印日志 |

[Top](#PageHeader)

参见

###### 引用

[TestMethod 类](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Log(Object[]) 方法

|  |  |
| --- | --- |
|  | TestMethodLog(Object) 方法 |

向Output.Engine输出通道中打印日志

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public void Log(
	params Object[] msg
)
```

###### 参数

msg  Object

参见

###### 引用

[TestMethod 类](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm)

[Log 重载](42523f20-c102-06bd-4811-21d4142dbd2e.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


##### Log(LogLevel, Object[]) 方法

|  |  |
| --- | --- |
|  | TestMethodLog(LogLevel, Object) 方法 |

向Output.Engine输出通道中打印日志

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public void Log(
	LogLevel level,
	params Object[] msg
)
```

###### 参数

level  [LogLevel](aaec65d4-7cb4-f48d-80f6-03bb853b8d2b.htm)

msg  Object

参见

###### 引用

[TestMethod 类](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm)

[Log 重载](42523f20-c102-06bd-4811-21d4142dbd2e.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### OnParameterChange 方法

|  |  |
| --- | --- |
|  | TestMethodOnParameterChange 方法 |

当运行中修改了TestSuite的Configuration，则会触发此事件
如果有需要，用户可以在TM中重写此方法

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public virtual void OnParameterChange()
```

###### 实现

[ITestMethodOnParameterChange](757bbf16-fb3f-5911-38d6-1d01a77f2182.htm)

参见

###### 引用

[TestMethod 类](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### PostExecute 方法

|  |  |
| --- | --- |
|  | TestMethodPostExecute 方法 |

每次执行TestSuite的Execute方法之后会执行此方法
如果有需要，用户可以在TM中重写此方法

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public virtual void PostExecute()
```

###### 实现

[ITestMethodPostExecute](d0944ef8-3071-76c6-935a-7e01a360b8cd.htm)

参见

###### 引用

[TestMethod 类](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)


#### PreExecute 方法

|  |  |
| --- | --- |
|  | TestMethodPreExecute 方法 |

每次执行TestSuite的Execute方法之前会执行此方法
如果有需要，用户可以在TM中重写此方法

  
**命名空间：** [Guwave.OneTest.TestMethod](4655117f-585f-f813-efe4-a383dd142066.htm)  
**程序集：** Guwave.OneTest.TestMethod (在 Guwave.OneTest.TestMethod.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public virtual void PreExecute()
```

###### 实现

[ITestMethodPreExecute](2e53cd21-0d75-910e-4ce7-0fceb0eac326.htm)

参见

###### 引用

[TestMethod 类](d8211943-5713-f86b-ebaa-4c5596bbfeca.htm)

[Guwave.OneTest.TestMethod 命名空间](4655117f-585f-f813-efe4-a383dd142066.htm)

