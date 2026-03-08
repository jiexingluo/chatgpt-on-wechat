|  |  |
| --- | --- |
|  | HIDParent 命名空间 |

类

|  | 类 | 说明 |
| --- | --- | --- |
| 公共类 | [HID](a0cc3449-3897-c501-18e3-2809809aec7a.htm) |  |

接口

|  | 接口 | 说明 |
| --- | --- | --- |
| 公共接口 | [IHID\_Instr](84f604be-6db0-f78b-9648-439198af767c.htm) |  |


## HID 类

|  |  |
| --- | --- |
|  | HID 类 |

继承层次

SystemObject
  
  MeasStation  
    HIDParentHID

  
**命名空间：** [HIDParent](b142ed42-aa11-2542-7a65-60028551e8eb.htm)  
**程序集：** HIDMeasStation (在 HIDMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public class HID : MeasStation
```

HID 类型公开以下成员。

构造函数

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [HID](93bc2de8-f2b1-43ba-a827-4997556fb06e.htm) | 初始化 HID 类的一个新实例 |

[Top](#PageHeader)

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [Reset](bcc98756-9f40-b5c8-8e34-9a1143ced6cc.htm) | Reset the instrument session. |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |
| 公共方法 | [WriteRead](be3f0501-b372-2022-3dd8-c090411258ce.htm) |  |

[Top](#PageHeader)

参见

##### 引用

[HIDParent 命名空间](b142ed42-aa11-2542-7a65-60028551e8eb.htm)


### HID 构造函数

|  |  |
| --- | --- |
|  | HID 构造函数 |

初始化 [HID](a0cc3449-3897-c501-18e3-2809809aec7a.htm) 类的一个新实例

  
**命名空间：** [HIDParent](b142ed42-aa11-2542-7a65-60028551e8eb.htm)  
**程序集：** HIDMeasStation (在 HIDMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public HID()
```

参见

###### 引用

[HID 类](a0cc3449-3897-c501-18e3-2809809aec7a.htm)

[HIDParent 命名空间](b142ed42-aa11-2542-7a65-60028551e8eb.htm)


### HID 方法

|  |  |
| --- | --- |
|  | HID 方法 |

[HID](a0cc3449-3897-c501-18e3-2809809aec7a.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [Reset](bcc98756-9f40-b5c8-8e34-9a1143ced6cc.htm) | Reset the instrument session. |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |
| 公共方法 | [WriteRead](be3f0501-b372-2022-3dd8-c090411258ce.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[HID 类](a0cc3449-3897-c501-18e3-2809809aec7a.htm)

[HIDParent 命名空间](b142ed42-aa11-2542-7a65-60028551e8eb.htm)


#### Reset 方法

|  |  |
| --- | --- |
|  | HIDReset 方法 |

Reset the instrument session.

  
**命名空间：** [HIDParent](b142ed42-aa11-2542-7a65-60028551e8eb.htm)  
**程序集：** HIDMeasStation (在 HIDMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public HID Reset()
```

###### 返回值

[HID](a0cc3449-3897-c501-18e3-2809809aec7a.htm)  
Return HID instance.

参见

###### 引用

[HID 类](a0cc3449-3897-c501-18e3-2809809aec7a.htm)

[HIDParent 命名空间](b142ed42-aa11-2542-7a65-60028551e8eb.htm)


#### WriteRead 方法

|  |  |
| --- | --- |
|  | HIDWriteRead 方法 |

  
**命名空间：** [HIDParent](b142ed42-aa11-2542-7a65-60028551e8eb.htm)  
**程序集：** HIDMeasStation (在 HIDMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long[]> WriteRead(
	long[] data
)
```

###### 参数

data  Int64

###### 返回值

DictionaryString, Int64

参见

###### 引用

[HID 类](a0cc3449-3897-c501-18e3-2809809aec7a.htm)

[HIDParent 命名空间](b142ed42-aa11-2542-7a65-60028551e8eb.htm)


## IHID_Instr 接口

|  |  |
| --- | --- |
|  | IHID\_Instr 接口 |

  
**命名空间：** [HIDParent](b142ed42-aa11-2542-7a65-60028551e8eb.htm)  
**程序集：** HIDMeasStation (在 HIDMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public interface IHID_Instr
```

IHID\_Instr 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Reset](d7c285ad-6390-4c54-664b-c03c3e560f3d.htm) |  |
| 公共方法 | [WriteRead](60374608-5d7e-d2f8-c9ea-9c8bc3842eae.htm) |  |

[Top](#PageHeader)

参见

##### 引用

[HIDParent 命名空间](b142ed42-aa11-2542-7a65-60028551e8eb.htm)


### IHID_Instr 方法

|  |  |
| --- | --- |
|  | IHID\_Instr 方法 |

[IHID\_Instr](84f604be-6db0-f78b-9648-439198af767c.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Reset](d7c285ad-6390-4c54-664b-c03c3e560f3d.htm) |  |
| 公共方法 | [WriteRead](60374608-5d7e-d2f8-c9ea-9c8bc3842eae.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[IHID\_Instr 接口](84f604be-6db0-f78b-9648-439198af767c.htm)

[HIDParent 命名空间](b142ed42-aa11-2542-7a65-60028551e8eb.htm)


#### Reset 方法

|  |  |
| --- | --- |
|  | IHID\_InstrReset 方法 |

  
**命名空间：** [HIDParent](b142ed42-aa11-2542-7a65-60028551e8eb.htm)  
**程序集：** HIDMeasStation (在 HIDMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Reset()
```

参见

###### 引用

[IHID\_Instr 接口](84f604be-6db0-f78b-9648-439198af767c.htm)

[HIDParent 命名空间](b142ed42-aa11-2542-7a65-60028551e8eb.htm)


#### WriteRead 方法

|  |  |
| --- | --- |
|  | IHID\_InstrWriteRead 方法 |

  
**命名空间：** [HIDParent](b142ed42-aa11-2542-7a65-60028551e8eb.htm)  
**程序集：** HIDMeasStation (在 HIDMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
byte[] WriteRead(
	byte[] data
)
```

###### 参数

data  Byte

###### 返回值

Byte

参见

###### 引用

[IHID\_Instr 接口](84f604be-6db0-f78b-9648-439198af767c.htm)

[HIDParent 命名空间](b142ed42-aa11-2542-7a65-60028551e8eb.htm)

