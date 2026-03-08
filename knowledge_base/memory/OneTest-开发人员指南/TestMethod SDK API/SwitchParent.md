|  |  |
| --- | --- |
|  | SwitchParent 命名空间 |

类

|  | 类 | 说明 |
| --- | --- | --- |
| 公共类 | [Switch](3690c03c-74e6-7072-c3c7-f9d985b5803a.htm) |  |

接口

|  | 接口 | 说明 |
| --- | --- | --- |
| 公共接口 | [ISwitch\_Instr](5cf462be-7211-8684-b1b7-1cb720de4be5.htm) |  |


## ISwitch_Instr 接口

|  |  |
| --- | --- |
|  | ISwitch\_Instr 接口 |

  
**命名空间：** [SwitchParent](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)  
**程序集：** SwitchMeasStation (在 SwitchMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public interface ISwitch_Instr
```

ISwitch\_Instr 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Connect](21cb47b2-1740-a0a8-9553-0f3e530f35c7.htm) |  |
| 公共方法 | [Disconnect](81263b20-84b0-4be9-3db1-d9d2729f35c4.htm) |  |
| 公共方法 | [DisconnectAllChannel](8e51541a-ba85-1e50-5615-3ed205692802.htm) |  |
| 公共方法 | [GetPathStatus](2aa9a8e5-8a61-f1c5-d72d-04ee882de8f9.htm) |  |
| 公共方法 | [GetRelayStatus](1cb1e3da-bbb9-a772-0cb8-641301a33098.htm) |  |
| 公共方法 | [IsDebounced](8e75cecd-504a-82a3-4417-8497241789d9.htm) |  |
| 公共方法 | [Reset](54eb9a9f-057a-c10f-109a-f1ccacc3cfc8.htm) |  |
| 公共方法 | [WaitForDebounce](251949ad-e0dc-3005-5b7f-bb64837915e8.htm) |  |

[Top](#PageHeader)

参见

##### 引用

[SwitchParent 命名空间](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)


### ISwitch_Instr 方法

|  |  |
| --- | --- |
|  | ISwitch\_Instr 方法 |

[ISwitch\_Instr](5cf462be-7211-8684-b1b7-1cb720de4be5.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Connect](21cb47b2-1740-a0a8-9553-0f3e530f35c7.htm) |  |
| 公共方法 | [Disconnect](81263b20-84b0-4be9-3db1-d9d2729f35c4.htm) |  |
| 公共方法 | [DisconnectAllChannel](8e51541a-ba85-1e50-5615-3ed205692802.htm) |  |
| 公共方法 | [GetPathStatus](2aa9a8e5-8a61-f1c5-d72d-04ee882de8f9.htm) |  |
| 公共方法 | [GetRelayStatus](1cb1e3da-bbb9-a772-0cb8-641301a33098.htm) |  |
| 公共方法 | [IsDebounced](8e75cecd-504a-82a3-4417-8497241789d9.htm) |  |
| 公共方法 | [Reset](54eb9a9f-057a-c10f-109a-f1ccacc3cfc8.htm) |  |
| 公共方法 | [WaitForDebounce](251949ad-e0dc-3005-5b7f-bb64837915e8.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[ISwitch\_Instr 接口](5cf462be-7211-8684-b1b7-1cb720de4be5.htm)

[SwitchParent 命名空间](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)


#### Connect 方法

|  |  |
| --- | --- |
|  | ISwitch\_InstrConnect 方法 |

  
**命名空间：** [SwitchParent](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)  
**程序集：** SwitchMeasStation (在 SwitchMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Connect(
	string channel1,
	string channel2
)
```

###### 参数

channel1  String

channel2  String

参见

###### 引用

[ISwitch\_Instr 接口](5cf462be-7211-8684-b1b7-1cb720de4be5.htm)

[SwitchParent 命名空间](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)


#### Disconnect 方法

|  |  |
| --- | --- |
|  | ISwitch\_InstrDisconnect 方法 |

  
**命名空间：** [SwitchParent](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)  
**程序集：** SwitchMeasStation (在 SwitchMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Disconnect(
	string channel1,
	string channel2
)
```

###### 参数

channel1  String

channel2  String

参见

###### 引用

[ISwitch\_Instr 接口](5cf462be-7211-8684-b1b7-1cb720de4be5.htm)

[SwitchParent 命名空间](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)


#### DisconnectAllChannel 方法

|  |  |
| --- | --- |
|  | ISwitch\_InstrDisconnectAllChannel 方法 |

  
**命名空间：** [SwitchParent](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)  
**程序集：** SwitchMeasStation (在 SwitchMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void DisconnectAllChannel()
```

参见

###### 引用

[ISwitch\_Instr 接口](5cf462be-7211-8684-b1b7-1cb720de4be5.htm)

[SwitchParent 命名空间](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)


#### GetPathStatus 方法

|  |  |
| --- | --- |
|  | ISwitch\_InstrGetPathStatus 方法 |

  
**命名空间：** [SwitchParent](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)  
**程序集：** SwitchMeasStation (在 SwitchMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool GetPathStatus(
	string channel1,
	string channel2
)
```

###### 参数

channel1  String

channel2  String

###### 返回值

Boolean

参见

###### 引用

[ISwitch\_Instr 接口](5cf462be-7211-8684-b1b7-1cb720de4be5.htm)

[SwitchParent 命名空间](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)


#### GetRelayStatus 方法

|  |  |
| --- | --- |
|  | ISwitch\_InstrGetRelayStatus 方法 |

  
**命名空间：** [SwitchParent](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)  
**程序集：** SwitchMeasStation (在 SwitchMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetRelayStatus(
	string relayName
)
```

###### 参数

relayName  String

###### 返回值

String

参见

###### 引用

[ISwitch\_Instr 接口](5cf462be-7211-8684-b1b7-1cb720de4be5.htm)

[SwitchParent 命名空间](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)


#### IsDebounced 方法

|  |  |
| --- | --- |
|  | ISwitch\_InstrIsDebounced 方法 |

  
**命名空间：** [SwitchParent](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)  
**程序集：** SwitchMeasStation (在 SwitchMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool IsDebounced()
```

###### 返回值

Boolean

参见

###### 引用

[ISwitch\_Instr 接口](5cf462be-7211-8684-b1b7-1cb720de4be5.htm)

[SwitchParent 命名空间](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)


#### Reset 方法

|  |  |
| --- | --- |
|  | ISwitch\_InstrReset 方法 |

  
**命名空间：** [SwitchParent](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)  
**程序集：** SwitchMeasStation (在 SwitchMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Reset()
```

参见

###### 引用

[ISwitch\_Instr 接口](5cf462be-7211-8684-b1b7-1cb720de4be5.htm)

[SwitchParent 命名空间](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)


#### WaitForDebounce 方法

|  |  |
| --- | --- |
|  | ISwitch\_InstrWaitForDebounce 方法 |

  
**命名空间：** [SwitchParent](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)  
**程序集：** SwitchMeasStation (在 SwitchMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WaitForDebounce(
	double maximumTime
)
```

###### 参数

maximumTime  Double

参见

###### 引用

[ISwitch\_Instr 接口](5cf462be-7211-8684-b1b7-1cb720de4be5.htm)

[SwitchParent 命名空间](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)


## Switch 类

|  |  |
| --- | --- |
|  | Switch 类 |

继承层次

SystemObject
  
  MeasStation  
    SwitchParentSwitch

  
**命名空间：** [SwitchParent](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)  
**程序集：** SwitchMeasStation (在 SwitchMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public class Switch : MeasStation
```

Switch 类型公开以下成员。

构造函数

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Switch](298e5f7a-b180-e716-dcd1-25c9d24c5aae.htm) | 初始化 Switch 类的一个新实例 |

[Top](#PageHeader)

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Connect](11014f7c-91c0-e2b6-c9ad-579550a6f4de.htm) |  |
| 公共方法 | [Disconnect](432a7f44-0b62-f279-99c3-9b52d5e8f8a8.htm) |  |
| 公共方法 | [DisconnectAllChannel](d9d76601-7810-e74e-248f-02a4308722c5.htm) |  |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | [GetPathStatus](0070a98e-44f3-a9ea-6afa-341fb3457f87.htm) |  |
| 公共方法 | [GetRelayStatus](d9071c2b-a781-bc7e-cf27-5e2222206c18.htm) |  |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | [IsDebounced](b723884f-f420-db58-ad2f-a611073be125.htm) |  |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [Reset](19b68608-f2cb-3829-2733-f9699e6535df.htm) | Reset the instrument session. |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |
| 公共方法 | [WaitForDebounce](d9c7a817-1a29-4991-9f7c-63efb0c70cfd.htm) |  |

[Top](#PageHeader)

参见

##### 引用

[SwitchParent 命名空间](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)


### Switch 构造函数

|  |  |
| --- | --- |
|  | Switch 构造函数 |

初始化 [Switch](3690c03c-74e6-7072-c3c7-f9d985b5803a.htm) 类的一个新实例

  
**命名空间：** [SwitchParent](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)  
**程序集：** SwitchMeasStation (在 SwitchMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Switch()
```

参见

###### 引用

[Switch 类](3690c03c-74e6-7072-c3c7-f9d985b5803a.htm)

[SwitchParent 命名空间](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)


### Switch 方法

|  |  |
| --- | --- |
|  | Switch 方法 |

[Switch](3690c03c-74e6-7072-c3c7-f9d985b5803a.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Connect](11014f7c-91c0-e2b6-c9ad-579550a6f4de.htm) |  |
| 公共方法 | [Disconnect](432a7f44-0b62-f279-99c3-9b52d5e8f8a8.htm) |  |
| 公共方法 | [DisconnectAllChannel](d9d76601-7810-e74e-248f-02a4308722c5.htm) |  |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | [GetPathStatus](0070a98e-44f3-a9ea-6afa-341fb3457f87.htm) |  |
| 公共方法 | [GetRelayStatus](d9071c2b-a781-bc7e-cf27-5e2222206c18.htm) |  |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | [IsDebounced](b723884f-f420-db58-ad2f-a611073be125.htm) |  |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [Reset](19b68608-f2cb-3829-2733-f9699e6535df.htm) | Reset the instrument session. |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |
| 公共方法 | [WaitForDebounce](d9c7a817-1a29-4991-9f7c-63efb0c70cfd.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[Switch 类](3690c03c-74e6-7072-c3c7-f9d985b5803a.htm)

[SwitchParent 命名空间](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)


#### Connect 方法

|  |  |
| --- | --- |
|  | SwitchConnect 方法 |

  
**命名空间：** [SwitchParent](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)  
**程序集：** SwitchMeasStation (在 SwitchMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Switch Connect(
	string channel1,
	string channel2
)
```

###### 参数

channel1  String

channel2  String

###### 返回值

[Switch](3690c03c-74e6-7072-c3c7-f9d985b5803a.htm)

参见

###### 引用

[Switch 类](3690c03c-74e6-7072-c3c7-f9d985b5803a.htm)

[SwitchParent 命名空间](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)


#### Disconnect 方法

|  |  |
| --- | --- |
|  | SwitchDisconnect 方法 |

  
**命名空间：** [SwitchParent](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)  
**程序集：** SwitchMeasStation (在 SwitchMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Switch Disconnect(
	string channel1,
	string channel2
)
```

###### 参数

channel1  String

channel2  String

###### 返回值

[Switch](3690c03c-74e6-7072-c3c7-f9d985b5803a.htm)

参见

###### 引用

[Switch 类](3690c03c-74e6-7072-c3c7-f9d985b5803a.htm)

[SwitchParent 命名空间](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)


#### DisconnectAllChannel 方法

|  |  |
| --- | --- |
|  | SwitchDisconnectAllChannel 方法 |

  
**命名空间：** [SwitchParent](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)  
**程序集：** SwitchMeasStation (在 SwitchMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Switch DisconnectAllChannel()
```

###### 返回值

[Switch](3690c03c-74e6-7072-c3c7-f9d985b5803a.htm)

参见

###### 引用

[Switch 类](3690c03c-74e6-7072-c3c7-f9d985b5803a.htm)

[SwitchParent 命名空间](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)


#### GetPathStatus 方法

|  |  |
| --- | --- |
|  | SwitchGetPathStatus 方法 |

  
**命名空间：** [SwitchParent](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)  
**程序集：** SwitchMeasStation (在 SwitchMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> GetPathStatus(
	string channel1,
	string channel2
)
```

###### 参数

channel1  String

channel2  String

###### 返回值

DictionaryString, Boolean

参见

###### 引用

[Switch 类](3690c03c-74e6-7072-c3c7-f9d985b5803a.htm)

[SwitchParent 命名空间](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)


#### GetRelayStatus 方法

|  |  |
| --- | --- |
|  | SwitchGetRelayStatus 方法 |

  
**命名空间：** [SwitchParent](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)  
**程序集：** SwitchMeasStation (在 SwitchMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetRelayStatus(
	string relayName
)
```

###### 参数

relayName  String

###### 返回值

DictionaryString, String

参见

###### 引用

[Switch 类](3690c03c-74e6-7072-c3c7-f9d985b5803a.htm)

[SwitchParent 命名空间](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)


#### IsDebounced 方法

|  |  |
| --- | --- |
|  | SwitchIsDebounced 方法 |

  
**命名空间：** [SwitchParent](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)  
**程序集：** SwitchMeasStation (在 SwitchMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> IsDebounced()
```

###### 返回值

DictionaryString, Boolean

参见

###### 引用

[Switch 类](3690c03c-74e6-7072-c3c7-f9d985b5803a.htm)

[SwitchParent 命名空间](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)


#### Reset 方法

|  |  |
| --- | --- |
|  | SwitchReset 方法 |

Reset the instrument session.

  
**命名空间：** [SwitchParent](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)  
**程序集：** SwitchMeasStation (在 SwitchMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Switch Reset()
```

###### 返回值

[Switch](3690c03c-74e6-7072-c3c7-f9d985b5803a.htm)  
Return Switch instance.

参见

###### 引用

[Switch 类](3690c03c-74e6-7072-c3c7-f9d985b5803a.htm)

[SwitchParent 命名空间](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)


#### WaitForDebounce 方法

|  |  |
| --- | --- |
|  | SwitchWaitForDebounce 方法 |

  
**命名空间：** [SwitchParent](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)  
**程序集：** SwitchMeasStation (在 SwitchMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Switch WaitForDebounce(
	double maximumTime
)
```

###### 参数

maximumTime  Double

###### 返回值

[Switch](3690c03c-74e6-7072-c3c7-f9d985b5803a.htm)

参见

###### 引用

[Switch 类](3690c03c-74e6-7072-c3c7-f9d985b5803a.htm)

[SwitchParent 命名空间](1d3efded-cf59-547d-1c77-3725d7a4bb64.htm)

