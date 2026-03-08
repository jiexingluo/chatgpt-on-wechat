|  |  |
| --- | --- |
|  | VisaParent 命名空间 |

类

|  | 类 | 说明 |
| --- | --- | --- |
| 公共类 | [Visa](b2f57cdd-a54a-e5f4-a0e4-13aa42796180.htm) |  |

接口

|  | 接口 | 说明 |
| --- | --- | --- |
| 公共接口 | [IVisa\_Instr](937e69ab-b6c2-ce19-95a7-ce5849d4d8a4.htm) |  |


## IVisa_Instr 接口

|  |  |
| --- | --- |
|  | IVisa\_Instr 接口 |

  
**命名空间：** [VisaParent](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)  
**程序集：** VisaMeasStation (在 VisaMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public interface IVisa_Instr
```

IVisa\_Instr 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [ReadString](60755350-7acd-18f6-ffa4-02279acb4509.htm) |  |
| 公共方法 | [Reset](1c3d50e9-0e55-2f36-0b86-194c68be2fd9.htm) |  |
| 公共方法 | [WaitUntilDone](838d78ce-3c05-70d0-d1df-73f9946698ce.htm) |  |
| 公共方法 | [WriteString](6fd98120-e538-9c62-2bea-88a9097a4b0b.htm) |  |

[Top](#PageHeader)

参见

##### 引用

[VisaParent 命名空间](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)


### IVisa_Instr 方法

|  |  |
| --- | --- |
|  | IVisa\_Instr 方法 |

[IVisa\_Instr](937e69ab-b6c2-ce19-95a7-ce5849d4d8a4.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [ReadString](60755350-7acd-18f6-ffa4-02279acb4509.htm) |  |
| 公共方法 | [Reset](1c3d50e9-0e55-2f36-0b86-194c68be2fd9.htm) |  |
| 公共方法 | [WaitUntilDone](838d78ce-3c05-70d0-d1df-73f9946698ce.htm) |  |
| 公共方法 | [WriteString](6fd98120-e538-9c62-2bea-88a9097a4b0b.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[IVisa\_Instr 接口](937e69ab-b6c2-ce19-95a7-ce5849d4d8a4.htm)

[VisaParent 命名空间](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)


#### ReadString 方法

|  |  |
| --- | --- |
|  | IVisa\_InstrReadString 方法 |

  
**命名空间：** [VisaParent](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)  
**程序集：** VisaMeasStation (在 VisaMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string ReadString()
```

###### 返回值

String

参见

###### 引用

[IVisa\_Instr 接口](937e69ab-b6c2-ce19-95a7-ce5849d4d8a4.htm)

[VisaParent 命名空间](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)


#### Reset 方法

|  |  |
| --- | --- |
|  | IVisa\_InstrReset 方法 |

  
**命名空间：** [VisaParent](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)  
**程序集：** VisaMeasStation (在 VisaMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Reset()
```

参见

###### 引用

[IVisa\_Instr 接口](937e69ab-b6c2-ce19-95a7-ce5849d4d8a4.htm)

[VisaParent 命名空间](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)


#### WaitUntilDone 方法

|  |  |
| --- | --- |
|  | IVisa\_InstrWaitUntilDone 方法 |

  
**命名空间：** [VisaParent](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)  
**程序集：** VisaMeasStation (在 VisaMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WaitUntilDone()
```

参见

###### 引用

[IVisa\_Instr 接口](937e69ab-b6c2-ce19-95a7-ce5849d4d8a4.htm)

[VisaParent 命名空间](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)


#### WriteString 方法

|  |  |
| --- | --- |
|  | IVisa\_InstrWriteString 方法 |

  
**命名空间：** [VisaParent](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)  
**程序集：** VisaMeasStation (在 VisaMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteString(
	string command
)
```

###### 参数

command  String

参见

###### 引用

[IVisa\_Instr 接口](937e69ab-b6c2-ce19-95a7-ce5849d4d8a4.htm)

[VisaParent 命名空间](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)


## Visa 类

|  |  |
| --- | --- |
|  | Visa 类 |

继承层次

SystemObject
  
  MeasStation  
    VisaParentVisa

  
**命名空间：** [VisaParent](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)  
**程序集：** VisaMeasStation (在 VisaMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public class Visa : MeasStation
```

Visa 类型公开以下成员。

构造函数

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Visa](6964e227-62ec-f0a0-c052-e56e7c59d829.htm) | 初始化 Visa 类的一个新实例 |

[Top](#PageHeader)

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [ReadString](5205a2d1-113a-25c3-f54e-c09fa8ea31e0.htm) |  |
| 公共方法 | [Reset](64797df4-1cde-46c8-2e6f-1c46b8cb62c8.htm) | Reset the instrument session. |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |
| 公共方法 | [WaitUntilDone](c7eb6b1b-26a8-e54f-833e-b3038460645a.htm) |  |
| 公共方法 | [WriteString](1668c304-f2a0-0ab7-d5ce-ab8424344406.htm) |  |

[Top](#PageHeader)

参见

##### 引用

[VisaParent 命名空间](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)


### Visa 构造函数

|  |  |
| --- | --- |
|  | Visa 构造函数 |

初始化 [Visa](b2f57cdd-a54a-e5f4-a0e4-13aa42796180.htm) 类的一个新实例

  
**命名空间：** [VisaParent](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)  
**程序集：** VisaMeasStation (在 VisaMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Visa()
```

参见

###### 引用

[Visa 类](b2f57cdd-a54a-e5f4-a0e4-13aa42796180.htm)

[VisaParent 命名空间](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)


### Visa 方法

|  |  |
| --- | --- |
|  | Visa 方法 |

[Visa](b2f57cdd-a54a-e5f4-a0e4-13aa42796180.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [ReadString](5205a2d1-113a-25c3-f54e-c09fa8ea31e0.htm) |  |
| 公共方法 | [Reset](64797df4-1cde-46c8-2e6f-1c46b8cb62c8.htm) | Reset the instrument session. |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |
| 公共方法 | [WaitUntilDone](c7eb6b1b-26a8-e54f-833e-b3038460645a.htm) |  |
| 公共方法 | [WriteString](1668c304-f2a0-0ab7-d5ce-ab8424344406.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[Visa 类](b2f57cdd-a54a-e5f4-a0e4-13aa42796180.htm)

[VisaParent 命名空间](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)


#### ReadString 方法

|  |  |
| --- | --- |
|  | VisaReadString 方法 |

  
**命名空间：** [VisaParent](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)  
**程序集：** VisaMeasStation (在 VisaMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> ReadString()
```

###### 返回值

DictionaryString, String

参见

###### 引用

[Visa 类](b2f57cdd-a54a-e5f4-a0e4-13aa42796180.htm)

[VisaParent 命名空间](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)


#### Reset 方法

|  |  |
| --- | --- |
|  | VisaReset 方法 |

Reset the instrument session.

  
**命名空间：** [VisaParent](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)  
**程序集：** VisaMeasStation (在 VisaMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Visa Reset()
```

###### 返回值

[Visa](b2f57cdd-a54a-e5f4-a0e4-13aa42796180.htm)  
Return Visa instance.

参见

###### 引用

[Visa 类](b2f57cdd-a54a-e5f4-a0e4-13aa42796180.htm)

[VisaParent 命名空间](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)


#### WaitUntilDone 方法

|  |  |
| --- | --- |
|  | VisaWaitUntilDone 方法 |

  
**命名空间：** [VisaParent](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)  
**程序集：** VisaMeasStation (在 VisaMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Visa WaitUntilDone()
```

###### 返回值

[Visa](b2f57cdd-a54a-e5f4-a0e4-13aa42796180.htm)

参见

###### 引用

[Visa 类](b2f57cdd-a54a-e5f4-a0e4-13aa42796180.htm)

[VisaParent 命名空间](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)


#### WriteString 方法

|  |  |
| --- | --- |
|  | VisaWriteString 方法 |

  
**命名空间：** [VisaParent](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)  
**程序集：** VisaMeasStation (在 VisaMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Visa WriteString(
	string command
)
```

###### 参数

command  String

###### 返回值

[Visa](b2f57cdd-a54a-e5f4-a0e4-13aa42796180.htm)

参见

###### 引用

[Visa 类](b2f57cdd-a54a-e5f4-a0e4-13aa42796180.htm)

[VisaParent 命名空间](4b6d8c15-6a57-4619-4af9-2ad0abb670ae.htm)

