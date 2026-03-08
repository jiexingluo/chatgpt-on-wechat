|  |  |
| --- | --- |
|  | SerialParent 命名空间 |

类

|  | 类 | 说明 |
| --- | --- | --- |
| 公共类 | [Serial](ac5c38b4-efd1-2405-d14f-e33d45245709.htm) |  |

接口

|  | 接口 | 说明 |
| --- | --- | --- |
| 公共接口 | [ISerial\_Instr](aaac64ee-5e27-5643-8323-7855fa25a821.htm) |  |


## ISerial_Instr 接口

|  |  |
| --- | --- |
|  | ISerial\_Instr 接口 |

  
**命名空间：** [SerialParent](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)  
**程序集：** SerialMeasStation (在 SerialMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public interface ISerial_Instr
```

ISerial\_Instr 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Configure](28b9206a-e9da-7a4e-22b0-3a9b6d19c367.htm) |  |
| 公共方法 | [GetData](9d497b1b-bc14-cefd-087e-97375cbe41e4.htm) |  |
| 公共方法 | [Reset](a157e27a-6c31-3d3b-8a80-dd13e6f804c3.htm) |  |
| 公共方法 | [SendData](d4e743ab-9c4c-5b23-31af-d7b6aee435ca.htm) |  |
| 公共方法 | [SendFile](7ad3e8a3-c660-5d0d-b7ee-ae1c52c27be4.htm) |  |

[Top](#PageHeader)

参见

##### 引用

[SerialParent 命名空间](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)


### ISerial_Instr 方法

|  |  |
| --- | --- |
|  | ISerial\_Instr 方法 |

[ISerial\_Instr](aaac64ee-5e27-5643-8323-7855fa25a821.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Configure](28b9206a-e9da-7a4e-22b0-3a9b6d19c367.htm) |  |
| 公共方法 | [GetData](9d497b1b-bc14-cefd-087e-97375cbe41e4.htm) |  |
| 公共方法 | [Reset](a157e27a-6c31-3d3b-8a80-dd13e6f804c3.htm) |  |
| 公共方法 | [SendData](d4e743ab-9c4c-5b23-31af-d7b6aee435ca.htm) |  |
| 公共方法 | [SendFile](7ad3e8a3-c660-5d0d-b7ee-ae1c52c27be4.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[ISerial\_Instr 接口](aaac64ee-5e27-5643-8323-7855fa25a821.htm)

[SerialParent 命名空间](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)


#### Configure 方法

|  |  |
| --- | --- |
|  | ISerial\_InstrConfigure 方法 |

  
**命名空间：** [SerialParent](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)  
**程序集：** SerialMeasStation (在 SerialMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Configure(
	int baudRate,
	int dataBit,
	double stopBit,
	string checkBit
)
```

###### 参数

baudRate  Int32

dataBit  Int32

stopBit  Double

checkBit  String

参见

###### 引用

[ISerial\_Instr 接口](aaac64ee-5e27-5643-8323-7855fa25a821.htm)

[SerialParent 命名空间](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)


#### GetData 方法

|  |  |
| --- | --- |
|  | ISerial\_InstrGetData 方法 |

  
**命名空间：** [SerialParent](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)  
**程序集：** SerialMeasStation (在 SerialMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetData(
	string dataFormat
)
```

###### 参数

dataFormat  String

###### 返回值

String

参见

###### 引用

[ISerial\_Instr 接口](aaac64ee-5e27-5643-8323-7855fa25a821.htm)

[SerialParent 命名空间](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)


#### Reset 方法

|  |  |
| --- | --- |
|  | ISerial\_InstrReset 方法 |

  
**命名空间：** [SerialParent](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)  
**程序集：** SerialMeasStation (在 SerialMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Reset()
```

参见

###### 引用

[ISerial\_Instr 接口](aaac64ee-5e27-5643-8323-7855fa25a821.htm)

[SerialParent 命名空间](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)


#### SendData 方法

|  |  |
| --- | --- |
|  | ISerial\_InstrSendData 方法 |

  
**命名空间：** [SerialParent](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)  
**程序集：** SerialMeasStation (在 SerialMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SendData(
	string sendData,
	string dataFormat
)
```

###### 参数

sendData  String

dataFormat  String

参见

###### 引用

[ISerial\_Instr 接口](aaac64ee-5e27-5643-8323-7855fa25a821.htm)

[SerialParent 命名空间](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)


#### SendFile 方法

|  |  |
| --- | --- |
|  | ISerial\_InstrSendFile 方法 |

  
**命名空间：** [SerialParent](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)  
**程序集：** SerialMeasStation (在 SerialMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SendFile(
	string filePath
)
```

###### 参数

filePath  String

参见

###### 引用

[ISerial\_Instr 接口](aaac64ee-5e27-5643-8323-7855fa25a821.htm)

[SerialParent 命名空间](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)


## Serial 类

|  |  |
| --- | --- |
|  | Serial 类 |

继承层次

SystemObject
  
  MeasStation  
    SerialParentSerial

  
**命名空间：** [SerialParent](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)  
**程序集：** SerialMeasStation (在 SerialMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public class Serial : MeasStation
```

Serial 类型公开以下成员。

构造函数

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Serial](6895d671-0fda-d792-6f4f-c746780e4a1c.htm) | 初始化 Serial 类的一个新实例 |

[Top](#PageHeader)

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Configure](5c7b6f67-2559-d69a-c554-55ebd5e57595.htm) |  |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | [GetData](6cc4583b-89b6-5e76-99bf-7decf6ed4feb.htm) |  |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [Reset](3ee31cd6-6217-c0ee-e6f3-28b44a97e2a8.htm) | Reset the instrument session. |
| 公共方法 | [SendData](43514b42-133b-1fb8-cc7c-75a18ba52113.htm) |  |
| 公共方法 | [SendFile](f9b8eac8-af75-b331-1572-ee69f0a32bbe.htm) |  |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |

[Top](#PageHeader)

参见

##### 引用

[SerialParent 命名空间](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)


### Serial 构造函数

|  |  |
| --- | --- |
|  | Serial 构造函数 |

初始化 [Serial](ac5c38b4-efd1-2405-d14f-e33d45245709.htm) 类的一个新实例

  
**命名空间：** [SerialParent](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)  
**程序集：** SerialMeasStation (在 SerialMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Serial()
```

参见

###### 引用

[Serial 类](ac5c38b4-efd1-2405-d14f-e33d45245709.htm)

[SerialParent 命名空间](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)


### Serial 方法

|  |  |
| --- | --- |
|  | Serial 方法 |

[Serial](ac5c38b4-efd1-2405-d14f-e33d45245709.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Configure](5c7b6f67-2559-d69a-c554-55ebd5e57595.htm) |  |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | [GetData](6cc4583b-89b6-5e76-99bf-7decf6ed4feb.htm) |  |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [Reset](3ee31cd6-6217-c0ee-e6f3-28b44a97e2a8.htm) | Reset the instrument session. |
| 公共方法 | [SendData](43514b42-133b-1fb8-cc7c-75a18ba52113.htm) |  |
| 公共方法 | [SendFile](f9b8eac8-af75-b331-1572-ee69f0a32bbe.htm) |  |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |

[Top](#PageHeader)

参见

###### 引用

[Serial 类](ac5c38b4-efd1-2405-d14f-e33d45245709.htm)

[SerialParent 命名空间](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)


#### Configure 方法

|  |  |
| --- | --- |
|  | SerialConfigure 方法 |

  
**命名空间：** [SerialParent](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)  
**程序集：** SerialMeasStation (在 SerialMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Serial Configure(
	long baudRate,
	long dataBit,
	double stopBit,
	string checkBit
)
```

###### 参数

baudRate  Int64

dataBit  Int64

stopBit  Double

checkBit  String

###### 返回值

[Serial](ac5c38b4-efd1-2405-d14f-e33d45245709.htm)

参见

###### 引用

[Serial 类](ac5c38b4-efd1-2405-d14f-e33d45245709.htm)

[SerialParent 命名空间](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)


#### GetData 方法

|  |  |
| --- | --- |
|  | SerialGetData 方法 |

  
**命名空间：** [SerialParent](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)  
**程序集：** SerialMeasStation (在 SerialMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetData(
	string dataFormat
)
```

###### 参数

dataFormat  String

###### 返回值

DictionaryString, String

参见

###### 引用

[Serial 类](ac5c38b4-efd1-2405-d14f-e33d45245709.htm)

[SerialParent 命名空间](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)


#### Reset 方法

|  |  |
| --- | --- |
|  | SerialReset 方法 |

Reset the instrument session.

  
**命名空间：** [SerialParent](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)  
**程序集：** SerialMeasStation (在 SerialMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Serial Reset()
```

###### 返回值

[Serial](ac5c38b4-efd1-2405-d14f-e33d45245709.htm)  
Return Serial instance.

参见

###### 引用

[Serial 类](ac5c38b4-efd1-2405-d14f-e33d45245709.htm)

[SerialParent 命名空间](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)


#### SendData 方法

|  |  |
| --- | --- |
|  | SerialSendData 方法 |

  
**命名空间：** [SerialParent](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)  
**程序集：** SerialMeasStation (在 SerialMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Serial SendData(
	string sendData,
	string dataFormat
)
```

###### 参数

sendData  String

dataFormat  String

###### 返回值

[Serial](ac5c38b4-efd1-2405-d14f-e33d45245709.htm)

参见

###### 引用

[Serial 类](ac5c38b4-efd1-2405-d14f-e33d45245709.htm)

[SerialParent 命名空间](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)


#### SendFile 方法

|  |  |
| --- | --- |
|  | SerialSendFile 方法 |

  
**命名空间：** [SerialParent](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)  
**程序集：** SerialMeasStation (在 SerialMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Serial SendFile(
	string filePath
)
```

###### 参数

filePath  String

###### 返回值

[Serial](ac5c38b4-efd1-2405-d14f-e33d45245709.htm)

参见

###### 引用

[Serial 类](ac5c38b4-efd1-2405-d14f-e33d45245709.htm)

[SerialParent 命名空间](ff6cc77c-72a7-5a64-eb24-42c35ae92bb7.htm)

