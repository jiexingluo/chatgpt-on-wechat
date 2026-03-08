|  |  |
| --- | --- |
|  | DCVIParent 命名空间 |

类

|  | 类 | 说明 |
| --- | --- | --- |
| 公共类 | [DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm) |  |

接口

|  | 接口 | 说明 |
| --- | --- | --- |
| 公共接口 | [IDCVI\_Instr](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm) |  |


## DCVI 类

|  |  |
| --- | --- |
|  | DCVI 类 |

继承层次

SystemObject
  
  MeasStation  
    DCVIParentDCVI

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public class DCVI : MeasStation
```

DCVI 类型公开以下成员。

构造函数

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [DCVI](40705062-e617-d82f-982a-ed81bd324afc.htm) | 初始化 DCVI 类的一个新实例 |

[Top](#PageHeader)

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Abort](9a8a6b65-3b8e-670a-c30d-cb499ea83493.htm) | Transitions the NI-DCPower session from the Running state to the Committed state. If a sequence is running, then the NI-DCPower session is stopped. |
| 公共方法 | [Commit](dbe6f31b-e5ee-4cca-2c64-13817ac9aa83.htm) | Applies the settings that you configured previously to the device. Calling this method moves the NI-DCPower session from the Uncommitted state into the Committed state. |
| 公共方法 | [ConfigureDigitalEdgeTrigger](a5183ba4-7782-e1dd-364a-8d098fab93a3.htm) | Configure the device to wait for digital edge. |
| 公共方法 | [ConfigureSoftwareTrigger](f162071a-66c2-4c31-fecf-72c379ffc575.htm) | Configure the device to wait for software edge. |
| 公共方法 | [Disable](da087f02-0339-3185-9f73-c3cc58f9ccec.htm) | Places the instrument in a quiescent state as quickly as possible. |
| 公共方法 | [DisableTrigger](c1635d10-426e-1443-1cdc-537b64fa54c0.htm) | Disable the previously configured trigger. |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 公共方法 | [ExportSignal](6fc7dab7-dd2f-3f6e-09f1-db548f4393da.htm) | Routes trigger and event signals to the output terminal you specify. The route is created when the session is committed. |
| 公共方法 | [Fetch](5e80bebd-147b-a36e-e676-9dfb862cc932.htm) | Return fetch result. |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | [GetApertureTime](013a1d90-f898-4478-c6a3-67fc3bc11e34.htm) | Gets the measurement aperture time, in seconds, for the channel configuration. You can specify aperture time units in the ApertureTimeUnits property. |
| 公共方法 | [GetAutoZero](18b09cf5-3b57-d329-b8f2-40c161fa5020.htm) | Gets the auto-zero method to use on the device. |
| 公共方法 | [GetBufferSize](d0e1ded3-56e1-fdae-e8f5-18c3c39a3014.htm) |  |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | [GetIClamp](dd11fbd2-c07b-89f9-aa3d-dea778399738.htm) | Gets the current limit, in amperes, for the output not to exceed when generating the desired voltage level. |
| 公共方法 | [GetIClampAutorange](2e1dd079-77b8-b791-6829-37d243c81339.htm) | Gets whether or not power supply automatically selects the current limit range based on the desired current limit. |
| 公共方法 | [GetIClampHigh](46807b44-0a8e-2120-b998-56eca9c00c92.htm) | Gets the current limit high, in amperes, for the output not to exceed when generating the desired voltage level. |
| 公共方法 | [GetIClampLow](a0ea0938-476c-6ad9-de3d-0358f7c8cbff.htm) | Gets the current limit low, in amperes, for the output not to exceed when generating the desired voltage level. |
| 公共方法 | [GetIClampRange](ae35cb94-3cc8-278e-f500-3b165427b5f0.htm) | Gets the current limit range, in amperes. |
| 公共方法 | [GetILevel](112b9edc-754a-9d0d-6e60-c6400a28e74e.htm) | Gets the current level, in amperes, that the device attempts to generate. |
| 公共方法 | [GetILevelAutorange](19b0c805-5981-0f98-d3f6-9be12f9d5526.htm) | Gets whether to automatically select the current level range based on the desired current level. |
| 公共方法 | [GetILevelRange](5d730cf4-ec67-d285-5fdd-ab4cac1379a1.htm) | Gets the current level range, in amperes. |
| 公共方法 | [GetIsRecordLengthFinite](1a23a318-f1b1-3431-ded4-e8e99653e79e.htm) | Gets a value indicating whether to take continuous measurements. |
| 公共方法 | [GetMeasureDelay](c7794ed4-edcc-3ee5-09d4-0b89cd4717a4.htm) | Gets the amount of time to delay the generation of the MeasureCompleteEvent. |
| 公共方法 | [GetMeasureWhen](8ab0c560-09f7-a37e-f245-4953684cd2f4.htm) | Gets when the measure unit should acquire measurements. |
| 公共方法 | [GetOutputConnected](4f092ffe-bb4c-ece7-955a-d6b122b649d7.htm) | Gets whether the output relay is connected (closed) or disconnected (open). |
| 公共方法 | [GetOutputEnabled](4537913d-3510-a7d8-9793-dbdd3ac02392.htm) | Gets whether the output is enabled. |
| 公共方法 | [GetOutputFunction](34e67b42-cdff-942b-68e4-b54e9592776d.htm) | Gets the output function. |
| 公共方法 | [GetOutputResistance](f0f544be-c3e2-394c-09a4-07485fe522e8.htm) | Gets the output resistance that the device attempts to generate for the specified channel(s). This property is valid only when you set the OutputFunction to DCVoltage. The default value is 0.0. |
| 公共方法 | [GetOvpEnabled](fbc6467b-b4bd-a178-7459-00a2b0ff0e73.htm) | Gets whether the overvoltage protection is enabled. |
| 公共方法 | [GetOvpLimit](4888de33-e0e7-5d78-580e-e18ce96a93e1.htm) | Gets the voltage the power supply allows. The units are Volts. |
| 公共方法 | [GetPulseBiasDelay](e14a21f9-903d-37e4-f3b7-95c79c2b1bd9.htm) | Gets the time, in seconds, when the device generates the PulseCompleteEvent. |
| 公共方法 | [GetPulseBiasIClamp](bdfacad6-38e8-9a11-0e6a-b04aa3b6d188.htm) | Gets the pulse current limit, in amperes, that the output cannot exceed when generating the desired voltage during the off phase of a pulse. |
| 公共方法 | [GetPulseBiasIClampHigh](4be1463b-23c7-8a74-5b9f-54efeb0c70f6.htm) | Gets the pulse current limit high, in amperes, that the output cannot exceed when generating the desired voltage during the off phase of a pulse. |
| 公共方法 | [GetPulseBiasIClampLow](ce732cb3-9d9a-ad93-2d8a-f7710cefbd2a.htm) | Gets the pulse current limit low, in amperes, that the output cannot exceed when generating the desired voltage during the off phase of a pulse. |
| 公共方法 | [GetPulseBiasILevel](95468b41-bb3d-f448-abdf-efa6aeeee905.htm) | Gets the pulse bias current level, in amperes, that the device attempts to generate during the off phase of a pulse. |
| 公共方法 | [GetPulseBiasVClamp](e3f2e017-74a8-b8cc-c1fe-fce0d2768ecf.htm) | Gets the pulse voltage limit, in volts, that the output cannot exceed when generating the desired current during the off phase of a pulse. |
| 公共方法 | [GetPulseBiasVClampHigh](27c5d981-a9e9-8112-6f7f-0373dc09fcdd.htm) | Gets the pulse voltage limit high, in volts, that the output cannot exceed when generating the desired current during the off phase of a pulse. |
| 公共方法 | [GetPulseBiasVClampLow](cc56ca68-0968-710a-9b2c-acb0d082254a.htm) | Gets the pulse voltage limit low, in volts, that the output cannot exceed when generating the desired current during the off phase of a pulse. |
| 公共方法 | [GetPulseBiasVLevel](09c48805-09a7-6350-1804-4b3b31e81f00.htm) | Gets the pulse bias voltage level, in volts, that the device attempts to generate during the off phase of a pulse. |
| 公共方法 | [GetPulseIClamp](9a916937-1132-20d0-adcf-fa94d1c6cf76.htm) | Gets the pulse current limit, in amperes, that the output cannot exceed when generating the desired voltage during the on phase of a pulse. |
| 公共方法 | [GetPulseIClampHigh](58958f27-cb49-8c19-a377-05a2608465d9.htm) | Gets the pulse current limit high, in amperes, that the output cannot exceed when generating the desired voltage during the on phase of a pulse. |
| 公共方法 | [GetPulseIClampLow](a38481db-08da-e5cd-02d0-09acc957157f.htm) | Gets the pulse current limit low, in amperes, that the output cannot exceed when generating the desired voltage during the on phase of a pulse. |
| 公共方法 | [GetPulseIClampRange](4704d19e-3278-249a-ba7d-c81bf5724c48.htm) | Gets the pulse current limit range, in amperes. |
| 公共方法 | [GetPulseILevel](4cc89edb-a248-2eb8-bc3f-03d9b25b46d7.htm) | Gets the pulse current level, in amperes, that the device attempts to generate during the on phase of a pulse. |
| 公共方法 | [GetPulseILevelRange](1f0145d3-0150-56f2-a470-23a9f02cf289.htm) | Gets the pulse current level range, in amperes. |
| 公共方法 | [GetPulseOffTime](81aa8b34-d1bb-3e84-6a10-8e2493dcef4b.htm) | Gets the length, in seconds, of the off phase of a pulse. |
| 公共方法 | [GetPulseOnTime](e8df5bd7-ac25-0ced-a597-db007bcd3860.htm) | Gets the length, in seconds, of the on phase of a pulse. |
| 公共方法 | [GetPulseVClamp](0bb25b01-1475-e761-ed87-767941fcefd1.htm) | Gets the pulse voltage limit, in volts, that the output cannot exceed when generating the desired pulse current during the on phase of a pulse. |
| 公共方法 | [GetPulseVClampHigh](d6a44060-00aa-a0f4-43af-e82a8d339961.htm) | Gets the pulse voltage limit high, in volts, that the output cannot exceed when generating the desired pulse current during the on phase of a pulse. |
| 公共方法 | [GetPulseVClampLow](98795db4-da30-9ee6-baa1-2d24784887e3.htm) | Gets the pulse voltage limit low, in volts, that the output cannot exceed when generating the desired pulse current during the on phase of a pulse. |
| 公共方法 | [GetPulseVClampRange](d88da85c-573f-43d1-f16c-2657d46f0029.htm) | Gets the pulse voltage limit range, in volts. |
| 公共方法 | [GetPulseVLevel](58ef6660-832e-4975-0a0e-eb68443545af.htm) | Gets the pulse voltage level, in volts, that the device attempts to generate during the on phase of a pulse. |
| 公共方法 | [GetPulseVLevelRange](5a2f9297-f975-c6aa-8cfb-17cfdccd6225.htm) | Gets the pulse voltage level range, in volts. |
| 公共方法 | [GetRecordLength](f751d655-abad-9e73-c58f-39530e16c737.htm) | Gets the number of measurements that compose a measure record. If you set this property to a value greater than 1, the MeasurementWhen property must be set to AutomaticallyAfterSourceComplete or OnMeasureTrigger. |
| 公共方法 | [GetSamplesToAverage](39edd145-b855-f131-f410-96d9382c67ec.htm) | Gets the number of samples to average when you take a measurement. Increasing the number of samples to average decreases measurement noise, but increases the time required to take a measurement. |
| 公共方法 | [GetSense](199b4c88-dca2-1b90-f6fb-ee0f9c5e8f9d.htm) | Gets either local or remote sensing of the output voltage for the specified channels. |
| 公共方法 | [GetSequenceLoopCountFinite](cbde9755-e375-de01-ad91-770e0532c1a9.htm) |  |
| 公共方法 | [GetSequenceStepDeltaTime](6a665c84-28b2-fa8b-a4c4-1ac74c42c0e9.htm) |  |
| 公共方法 | [GetSequenceStepDeltaTimeEnabled](e52ccc03-6236-c7a9-4411-474abbba5d3d.htm) |  |
| 公共方法 | [GetSourceDelay](0393d7ec-b156-7d49-23ae-8ff77ad21ee1.htm) | Gets the delay of the device generates the Source Complete event. |
| 公共方法 | [GetSourceMode](4e20a852-3b25-86fc-c9c9-77bb2f6c77e2.htm) | Gets the source mode. |
| 公共方法 | [GetTransientResponse](1ebf2a0b-fbdd-5372-7b01-151bc4ac291b.htm) | Gets the transient response. The default values is "Normal". |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | [GetVClamp](a817a727-f9df-0577-3cf8-d2be26d6bee8.htm) | Gets the voltage limit for the output to not exceed when generating the desired current level. |
| 公共方法 | [GetVClampAutorange](b54169aa-92ed-bedb-e8e5-a05b406cf91e.htm) | Gets whether to automatically select the voltage limit range based on the desired voltage limit. |
| 公共方法 | [GetVClampHigh](c3048cea-3eab-5a60-44ce-ba5dcbc9cd00.htm) | Gets the voltage limit high for the output to not exceed when generating the desired current level. |
| 公共方法 | [GetVClampLow](339be06b-e256-e4f6-ccd2-0f894b1d6850.htm) | Gets the voltage limit low for the output to not exceed when generating the desired current level. |
| 公共方法 | [GetVClampRange](b8172764-eaf6-dfeb-2781-d238eb1c19fd.htm) | Gets the voltage limit range, in volts. |
| 公共方法 | [GetVLevel](84ffed3f-b4f8-6237-e95f-99a71df39874.htm) | Gets the voltage level, in volts. |
| 公共方法 | [GetVLevelAutorange](3e0e61e0-d731-fa9f-d59d-65ae667a272c.htm) | Gets whether or not power supply automatically selects the voltage level range based on the desired voltage level. |
| 公共方法 | [GetVLevelRange](d3e8c911-3584-4fdb-800c-435f26a79611.htm) | Gets the voltage level range, in volts. |
| 公共方法 | [IForce(Double)](d93f1f8a-6bcc-a6be-894c-9a8723191673.htm) | Generates specific current level, other parameters are previous defined values or default values. |
| 公共方法 | [IForce(Double, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, String, String)](66180131-4088-f6ab-676d-d893b53c5b2f.htm) | Generates current with the input parameters.If keep the paremeter null, it will use the previous defined value or default value. |
| 公共方法 | [IForceIMeasure](d372a52d-8709-4fd7-3dfe-4f94e1b0dbd7.htm) | Generates current with the input parameters and returns the measured current.If keep the paremeter null, it will use the previous defined value or default value. |
| 公共方法 | [IForceVMeasure](de0b6869-c2e7-10f8-aa9f-ebd9cdbd6585.htm) | Generates current with the input parameters and returns the measured voltage.If keep the paremeter null, it will use the previous defined value or default value. |
| 公共方法 | [IMeasure](68221846-fb5f-6cf8-a04d-9cb6fd2aa1c4.htm) | Returns the measured current. |
| 公共方法 | [Initiate](f7519b9d-8645-c086-c241-6bdb40ce1d56.htm) | Starts generation or acquisition, causing session to leave the Uncommitted state or Committed state and enter the Running state. |
| 公共方法 | [IPulse](f002da6b-e5e3-88f5-ba02-9fccf877f839.htm) | Generate a single Current pulse. |
| 公共方法 | [IPulseIMeasure](18cab84e-3818-fa00-5754-f40ec7d72506.htm) | Generate a single Current pulse and fetch current. |
| 公共方法 | [IPulseVMeasure](9a7acacf-27e6-6e3e-b35d-63454ca56708.htm) | Generate a single Current pulse and fetch voltage. |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [QueryInCompliance](e65cfee9-f73a-ed2c-152a-c7268194ccb9.htm) | Queries the device to indicate if the output is operating at the compliance limit. |
| 公共方法 | [QueryOutputState](3f7221d1-bc03-94c5-083a-fdad8b02df5f.htm) | Queries the specified output channel to determine if the output channel is currently in the state specified by outputState. |
| 公共方法 | [ReadState](e5c15757-fba4-6ca4-7223-a2f8e5e96d0c.htm) |  |
| 公共方法 | [ReadString](27ff315a-ded0-477a-0d87-e3b578190e08.htm) |  |
| 公共方法 | [Reset](e6a72de9-491a-2ce7-030a-58c556cc7352.htm) | Reset the instrument session |
| 公共方法 | [ResetDevice](d6b5beec-08ca-9df7-272c-75af744d7554.htm) | Performs a hard reset on the device. |
| 公共方法 | [SelfCalibrate](7c995020-f379-1e16-f5a2-f2d3c4bb2812.htm) | Performs a self calibrate on the device. |
| 公共方法 | [SelfTest](464dd1ad-bbb8-7208-6596-713db10e88f5.htm) | Performs a self test on the device. |
| 公共方法 | [SendSoftwareTrigger](798ff9f4-085e-7e27-4511-2aa6b7493f9e.htm) | Sends a Software Edge. |
| 公共方法 | [SetApertureTime](5ec4c760-10ed-d167-ca7d-59418ade4983.htm) | Sets the measurement aperture time, in seconds, for the channel configuration. You can specify aperture time units in the ApertureTimeUnits property. |
| 公共方法 | [SetAutoZero](1acc4838-3e2f-6aa0-dcbe-2a2b8b18fe34.htm) | Sets the auto-zero method to use on the device. |
| 公共方法 | [SetBufferSize](24f5bbe7-a1be-3d8c-dbde-87968e85eab9.htm) |  |
| 公共方法 | [SetIClamp](65edadc6-9a29-8d22-f0a8-b4517cb4361c.htm) | Sets the current limit, in amperes, for the output not to exceed when generating the desired voltage level. |
| 公共方法 | [SetIClampAutorange](44982e38-bc48-74d2-9e4f-8fbb4e28ee0a.htm) | Sets whether or not power supply automatically selects the current limit range based on the desired current limit. |
| 公共方法 | [SetIClampHigh](e5659cf0-0412-f28c-7e04-8e7005fd62e8.htm) | Sets the current limit high, in amperes, for the output not to exceed when generating the desired voltage level. |
| 公共方法 | [SetIClampLow](48d001b8-bbda-f31d-d886-1a3e3d82fd44.htm) | Sets the current limit low, in amperes, for the output not to exceed when generating the desired voltage level. |
| 公共方法 | [SetIClampRange](a83fd102-a48c-d335-ff06-70acafb243b8.htm) | Sets the current limit range, in amperes. |
| 公共方法 | [SetILevel](177b2bce-3e71-e9de-8ff0-2ede2185eb03.htm) | Sets the current level, in amperes, that the device attempts to generate. |
| 公共方法 | [SetILevelAutorange](af0076e4-2b6f-1455-b48c-d8e6de0ca3b8.htm) | Sets whether to automatically select the current level range based on the desired current level. |
| 公共方法 | [SetILevelRange](f7baede4-510e-11dc-192a-88292d3c7675.htm) | Sets the current level range, in amperes. |
| 公共方法 | [SetIsRecordLengthFinite](25b04c6d-c532-ef69-0d1a-30534d44b2ba.htm) | Sets a value indicating whether to take continuous measurements. |
| 公共方法 | [SetMeasureDelay](fbb987f2-9e25-ccc0-3078-4c9b3e65c5fd.htm) | Sets the amount of time to delay the generation of the MeasureCompleteEvent. |
| 公共方法 | [SetMeasureWhen](f2b50f34-c81a-12b5-5d70-9cca300af96e.htm) | Sets when the measure unit should acquire measurements. |
| 公共方法 | [SetOutputConnected](0921433f-42e5-76ec-3483-1dec2fa0196c.htm) | Sets whether the output relay is connected (closed) or disconnected (open). The Enabled property does not change based on this property; they are independent of each other. Set this property to false to disconnect the output terminal from the output. The default value is true. |
| 公共方法 | [SetOutputEnabled](9bb1d364-fa34-1d5e-726a-e0878e7a2341.htm) | Enables or disables the output. |
| 公共方法 | [SetOutputFunction](073f1cb8-f1f7-2c30-447d-81d3b757f85a.htm) | Generate current or voltage on the specified channel(s). |
| 公共方法 | [SetOutputResistance](384363ce-0b24-3dcf-038f-392e88c7ee41.htm) | Sets the output resistance that the device attempts to generate for the specified channel(s). This property is valid only when you set the OutputFunction to DCVoltage. The default value is 0.0. |
| 公共方法 | [SetOvpEnabled](9b26b7df-480a-1010-6320-5f2f1c05a3cb.htm) | Enables or disables overvoltage protection (OVP). |
| 公共方法 | [SetOvpLimit](9663052c-8dd3-0171-5406-1e7995bcd8d6.htm) | Sets the voltage the power supply allows. The units are Volts. |
| 公共方法 | [SetPulseBiasDelay](9ef61738-186a-75e4-6001-6bfce0677c7f.htm) | Sets the time, in seconds, when the device generates the PulseCompleteEvent. |
| 公共方法 | [SetPulseBiasIClamp](e5a11ddc-60ce-7b60-dfff-b7f79b9161b8.htm) | Sets the pulse current limit, in amperes, that the output cannot exceed when generating the desired voltage during the off phase of a pulse. |
| 公共方法 | [SetPulseBiasIClampHigh](d92fc21d-8436-49ab-ba68-fc1569590931.htm) | Sets the pulse current limit high, in amperes, that the output cannot exceed when generating the desired voltage during the off phase of a pulse. |
| 公共方法 | [SetPulseBiasIClampLow](672ea135-5cba-d89b-c559-cbc9056e1d81.htm) | Sets the pulse current limit low, in amperes, that the output cannot exceed when generating the desired voltage during the off phase of a pulse. |
| 公共方法 | [SetPulseBiasILevel](9b18414b-79b3-8556-81b8-b3a8d613ad37.htm) | Sets the pulse bias current level, in amperes, that the device attempts to generate during the off phase of a pulse. |
| 公共方法 | [SetPulseBiasVClamp](d41c7081-8cbe-466f-5632-e95d4f0b8474.htm) | Sets the pulse voltage limit, in volts, that the output cannot exceed when generating the desired current during the off phase of a pulse. |
| 公共方法 | [SetPulseBiasVClampHigh](1ca17942-604c-57d6-75e5-d93249112570.htm) | Sets the pulse voltage limit high, in volts, that the output cannot exceed when generating the desired current during the off phase of a pulse. |
| 公共方法 | [SetPulseBiasVClampLow](672efa5e-9692-6640-5cff-84c6984e01e4.htm) | Sets the pulse voltage limit low, in volts, that the output cannot exceed when generating the desired current during the off phase of a pulse. |
| 公共方法 | [SetPulseBiasVLevel](75dca2db-f376-d3b9-9f0c-7ee45763b043.htm) | Sets the pulse bias voltage level, in volts, that the device attempts to generate during the off phase of a pulse. |
| 公共方法 | [SetPulseIClamp](7799adae-2947-0171-9417-7a77280cf4df.htm) | Sets the pulse current limit, in amperes, that the output cannot exceed when generating the desired voltage during the on phase of a pulse. |
| 公共方法 | [SetPulseIClampHigh](cde9a845-7297-7c81-8a94-41786451f85b.htm) | Sets the pulse current limit high, in amperes, that the output cannot exceed when generating the desired voltage during the on phase of a pulse. |
| 公共方法 | [SetPulseIClampLow](ff47e9e8-4b30-f8f4-3038-16ac4d5d41d7.htm) | Sets the pulse current limit low, in amperes, that the output cannot exceed when generating the desired voltage during the on phase of a pulse. |
| 公共方法 | [SetPulseIClampRange](abab0bb8-720c-ccb8-9ab8-ef1768f3bdc9.htm) | Sets the pulse current limit range, in amperes. |
| 公共方法 | [SetPulseILevel](35d7bea2-c6d9-3ee0-1a00-3e4aed284a3f.htm) | Sets the pulse current level, in amperes, that the device attempts to generate during the on phase of a pulse. |
| 公共方法 | [SetPulseILevelRange](e6612d17-4868-87b8-9269-407406e42b80.htm) | Sets the pulse current level range, in amperes. |
| 公共方法 | [SetPulseOffTime](8b3dfcbb-fb64-7361-00fa-0682d7639de4.htm) | Sets the length, in seconds, of the off phase of a pulse. |
| 公共方法 | [SetPulseOnTime](56324ef4-5e25-0fbf-a2ce-5587c3322199.htm) | Sets the length, in seconds, of the on phase of a pulse. |
| 公共方法 | [SetPulseVClamp](412b7ce7-4650-da3f-6361-74814aa70532.htm) | Sets the pulse voltage limit, in volts, that the output cannot exceed when generating the desired pulse current during the on phase of a pulse. |
| 公共方法 | [SetPulseVClampHigh](dd6c3ae2-c14f-bdd1-50b7-2da528d484d7.htm) | Sets the pulse voltage limit high, in volts, that the output cannot exceed when generating the desired pulse current during the on phase of a pulse. |
| 公共方法 | [SetPulseVClampLow](31f10e48-c5d6-f83d-1709-250d1bd3ab7c.htm) | Sets the pulse voltage limit low, in volts, that the output cannot exceed when generating the desired pulse current during the on phase of a pulse. |
| 公共方法 | [SetPulseVClampRange](7164e5a1-0534-536c-25e4-e8930f1e84e6.htm) | Sets the pulse voltage limit range, in volts. |
| 公共方法 | [SetPulseVLevel](21aa16b8-c241-c34e-e2ae-71b76134d9bb.htm) | Sets the pulse voltage level, in volts, that the device attempts to generate during the on phase of a pulse. |
| 公共方法 | [SetPulseVLevelRange](124dc9b1-ddd6-afef-352a-04f0ed0063a7.htm) | Sets the pulse voltage level range, in volts. |
| 公共方法 | [SetRecordLength](bf045c08-6980-b826-fd48-934929d0c805.htm) | Sets the number of measurements that compose a measure record. If you set this property to a value greater than 1, the MeasurementWhen property must be set to AutomaticallyAfterSourceComplete or OnMeasureTrigger. |
| 公共方法 | [SetSamplesToAverage](5dfc2d82-b935-9775-da03-e59874e913d7.htm) | Sets the number of samples to average when you take a measurement. Increasing the number of samples to average decreases measurement noise, but increases the time required to take a measurement. |
| 公共方法 | [SetSense](b49560d7-1bdd-7d64-66a5-4e1da5b3278f.htm) | Sets either local or remote sensing of the output voltage for the specified channels. |
| 公共方法 | [SetSequence(Double)](2d2ca427-1593-5820-8f2d-63d47305515a.htm) | Configures a series of voltage or current outputs and corresponding source delays. The source mode must be set to Sequence for this method to take effect. |
| 公共方法 | [SetSequence(Double, Double)](f45c2dea-e4bc-3a06-127a-29b1776e0f87.htm) | Configures a series of voltage or current outputs and corresponding source delays. |
| 公共方法 | [SetSequenceLoopCountFinite](b01ec5ce-f0ec-6778-5676-20098328f2bd.htm) |  |
| 公共方法 | [SetSequenceStepDeltaTime](ca54f912-9d60-f99d-9da4-6b46e6c45531.htm) |  |
| 公共方法 | [SetSequenceStepDeltaTimeEnabled](bc88d4cc-419f-f951-1049-9621a5fbf264.htm) |  |
| 公共方法 | [SetSourceDelay](3bd08fdc-d3eb-bf35-8e68-0930e66e34c6.htm) | Determines when, in seconds, the device generates the Source Complete event, potentially starting a measurement if the MeasureWhen attribute is set to AutomaticallyAfterSourceComplete. |
| 公共方法 | [SetSourceMode](773da792-2324-0a58-8ede-c421ade2440f.htm) | Sets whether to run a single output point or a sequence. |
| 公共方法 | [SetTransientResponse](9b9ce0e4-5687-4ac1-988c-13b475803bc1.htm) | Sets the transient response. The default values is "Normal". |
| 公共方法 | [SetVClamp](bc7786cd-1d27-2ccb-5701-764ad8fa680d.htm) | Sets the voltage limit for the output to not exceed when generating the desired current level. |
| 公共方法 | [SetVClampAutorange](ab839237-b582-e9f0-956c-654edf6e7964.htm) | Sets whether to automatically select the voltage limit range based on the desired voltage limit. |
| 公共方法 | [SetVClampHigh](eeb56288-7369-8692-fa68-0bff6768e60e.htm) | Sets the voltage limit high for the output to not exceed when generating the desired current level. |
| 公共方法 | [SetVClampLow](d3cb1ab1-2392-dc97-9b43-7b9b6568ecf6.htm) | Sets the voltage limit low for the output to not exceed when generating the desired current level. |
| 公共方法 | [SetVClampRange](622eabb4-e4a4-51e5-7877-0e5ff7d93f73.htm) | Sets the voltage limit range, in volts. |
| 公共方法 | [SetVLevel](2cb05592-180a-61a6-ac91-b60ce8f8ef0a.htm) | Sets the voltage level, in volts. |
| 公共方法 | [SetVLevelAutorange](beaa8933-66fa-1aae-89db-0b730fdb51fe.htm) | Sets whether or not power supply automatically selects the voltage level range based on the desired voltage level. |
| 公共方法 | [SetVLevelRange](ad124591-8c52-5455-d6ce-8c6c0a057de0.htm) | Sets the voltage level range, in volts. |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |
| 公共方法 | [VForce(Double)](d86c9067-4c5a-c264-3a56-43f7ea88227a.htm) | Generates specific voltage level, other parameters are previous defined values or default values. |
| 公共方法 | [VForce(Double, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, String, String)](a2f3776b-8765-90a4-2808-bd63b8441fce.htm) | Generates voltage with the input parameters.If keep the paremeter null, it will use the previous defined value or default value. |
| 公共方法 | [VForceIMeasure](9c699458-0866-6298-237c-c167342100bc.htm) | Generates voltage with the input parameters and returns the measured current.If keep the paremeter null, it will use the previous defined value or default value. |
| 公共方法 | [VForceVMeasure](cb6e368f-a536-59ce-1656-0fcb2b68d486.htm) | Generates voltage with the input parameters and returns the measured voltage.If keep the paremeter null, it will use the previous defined value or default value. |
| 公共方法 | [VIMeasure2](d9abd6f9-9e6a-d683-5be8-74f596b6d1fe.htm) |  |
| 公共方法 | [VMeasure](141b5109-b018-1300-eb63-966a5607b86e.htm) | Returns the measured voltage. |
| 公共方法 | [VPulse](0eddec77-93e5-0b1b-a3b3-3c8175c55493.htm) | Generate a single Voltage pulse. |
| 公共方法 | [VPulseIMeasure](4250ff13-7359-4190-cefc-8e364f8c5e94.htm) | Generate a single Voltage pulse and fetch current. |
| 公共方法 | [VPulseVMeasure](3b00483b-a149-8978-630d-cfbddb8ed2db.htm) | Generate a single Voltage pulse and fetch voltage. |
| 公共方法 | [WaitForEvent](26cc1a09-b69b-f340-d085-0a95ef8b7e45.htm) | Waits until the device has generated the specified event. |
| 公共方法 | [WriteString](13614734-c317-2b92-0c5b-ab1e6376ac8f.htm) |  |

[Top](#PageHeader)

参见

##### 引用

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


### DCVI 构造函数

|  |  |
| --- | --- |
|  | DCVI 构造函数 |

初始化 [DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm) 类的一个新实例

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI()
```

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


### DCVI 方法

|  |  |
| --- | --- |
|  | DCVI 方法 |

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Abort](9a8a6b65-3b8e-670a-c30d-cb499ea83493.htm) | Transitions the NI-DCPower session from the Running state to the Committed state. If a sequence is running, then the NI-DCPower session is stopped. |
| 公共方法 | [Commit](dbe6f31b-e5ee-4cca-2c64-13817ac9aa83.htm) | Applies the settings that you configured previously to the device. Calling this method moves the NI-DCPower session from the Uncommitted state into the Committed state. |
| 公共方法 | [ConfigureDigitalEdgeTrigger](a5183ba4-7782-e1dd-364a-8d098fab93a3.htm) | Configure the device to wait for digital edge. |
| 公共方法 | [ConfigureSoftwareTrigger](f162071a-66c2-4c31-fecf-72c379ffc575.htm) | Configure the device to wait for software edge. |
| 公共方法 | [Disable](da087f02-0339-3185-9f73-c3cc58f9ccec.htm) | Places the instrument in a quiescent state as quickly as possible. |
| 公共方法 | [DisableTrigger](c1635d10-426e-1443-1cdc-537b64fa54c0.htm) | Disable the previously configured trigger. |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 公共方法 | [ExportSignal](6fc7dab7-dd2f-3f6e-09f1-db548f4393da.htm) | Routes trigger and event signals to the output terminal you specify. The route is created when the session is committed. |
| 公共方法 | [Fetch](5e80bebd-147b-a36e-e676-9dfb862cc932.htm) | Return fetch result. |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | [GetApertureTime](013a1d90-f898-4478-c6a3-67fc3bc11e34.htm) | Gets the measurement aperture time, in seconds, for the channel configuration. You can specify aperture time units in the ApertureTimeUnits property. |
| 公共方法 | [GetAutoZero](18b09cf5-3b57-d329-b8f2-40c161fa5020.htm) | Gets the auto-zero method to use on the device. |
| 公共方法 | [GetBufferSize](d0e1ded3-56e1-fdae-e8f5-18c3c39a3014.htm) |  |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | [GetIClamp](dd11fbd2-c07b-89f9-aa3d-dea778399738.htm) | Gets the current limit, in amperes, for the output not to exceed when generating the desired voltage level. |
| 公共方法 | [GetIClampAutorange](2e1dd079-77b8-b791-6829-37d243c81339.htm) | Gets whether or not power supply automatically selects the current limit range based on the desired current limit. |
| 公共方法 | [GetIClampHigh](46807b44-0a8e-2120-b998-56eca9c00c92.htm) | Gets the current limit high, in amperes, for the output not to exceed when generating the desired voltage level. |
| 公共方法 | [GetIClampLow](a0ea0938-476c-6ad9-de3d-0358f7c8cbff.htm) | Gets the current limit low, in amperes, for the output not to exceed when generating the desired voltage level. |
| 公共方法 | [GetIClampRange](ae35cb94-3cc8-278e-f500-3b165427b5f0.htm) | Gets the current limit range, in amperes. |
| 公共方法 | [GetILevel](112b9edc-754a-9d0d-6e60-c6400a28e74e.htm) | Gets the current level, in amperes, that the device attempts to generate. |
| 公共方法 | [GetILevelAutorange](19b0c805-5981-0f98-d3f6-9be12f9d5526.htm) | Gets whether to automatically select the current level range based on the desired current level. |
| 公共方法 | [GetILevelRange](5d730cf4-ec67-d285-5fdd-ab4cac1379a1.htm) | Gets the current level range, in amperes. |
| 公共方法 | [GetIsRecordLengthFinite](1a23a318-f1b1-3431-ded4-e8e99653e79e.htm) | Gets a value indicating whether to take continuous measurements. |
| 公共方法 | [GetMeasureDelay](c7794ed4-edcc-3ee5-09d4-0b89cd4717a4.htm) | Gets the amount of time to delay the generation of the MeasureCompleteEvent. |
| 公共方法 | [GetMeasureWhen](8ab0c560-09f7-a37e-f245-4953684cd2f4.htm) | Gets when the measure unit should acquire measurements. |
| 公共方法 | [GetOutputConnected](4f092ffe-bb4c-ece7-955a-d6b122b649d7.htm) | Gets whether the output relay is connected (closed) or disconnected (open). |
| 公共方法 | [GetOutputEnabled](4537913d-3510-a7d8-9793-dbdd3ac02392.htm) | Gets whether the output is enabled. |
| 公共方法 | [GetOutputFunction](34e67b42-cdff-942b-68e4-b54e9592776d.htm) | Gets the output function. |
| 公共方法 | [GetOutputResistance](f0f544be-c3e2-394c-09a4-07485fe522e8.htm) | Gets the output resistance that the device attempts to generate for the specified channel(s). This property is valid only when you set the OutputFunction to DCVoltage. The default value is 0.0. |
| 公共方法 | [GetOvpEnabled](fbc6467b-b4bd-a178-7459-00a2b0ff0e73.htm) | Gets whether the overvoltage protection is enabled. |
| 公共方法 | [GetOvpLimit](4888de33-e0e7-5d78-580e-e18ce96a93e1.htm) | Gets the voltage the power supply allows. The units are Volts. |
| 公共方法 | [GetPulseBiasDelay](e14a21f9-903d-37e4-f3b7-95c79c2b1bd9.htm) | Gets the time, in seconds, when the device generates the PulseCompleteEvent. |
| 公共方法 | [GetPulseBiasIClamp](bdfacad6-38e8-9a11-0e6a-b04aa3b6d188.htm) | Gets the pulse current limit, in amperes, that the output cannot exceed when generating the desired voltage during the off phase of a pulse. |
| 公共方法 | [GetPulseBiasIClampHigh](4be1463b-23c7-8a74-5b9f-54efeb0c70f6.htm) | Gets the pulse current limit high, in amperes, that the output cannot exceed when generating the desired voltage during the off phase of a pulse. |
| 公共方法 | [GetPulseBiasIClampLow](ce732cb3-9d9a-ad93-2d8a-f7710cefbd2a.htm) | Gets the pulse current limit low, in amperes, that the output cannot exceed when generating the desired voltage during the off phase of a pulse. |
| 公共方法 | [GetPulseBiasILevel](95468b41-bb3d-f448-abdf-efa6aeeee905.htm) | Gets the pulse bias current level, in amperes, that the device attempts to generate during the off phase of a pulse. |
| 公共方法 | [GetPulseBiasVClamp](e3f2e017-74a8-b8cc-c1fe-fce0d2768ecf.htm) | Gets the pulse voltage limit, in volts, that the output cannot exceed when generating the desired current during the off phase of a pulse. |
| 公共方法 | [GetPulseBiasVClampHigh](27c5d981-a9e9-8112-6f7f-0373dc09fcdd.htm) | Gets the pulse voltage limit high, in volts, that the output cannot exceed when generating the desired current during the off phase of a pulse. |
| 公共方法 | [GetPulseBiasVClampLow](cc56ca68-0968-710a-9b2c-acb0d082254a.htm) | Gets the pulse voltage limit low, in volts, that the output cannot exceed when generating the desired current during the off phase of a pulse. |
| 公共方法 | [GetPulseBiasVLevel](09c48805-09a7-6350-1804-4b3b31e81f00.htm) | Gets the pulse bias voltage level, in volts, that the device attempts to generate during the off phase of a pulse. |
| 公共方法 | [GetPulseIClamp](9a916937-1132-20d0-adcf-fa94d1c6cf76.htm) | Gets the pulse current limit, in amperes, that the output cannot exceed when generating the desired voltage during the on phase of a pulse. |
| 公共方法 | [GetPulseIClampHigh](58958f27-cb49-8c19-a377-05a2608465d9.htm) | Gets the pulse current limit high, in amperes, that the output cannot exceed when generating the desired voltage during the on phase of a pulse. |
| 公共方法 | [GetPulseIClampLow](a38481db-08da-e5cd-02d0-09acc957157f.htm) | Gets the pulse current limit low, in amperes, that the output cannot exceed when generating the desired voltage during the on phase of a pulse. |
| 公共方法 | [GetPulseIClampRange](4704d19e-3278-249a-ba7d-c81bf5724c48.htm) | Gets the pulse current limit range, in amperes. |
| 公共方法 | [GetPulseILevel](4cc89edb-a248-2eb8-bc3f-03d9b25b46d7.htm) | Gets the pulse current level, in amperes, that the device attempts to generate during the on phase of a pulse. |
| 公共方法 | [GetPulseILevelRange](1f0145d3-0150-56f2-a470-23a9f02cf289.htm) | Gets the pulse current level range, in amperes. |
| 公共方法 | [GetPulseOffTime](81aa8b34-d1bb-3e84-6a10-8e2493dcef4b.htm) | Gets the length, in seconds, of the off phase of a pulse. |
| 公共方法 | [GetPulseOnTime](e8df5bd7-ac25-0ced-a597-db007bcd3860.htm) | Gets the length, in seconds, of the on phase of a pulse. |
| 公共方法 | [GetPulseVClamp](0bb25b01-1475-e761-ed87-767941fcefd1.htm) | Gets the pulse voltage limit, in volts, that the output cannot exceed when generating the desired pulse current during the on phase of a pulse. |
| 公共方法 | [GetPulseVClampHigh](d6a44060-00aa-a0f4-43af-e82a8d339961.htm) | Gets the pulse voltage limit high, in volts, that the output cannot exceed when generating the desired pulse current during the on phase of a pulse. |
| 公共方法 | [GetPulseVClampLow](98795db4-da30-9ee6-baa1-2d24784887e3.htm) | Gets the pulse voltage limit low, in volts, that the output cannot exceed when generating the desired pulse current during the on phase of a pulse. |
| 公共方法 | [GetPulseVClampRange](d88da85c-573f-43d1-f16c-2657d46f0029.htm) | Gets the pulse voltage limit range, in volts. |
| 公共方法 | [GetPulseVLevel](58ef6660-832e-4975-0a0e-eb68443545af.htm) | Gets the pulse voltage level, in volts, that the device attempts to generate during the on phase of a pulse. |
| 公共方法 | [GetPulseVLevelRange](5a2f9297-f975-c6aa-8cfb-17cfdccd6225.htm) | Gets the pulse voltage level range, in volts. |
| 公共方法 | [GetRecordLength](f751d655-abad-9e73-c58f-39530e16c737.htm) | Gets the number of measurements that compose a measure record. If you set this property to a value greater than 1, the MeasurementWhen property must be set to AutomaticallyAfterSourceComplete or OnMeasureTrigger. |
| 公共方法 | [GetSamplesToAverage](39edd145-b855-f131-f410-96d9382c67ec.htm) | Gets the number of samples to average when you take a measurement. Increasing the number of samples to average decreases measurement noise, but increases the time required to take a measurement. |
| 公共方法 | [GetSense](199b4c88-dca2-1b90-f6fb-ee0f9c5e8f9d.htm) | Gets either local or remote sensing of the output voltage for the specified channels. |
| 公共方法 | [GetSequenceLoopCountFinite](cbde9755-e375-de01-ad91-770e0532c1a9.htm) |  |
| 公共方法 | [GetSequenceStepDeltaTime](6a665c84-28b2-fa8b-a4c4-1ac74c42c0e9.htm) |  |
| 公共方法 | [GetSequenceStepDeltaTimeEnabled](e52ccc03-6236-c7a9-4411-474abbba5d3d.htm) |  |
| 公共方法 | [GetSourceDelay](0393d7ec-b156-7d49-23ae-8ff77ad21ee1.htm) | Gets the delay of the device generates the Source Complete event. |
| 公共方法 | [GetSourceMode](4e20a852-3b25-86fc-c9c9-77bb2f6c77e2.htm) | Gets the source mode. |
| 公共方法 | [GetTransientResponse](1ebf2a0b-fbdd-5372-7b01-151bc4ac291b.htm) | Gets the transient response. The default values is "Normal". |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | [GetVClamp](a817a727-f9df-0577-3cf8-d2be26d6bee8.htm) | Gets the voltage limit for the output to not exceed when generating the desired current level. |
| 公共方法 | [GetVClampAutorange](b54169aa-92ed-bedb-e8e5-a05b406cf91e.htm) | Gets whether to automatically select the voltage limit range based on the desired voltage limit. |
| 公共方法 | [GetVClampHigh](c3048cea-3eab-5a60-44ce-ba5dcbc9cd00.htm) | Gets the voltage limit high for the output to not exceed when generating the desired current level. |
| 公共方法 | [GetVClampLow](339be06b-e256-e4f6-ccd2-0f894b1d6850.htm) | Gets the voltage limit low for the output to not exceed when generating the desired current level. |
| 公共方法 | [GetVClampRange](b8172764-eaf6-dfeb-2781-d238eb1c19fd.htm) | Gets the voltage limit range, in volts. |
| 公共方法 | [GetVLevel](84ffed3f-b4f8-6237-e95f-99a71df39874.htm) | Gets the voltage level, in volts. |
| 公共方法 | [GetVLevelAutorange](3e0e61e0-d731-fa9f-d59d-65ae667a272c.htm) | Gets whether or not power supply automatically selects the voltage level range based on the desired voltage level. |
| 公共方法 | [GetVLevelRange](d3e8c911-3584-4fdb-800c-435f26a79611.htm) | Gets the voltage level range, in volts. |
| 公共方法 | [IForce(Double)](d93f1f8a-6bcc-a6be-894c-9a8723191673.htm) | Generates specific current level, other parameters are previous defined values or default values. |
| 公共方法 | [IForce(Double, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, String, String)](66180131-4088-f6ab-676d-d893b53c5b2f.htm) | Generates current with the input parameters.If keep the paremeter null, it will use the previous defined value or default value. |
| 公共方法 | [IForceIMeasure](d372a52d-8709-4fd7-3dfe-4f94e1b0dbd7.htm) | Generates current with the input parameters and returns the measured current.If keep the paremeter null, it will use the previous defined value or default value. |
| 公共方法 | [IForceVMeasure](de0b6869-c2e7-10f8-aa9f-ebd9cdbd6585.htm) | Generates current with the input parameters and returns the measured voltage.If keep the paremeter null, it will use the previous defined value or default value. |
| 公共方法 | [IMeasure](68221846-fb5f-6cf8-a04d-9cb6fd2aa1c4.htm) | Returns the measured current. |
| 公共方法 | [Initiate](f7519b9d-8645-c086-c241-6bdb40ce1d56.htm) | Starts generation or acquisition, causing session to leave the Uncommitted state or Committed state and enter the Running state. |
| 公共方法 | [IPulse](f002da6b-e5e3-88f5-ba02-9fccf877f839.htm) | Generate a single Current pulse. |
| 公共方法 | [IPulseIMeasure](18cab84e-3818-fa00-5754-f40ec7d72506.htm) | Generate a single Current pulse and fetch current. |
| 公共方法 | [IPulseVMeasure](9a7acacf-27e6-6e3e-b35d-63454ca56708.htm) | Generate a single Current pulse and fetch voltage. |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [QueryInCompliance](e65cfee9-f73a-ed2c-152a-c7268194ccb9.htm) | Queries the device to indicate if the output is operating at the compliance limit. |
| 公共方法 | [QueryOutputState](3f7221d1-bc03-94c5-083a-fdad8b02df5f.htm) | Queries the specified output channel to determine if the output channel is currently in the state specified by outputState. |
| 公共方法 | [ReadState](e5c15757-fba4-6ca4-7223-a2f8e5e96d0c.htm) |  |
| 公共方法 | [ReadString](27ff315a-ded0-477a-0d87-e3b578190e08.htm) |  |
| 公共方法 | [Reset](e6a72de9-491a-2ce7-030a-58c556cc7352.htm) | Reset the instrument session |
| 公共方法 | [ResetDevice](d6b5beec-08ca-9df7-272c-75af744d7554.htm) | Performs a hard reset on the device. |
| 公共方法 | [SelfCalibrate](7c995020-f379-1e16-f5a2-f2d3c4bb2812.htm) | Performs a self calibrate on the device. |
| 公共方法 | [SelfTest](464dd1ad-bbb8-7208-6596-713db10e88f5.htm) | Performs a self test on the device. |
| 公共方法 | [SendSoftwareTrigger](798ff9f4-085e-7e27-4511-2aa6b7493f9e.htm) | Sends a Software Edge. |
| 公共方法 | [SetApertureTime](5ec4c760-10ed-d167-ca7d-59418ade4983.htm) | Sets the measurement aperture time, in seconds, for the channel configuration. You can specify aperture time units in the ApertureTimeUnits property. |
| 公共方法 | [SetAutoZero](1acc4838-3e2f-6aa0-dcbe-2a2b8b18fe34.htm) | Sets the auto-zero method to use on the device. |
| 公共方法 | [SetBufferSize](24f5bbe7-a1be-3d8c-dbde-87968e85eab9.htm) |  |
| 公共方法 | [SetIClamp](65edadc6-9a29-8d22-f0a8-b4517cb4361c.htm) | Sets the current limit, in amperes, for the output not to exceed when generating the desired voltage level. |
| 公共方法 | [SetIClampAutorange](44982e38-bc48-74d2-9e4f-8fbb4e28ee0a.htm) | Sets whether or not power supply automatically selects the current limit range based on the desired current limit. |
| 公共方法 | [SetIClampHigh](e5659cf0-0412-f28c-7e04-8e7005fd62e8.htm) | Sets the current limit high, in amperes, for the output not to exceed when generating the desired voltage level. |
| 公共方法 | [SetIClampLow](48d001b8-bbda-f31d-d886-1a3e3d82fd44.htm) | Sets the current limit low, in amperes, for the output not to exceed when generating the desired voltage level. |
| 公共方法 | [SetIClampRange](a83fd102-a48c-d335-ff06-70acafb243b8.htm) | Sets the current limit range, in amperes. |
| 公共方法 | [SetILevel](177b2bce-3e71-e9de-8ff0-2ede2185eb03.htm) | Sets the current level, in amperes, that the device attempts to generate. |
| 公共方法 | [SetILevelAutorange](af0076e4-2b6f-1455-b48c-d8e6de0ca3b8.htm) | Sets whether to automatically select the current level range based on the desired current level. |
| 公共方法 | [SetILevelRange](f7baede4-510e-11dc-192a-88292d3c7675.htm) | Sets the current level range, in amperes. |
| 公共方法 | [SetIsRecordLengthFinite](25b04c6d-c532-ef69-0d1a-30534d44b2ba.htm) | Sets a value indicating whether to take continuous measurements. |
| 公共方法 | [SetMeasureDelay](fbb987f2-9e25-ccc0-3078-4c9b3e65c5fd.htm) | Sets the amount of time to delay the generation of the MeasureCompleteEvent. |
| 公共方法 | [SetMeasureWhen](f2b50f34-c81a-12b5-5d70-9cca300af96e.htm) | Sets when the measure unit should acquire measurements. |
| 公共方法 | [SetOutputConnected](0921433f-42e5-76ec-3483-1dec2fa0196c.htm) | Sets whether the output relay is connected (closed) or disconnected (open). The Enabled property does not change based on this property; they are independent of each other. Set this property to false to disconnect the output terminal from the output. The default value is true. |
| 公共方法 | [SetOutputEnabled](9bb1d364-fa34-1d5e-726a-e0878e7a2341.htm) | Enables or disables the output. |
| 公共方法 | [SetOutputFunction](073f1cb8-f1f7-2c30-447d-81d3b757f85a.htm) | Generate current or voltage on the specified channel(s). |
| 公共方法 | [SetOutputResistance](384363ce-0b24-3dcf-038f-392e88c7ee41.htm) | Sets the output resistance that the device attempts to generate for the specified channel(s). This property is valid only when you set the OutputFunction to DCVoltage. The default value is 0.0. |
| 公共方法 | [SetOvpEnabled](9b26b7df-480a-1010-6320-5f2f1c05a3cb.htm) | Enables or disables overvoltage protection (OVP). |
| 公共方法 | [SetOvpLimit](9663052c-8dd3-0171-5406-1e7995bcd8d6.htm) | Sets the voltage the power supply allows. The units are Volts. |
| 公共方法 | [SetPulseBiasDelay](9ef61738-186a-75e4-6001-6bfce0677c7f.htm) | Sets the time, in seconds, when the device generates the PulseCompleteEvent. |
| 公共方法 | [SetPulseBiasIClamp](e5a11ddc-60ce-7b60-dfff-b7f79b9161b8.htm) | Sets the pulse current limit, in amperes, that the output cannot exceed when generating the desired voltage during the off phase of a pulse. |
| 公共方法 | [SetPulseBiasIClampHigh](d92fc21d-8436-49ab-ba68-fc1569590931.htm) | Sets the pulse current limit high, in amperes, that the output cannot exceed when generating the desired voltage during the off phase of a pulse. |
| 公共方法 | [SetPulseBiasIClampLow](672ea135-5cba-d89b-c559-cbc9056e1d81.htm) | Sets the pulse current limit low, in amperes, that the output cannot exceed when generating the desired voltage during the off phase of a pulse. |
| 公共方法 | [SetPulseBiasILevel](9b18414b-79b3-8556-81b8-b3a8d613ad37.htm) | Sets the pulse bias current level, in amperes, that the device attempts to generate during the off phase of a pulse. |
| 公共方法 | [SetPulseBiasVClamp](d41c7081-8cbe-466f-5632-e95d4f0b8474.htm) | Sets the pulse voltage limit, in volts, that the output cannot exceed when generating the desired current during the off phase of a pulse. |
| 公共方法 | [SetPulseBiasVClampHigh](1ca17942-604c-57d6-75e5-d93249112570.htm) | Sets the pulse voltage limit high, in volts, that the output cannot exceed when generating the desired current during the off phase of a pulse. |
| 公共方法 | [SetPulseBiasVClampLow](672efa5e-9692-6640-5cff-84c6984e01e4.htm) | Sets the pulse voltage limit low, in volts, that the output cannot exceed when generating the desired current during the off phase of a pulse. |
| 公共方法 | [SetPulseBiasVLevel](75dca2db-f376-d3b9-9f0c-7ee45763b043.htm) | Sets the pulse bias voltage level, in volts, that the device attempts to generate during the off phase of a pulse. |
| 公共方法 | [SetPulseIClamp](7799adae-2947-0171-9417-7a77280cf4df.htm) | Sets the pulse current limit, in amperes, that the output cannot exceed when generating the desired voltage during the on phase of a pulse. |
| 公共方法 | [SetPulseIClampHigh](cde9a845-7297-7c81-8a94-41786451f85b.htm) | Sets the pulse current limit high, in amperes, that the output cannot exceed when generating the desired voltage during the on phase of a pulse. |
| 公共方法 | [SetPulseIClampLow](ff47e9e8-4b30-f8f4-3038-16ac4d5d41d7.htm) | Sets the pulse current limit low, in amperes, that the output cannot exceed when generating the desired voltage during the on phase of a pulse. |
| 公共方法 | [SetPulseIClampRange](abab0bb8-720c-ccb8-9ab8-ef1768f3bdc9.htm) | Sets the pulse current limit range, in amperes. |
| 公共方法 | [SetPulseILevel](35d7bea2-c6d9-3ee0-1a00-3e4aed284a3f.htm) | Sets the pulse current level, in amperes, that the device attempts to generate during the on phase of a pulse. |
| 公共方法 | [SetPulseILevelRange](e6612d17-4868-87b8-9269-407406e42b80.htm) | Sets the pulse current level range, in amperes. |
| 公共方法 | [SetPulseOffTime](8b3dfcbb-fb64-7361-00fa-0682d7639de4.htm) | Sets the length, in seconds, of the off phase of a pulse. |
| 公共方法 | [SetPulseOnTime](56324ef4-5e25-0fbf-a2ce-5587c3322199.htm) | Sets the length, in seconds, of the on phase of a pulse. |
| 公共方法 | [SetPulseVClamp](412b7ce7-4650-da3f-6361-74814aa70532.htm) | Sets the pulse voltage limit, in volts, that the output cannot exceed when generating the desired pulse current during the on phase of a pulse. |
| 公共方法 | [SetPulseVClampHigh](dd6c3ae2-c14f-bdd1-50b7-2da528d484d7.htm) | Sets the pulse voltage limit high, in volts, that the output cannot exceed when generating the desired pulse current during the on phase of a pulse. |
| 公共方法 | [SetPulseVClampLow](31f10e48-c5d6-f83d-1709-250d1bd3ab7c.htm) | Sets the pulse voltage limit low, in volts, that the output cannot exceed when generating the desired pulse current during the on phase of a pulse. |
| 公共方法 | [SetPulseVClampRange](7164e5a1-0534-536c-25e4-e8930f1e84e6.htm) | Sets the pulse voltage limit range, in volts. |
| 公共方法 | [SetPulseVLevel](21aa16b8-c241-c34e-e2ae-71b76134d9bb.htm) | Sets the pulse voltage level, in volts, that the device attempts to generate during the on phase of a pulse. |
| 公共方法 | [SetPulseVLevelRange](124dc9b1-ddd6-afef-352a-04f0ed0063a7.htm) | Sets the pulse voltage level range, in volts. |
| 公共方法 | [SetRecordLength](bf045c08-6980-b826-fd48-934929d0c805.htm) | Sets the number of measurements that compose a measure record. If you set this property to a value greater than 1, the MeasurementWhen property must be set to AutomaticallyAfterSourceComplete or OnMeasureTrigger. |
| 公共方法 | [SetSamplesToAverage](5dfc2d82-b935-9775-da03-e59874e913d7.htm) | Sets the number of samples to average when you take a measurement. Increasing the number of samples to average decreases measurement noise, but increases the time required to take a measurement. |
| 公共方法 | [SetSense](b49560d7-1bdd-7d64-66a5-4e1da5b3278f.htm) | Sets either local or remote sensing of the output voltage for the specified channels. |
| 公共方法 | [SetSequence(Double)](2d2ca427-1593-5820-8f2d-63d47305515a.htm) | Configures a series of voltage or current outputs and corresponding source delays. The source mode must be set to Sequence for this method to take effect. |
| 公共方法 | [SetSequence(Double, Double)](f45c2dea-e4bc-3a06-127a-29b1776e0f87.htm) | Configures a series of voltage or current outputs and corresponding source delays. |
| 公共方法 | [SetSequenceLoopCountFinite](b01ec5ce-f0ec-6778-5676-20098328f2bd.htm) |  |
| 公共方法 | [SetSequenceStepDeltaTime](ca54f912-9d60-f99d-9da4-6b46e6c45531.htm) |  |
| 公共方法 | [SetSequenceStepDeltaTimeEnabled](bc88d4cc-419f-f951-1049-9621a5fbf264.htm) |  |
| 公共方法 | [SetSourceDelay](3bd08fdc-d3eb-bf35-8e68-0930e66e34c6.htm) | Determines when, in seconds, the device generates the Source Complete event, potentially starting a measurement if the MeasureWhen attribute is set to AutomaticallyAfterSourceComplete. |
| 公共方法 | [SetSourceMode](773da792-2324-0a58-8ede-c421ade2440f.htm) | Sets whether to run a single output point or a sequence. |
| 公共方法 | [SetTransientResponse](9b9ce0e4-5687-4ac1-988c-13b475803bc1.htm) | Sets the transient response. The default values is "Normal". |
| 公共方法 | [SetVClamp](bc7786cd-1d27-2ccb-5701-764ad8fa680d.htm) | Sets the voltage limit for the output to not exceed when generating the desired current level. |
| 公共方法 | [SetVClampAutorange](ab839237-b582-e9f0-956c-654edf6e7964.htm) | Sets whether to automatically select the voltage limit range based on the desired voltage limit. |
| 公共方法 | [SetVClampHigh](eeb56288-7369-8692-fa68-0bff6768e60e.htm) | Sets the voltage limit high for the output to not exceed when generating the desired current level. |
| 公共方法 | [SetVClampLow](d3cb1ab1-2392-dc97-9b43-7b9b6568ecf6.htm) | Sets the voltage limit low for the output to not exceed when generating the desired current level. |
| 公共方法 | [SetVClampRange](622eabb4-e4a4-51e5-7877-0e5ff7d93f73.htm) | Sets the voltage limit range, in volts. |
| 公共方法 | [SetVLevel](2cb05592-180a-61a6-ac91-b60ce8f8ef0a.htm) | Sets the voltage level, in volts. |
| 公共方法 | [SetVLevelAutorange](beaa8933-66fa-1aae-89db-0b730fdb51fe.htm) | Sets whether or not power supply automatically selects the voltage level range based on the desired voltage level. |
| 公共方法 | [SetVLevelRange](ad124591-8c52-5455-d6ce-8c6c0a057de0.htm) | Sets the voltage level range, in volts. |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |
| 公共方法 | [VForce(Double)](d86c9067-4c5a-c264-3a56-43f7ea88227a.htm) | Generates specific voltage level, other parameters are previous defined values or default values. |
| 公共方法 | [VForce(Double, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, String, String)](a2f3776b-8765-90a4-2808-bd63b8441fce.htm) | Generates voltage with the input parameters.If keep the paremeter null, it will use the previous defined value or default value. |
| 公共方法 | [VForceIMeasure](9c699458-0866-6298-237c-c167342100bc.htm) | Generates voltage with the input parameters and returns the measured current.If keep the paremeter null, it will use the previous defined value or default value. |
| 公共方法 | [VForceVMeasure](cb6e368f-a536-59ce-1656-0fcb2b68d486.htm) | Generates voltage with the input parameters and returns the measured voltage.If keep the paremeter null, it will use the previous defined value or default value. |
| 公共方法 | [VIMeasure2](d9abd6f9-9e6a-d683-5be8-74f596b6d1fe.htm) |  |
| 公共方法 | [VMeasure](141b5109-b018-1300-eb63-966a5607b86e.htm) | Returns the measured voltage. |
| 公共方法 | [VPulse](0eddec77-93e5-0b1b-a3b3-3c8175c55493.htm) | Generate a single Voltage pulse. |
| 公共方法 | [VPulseIMeasure](4250ff13-7359-4190-cefc-8e364f8c5e94.htm) | Generate a single Voltage pulse and fetch current. |
| 公共方法 | [VPulseVMeasure](3b00483b-a149-8978-630d-cfbddb8ed2db.htm) | Generate a single Voltage pulse and fetch voltage. |
| 公共方法 | [WaitForEvent](26cc1a09-b69b-f340-d085-0a95ef8b7e45.htm) | Waits until the device has generated the specified event. |
| 公共方法 | [WriteString](13614734-c317-2b92-0c5b-ab1e6376ac8f.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### Abort 方法

|  |  |
| --- | --- |
|  | DCVIAbort 方法 |

Transitions the NI-DCPower session from the Running state to the Committed state. If a sequence is running, then the NI-DCPower session is stopped.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI Abort()
```

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### Commit 方法

|  |  |
| --- | --- |
|  | DCVICommit 方法 |

Applies the settings that you configured previously to the device. Calling this method moves the NI-DCPower session from the Uncommitted state into the Committed state.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI Commit()
```

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### ConfigureDigitalEdgeTrigger 方法

|  |  |
| --- | --- |
|  | DCVIConfigureDigitalEdgeTrigger 方法 |

Configure the device to wait for digital edge.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI ConfigureDigitalEdgeTrigger(
	string triggerClass,
	string source,
	string edgeType
)
```

###### 参数

triggerClass  String
:   "Start", "SequenceAdvance", "Source", "Measure", "Pulse"

source  String
:   Input terminal

edgeType  String
:   "Rising" or "Falling"

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### ConfigureSoftwareTrigger 方法

|  |  |
| --- | --- |
|  | DCVIConfigureSoftwareTrigger 方法 |

Configure the device to wait for software edge.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI ConfigureSoftwareTrigger(
	string triggerClass
)
```

###### 参数

triggerClass  String
:   "Start", "SequenceAdvance", "Source", "Measure", "Pulse"

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### Disable 方法

|  |  |
| --- | --- |
|  | DCVIDisable 方法 |

Places the instrument in a quiescent state as quickly as possible.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI Disable()
```

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### DisableTrigger 方法

|  |  |
| --- | --- |
|  | DCVIDisableTrigger 方法 |

Disable the previously configured trigger.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI DisableTrigger(
	string triggerClass
)
```

###### 参数

triggerClass  String
:   "Start", "SequenceAdvance", "Source", "Pulse"

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### ExportSignal 方法

|  |  |
| --- | --- |
|  | DCVIExportSignal 方法 |

Routes trigger and event signals to the output terminal you specify. The route is created when the session is committed.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI ExportSignal(
	string signalSource,
	string outputTerminal
)
```

###### 参数

signalSource  String
:   "MeasureCompleteEvent", "PulseCompleteEvent", "SequenceEngineDoneEvent", "SequenceIterationCompleteEvent", "SourceCompleteEvent"
    "MeasureTrigger", "PulseTrigger", "SequenceAdvanceTrigger", "SourceTrigger", "StartTrigger"

outputTerminal  String
:   The terminal to route the signal to.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### Fetch 方法

|  |  |
| --- | --- |
|  | DCVIFetch 方法 |

Return fetch result.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public (Dictionary<string, double[]> current, Dictionary<string, double[]> voltage, Dictionary<string, bool[]> compliance) Fetch(
	double timeout,
	int pointsToFetch
)
```

###### 参数

timeout  Double
:   Specifies the maximum time allowed for this method to complete, in seconds.

pointsToFetch  Int32
:   Specifies the number of measurements to fetch.

###### 返回值

ValueTupleDictionaryString, Double, DictionaryString, Double, DictionaryString, Boolean  
A dictionary collection.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetApertureTime 方法

|  |  |
| --- | --- |
|  | DCVIGetApertureTime 方法 |

Gets the measurement aperture time, in seconds, for the channel configuration. You can specify aperture time units in the ApertureTimeUnits property.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetApertureTime()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetAutoZero 方法

|  |  |
| --- | --- |
|  | DCVIGetAutoZero 方法 |

Gets the auto-zero method to use on the device.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetAutoZero()
```

###### 返回值

DictionaryString, String  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetBufferSize 方法

|  |  |
| --- | --- |
|  | DCVIGetBufferSize 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetBufferSize()
```

###### 返回值

DictionaryString, Double

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetIClamp 方法

|  |  |
| --- | --- |
|  | DCVIGetIClamp 方法 |

Gets the current limit, in amperes, for the output not to exceed when generating the desired voltage level.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetIClamp()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetIClampAutorange 方法

|  |  |
| --- | --- |
|  | DCVIGetIClampAutorange 方法 |

Gets whether or not power supply automatically selects the current limit range based on the desired current limit.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> GetIClampAutorange()
```

###### 返回值

DictionaryString, Boolean  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetIClampHigh 方法

|  |  |
| --- | --- |
|  | DCVIGetIClampHigh 方法 |

Gets the current limit high, in amperes, for the output not to exceed when generating the desired voltage level.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetIClampHigh()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetIClampLow 方法

|  |  |
| --- | --- |
|  | DCVIGetIClampLow 方法 |

Gets the current limit low, in amperes, for the output not to exceed when generating the desired voltage level.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetIClampLow()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetIClampRange 方法

|  |  |
| --- | --- |
|  | DCVIGetIClampRange 方法 |

Gets the current limit range, in amperes.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetIClampRange()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetILevel 方法

|  |  |
| --- | --- |
|  | DCVIGetILevel 方法 |

Gets the current level, in amperes, that the device attempts to generate.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetILevel()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetILevelAutorange 方法

|  |  |
| --- | --- |
|  | DCVIGetILevelAutorange 方法 |

Gets whether to automatically select the current level range based on the desired current level.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> GetILevelAutorange()
```

###### 返回值

DictionaryString, Boolean  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetILevelRange 方法

|  |  |
| --- | --- |
|  | DCVIGetILevelRange 方法 |

Gets the current level range, in amperes.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetILevelRange()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetIsRecordLengthFinite 方法

|  |  |
| --- | --- |
|  | DCVIGetIsRecordLengthFinite 方法 |

Gets a value indicating whether to take continuous measurements.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> GetIsRecordLengthFinite()
```

###### 返回值

DictionaryString, Boolean  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetMeasureDelay 方法

|  |  |
| --- | --- |
|  | DCVIGetMeasureDelay 方法 |

Gets the amount of time to delay the generation of the MeasureCompleteEvent.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetMeasureDelay()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetMeasureWhen 方法

|  |  |
| --- | --- |
|  | DCVIGetMeasureWhen 方法 |

Gets when the measure unit should acquire measurements.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetMeasureWhen()
```

###### 返回值

DictionaryString, String  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetOutputConnected 方法

|  |  |
| --- | --- |
|  | DCVIGetOutputConnected 方法 |

Gets whether the output relay is connected (closed) or disconnected (open).

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> GetOutputConnected()
```

###### 返回值

DictionaryString, Boolean  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetOutputEnabled 方法

|  |  |
| --- | --- |
|  | DCVIGetOutputEnabled 方法 |

Gets whether the output is enabled.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> GetOutputEnabled()
```

###### 返回值

DictionaryString, Boolean  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetOutputFunction 方法

|  |  |
| --- | --- |
|  | DCVIGetOutputFunction 方法 |

Gets the output function.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetOutputFunction()
```

###### 返回值

DictionaryString, String  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetOutputResistance 方法

|  |  |
| --- | --- |
|  | DCVIGetOutputResistance 方法 |

Gets the output resistance that the device attempts to generate for the specified channel(s).
This property is valid only when you set the OutputFunction to DCVoltage.
The default value is 0.0.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetOutputResistance()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetOvpEnabled 方法

|  |  |
| --- | --- |
|  | DCVIGetOvpEnabled 方法 |

Gets whether the overvoltage protection is enabled.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> GetOvpEnabled()
```

###### 返回值

DictionaryString, Boolean  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetOvpLimit 方法

|  |  |
| --- | --- |
|  | DCVIGetOvpLimit 方法 |

Gets the voltage the power supply allows. The units are Volts.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetOvpLimit()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of voltage limit.The key of the collection is pin name, the value is multisite voltage limit.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseBiasDelay 方法

|  |  |
| --- | --- |
|  | DCVIGetPulseBiasDelay 方法 |

Gets the time, in seconds, when the device generates the PulseCompleteEvent.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetPulseBiasDelay()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseBiasIClamp 方法

|  |  |
| --- | --- |
|  | DCVIGetPulseBiasIClamp 方法 |

Gets the pulse current limit, in amperes, that the output cannot exceed when generating the desired voltage during the off phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetPulseBiasIClamp()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseBiasIClampHigh 方法

|  |  |
| --- | --- |
|  | DCVIGetPulseBiasIClampHigh 方法 |

Gets the pulse current limit high, in amperes, that the output cannot exceed when generating the desired voltage during the off phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetPulseBiasIClampHigh()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseBiasIClampLow 方法

|  |  |
| --- | --- |
|  | DCVIGetPulseBiasIClampLow 方法 |

Gets the pulse current limit low, in amperes, that the output cannot exceed when generating the desired voltage during the off phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetPulseBiasIClampLow()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseBiasILevel 方法

|  |  |
| --- | --- |
|  | DCVIGetPulseBiasILevel 方法 |

Gets the pulse bias current level, in amperes, that the device attempts to generate during the off phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetPulseBiasILevel()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseBiasVClamp 方法

|  |  |
| --- | --- |
|  | DCVIGetPulseBiasVClamp 方法 |

Gets the pulse voltage limit, in volts, that the output cannot exceed when generating the desired current during the off phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetPulseBiasVClamp()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseBiasVClampHigh 方法

|  |  |
| --- | --- |
|  | DCVIGetPulseBiasVClampHigh 方法 |

Gets the pulse voltage limit high, in volts, that the output cannot exceed when generating the desired current during the off phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetPulseBiasVClampHigh()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseBiasVClampLow 方法

|  |  |
| --- | --- |
|  | DCVIGetPulseBiasVClampLow 方法 |

Gets the pulse voltage limit low, in volts, that the output cannot exceed when generating the desired current during the off phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetPulseBiasVClampLow()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseBiasVLevel 方法

|  |  |
| --- | --- |
|  | DCVIGetPulseBiasVLevel 方法 |

Gets the pulse bias voltage level, in volts, that the device attempts to generate during the off phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetPulseBiasVLevel()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseIClamp 方法

|  |  |
| --- | --- |
|  | DCVIGetPulseIClamp 方法 |

Gets the pulse current limit, in amperes, that the output cannot exceed when generating the desired voltage during the on phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetPulseIClamp()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseIClampHigh 方法

|  |  |
| --- | --- |
|  | DCVIGetPulseIClampHigh 方法 |

Gets the pulse current limit high, in amperes, that the output cannot exceed when generating the desired voltage during the on phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetPulseIClampHigh()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseIClampLow 方法

|  |  |
| --- | --- |
|  | DCVIGetPulseIClampLow 方法 |

Gets the pulse current limit low, in amperes, that the output cannot exceed when generating the desired voltage during the on phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetPulseIClampLow()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseIClampRange 方法

|  |  |
| --- | --- |
|  | DCVIGetPulseIClampRange 方法 |

Gets the pulse current limit range, in amperes.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetPulseIClampRange()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseILevel 方法

|  |  |
| --- | --- |
|  | DCVIGetPulseILevel 方法 |

Gets the pulse current level, in amperes, that the device attempts to generate during the on phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetPulseILevel()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseILevelRange 方法

|  |  |
| --- | --- |
|  | DCVIGetPulseILevelRange 方法 |

Gets the pulse current level range, in amperes.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetPulseILevelRange()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseOffTime 方法

|  |  |
| --- | --- |
|  | DCVIGetPulseOffTime 方法 |

Gets the length, in seconds, of the off phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetPulseOffTime()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseOnTime 方法

|  |  |
| --- | --- |
|  | DCVIGetPulseOnTime 方法 |

Gets the length, in seconds, of the on phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetPulseOnTime()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseVClamp 方法

|  |  |
| --- | --- |
|  | DCVIGetPulseVClamp 方法 |

Gets the pulse voltage limit, in volts, that the output cannot exceed when generating the desired pulse current during the on phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetPulseVClamp()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseVClampHigh 方法

|  |  |
| --- | --- |
|  | DCVIGetPulseVClampHigh 方法 |

Gets the pulse voltage limit high, in volts, that the output cannot exceed when generating the desired pulse current during the on phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetPulseVClampHigh()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseVClampLow 方法

|  |  |
| --- | --- |
|  | DCVIGetPulseVClampLow 方法 |

Gets the pulse voltage limit low, in volts, that the output cannot exceed when generating the desired pulse current during the on phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetPulseVClampLow()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseVClampRange 方法

|  |  |
| --- | --- |
|  | DCVIGetPulseVClampRange 方法 |

Gets the pulse voltage limit range, in volts.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetPulseVClampRange()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseVLevel 方法

|  |  |
| --- | --- |
|  | DCVIGetPulseVLevel 方法 |

Gets the pulse voltage level, in volts, that the device attempts to generate during the on phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetPulseVLevel()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseVLevelRange 方法

|  |  |
| --- | --- |
|  | DCVIGetPulseVLevelRange 方法 |

Gets the pulse voltage level range, in volts.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetPulseVLevelRange()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetRecordLength 方法

|  |  |
| --- | --- |
|  | DCVIGetRecordLength 方法 |

Gets the number of measurements that compose a measure record. If you set this property to a value greater than 1, the MeasurementWhen property must be set to AutomaticallyAfterSourceComplete or OnMeasureTrigger.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, int> GetRecordLength()
```

###### 返回值

DictionaryString, Int32  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetSamplesToAverage 方法

|  |  |
| --- | --- |
|  | DCVIGetSamplesToAverage 方法 |

Gets the number of samples to average when you take a measurement. Increasing the number of samples to average decreases measurement noise, but increases the time required to take a measurement.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, int> GetSamplesToAverage()
```

###### 返回值

DictionaryString, Int32  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetSense 方法

|  |  |
| --- | --- |
|  | DCVIGetSense 方法 |

Gets either local or remote sensing of the output voltage for the specified channels.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetSense()
```

###### 返回值

DictionaryString, String  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetSequenceLoopCountFinite 方法

|  |  |
| --- | --- |
|  | DCVIGetSequenceLoopCountFinite 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> GetSequenceLoopCountFinite()
```

###### 返回值

DictionaryString, Boolean

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetSequenceStepDeltaTime 方法

|  |  |
| --- | --- |
|  | DCVIGetSequenceStepDeltaTime 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetSequenceStepDeltaTime()
```

###### 返回值

DictionaryString, Double

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetSequenceStepDeltaTimeEnabled 方法

|  |  |
| --- | --- |
|  | DCVIGetSequenceStepDeltaTimeEnabled 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> GetSequenceStepDeltaTimeEnabled()
```

###### 返回值

DictionaryString, Boolean

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetSourceDelay 方法

|  |  |
| --- | --- |
|  | DCVIGetSourceDelay 方法 |

Gets the delay of the device generates the Source Complete event.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetSourceDelay()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetSourceMode 方法

|  |  |
| --- | --- |
|  | DCVIGetSourceMode 方法 |

Gets the source mode.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetSourceMode()
```

###### 返回值

DictionaryString, String  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetTransientResponse 方法

|  |  |
| --- | --- |
|  | DCVIGetTransientResponse 方法 |

Gets the transient response. The default values is "Normal".

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetTransientResponse()
```

###### 返回值

DictionaryString, String  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetVClamp 方法

|  |  |
| --- | --- |
|  | DCVIGetVClamp 方法 |

Gets the voltage limit for the output to not exceed when generating the desired current level.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetVClamp()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetVClampAutorange 方法

|  |  |
| --- | --- |
|  | DCVIGetVClampAutorange 方法 |

Gets whether to automatically select the voltage limit range based on the desired voltage limit.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> GetVClampAutorange()
```

###### 返回值

DictionaryString, Boolean  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetVClampHigh 方法

|  |  |
| --- | --- |
|  | DCVIGetVClampHigh 方法 |

Gets the voltage limit high for the output to not exceed when generating the desired current level.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetVClampHigh()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetVClampLow 方法

|  |  |
| --- | --- |
|  | DCVIGetVClampLow 方法 |

Gets the voltage limit low for the output to not exceed when generating the desired current level.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetVClampLow()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetVClampRange 方法

|  |  |
| --- | --- |
|  | DCVIGetVClampRange 方法 |

Gets the voltage limit range, in volts.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetVClampRange()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetVLevel 方法

|  |  |
| --- | --- |
|  | DCVIGetVLevel 方法 |

Gets the voltage level, in volts.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetVLevel()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetVLevelAutorange 方法

|  |  |
| --- | --- |
|  | DCVIGetVLevelAutorange 方法 |

Gets whether or not power supply automatically selects the voltage level range based on the desired voltage level.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> GetVLevelAutorange()
```

###### 返回值

DictionaryString, Boolean  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetVLevelRange 方法

|  |  |
| --- | --- |
|  | DCVIGetVLevelRange 方法 |

Gets the voltage level range, in volts.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetVLevelRange()
```

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### IForce 方法

|  |  |
| --- | --- |
|  | DCVIIForce 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [IForce(Double)](d93f1f8a-6bcc-a6be-894c-9a8723191673.htm) | Generates specific current level, other parameters are previous defined values or default values. |
| 公共方法 | [IForce(Double, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, String, String)](66180131-4088-f6ab-676d-d893b53c5b2f.htm) | Generates current with the input parameters.If keep the paremeter null, it will use the previous defined value or default value. |

[Top](#PageHeader)

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


##### IForce(Double) 方法

|  |  |
| --- | --- |
|  | DCVIIForce(Double) 方法 |

Generates specific current level, other parameters are previous defined values or default values.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI IForce(
	double level
)
```

###### 参数

level  Double
:   The current level, in amperes, that the device attempts to generate.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[IForce 重载](d33ce55c-66ff-d55b-bd9c-b78d7eddd155.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


##### IForce(Double, Nullable&lt;Double&gt;, Nullable&lt;Double&gt;, Nullable&lt;Double&gt;, Nullable&lt;Double&gt;, Nullable&lt;Double&gt;, Nullable&lt;Double&gt;, String, String) 方法

|  |  |
| --- | --- |
|  | DCVIIForce(Double, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, String, String) 方法 |

Generates current with the input parameters.If keep the paremeter null, it will use the previous defined value or default value.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI IForce(
	double forceLevel,
	double? vClamp,
	double? iLevelRange = null,
	double? vClampRange = null,
	double? vClampLow = null,
	double? vClampHigh = null,
	double? sourceDelay = null,
	string sense = null,
	string forceCompleteEventOutputTerminal = null
)
```

###### 参数

forceLevel  Double
:   The current level, in amperes, that the device attempts to generate.

vClamp  NullableDouble
:   The voltage limit for the output to not exceed when generating the desired current level. If you want to set asymmetric limit, input null for this then use vClampLow and vClampHigh.

iLevelRange  NullableDouble  (Optional)
:   The current level range, in amperes. If keep null, to automatically select the current level range based on the desired current level.

vClampRange  NullableDouble  (Optional)
:   The voltage limit range, in volts. If keep null, to automatically select the voltage limit range based on the desired voltage limit.

vClampLow  NullableDouble  (Optional)
:   The voltage limit low for the output to not exceed when generating the desired current level.

vClampHigh  NullableDouble  (Optional)
:   The voltage limit high for the output to not exceed when generating the desired current level.

sourceDelay  NullableDouble  (Optional)
:   The time, in seconds, when the device generates the SourceCompleteEvent.

sense  String  (Optional)
:   Local or remote sensing of performing voltage and output measurements.Local sense describes measurements taken using a single set of leads while remote sense describes measurements taken using two sets of leads.

forceCompleteEventOutputTerminal  String  (Optional)
:   Routes the SourceCompleteEvent signal to the output terminal you specify.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[IForce 重载](d33ce55c-66ff-d55b-bd9c-b78d7eddd155.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### IForceIMeasure 方法

|  |  |
| --- | --- |
|  | DCVIIForceIMeasure 方法 |

Generates current with the input parameters and returns the measured current.If keep the paremeter null, it will use the previous defined value or default value.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> IForceIMeasure(
	double forceLevel,
	double? vClamp = null,
	double? iLevelRange = null,
	double? vClampRange = null,
	double? vClampLow = null,
	double? vClampHigh = null,
	double? apertureTime = null,
	double? sourceDelay = null,
	double? measureDelay = null,
	string sense = null,
	string forceCompleteEventOutputTerminal = null,
	string measureCompleteEventOutputTerminal = null
)
```

###### 参数

forceLevel  Double
:   The current level, in amperes, that the device attempts to generate.

vClamp  NullableDouble  (Optional)
:   The voltage limit for the output to not exceed when generating the desired current level. If you want to set asymmetric limit, input null for this then use vClampLow and vClampHigh.

iLevelRange  NullableDouble  (Optional)
:   The current level range, in amperes. If keep null, to automatically select the current level range based on the desired current level.

vClampRange  NullableDouble  (Optional)
:   The voltage limit range, in volts. If keep null, to automatically select the voltage limit range based on the desired voltage limit.

vClampLow  NullableDouble  (Optional)
:   The voltage limit low for the output to not exceed when generating the desired current level.

vClampHigh  NullableDouble  (Optional)
:   The voltage limit high for the output to not exceed when generating the desired current level.

apertureTime  NullableDouble  (Optional)
:   The measurement aperture time, in seconds.

sourceDelay  NullableDouble  (Optional)
:   The time, in seconds, when the device generates the SourceCompleteEvent.

measureDelay  NullableDouble  (Optional)
:   The time, in seconds, to delay the generation of the MeasureCompleteEvent.

sense  String  (Optional)
:   Local or remote sensing of performing voltage and output measurements. Local sense describes measurements taken using a single set of leads while remote sense describes measurements taken using two sets of leads.

forceCompleteEventOutputTerminal  String  (Optional)
:   Routes the SourceCompleteEvent signal to the output terminal you specify.

measureCompleteEventOutputTerminal  String  (Optional)
:   Routes the MeasureCompleteEvent signal to the output terminal you specify.

###### 返回值

DictionaryString, Double  
A dictionary collection of measured current.The key of the collection is pin name, the value is multisite current result.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### IForceVMeasure 方法

|  |  |
| --- | --- |
|  | DCVIIForceVMeasure 方法 |

Generates current with the input parameters and returns the measured voltage.If keep the paremeter null, it will use the previous defined value or default value.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> IForceVMeasure(
	double forceLevel,
	double? vClamp = null,
	double? iLevelRange = null,
	double? vClampRange = null,
	double? vClampLow = null,
	double? vClampHigh = null,
	double? apertureTime = null,
	double? sourceDelay = null,
	double? measureDelay = null,
	string sense = null,
	string forceCompleteEventOutputTerminal = null,
	string measureCompleteEventOutputTerminal = null
)
```

###### 参数

forceLevel  Double
:   The current level, in amperes, that the device attempts to generate.

vClamp  NullableDouble  (Optional)
:   The voltage limit for the output to not exceed when generating the desired current level. If you want to set asymmetric limit, input null for this then use vClampLow and vClampHigh.

iLevelRange  NullableDouble  (Optional)
:   The current level range, in amperes. If keep null, to automatically select the current level range based on the desired current level.

vClampRange  NullableDouble  (Optional)
:   The voltage limit range, in volts. If keep null, to automatically select the voltage limit range based on the desired voltage limit.

vClampLow  NullableDouble  (Optional)
:   The voltage limit low for the output to not exceed when generating the desired current level.

vClampHigh  NullableDouble  (Optional)
:   The voltage limit high for the output to not exceed when generating the desired current level.

apertureTime  NullableDouble  (Optional)
:   The measurement aperture time, in seconds.

sourceDelay  NullableDouble  (Optional)
:   The time, in seconds, when the device generates the SourceCompleteEvent.

measureDelay  NullableDouble  (Optional)
:   The time, in seconds, to delay the generation of the MeasureCompleteEvent.

sense  String  (Optional)
:   Local or remote sensing of performing voltage and output measurements.Local sense describes measurements taken using a single set of leads while remote sense describes measurements taken using two sets of leads.

forceCompleteEventOutputTerminal  String  (Optional)
:   Routes the SourceCompleteEvent signal to the output terminal you specify.

measureCompleteEventOutputTerminal  String  (Optional)
:   Routes the MeasureCompleteEvent signal to the output terminal you specify.

###### 返回值

DictionaryString, Double  
A dictionary collection of measured voltage.The key of the collection is pin name, the value is multisite voltage result.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### IMeasure 方法

|  |  |
| --- | --- |
|  | DCVIIMeasure 方法 |

Returns the measured current.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> IMeasure()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of measured current.The key of the collection is pin name, the value is multisite current result.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### Initiate 方法

|  |  |
| --- | --- |
|  | DCVIInitiate 方法 |

Starts generation or acquisition, causing session to leave the Uncommitted state or Committed state and enter the Running state.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI Initiate()
```

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### IPulse 方法

|  |  |
| --- | --- |
|  | DCVIIPulse 方法 |

Generate a single Current pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI IPulse(
	double level
)
```

###### 参数

level  Double
:   The pulse current level during the on phase of a pulse.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### IPulseIMeasure 方法

|  |  |
| --- | --- |
|  | DCVIIPulseIMeasure 方法 |

Generate a single Current pulse and fetch current.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> IPulseIMeasure(
	double pulseLevel
)
```

###### 参数

pulseLevel  Double
:   The pulse current level during the on phase of a pulse.

###### 返回值

DictionaryString, Double  
A dictionary collection of fetch current.The key of the collection is pin name, the value is multisite current result.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### IPulseVMeasure 方法

|  |  |
| --- | --- |
|  | DCVIIPulseVMeasure 方法 |

Generate a single Current pulse and fetch voltage.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> IPulseVMeasure(
	double pulseLevel
)
```

###### 参数

pulseLevel  Double
:   The pulse current level during the on phase of a pulse.

###### 返回值

DictionaryString, Double  
A dictionary collection of fetch voltage.The key of the collection is pin name, the value is multisite voltage result.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### QueryInCompliance 方法

|  |  |
| --- | --- |
|  | DCVIQueryInCompliance 方法 |

Queries the device to indicate if the output is operating at the compliance limit.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> QueryInCompliance()
```

###### 返回值

DictionaryString, Boolean  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### QueryOutputState 方法

|  |  |
| --- | --- |
|  | DCVIQueryOutputState 方法 |

Queries the specified output channel to determine if the output channel is currently in the state specified by outputState.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> QueryOutputState()
```

###### 返回值

DictionaryString, String  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### ReadState 方法

|  |  |
| --- | --- |
|  | DCVIReadState 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> ReadState()
```

###### 返回值

DictionaryString, Double

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### ReadString 方法

|  |  |
| --- | --- |
|  | DCVIReadString 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

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

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### Reset 方法

|  |  |
| --- | --- |
|  | DCVIReset 方法 |

Reset the instrument session

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI Reset()
```

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### ResetDevice 方法

|  |  |
| --- | --- |
|  | DCVIResetDevice 方法 |

Performs a hard reset on the device.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI ResetDevice()
```

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SelfCalibrate 方法

|  |  |
| --- | --- |
|  | DCVISelfCalibrate 方法 |

Performs a self calibrate on the device.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SelfCalibrate()
```

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SelfTest 方法

|  |  |
| --- | --- |
|  | DCVISelfTest 方法 |

Performs a self test on the device.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SelfTest()
```

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SendSoftwareTrigger 方法

|  |  |
| --- | --- |
|  | DCVISendSoftwareTrigger 方法 |

Sends a Software Edge.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SendSoftwareTrigger(
	string triggerClass
)
```

###### 参数

triggerClass  String
:   "Start", "SequenceAdvance", "Source", "Measure", "Pulse"

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetApertureTime 方法

|  |  |
| --- | --- |
|  | DCVISetApertureTime 方法 |

Sets the measurement aperture time, in seconds, for the channel configuration. You can specify aperture time units in the ApertureTimeUnits property.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetApertureTime(
	double apertureTime
)
```

###### 参数

apertureTime  Double
:   The default value is 0.01666666 seconds.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetAutoZero 方法

|  |  |
| --- | --- |
|  | DCVISetAutoZero 方法 |

Sets the auto-zero method to use on the device.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetAutoZero(
	string autoZero
)
```

###### 参数

autoZero  String
:   "Off", "On" and "Once".

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetBufferSize 方法

|  |  |
| --- | --- |
|  | DCVISetBufferSize 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetBufferSize(
	ulong Size
)
```

###### 参数

Size  UInt64

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetIClamp 方法

|  |  |
| --- | --- |
|  | DCVISetIClamp 方法 |

Sets the current limit, in amperes, for the output not to exceed when generating the desired voltage level.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetIClamp(
	double limit
)
```

###### 参数

limit  Double
:   The current limit.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetIClampAutorange 方法

|  |  |
| --- | --- |
|  | DCVISetIClampAutorange 方法 |

Sets whether or not power supply automatically selects the current limit range based on the desired current limit.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetIClampAutorange(
	bool autorange
)
```

###### 参数

autorange  Boolean
:   true or false.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetIClampHigh 方法

|  |  |
| --- | --- |
|  | DCVISetIClampHigh 方法 |

Sets the current limit high, in amperes, for the output not to exceed when generating the desired voltage level.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetIClampHigh(
	double high
)
```

###### 参数

high  Double
:   The current limit high.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetIClampLow 方法

|  |  |
| --- | --- |
|  | DCVISetIClampLow 方法 |

Sets the current limit low, in amperes, for the output not to exceed when generating the desired voltage level.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetIClampLow(
	double low
)
```

###### 参数

low  Double
:   The current limit low.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetIClampRange 方法

|  |  |
| --- | --- |
|  | DCVISetIClampRange 方法 |

Sets the current limit range, in amperes.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetIClampRange(
	double range
)
```

###### 参数

range  Double
:   The current limit range.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetILevel 方法

|  |  |
| --- | --- |
|  | DCVISetILevel 方法 |

Sets the current level, in amperes, that the device attempts to generate.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetILevel(
	double level
)
```

###### 参数

level  Double
:   The current level.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetILevelAutorange 方法

|  |  |
| --- | --- |
|  | DCVISetILevelAutorange 方法 |

Sets whether to automatically select the current level range based on the desired current level.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetILevelAutorange(
	bool autorange
)
```

###### 参数

autorange  Boolean
:   ture or false.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetILevelRange 方法

|  |  |
| --- | --- |
|  | DCVISetILevelRange 方法 |

Sets the current level range, in amperes.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetILevelRange(
	double range
)
```

###### 参数

range  Double
:   The current level range.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetIsRecordLengthFinite 方法

|  |  |
| --- | --- |
|  | DCVISetIsRecordLengthFinite 方法 |

Sets a value indicating whether to take continuous measurements.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetIsRecordLengthFinite(
	bool value
)
```

###### 参数

value  Boolean
:   true, if continuous measurements are allowed; otherwise, false.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetMeasureDelay 方法

|  |  |
| --- | --- |
|  | DCVISetMeasureDelay 方法 |

Sets the amount of time to delay the generation of the MeasureCompleteEvent.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetMeasureDelay(
	double delay
)
```

###### 参数

delay  Double
:   A time, in seconds, to delay the generation of the MeasureCompleteEvent.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetMeasureWhen 方法

|  |  |
| --- | --- |
|  | DCVISetMeasureWhen 方法 |

Sets when the measure unit should acquire measurements.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetMeasureWhen(
	string measureWhen
)
```

###### 参数

measureWhen  String
:   "AutomaticallyAfterSourceComplete", "OnDemand" and "OnMeasureTrigger".
    The default value is OnDemand if you set the SourceMode property to SinglePoint and supports only the Measure method.
    The default value is AutomaticallyAfterSourceComplete if you set the SourceMode property to Sequence and supports only the Fetch method.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetOutputConnected 方法

|  |  |
| --- | --- |
|  | DCVISetOutputConnected 方法 |

Sets whether the output relay is connected (closed) or disconnected (open).
The Enabled property does not change based on this property; they are independent of each other.
Set this property to false to disconnect the output terminal from the output.
The default value is true.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetOutputConnected(
	bool connected
)
```

###### 参数

connected  Boolean
:   true or false.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetOutputEnabled 方法

|  |  |
| --- | --- |
|  | DCVISetOutputEnabled 方法 |

Enables or disables the output.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetOutputEnabled(
	bool enabled
)
```

###### 参数

enabled  Boolean
:   true, enalbed;false, disabled.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetOutputFunction 方法

|  |  |
| --- | --- |
|  | DCVISetOutputFunction 方法 |

Generate current or voltage on the specified channel(s).

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetOutputFunction(
	string outputFunction
)
```

###### 参数

outputFunction  String
:   "DCCurrent", "DCVoltage", "PulseCurrent" or "PulseVoltage"

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetOutputResistance 方法

|  |  |
| --- | --- |
|  | DCVISetOutputResistance 方法 |

Sets the output resistance that the device attempts to generate for the specified channel(s).
This property is valid only when you set the OutputFunction to DCVoltage.
The default value is 0.0.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetOutputResistance(
	double resistance
)
```

###### 参数

resistance  Double
:   The output resistance

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetOvpEnabled 方法

|  |  |
| --- | --- |
|  | DCVISetOvpEnabled 方法 |

Enables or disables overvoltage protection (OVP).

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetOvpEnabled(
	bool OvpEnabled
)
```

###### 参数

OvpEnabled  Boolean
:   true or false.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetOvpLimit 方法

|  |  |
| --- | --- |
|  | DCVISetOvpLimit 方法 |

Sets the voltage the power supply allows. The units are Volts.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetOvpLimit(
	double limit
)
```

###### 参数

limit  Double
:   The max value of the voltage of the power supplu allows.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseBiasDelay 方法

|  |  |
| --- | --- |
|  | DCVISetPulseBiasDelay 方法 |

Sets the time, in seconds, when the device generates the PulseCompleteEvent.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetPulseBiasDelay(
	double delay
)
```

###### 参数

delay  Double
:   The time, in seconds, to set.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseBiasIClamp 方法

|  |  |
| --- | --- |
|  | DCVISetPulseBiasIClamp 方法 |

Sets the pulse current limit, in amperes, that the output cannot exceed when generating the desired voltage during the off phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetPulseBiasIClamp(
	double limit
)
```

###### 参数

limit  Double
:   The pulse current limit during the off phase of a pulse.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseBiasIClampHigh 方法

|  |  |
| --- | --- |
|  | DCVISetPulseBiasIClampHigh 方法 |

Sets the pulse current limit high, in amperes, that the output cannot exceed when generating the desired voltage during the off phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetPulseBiasIClampHigh(
	double high
)
```

###### 参数

high  Double
:   The pulse current limit high during the off phase of a pulse.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseBiasIClampLow 方法

|  |  |
| --- | --- |
|  | DCVISetPulseBiasIClampLow 方法 |

Sets the pulse current limit low, in amperes, that the output cannot exceed when generating the desired voltage during the off phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetPulseBiasIClampLow(
	double low
)
```

###### 参数

low  Double
:   The pulse current limit low during the off phase of a pulse.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseBiasILevel 方法

|  |  |
| --- | --- |
|  | DCVISetPulseBiasILevel 方法 |

Sets the pulse bias current level, in amperes, that the device attempts to generate during the off phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetPulseBiasILevel(
	double level
)
```

###### 参数

level  Double
:   The pulse bias current level.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseBiasVClamp 方法

|  |  |
| --- | --- |
|  | DCVISetPulseBiasVClamp 方法 |

Sets the pulse voltage limit, in volts, that the output cannot exceed when generating the desired current during the off phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetPulseBiasVClamp(
	double limit
)
```

###### 参数

limit  Double
:   The pulse voltage limit during the off phase of a pulse.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseBiasVClampHigh 方法

|  |  |
| --- | --- |
|  | DCVISetPulseBiasVClampHigh 方法 |

Sets the pulse voltage limit high, in volts, that the output cannot exceed when generating the desired current during the off phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetPulseBiasVClampHigh(
	double high
)
```

###### 参数

high  Double
:   The pulse voltage limit high during the off phase of a pulse.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseBiasVClampLow 方法

|  |  |
| --- | --- |
|  | DCVISetPulseBiasVClampLow 方法 |

Sets the pulse voltage limit low, in volts, that the output cannot exceed when generating the desired current during the off phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetPulseBiasVClampLow(
	double low
)
```

###### 参数

low  Double
:   The pulse voltage limit low during the off phase of a pulse.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseBiasVLevel 方法

|  |  |
| --- | --- |
|  | DCVISetPulseBiasVLevel 方法 |

Sets the pulse bias voltage level, in volts, that the device attempts to generate during the off phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetPulseBiasVLevel(
	double level
)
```

###### 参数

level  Double
:   The pulse bias voltage level during the off phase of a pulse.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseIClamp 方法

|  |  |
| --- | --- |
|  | DCVISetPulseIClamp 方法 |

Sets the pulse current limit, in amperes, that the output cannot exceed when generating the desired voltage during the on phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetPulseIClamp(
	double limit
)
```

###### 参数

limit  Double
:   The pulse current limit during the on phase of a pulse.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseIClampHigh 方法

|  |  |
| --- | --- |
|  | DCVISetPulseIClampHigh 方法 |

Sets the pulse current limit high, in amperes, that the output cannot exceed when generating the desired voltage during the on phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetPulseIClampHigh(
	double high
)
```

###### 参数

high  Double
:   The pulse current limit high during the on phase of a pulse.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseIClampLow 方法

|  |  |
| --- | --- |
|  | DCVISetPulseIClampLow 方法 |

Sets the pulse current limit low, in amperes, that the output cannot exceed when generating the desired voltage during the on phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetPulseIClampLow(
	double low
)
```

###### 参数

low  Double
:   The pulse current limit low during the on phase of a pulse.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseIClampRange 方法

|  |  |
| --- | --- |
|  | DCVISetPulseIClampRange 方法 |

Sets the pulse current limit range, in amperes.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetPulseIClampRange(
	double range
)
```

###### 参数

range  Double
:   The current limit range.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseILevel 方法

|  |  |
| --- | --- |
|  | DCVISetPulseILevel 方法 |

Sets the pulse current level, in amperes, that the device attempts to generate during the on phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetPulseILevel(
	double level
)
```

###### 参数

level  Double
:   The pulse current level during the on phase of a pulse.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseILevelRange 方法

|  |  |
| --- | --- |
|  | DCVISetPulseILevelRange 方法 |

Sets the pulse current level range, in amperes.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetPulseILevelRange(
	double range
)
```

###### 参数

range  Double
:   The pulse current level range.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseOffTime 方法

|  |  |
| --- | --- |
|  | DCVISetPulseOffTime 方法 |

Sets the length, in seconds, of the off phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetPulseOffTime(
	double time
)
```

###### 参数

time  Double
:   The time of the off phase of a pulse.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseOnTime 方法

|  |  |
| --- | --- |
|  | DCVISetPulseOnTime 方法 |

Sets the length, in seconds, of the on phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetPulseOnTime(
	double time
)
```

###### 参数

time  Double
:   The time of the on phase of a pulse.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseVClamp 方法

|  |  |
| --- | --- |
|  | DCVISetPulseVClamp 方法 |

Sets the pulse voltage limit, in volts, that the output cannot exceed when generating the desired pulse current during the on phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetPulseVClamp(
	double limit
)
```

###### 参数

limit  Double
:   The pulse voltage limit during the on phase of a pulse.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseVClampHigh 方法

|  |  |
| --- | --- |
|  | DCVISetPulseVClampHigh 方法 |

Sets the pulse voltage limit high, in volts, that the output cannot exceed when generating the desired pulse current during the on phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetPulseVClampHigh(
	double high
)
```

###### 参数

high  Double
:   The pulse voltage limit high during the on phase of a pulse.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseVClampLow 方法

|  |  |
| --- | --- |
|  | DCVISetPulseVClampLow 方法 |

Sets the pulse voltage limit low, in volts, that the output cannot exceed when generating the desired pulse current during the on phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetPulseVClampLow(
	double low
)
```

###### 参数

low  Double
:   The pulse voltage limit low during the on phase of a pulse.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseVClampRange 方法

|  |  |
| --- | --- |
|  | DCVISetPulseVClampRange 方法 |

Sets the pulse voltage limit range, in volts.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetPulseVClampRange(
	double range
)
```

###### 参数

range  Double
:   The pulse voltage limit range.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseVLevel 方法

|  |  |
| --- | --- |
|  | DCVISetPulseVLevel 方法 |

Sets the pulse voltage level, in volts, that the device attempts to generate during the on phase of a pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetPulseVLevel(
	double level
)
```

###### 参数

level  Double
:   The pulse voltage level during the on phase of a pulse.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseVLevelRange 方法

|  |  |
| --- | --- |
|  | DCVISetPulseVLevelRange 方法 |

Sets the pulse voltage level range, in volts.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetPulseVLevelRange(
	double range
)
```

###### 参数

range  Double
:   The pulse voltage level range.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetRecordLength 方法

|  |  |
| --- | --- |
|  | DCVISetRecordLength 方法 |

Sets the number of measurements that compose a measure record. If you set this property to a value greater than 1, the MeasurementWhen property must be set to AutomaticallyAfterSourceComplete or OnMeasureTrigger.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetRecordLength(
	int recordLength
)
```

###### 参数

recordLength  Int32
:   Valid values range from 1 to 16,777,216. The default value is 1.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetSamplesToAverage 方法

|  |  |
| --- | --- |
|  | DCVISetSamplesToAverage 方法 |

Sets the number of samples to average when you take a measurement. Increasing the number of samples to average decreases measurement noise, but increases the time required to take a measurement.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetSamplesToAverage(
	int samples
)
```

###### 参数

samples  Int32
:   The average number of samples.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetSense 方法

|  |  |
| --- | --- |
|  | DCVISetSense 方法 |

Sets either local or remote sensing of the output voltage for the specified channels.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetSense(
	string sense
)
```

###### 参数

sense  String
:   "Local" or "Remote", the default value is "Local".

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetSequence 方法

|  |  |
| --- | --- |
|  | DCVISetSequence 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [SetSequence(Double)](2d2ca427-1593-5820-8f2d-63d47305515a.htm) | Configures a series of voltage or current outputs and corresponding source delays. The source mode must be set to Sequence for this method to take effect. |
| 公共方法 | [SetSequence(Double, Double)](f45c2dea-e4bc-3a06-127a-29b1776e0f87.htm) | Configures a series of voltage or current outputs and corresponding source delays. |

[Top](#PageHeader)

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


##### SetSequence(Double[]) 方法

|  |  |
| --- | --- |
|  | DCVISetSequence(Double) 方法 |

Configures a series of voltage or current outputs and corresponding source delays.
The source mode must be set to Sequence for this method to take effect.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetSequence(
	double[] values
)
```

###### 参数

values  Double
:   Specifies the series of voltage levels or current levels, depending on the configured output method.
    The valid values for this parameter are defined by the voltage level range or current level range.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[SetSequence 重载](21bb50d0-3692-bbf5-f7ac-bd2df68cb2b5.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


##### SetSequence(Double[], Double[]) 方法

|  |  |
| --- | --- |
|  | DCVISetSequence(Double, Double) 方法 |

Configures a series of voltage or current outputs and corresponding source delays.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetSequence(
	double[] values,
	double[] sourceDelays
)
```

###### 参数

values  Double
:   Specifies the series of voltage levels or current levels, depending on the configured output method.
    The valid values for this parameter are defined by the voltage level range or current level range.

sourceDelays  Double
:   Specifies the source delay, in seconds, that follows the configuration of each value in the sequence.
    The valid values must be in the range of[0, 167].

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
A dictionary collection.The key of the collection is pin name, the value is multisite values.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[SetSequence 重载](21bb50d0-3692-bbf5-f7ac-bd2df68cb2b5.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetSequenceLoopCountFinite 方法

|  |  |
| --- | --- |
|  | DCVISetSequenceLoopCountFinite 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetSequenceLoopCountFinite(
	bool isFinite
)
```

###### 参数

isFinite  Boolean

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetSequenceStepDeltaTime 方法

|  |  |
| --- | --- |
|  | DCVISetSequenceStepDeltaTime 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetSequenceStepDeltaTime(
	double time
)
```

###### 参数

time  Double

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetSequenceStepDeltaTimeEnabled 方法

|  |  |
| --- | --- |
|  | DCVISetSequenceStepDeltaTimeEnabled 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetSequenceStepDeltaTimeEnabled(
	bool deltaTimeEnabled
)
```

###### 参数

deltaTimeEnabled  Boolean

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetSourceDelay 方法

|  |  |
| --- | --- |
|  | DCVISetSourceDelay 方法 |

Determines when, in seconds, the device generates the Source Complete event, potentially starting a measurement if the MeasureWhen attribute is set to AutomaticallyAfterSourceComplete.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetSourceDelay(
	double delay
)
```

###### 参数

delay  Double
:   A value representing when, in seconds, the device generates the Source Complete event. Valid Values are 0 to 167. The default value is 0.01667.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetSourceMode 方法

|  |  |
| --- | --- |
|  | DCVISetSourceMode 方法 |

Sets whether to run a single output point or a sequence.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetSourceMode(
	string sourceMode
)
```

###### 参数

sourceMode  String
:   "SinglePoint" or "Sequence"

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetTransientResponse 方法

|  |  |
| --- | --- |
|  | DCVISetTransientResponse 方法 |

Sets the transient response. The default values is "Normal".

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetTransientResponse(
	string response
)
```

###### 参数

response  String
:   "Fast", "Normal" and "Slow".

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetVClamp 方法

|  |  |
| --- | --- |
|  | DCVISetVClamp 方法 |

Sets the voltage limit for the output to not exceed when generating the desired current level.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetVClamp(
	double limit
)
```

###### 参数

limit  Double
:   The voltage limit.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetVClampAutorange 方法

|  |  |
| --- | --- |
|  | DCVISetVClampAutorange 方法 |

Sets whether to automatically select the voltage limit range based on the desired voltage limit.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetVClampAutorange(
	bool autorange
)
```

###### 参数

autorange  Boolean
:   true or false.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetVClampHigh 方法

|  |  |
| --- | --- |
|  | DCVISetVClampHigh 方法 |

Sets the voltage limit high for the output to not exceed when generating the desired current level.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetVClampHigh(
	double high
)
```

###### 参数

high  Double
:   The voltage limit high.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetVClampLow 方法

|  |  |
| --- | --- |
|  | DCVISetVClampLow 方法 |

Sets the voltage limit low for the output to not exceed when generating the desired current level.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetVClampLow(
	double low
)
```

###### 参数

low  Double
:   The voltage limit low.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetVClampRange 方法

|  |  |
| --- | --- |
|  | DCVISetVClampRange 方法 |

Sets the voltage limit range, in volts.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetVClampRange(
	double range
)
```

###### 参数

range  Double
:   The voltage limit range.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetVLevel 方法

|  |  |
| --- | --- |
|  | DCVISetVLevel 方法 |

Sets the voltage level, in volts.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetVLevel(
	double level
)
```

###### 参数

level  Double
:   The voltage level.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetVLevelAutorange 方法

|  |  |
| --- | --- |
|  | DCVISetVLevelAutorange 方法 |

Sets whether or not power supply automatically selects the voltage level range based on the desired voltage level.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetVLevelAutorange(
	bool autorange
)
```

###### 参数

autorange  Boolean
:   true or false.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetVLevelRange 方法

|  |  |
| --- | --- |
|  | DCVISetVLevelRange 方法 |

Sets the voltage level range, in volts.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI SetVLevelRange(
	double range
)
```

###### 参数

range  Double
:   the voltage level range, in volts.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### VForce 方法

|  |  |
| --- | --- |
|  | DCVIVForce 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [VForce(Double)](d86c9067-4c5a-c264-3a56-43f7ea88227a.htm) | Generates specific voltage level, other parameters are previous defined values or default values. |
| 公共方法 | [VForce(Double, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, String, String)](a2f3776b-8765-90a4-2808-bd63b8441fce.htm) | Generates voltage with the input parameters.If keep the paremeter null, it will use the previous defined value or default value. |

[Top](#PageHeader)

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


##### VForce(Double) 方法

|  |  |
| --- | --- |
|  | DCVIVForce(Double) 方法 |

Generates specific voltage level, other parameters are previous defined values or default values.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI VForce(
	double level
)
```

###### 参数

level  Double
:   The voltage level, in volts, that the device attempts to generate.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[VForce 重载](314f0537-c7f8-4bef-54d5-d774f6c1b58d.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


##### VForce(Double, Nullable&lt;Double&gt;, Nullable&lt;Double&gt;, Nullable&lt;Double&gt;, Nullable&lt;Double&gt;, Nullable&lt;Double&gt;, Nullable&lt;Double&gt;, String, String) 方法

|  |  |
| --- | --- |
|  | DCVIVForce(Double, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, String, String) 方法 |

Generates voltage with the input parameters.If keep the paremeter null, it will use the previous defined value or default value.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI VForce(
	double forceLevel,
	double? iClamp,
	double? vLevelRange = null,
	double? iClampRange = null,
	double? iClampLow = null,
	double? iClampHigh = null,
	double? sourceDelay = null,
	string sense = null,
	string forceCompleteEventOutputTerminal = null
)
```

###### 参数

forceLevel  Double
:   The voltage level, in volts, that the device attempts to generate.

iClamp  NullableDouble
:   The current limit, in amperes, for the output not to exceed when generating the desired voltage level. If you want to set asymmetric limit, input null for this then use iClampLow and iClampHigh.

vLevelRange  NullableDouble  (Optional)
:   The voltage level range, in volts. If keep null, to automatically select the voltage level range based on the desired voltage level.

iClampRange  NullableDouble  (Optional)
:   The current limit range, in amperes. If keep null, to automatically select the current limit range based on the desired current limit.

iClampLow  NullableDouble  (Optional)
:   The current limit low, in amperes, for the output not to exceed when generating the desired voltage level.

iClampHigh  NullableDouble  (Optional)
:   The current limit high, in amperes, for the output not to exceed when generating the desired voltage level.

sourceDelay  NullableDouble  (Optional)
:   The time, in seconds, when the device generates the SourceCompleteEvent.

sense  String  (Optional)
:   Local or remote sensing of performing voltage and output measurements.Local sense describes measurements taken using a single set of leads while remote sense describes measurements taken using two sets of leads.

forceCompleteEventOutputTerminal  String  (Optional)
:   Routes the SourceCompleteEvent signal to the output terminal you specify.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[VForce 重载](314f0537-c7f8-4bef-54d5-d774f6c1b58d.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### VForceIMeasure 方法

|  |  |
| --- | --- |
|  | DCVIVForceIMeasure 方法 |

Generates voltage with the input parameters and returns the measured current.If keep the paremeter null, it will use the previous defined value or default value.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> VForceIMeasure(
	double forceLevel,
	double? iClamp = null,
	double? vLevelRange = null,
	double? iClampRange = null,
	double? iClampLow = null,
	double? iClampHigh = null,
	double? apertureTime = null,
	double? sourceDelay = null,
	double? measureDelay = null,
	string sense = null,
	string forceCompleteEventOutputTerminal = null,
	string measureCompleteEventOutputTerminal = null
)
```

###### 参数

forceLevel  Double
:   The voltage level, in volts, that the device attempts to generate.

iClamp  NullableDouble  (Optional)
:   The current limit, in amperes, for the output not to exceed when generating the desired voltage level. If you want to set asymmetric limit, input null for this then use iClampLow and iClampHigh.

vLevelRange  NullableDouble  (Optional)
:   The voltage level range, in volts. If keep null, to automatically select the voltage level range based on the desired voltage level.

iClampRange  NullableDouble  (Optional)
:   The current limit range, in amperes. If keep null, to automatically select the current limit range based on the desired current limit.

iClampLow  NullableDouble  (Optional)
:   The current limit low, in amperes, for the output not to exceed when generating the desired voltage level.

iClampHigh  NullableDouble  (Optional)
:   The current limit high, in amperes, for the output not to exceed when generating the desired voltage level.

apertureTime  NullableDouble  (Optional)
:   The measurement aperture time, in seconds.

sourceDelay  NullableDouble  (Optional)
:   The time, in seconds, when the device generates the SourceCompleteEvent.

measureDelay  NullableDouble  (Optional)
:   The time, in seconds, to delay the generation of the MeasureCompleteEvent.

sense  String  (Optional)
:   Local or remote sensing of performing voltage and output measurements. Local sense describes measurements taken using a single set of leads while remote sense describes measurements taken using two sets of leads.

forceCompleteEventOutputTerminal  String  (Optional)
:   Routes the SourceCompleteEvent signal to the output terminal you specify.

measureCompleteEventOutputTerminal  String  (Optional)
:   Routes the MeasureCompleteEvent signal to the output terminal you specify.

###### 返回值

DictionaryString, Double  
A dictionary collection of measured current.The key of the collection is pin name, the value is multisite current result.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### VForceVMeasure 方法

|  |  |
| --- | --- |
|  | DCVIVForceVMeasure 方法 |

Generates voltage with the input parameters and returns the measured voltage.If keep the paremeter null, it will use the previous defined value or default value.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> VForceVMeasure(
	double forceLevel,
	double? iClamp = null,
	double? vLevelRange = null,
	double? iClampRange = null,
	double? iClampLow = null,
	double? iClampHigh = null,
	double? apertureTime = null,
	double? sourceDelay = null,
	double? measureDelay = null,
	string sense = null,
	string forceCompleteEventOutputTerminal = null,
	string measureCompleteEventOutputTerminal = null
)
```

###### 参数

forceLevel  Double
:   The voltage level, in volts, that the device attempts to generate.

iClamp  NullableDouble  (Optional)
:   The current limit, in amperes, for the output not to exceed when generating the desired voltage level. If you want to set asymmetric limit, input null for this then use iClampLow and iClampHigh.

vLevelRange  NullableDouble  (Optional)
:   The voltage level range, in volts. If keep null, to automatically select the voltage level range based on the desired voltage level.

iClampRange  NullableDouble  (Optional)
:   The current limit range, in amperes. If keep null, to automatically select the current limit range based on the desired current limit.

iClampLow  NullableDouble  (Optional)
:   The current limit low, in amperes, for the output not to exceed when generating the desired voltage level.

iClampHigh  NullableDouble  (Optional)
:   The current limit high, in amperes, for the output not to exceed when generating the desired voltage level.

apertureTime  NullableDouble  (Optional)
:   The measurement aperture time, in seconds.

sourceDelay  NullableDouble  (Optional)
:   The time, in seconds, when the device generates the SourceCompleteEvent.

measureDelay  NullableDouble  (Optional)
:   The time, in seconds, to delay the generation of the MeasureCompleteEvent.

sense  String  (Optional)
:   Local or remote sensing of performing voltage and output measurements. Local sense describes measurements taken using a single set of leads while remote sense describes measurements taken using two sets of leads.

forceCompleteEventOutputTerminal  String  (Optional)
:   Routes the SourceCompleteEvent signal to the output terminal you specify.

measureCompleteEventOutputTerminal  String  (Optional)
:   Routes the MeasureCompleteEvent signal to the output terminal you specify.

###### 返回值

DictionaryString, Double  
A dictionary collection of measured voltage.The key of the collection is pin name, the value is multisite voltage result.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### VIMeasure2 方法

|  |  |
| --- | --- |
|  | DCVIVIMeasure2 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public (Dictionary<string, double> current, Dictionary<string, double> voltage) VIMeasure2()
```

###### 返回值

ValueTupleDictionaryString, Double, DictionaryString, Double

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### VMeasure 方法

|  |  |
| --- | --- |
|  | DCVIVMeasure 方法 |

Returns the measured voltage.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> VMeasure()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of measured voltage.The key of the collection is pin name, the value is multisite voltage result.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### VPulse 方法

|  |  |
| --- | --- |
|  | DCVIVPulse 方法 |

Generate a single Voltage pulse.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI VPulse(
	double level
)
```

###### 参数

level  Double
:   The pulse voltage level during the on phase of a pulse.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### VPulseIMeasure 方法

|  |  |
| --- | --- |
|  | DCVIVPulseIMeasure 方法 |

Generate a single Voltage pulse and fetch current.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> VPulseIMeasure(
	double pulseLevel
)
```

###### 参数

pulseLevel  Double
:   The pulse voltage level during the on phase of a pulse.

###### 返回值

DictionaryString, Double  
A dictionary collection of fetch current.The key of the collection is pin name, the value is multisite current result.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### VPulseVMeasure 方法

|  |  |
| --- | --- |
|  | DCVIVPulseVMeasure 方法 |

Generate a single Voltage pulse and fetch voltage.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> VPulseVMeasure(
	double pulseLevel
)
```

###### 参数

pulseLevel  Double
:   The pulse voltage level during the on phase of a pulse.

###### 返回值

DictionaryString, Double  
A dictionary collection of fetch voltage.The key of the collection is pin name, the value is multisite voltage result.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### WaitForEvent 方法

|  |  |
| --- | --- |
|  | DCVIWaitForEvent 方法 |

Waits until the device has generated the specified event.

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI WaitForEvent(
	string eventSource,
	double timeout
)
```

###### 参数

eventSource  String
:   "MeasureCompleteEvent", "PulseCompleteEvent", "ReadyForPulseTriggerEvent", "SequenceEngineDoneEvent", "SequenceIterationCompleteEvent", "SourceCompleteEvent"

timeout  Double
:   Specifies the maximum time allowed for this function to complete, in seconds.

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### WriteString 方法

|  |  |
| --- | --- |
|  | DCVIWriteString 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public DCVI WriteString(
	string cmd
)
```

###### 参数

cmd  String

###### 返回值

[DCVI](81d0e576-6187-e121-64de-e63c34278db2.htm)

参见

###### 引用

[DCVI 类](81d0e576-6187-e121-64de-e63c34278db2.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


## IDCVI_Instr 接口

|  |  |
| --- | --- |
|  | IDCVI\_Instr 接口 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public interface IDCVI_Instr
```

IDCVI\_Instr 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Abort](2acd8c07-8588-699d-7422-737ec432371c.htm) |  |
| 公共方法 | [Commit](94975378-1059-323c-5d8d-25d5c8766dd6.htm) |  |
| 公共方法 | [ConfigureDigitalEdgeTrigger](344d8048-944b-0104-d6d4-37264864cf17.htm) |  |
| 公共方法 | [ConfigureSoftwareTrigger](67814703-77ea-036f-f6f2-878b0a6c1b5c.htm) |  |
| 公共方法 | [Disable](eb974e34-2ecf-ed81-1f51-2adad4a13b05.htm) |  |
| 公共方法 | [DisableTrigger](029ec745-3627-aa39-6f46-079fb88206d7.htm) |  |
| 公共方法 | [ExportSignal](da01d787-9798-af92-2524-49c67f7c98c4.htm) |  |
| 公共方法 | [Fetch](e6b3bd22-f9c1-2ce7-a409-2cee03551d35.htm) |  |
| 公共方法 | [GetApertureTime](365ee2e0-9c7d-eded-3efb-f58847a908cf.htm) |  |
| 公共方法 | [GetAutoZero](7b3f251e-a185-821d-3a13-e16a3734cd14.htm) |  |
| 公共方法 | [GetBufferSize](f9e28aab-1770-5f3b-11aa-09ca02c3fb21.htm) |  |
| 公共方法 | [GetIClamp](6e330b65-1822-2e74-e790-36c46ad0caaf.htm) |  |
| 公共方法 | [GetIClampAutorange](f0b3938b-5919-8224-d613-80e7a3d99899.htm) |  |
| 公共方法 | [GetIClampHigh](8dedaf11-bcd9-2b75-09f8-da9c4c1a1d96.htm) |  |
| 公共方法 | [GetIClampLow](dd1da9f1-ce4a-07ec-9193-06d1fd629529.htm) |  |
| 公共方法 | [GetIClampRange](fc58f53a-f5ef-d544-60f4-4923d4bbb637.htm) |  |
| 公共方法 | [GetILevel](518cc30c-95a3-c0ee-fff6-91168c93648c.htm) |  |
| 公共方法 | [GetILevelAutorange](dc8a414d-3623-7335-8200-7ad71bf3a954.htm) |  |
| 公共方法 | [GetILevelRange](9549f8cc-6c40-ecbf-5521-bb2a8ea670df.htm) |  |
| 公共方法 | [GetIsRecordLengthFinite](d6e2ae42-d9b7-9f6e-1d08-a5b84b6b08a1.htm) |  |
| 公共方法 | [GetMeasureDelay](e382bebb-15ce-8bac-9ff5-c39782f9f9c4.htm) |  |
| 公共方法 | [GetMeasureWhen](67e6b322-8511-5631-b671-b4614e06d1a7.htm) |  |
| 公共方法 | [GetOutputConnected](62eb291c-44e3-ade7-8e05-3bf1a9d47531.htm) |  |
| 公共方法 | [GetOutputEnabled](38c3ef65-cd6d-2809-876a-5c1e5331d725.htm) |  |
| 公共方法 | [GetOutputFunction](d2c16591-c258-2c9e-09bc-907ef3af08bf.htm) |  |
| 公共方法 | [GetOutputResistance](ef0ca39b-b877-fcf1-24bb-271ccf6c9980.htm) |  |
| 公共方法 | [GetOvpEnabled](bc897a40-ef78-cb20-83b3-9cd909c211d5.htm) |  |
| 公共方法 | [GetOvpLimit](eec1a132-cb80-6b6c-4827-72d812318752.htm) |  |
| 公共方法 | [GetPulseBiasDelay](f00e32a5-62bb-5fa7-1fb1-7af693144699.htm) |  |
| 公共方法 | [GetPulseBiasIClamp](715e4b57-21c6-cc15-cef5-41212e734678.htm) |  |
| 公共方法 | [GetPulseBiasIClampHigh](f00588d5-5984-b079-f3db-168f7b6f8fe4.htm) |  |
| 公共方法 | [GetPulseBiasIClampLow](e0d7e770-dd61-7cb0-8a6a-469584c53be9.htm) |  |
| 公共方法 | [GetPulseBiasILevel](a47fbfd0-accf-8fa2-5bf6-4fa90488a0f7.htm) |  |
| 公共方法 | [GetPulseBiasVClamp](e9ff5d70-b2a0-54db-82da-5505dd5d4c04.htm) |  |
| 公共方法 | [GetPulseBiasVClampHigh](ccf463de-bfb0-17da-fe80-b1b9f9c4e168.htm) |  |
| 公共方法 | [GetPulseBiasVClampLow](c903b77f-7a3f-ac84-f422-012b7e24b9df.htm) |  |
| 公共方法 | [GetPulseBiasVLevel](c2325e02-c0a9-6941-6b58-10e49de50d16.htm) |  |
| 公共方法 | [GetPulseIClamp](94906a71-9848-42d8-89f9-0f91ee33dd01.htm) |  |
| 公共方法 | [GetPulseIClampHigh](d6295cf0-451d-d1b6-3278-239b5b841130.htm) |  |
| 公共方法 | [GetPulseIClampLow](9371e9c2-c8a2-78ce-eff8-b3719c58cda5.htm) |  |
| 公共方法 | [GetPulseIClampRange](1a2c2f3f-b1f4-e999-b0f3-56cb94b7b607.htm) |  |
| 公共方法 | [GetPulseILevel](5740c479-5767-86b4-441f-db3f4fac2d22.htm) |  |
| 公共方法 | [GetPulseILevelRange](3c4ac7ab-b284-6c43-fd13-7299ca134b5b.htm) |  |
| 公共方法 | [GetPulseOffTime](0f94fdfe-705f-01f9-20f2-30f5b1fc2e88.htm) |  |
| 公共方法 | [GetPulseOnTime](fa541fcd-3f39-e2dd-e2ef-461471b5e573.htm) |  |
| 公共方法 | [GetPulseVClamp](7f626923-6971-e4c3-3a65-4178c8050a35.htm) |  |
| 公共方法 | [GetPulseVClampHigh](5f061325-973d-f98d-7028-9752478ff2b3.htm) |  |
| 公共方法 | [GetPulseVClampLow](bf72ef31-e9ab-b788-1cd8-7ff81736b92a.htm) |  |
| 公共方法 | [GetPulseVClampRange](20c224be-df9c-e7a5-3c9b-69faa201be6b.htm) |  |
| 公共方法 | [GetPulseVLevel](8fe74e2d-f3c2-23d8-dac2-7dfaaa81a8f0.htm) |  |
| 公共方法 | [GetPulseVLevelRange](c41c9d07-0f57-bcdb-3069-c42c8ad7757a.htm) |  |
| 公共方法 | [GetRecordLength](df993ad4-fdff-d83d-1dd5-dab498624763.htm) |  |
| 公共方法 | [GetSamplesToAverage](79c88242-a06d-9f55-7191-2d7aff7317bd.htm) |  |
| 公共方法 | [GetSense](41730040-636c-4381-971c-2080a8c96468.htm) |  |
| 公共方法 | [GetSequenceLoopCountFinite](a66f1ca6-2c8b-bf20-5e85-b0cdf443bf1f.htm) |  |
| 公共方法 | [GetSequenceStepDeltaTime](a1a8d4d3-35f4-5454-b62e-2c8a5757857c.htm) |  |
| 公共方法 | [GetSequenceStepDeltaTimeEnabled](0bcd7296-7256-65cc-0bc6-d419d4636c68.htm) |  |
| 公共方法 | [GetSourceDelay](238bbc15-dfc7-af4e-625a-e7b986e46aa1.htm) |  |
| 公共方法 | [GetSourceMode](ebc86bf5-6547-dca2-a3e3-aace05e2d2ae.htm) |  |
| 公共方法 | [GetTransientResponse](2e8adc37-7468-79d1-5cfd-6f643e774956.htm) |  |
| 公共方法 | [GetVClamp](0d102fa4-eb77-a875-179d-ae1277b25d6d.htm) |  |
| 公共方法 | [GetVClampAutorange](e9db9165-8fa0-50e1-18ab-0e0e9bc9464e.htm) |  |
| 公共方法 | [GetVClampHigh](6885b871-7dfa-ce43-3739-5a6cd47ecd25.htm) |  |
| 公共方法 | [GetVClampLow](f6a89c24-8334-8358-09b9-e401e054ba0f.htm) |  |
| 公共方法 | [GetVClampRange](4bfafefc-4147-3979-96a7-4b66e63e0d0e.htm) |  |
| 公共方法 | [GetVLevel](7d017f2a-44f5-7ddb-97b7-6c0bc2906569.htm) |  |
| 公共方法 | [GetVLevelAutorange](c309d4f3-22c1-d8d5-67b0-54b2d9a2352b.htm) |  |
| 公共方法 | [GetVLevelRange](1087199d-6e32-c1fb-f9dc-5181da7b9171.htm) |  |
| 公共方法 | [IForce(String, Double)](5bc8f260-367a-2799-ba6d-f4bd30b34d07.htm) |  |
| 公共方法 | [IForce(String, Double, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, String, String)](fafedf90-ce21-386e-a9a9-70ac5a33f8ff.htm) |  |
| 公共方法 | [IForceIMeasure](eb9e25fc-e804-3732-7981-8285d7118cb0.htm) |  |
| 公共方法 | [IForceVMeasure](2a6fb23d-7e03-5f5b-ea4b-1629f0f34d3c.htm) |  |
| 公共方法 | [IMeasure](d46c8640-26c6-d89c-7754-f91ccaa5065f.htm) |  |
| 公共方法 | [Initiate](6d51cee8-48e3-af6d-66fd-3614451f4af0.htm) |  |
| 公共方法 | [IPulse](886b325d-dbac-6791-af9d-63382905e085.htm) |  |
| 公共方法 | [IPulseIMeasure](805fcc8f-a37e-4ddd-1ad7-742b28700c60.htm) |  |
| 公共方法 | [IPulseVMeasure](c54ccf00-7431-c361-0ccb-e3b9a6ab40bb.htm) |  |
| 公共方法 | [QueryInCompliance](98c65b4a-5ca2-ba5b-86d4-252095589d7e.htm) |  |
| 公共方法 | [QueryOutputState](130e45bb-3339-cc73-c6fb-977e9d9461bc.htm) |  |
| 公共方法 | [ReadState](f5f3767b-2208-bcd3-9ffd-4cc13d5d2c38.htm) |  |
| 公共方法 | [ReadString](786d91b5-2651-266c-a4aa-9d5281169440.htm) |  |
| 公共方法 | [Reset](29b792b4-d0ef-934a-0a1b-e0febaf4707c.htm) |  |
| 公共方法 | [ResetDevice](8fcdaacb-c496-83ef-80c2-300848ee896c.htm) |  |
| 公共方法 | [SelfCalibrate](697bae8e-f808-f6c9-5853-1191988113a8.htm) |  |
| 公共方法 | [SelfTest](0de454f1-0c6b-b0fb-74b8-6d57eaba9bc5.htm) |  |
| 公共方法 | [SendSoftwareTrigger](db4aba7c-d8da-1b23-5a32-2c59c9794f4f.htm) |  |
| 公共方法 | [SetApertureTime](edad480e-0601-3bb1-55c4-a382371b557a.htm) |  |
| 公共方法 | [SetAutoZero](3ac7f39b-0f61-21f3-7cf0-b5ccc737f6a4.htm) |  |
| 公共方法 | [SetBufferSize](20a73a9b-480d-5e1c-be39-30f6cb5f2162.htm) |  |
| 公共方法 | [SetIClamp](3d3695db-8634-beec-3f8e-3934ea320e6a.htm) |  |
| 公共方法 | [SetIClampAutorange](f7709ffe-e60c-db14-2345-e7b1de52c662.htm) |  |
| 公共方法 | [SetIClampHigh](222cbf1e-69a3-1a0e-9673-d43abbcbc030.htm) |  |
| 公共方法 | [SetIClampLow](3e821cf1-3b78-cf36-53e2-f80cc96b0261.htm) |  |
| 公共方法 | [SetIClampRange](cc0e4d02-2ff9-571a-8690-1e2aa239a44d.htm) |  |
| 公共方法 | [SetILevel](05849a37-1296-9a76-75fc-6a2410d8a4c8.htm) |  |
| 公共方法 | [SetILevelAutorange](0677a50a-d716-c9e6-14fd-df03ce2cb774.htm) |  |
| 公共方法 | [SetILevelRange](47be3f96-2e36-2236-0b69-f2d56acb7a72.htm) |  |
| 公共方法 | [SetIsRecordLengthFinite](82e3323e-ef79-615f-3382-c4bbec02b539.htm) |  |
| 公共方法 | [SetMeasureDelay](615df8c9-2e2e-5d6f-8b73-5eef37ef97e2.htm) |  |
| 公共方法 | [SetMeasureWhen](d54084c4-fd17-f1bc-d4c1-f2909b2a3bd7.htm) |  |
| 公共方法 | [SetOutputConnected](bcb401b5-3e6f-b610-f1d0-65dc91977877.htm) |  |
| 公共方法 | [SetOutputEnabled](f34ef6f4-9f4a-1bc9-7ca4-a349f0aa62a0.htm) |  |
| 公共方法 | [SetOutputFunction](a1eb8805-2dfa-36bb-8433-cf80e7f9af8e.htm) |  |
| 公共方法 | [SetOutputResistance](cf748160-f40f-74b3-ef81-d255779847bf.htm) |  |
| 公共方法 | [SetOvpEnabled](f9f6b2dc-e4d4-e5ea-87ac-eb43c2a15b9b.htm) |  |
| 公共方法 | [SetOvpLimit](6aa60158-ffcf-3622-c7fc-f1f1d262d095.htm) |  |
| 公共方法 | [SetPulseBiasDelay](06a45db7-9b84-aacd-933c-0efc17a9a94b.htm) |  |
| 公共方法 | [SetPulseBiasIClamp](052579c4-e825-807b-3ad6-9841705bdd12.htm) |  |
| 公共方法 | [SetPulseBiasIClampHigh](2bb3cc1b-6b43-7f58-8850-0def4ded99db.htm) |  |
| 公共方法 | [SetPulseBiasIClampLow](349ea2a1-74ae-03e2-4609-1c40a63bee54.htm) |  |
| 公共方法 | [SetPulseBiasILevel](f20b521c-10aa-2fef-fa51-94dbb68ba77e.htm) |  |
| 公共方法 | [SetPulseBiasVClamp](d527f9ed-bba4-e99e-c031-e843715873c8.htm) |  |
| 公共方法 | [SetPulseBiasVClampHigh](61c4eed3-38f3-7abd-0a1e-5d47a32d03a9.htm) |  |
| 公共方法 | [SetPulseBiasVClampLow](4057b187-0348-e066-f6df-69e8e6c242c8.htm) |  |
| 公共方法 | [SetPulseBiasVLevel](b83005c4-1e44-fb4a-7d91-4b385a5e9960.htm) |  |
| 公共方法 | [SetPulseIClamp](8b6f3d8b-c2fe-304d-91a4-1f475d36cf9d.htm) |  |
| 公共方法 | [SetPulseIClampHigh](a354fc9c-28e3-3242-2d8f-dedb1df37563.htm) |  |
| 公共方法 | [SetPulseIClampLow](4774bccd-0e91-fdae-8ef3-70afc3316fb0.htm) |  |
| 公共方法 | [SetPulseIClampRange](089aa55c-b73e-60b1-ae26-2734f50d9775.htm) |  |
| 公共方法 | [SetPulseILevel](325fc4d0-4c61-5786-0ad0-c58858e52dc8.htm) |  |
| 公共方法 | [SetPulseILevelRange](9e822093-f731-aa26-46d9-8d067148658b.htm) |  |
| 公共方法 | [SetPulseOffTime](6e4c530c-30ea-216d-edad-8614542442dd.htm) |  |
| 公共方法 | [SetPulseOnTime](c120bc2b-8564-4f7a-99f2-6c3a77a559af.htm) |  |
| 公共方法 | [SetPulseVClamp](e2e62ee9-2f17-41bc-6d3e-995eda34c78b.htm) |  |
| 公共方法 | [SetPulseVClampHigh](6dbe1b10-a60a-f200-524a-866fac5a132f.htm) |  |
| 公共方法 | [SetPulseVClampLow](cf4c0bf5-a365-929d-4f74-ad1f96ab9059.htm) |  |
| 公共方法 | [SetPulseVClampRange](eb5aca7d-cfec-2f67-b204-049c45bcc8c7.htm) |  |
| 公共方法 | [SetPulseVLevel](539a48b4-67dd-3f23-662a-49d2a01e299a.htm) |  |
| 公共方法 | [SetPulseVLevelRange](e20539f1-4f02-f231-9960-62a0c08690a8.htm) |  |
| 公共方法 | [SetRecordLength](098d4c1c-e0b8-6919-575c-8f147916c5c8.htm) |  |
| 公共方法 | [SetSamplesToAverage](cb0e87f3-79e7-4a3c-86de-a16ecaa3a4be.htm) |  |
| 公共方法 | [SetSense](db4ebde5-b8a9-7784-dd47-308f927986a0.htm) |  |
| 公共方法 | [SetSequence(String, Double)](ae3e9c56-2e32-092b-1dc2-2bfa946aeb57.htm) |  |
| 公共方法 | [SetSequence(String, Double, Double)](93605146-90e9-2f9a-b699-068ab16a3595.htm) |  |
| 公共方法 | [SetSequenceLoopCountFinite](d2e499db-00af-935b-f5e0-e2cfa33f4a9d.htm) |  |
| 公共方法 | [SetSequenceStepDeltaTime](d3398b01-dbd4-c7a0-5313-d8526abea7e8.htm) |  |
| 公共方法 | [SetSequenceStepDeltaTimeEnabled](f6d58daf-3618-111b-b9eb-80e4b544ac62.htm) |  |
| 公共方法 | [SetSourceDelay](539bca22-270e-a5e0-5501-0c1feaa700b3.htm) |  |
| 公共方法 | [SetSourceMode](10a0ed45-fcc7-af9e-8359-661e899a2b21.htm) |  |
| 公共方法 | [SetTransientResponse](0b19ee05-d1aa-655b-7ef5-7fd582bb6556.htm) |  |
| 公共方法 | [SetVClamp](f365c354-156f-ceaa-928f-92511120b80a.htm) |  |
| 公共方法 | [SetVClampAutorange](fb89e179-1088-7dd2-8fc4-0793319db786.htm) |  |
| 公共方法 | [SetVClampHigh](9d8cdd3f-e619-e768-89e4-a4bf2a7d5937.htm) |  |
| 公共方法 | [SetVClampLow](3c023b20-2f3e-63c4-0424-b1c7d51e3b95.htm) |  |
| 公共方法 | [SetVClampRange](0a10b45e-bd48-8c36-c23d-e31cc34fe6e8.htm) |  |
| 公共方法 | [SetVLevel](ee056303-4ba6-6ce5-3b37-f0ab8e43baf4.htm) |  |
| 公共方法 | [SetVLevelAutorange](b43b8979-b425-4a58-470a-75b6dfa7623b.htm) |  |
| 公共方法 | [SetVLevelRange](88f3ad10-89a5-4ab1-8177-da0a624444e7.htm) |  |
| 公共方法 | [VForce(String, Double)](e51fbd2f-f9fd-ff2f-51a9-7aad835cbafc.htm) |  |
| 公共方法 | [VForce(String, Double, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, String, String)](eb70ebd1-b17f-8579-76b2-6d4026d05399.htm) |  |
| 公共方法 | [VForceIMeasure](69da4a98-be2c-396a-951f-981d6957ed97.htm) |  |
| 公共方法 | [VForceVMeasure](1f3d6fe8-b20c-6237-ad87-293d9392ce14.htm) |  |
| 公共方法 | [VIMeasure](e28ee4b0-eaeb-08b7-f6a7-8cc35bf392cc.htm) |  |
| 公共方法 | [VMeasure](e6912eaf-920f-1765-3487-df32639f36b3.htm) |  |
| 公共方法 | [VPulse](4e20eb43-0e0c-b9da-aefc-bdd066a749c0.htm) |  |
| 公共方法 | [VPulseIMeasure](cd4e9007-eff1-8cd0-c8c2-26a1378f8789.htm) |  |
| 公共方法 | [VPulseVMeasure](58d545c9-3750-b663-757b-7133d13898e2.htm) |  |
| 公共方法 | [WaitForEvent](37a93bc3-625b-3f99-f1a2-cf8fd586b0e4.htm) |  |
| 公共方法 | [WriteString](00f0057f-4c74-8302-a886-b9721cd42771.htm) |  |

[Top](#PageHeader)

参见

##### 引用

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


### IDCVI_Instr 方法

|  |  |
| --- | --- |
|  | IDCVI\_Instr 方法 |

[IDCVI\_Instr](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Abort](2acd8c07-8588-699d-7422-737ec432371c.htm) |  |
| 公共方法 | [Commit](94975378-1059-323c-5d8d-25d5c8766dd6.htm) |  |
| 公共方法 | [ConfigureDigitalEdgeTrigger](344d8048-944b-0104-d6d4-37264864cf17.htm) |  |
| 公共方法 | [ConfigureSoftwareTrigger](67814703-77ea-036f-f6f2-878b0a6c1b5c.htm) |  |
| 公共方法 | [Disable](eb974e34-2ecf-ed81-1f51-2adad4a13b05.htm) |  |
| 公共方法 | [DisableTrigger](029ec745-3627-aa39-6f46-079fb88206d7.htm) |  |
| 公共方法 | [ExportSignal](da01d787-9798-af92-2524-49c67f7c98c4.htm) |  |
| 公共方法 | [Fetch](e6b3bd22-f9c1-2ce7-a409-2cee03551d35.htm) |  |
| 公共方法 | [GetApertureTime](365ee2e0-9c7d-eded-3efb-f58847a908cf.htm) |  |
| 公共方法 | [GetAutoZero](7b3f251e-a185-821d-3a13-e16a3734cd14.htm) |  |
| 公共方法 | [GetBufferSize](f9e28aab-1770-5f3b-11aa-09ca02c3fb21.htm) |  |
| 公共方法 | [GetIClamp](6e330b65-1822-2e74-e790-36c46ad0caaf.htm) |  |
| 公共方法 | [GetIClampAutorange](f0b3938b-5919-8224-d613-80e7a3d99899.htm) |  |
| 公共方法 | [GetIClampHigh](8dedaf11-bcd9-2b75-09f8-da9c4c1a1d96.htm) |  |
| 公共方法 | [GetIClampLow](dd1da9f1-ce4a-07ec-9193-06d1fd629529.htm) |  |
| 公共方法 | [GetIClampRange](fc58f53a-f5ef-d544-60f4-4923d4bbb637.htm) |  |
| 公共方法 | [GetILevel](518cc30c-95a3-c0ee-fff6-91168c93648c.htm) |  |
| 公共方法 | [GetILevelAutorange](dc8a414d-3623-7335-8200-7ad71bf3a954.htm) |  |
| 公共方法 | [GetILevelRange](9549f8cc-6c40-ecbf-5521-bb2a8ea670df.htm) |  |
| 公共方法 | [GetIsRecordLengthFinite](d6e2ae42-d9b7-9f6e-1d08-a5b84b6b08a1.htm) |  |
| 公共方法 | [GetMeasureDelay](e382bebb-15ce-8bac-9ff5-c39782f9f9c4.htm) |  |
| 公共方法 | [GetMeasureWhen](67e6b322-8511-5631-b671-b4614e06d1a7.htm) |  |
| 公共方法 | [GetOutputConnected](62eb291c-44e3-ade7-8e05-3bf1a9d47531.htm) |  |
| 公共方法 | [GetOutputEnabled](38c3ef65-cd6d-2809-876a-5c1e5331d725.htm) |  |
| 公共方法 | [GetOutputFunction](d2c16591-c258-2c9e-09bc-907ef3af08bf.htm) |  |
| 公共方法 | [GetOutputResistance](ef0ca39b-b877-fcf1-24bb-271ccf6c9980.htm) |  |
| 公共方法 | [GetOvpEnabled](bc897a40-ef78-cb20-83b3-9cd909c211d5.htm) |  |
| 公共方法 | [GetOvpLimit](eec1a132-cb80-6b6c-4827-72d812318752.htm) |  |
| 公共方法 | [GetPulseBiasDelay](f00e32a5-62bb-5fa7-1fb1-7af693144699.htm) |  |
| 公共方法 | [GetPulseBiasIClamp](715e4b57-21c6-cc15-cef5-41212e734678.htm) |  |
| 公共方法 | [GetPulseBiasIClampHigh](f00588d5-5984-b079-f3db-168f7b6f8fe4.htm) |  |
| 公共方法 | [GetPulseBiasIClampLow](e0d7e770-dd61-7cb0-8a6a-469584c53be9.htm) |  |
| 公共方法 | [GetPulseBiasILevel](a47fbfd0-accf-8fa2-5bf6-4fa90488a0f7.htm) |  |
| 公共方法 | [GetPulseBiasVClamp](e9ff5d70-b2a0-54db-82da-5505dd5d4c04.htm) |  |
| 公共方法 | [GetPulseBiasVClampHigh](ccf463de-bfb0-17da-fe80-b1b9f9c4e168.htm) |  |
| 公共方法 | [GetPulseBiasVClampLow](c903b77f-7a3f-ac84-f422-012b7e24b9df.htm) |  |
| 公共方法 | [GetPulseBiasVLevel](c2325e02-c0a9-6941-6b58-10e49de50d16.htm) |  |
| 公共方法 | [GetPulseIClamp](94906a71-9848-42d8-89f9-0f91ee33dd01.htm) |  |
| 公共方法 | [GetPulseIClampHigh](d6295cf0-451d-d1b6-3278-239b5b841130.htm) |  |
| 公共方法 | [GetPulseIClampLow](9371e9c2-c8a2-78ce-eff8-b3719c58cda5.htm) |  |
| 公共方法 | [GetPulseIClampRange](1a2c2f3f-b1f4-e999-b0f3-56cb94b7b607.htm) |  |
| 公共方法 | [GetPulseILevel](5740c479-5767-86b4-441f-db3f4fac2d22.htm) |  |
| 公共方法 | [GetPulseILevelRange](3c4ac7ab-b284-6c43-fd13-7299ca134b5b.htm) |  |
| 公共方法 | [GetPulseOffTime](0f94fdfe-705f-01f9-20f2-30f5b1fc2e88.htm) |  |
| 公共方法 | [GetPulseOnTime](fa541fcd-3f39-e2dd-e2ef-461471b5e573.htm) |  |
| 公共方法 | [GetPulseVClamp](7f626923-6971-e4c3-3a65-4178c8050a35.htm) |  |
| 公共方法 | [GetPulseVClampHigh](5f061325-973d-f98d-7028-9752478ff2b3.htm) |  |
| 公共方法 | [GetPulseVClampLow](bf72ef31-e9ab-b788-1cd8-7ff81736b92a.htm) |  |
| 公共方法 | [GetPulseVClampRange](20c224be-df9c-e7a5-3c9b-69faa201be6b.htm) |  |
| 公共方法 | [GetPulseVLevel](8fe74e2d-f3c2-23d8-dac2-7dfaaa81a8f0.htm) |  |
| 公共方法 | [GetPulseVLevelRange](c41c9d07-0f57-bcdb-3069-c42c8ad7757a.htm) |  |
| 公共方法 | [GetRecordLength](df993ad4-fdff-d83d-1dd5-dab498624763.htm) |  |
| 公共方法 | [GetSamplesToAverage](79c88242-a06d-9f55-7191-2d7aff7317bd.htm) |  |
| 公共方法 | [GetSense](41730040-636c-4381-971c-2080a8c96468.htm) |  |
| 公共方法 | [GetSequenceLoopCountFinite](a66f1ca6-2c8b-bf20-5e85-b0cdf443bf1f.htm) |  |
| 公共方法 | [GetSequenceStepDeltaTime](a1a8d4d3-35f4-5454-b62e-2c8a5757857c.htm) |  |
| 公共方法 | [GetSequenceStepDeltaTimeEnabled](0bcd7296-7256-65cc-0bc6-d419d4636c68.htm) |  |
| 公共方法 | [GetSourceDelay](238bbc15-dfc7-af4e-625a-e7b986e46aa1.htm) |  |
| 公共方法 | [GetSourceMode](ebc86bf5-6547-dca2-a3e3-aace05e2d2ae.htm) |  |
| 公共方法 | [GetTransientResponse](2e8adc37-7468-79d1-5cfd-6f643e774956.htm) |  |
| 公共方法 | [GetVClamp](0d102fa4-eb77-a875-179d-ae1277b25d6d.htm) |  |
| 公共方法 | [GetVClampAutorange](e9db9165-8fa0-50e1-18ab-0e0e9bc9464e.htm) |  |
| 公共方法 | [GetVClampHigh](6885b871-7dfa-ce43-3739-5a6cd47ecd25.htm) |  |
| 公共方法 | [GetVClampLow](f6a89c24-8334-8358-09b9-e401e054ba0f.htm) |  |
| 公共方法 | [GetVClampRange](4bfafefc-4147-3979-96a7-4b66e63e0d0e.htm) |  |
| 公共方法 | [GetVLevel](7d017f2a-44f5-7ddb-97b7-6c0bc2906569.htm) |  |
| 公共方法 | [GetVLevelAutorange](c309d4f3-22c1-d8d5-67b0-54b2d9a2352b.htm) |  |
| 公共方法 | [GetVLevelRange](1087199d-6e32-c1fb-f9dc-5181da7b9171.htm) |  |
| 公共方法 | [IForce(String, Double)](5bc8f260-367a-2799-ba6d-f4bd30b34d07.htm) |  |
| 公共方法 | [IForce(String, Double, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, String, String)](fafedf90-ce21-386e-a9a9-70ac5a33f8ff.htm) |  |
| 公共方法 | [IForceIMeasure](eb9e25fc-e804-3732-7981-8285d7118cb0.htm) |  |
| 公共方法 | [IForceVMeasure](2a6fb23d-7e03-5f5b-ea4b-1629f0f34d3c.htm) |  |
| 公共方法 | [IMeasure](d46c8640-26c6-d89c-7754-f91ccaa5065f.htm) |  |
| 公共方法 | [Initiate](6d51cee8-48e3-af6d-66fd-3614451f4af0.htm) |  |
| 公共方法 | [IPulse](886b325d-dbac-6791-af9d-63382905e085.htm) |  |
| 公共方法 | [IPulseIMeasure](805fcc8f-a37e-4ddd-1ad7-742b28700c60.htm) |  |
| 公共方法 | [IPulseVMeasure](c54ccf00-7431-c361-0ccb-e3b9a6ab40bb.htm) |  |
| 公共方法 | [QueryInCompliance](98c65b4a-5ca2-ba5b-86d4-252095589d7e.htm) |  |
| 公共方法 | [QueryOutputState](130e45bb-3339-cc73-c6fb-977e9d9461bc.htm) |  |
| 公共方法 | [ReadState](f5f3767b-2208-bcd3-9ffd-4cc13d5d2c38.htm) |  |
| 公共方法 | [ReadString](786d91b5-2651-266c-a4aa-9d5281169440.htm) |  |
| 公共方法 | [Reset](29b792b4-d0ef-934a-0a1b-e0febaf4707c.htm) |  |
| 公共方法 | [ResetDevice](8fcdaacb-c496-83ef-80c2-300848ee896c.htm) |  |
| 公共方法 | [SelfCalibrate](697bae8e-f808-f6c9-5853-1191988113a8.htm) |  |
| 公共方法 | [SelfTest](0de454f1-0c6b-b0fb-74b8-6d57eaba9bc5.htm) |  |
| 公共方法 | [SendSoftwareTrigger](db4aba7c-d8da-1b23-5a32-2c59c9794f4f.htm) |  |
| 公共方法 | [SetApertureTime](edad480e-0601-3bb1-55c4-a382371b557a.htm) |  |
| 公共方法 | [SetAutoZero](3ac7f39b-0f61-21f3-7cf0-b5ccc737f6a4.htm) |  |
| 公共方法 | [SetBufferSize](20a73a9b-480d-5e1c-be39-30f6cb5f2162.htm) |  |
| 公共方法 | [SetIClamp](3d3695db-8634-beec-3f8e-3934ea320e6a.htm) |  |
| 公共方法 | [SetIClampAutorange](f7709ffe-e60c-db14-2345-e7b1de52c662.htm) |  |
| 公共方法 | [SetIClampHigh](222cbf1e-69a3-1a0e-9673-d43abbcbc030.htm) |  |
| 公共方法 | [SetIClampLow](3e821cf1-3b78-cf36-53e2-f80cc96b0261.htm) |  |
| 公共方法 | [SetIClampRange](cc0e4d02-2ff9-571a-8690-1e2aa239a44d.htm) |  |
| 公共方法 | [SetILevel](05849a37-1296-9a76-75fc-6a2410d8a4c8.htm) |  |
| 公共方法 | [SetILevelAutorange](0677a50a-d716-c9e6-14fd-df03ce2cb774.htm) |  |
| 公共方法 | [SetILevelRange](47be3f96-2e36-2236-0b69-f2d56acb7a72.htm) |  |
| 公共方法 | [SetIsRecordLengthFinite](82e3323e-ef79-615f-3382-c4bbec02b539.htm) |  |
| 公共方法 | [SetMeasureDelay](615df8c9-2e2e-5d6f-8b73-5eef37ef97e2.htm) |  |
| 公共方法 | [SetMeasureWhen](d54084c4-fd17-f1bc-d4c1-f2909b2a3bd7.htm) |  |
| 公共方法 | [SetOutputConnected](bcb401b5-3e6f-b610-f1d0-65dc91977877.htm) |  |
| 公共方法 | [SetOutputEnabled](f34ef6f4-9f4a-1bc9-7ca4-a349f0aa62a0.htm) |  |
| 公共方法 | [SetOutputFunction](a1eb8805-2dfa-36bb-8433-cf80e7f9af8e.htm) |  |
| 公共方法 | [SetOutputResistance](cf748160-f40f-74b3-ef81-d255779847bf.htm) |  |
| 公共方法 | [SetOvpEnabled](f9f6b2dc-e4d4-e5ea-87ac-eb43c2a15b9b.htm) |  |
| 公共方法 | [SetOvpLimit](6aa60158-ffcf-3622-c7fc-f1f1d262d095.htm) |  |
| 公共方法 | [SetPulseBiasDelay](06a45db7-9b84-aacd-933c-0efc17a9a94b.htm) |  |
| 公共方法 | [SetPulseBiasIClamp](052579c4-e825-807b-3ad6-9841705bdd12.htm) |  |
| 公共方法 | [SetPulseBiasIClampHigh](2bb3cc1b-6b43-7f58-8850-0def4ded99db.htm) |  |
| 公共方法 | [SetPulseBiasIClampLow](349ea2a1-74ae-03e2-4609-1c40a63bee54.htm) |  |
| 公共方法 | [SetPulseBiasILevel](f20b521c-10aa-2fef-fa51-94dbb68ba77e.htm) |  |
| 公共方法 | [SetPulseBiasVClamp](d527f9ed-bba4-e99e-c031-e843715873c8.htm) |  |
| 公共方法 | [SetPulseBiasVClampHigh](61c4eed3-38f3-7abd-0a1e-5d47a32d03a9.htm) |  |
| 公共方法 | [SetPulseBiasVClampLow](4057b187-0348-e066-f6df-69e8e6c242c8.htm) |  |
| 公共方法 | [SetPulseBiasVLevel](b83005c4-1e44-fb4a-7d91-4b385a5e9960.htm) |  |
| 公共方法 | [SetPulseIClamp](8b6f3d8b-c2fe-304d-91a4-1f475d36cf9d.htm) |  |
| 公共方法 | [SetPulseIClampHigh](a354fc9c-28e3-3242-2d8f-dedb1df37563.htm) |  |
| 公共方法 | [SetPulseIClampLow](4774bccd-0e91-fdae-8ef3-70afc3316fb0.htm) |  |
| 公共方法 | [SetPulseIClampRange](089aa55c-b73e-60b1-ae26-2734f50d9775.htm) |  |
| 公共方法 | [SetPulseILevel](325fc4d0-4c61-5786-0ad0-c58858e52dc8.htm) |  |
| 公共方法 | [SetPulseILevelRange](9e822093-f731-aa26-46d9-8d067148658b.htm) |  |
| 公共方法 | [SetPulseOffTime](6e4c530c-30ea-216d-edad-8614542442dd.htm) |  |
| 公共方法 | [SetPulseOnTime](c120bc2b-8564-4f7a-99f2-6c3a77a559af.htm) |  |
| 公共方法 | [SetPulseVClamp](e2e62ee9-2f17-41bc-6d3e-995eda34c78b.htm) |  |
| 公共方法 | [SetPulseVClampHigh](6dbe1b10-a60a-f200-524a-866fac5a132f.htm) |  |
| 公共方法 | [SetPulseVClampLow](cf4c0bf5-a365-929d-4f74-ad1f96ab9059.htm) |  |
| 公共方法 | [SetPulseVClampRange](eb5aca7d-cfec-2f67-b204-049c45bcc8c7.htm) |  |
| 公共方法 | [SetPulseVLevel](539a48b4-67dd-3f23-662a-49d2a01e299a.htm) |  |
| 公共方法 | [SetPulseVLevelRange](e20539f1-4f02-f231-9960-62a0c08690a8.htm) |  |
| 公共方法 | [SetRecordLength](098d4c1c-e0b8-6919-575c-8f147916c5c8.htm) |  |
| 公共方法 | [SetSamplesToAverage](cb0e87f3-79e7-4a3c-86de-a16ecaa3a4be.htm) |  |
| 公共方法 | [SetSense](db4ebde5-b8a9-7784-dd47-308f927986a0.htm) |  |
| 公共方法 | [SetSequence(String, Double)](ae3e9c56-2e32-092b-1dc2-2bfa946aeb57.htm) |  |
| 公共方法 | [SetSequence(String, Double, Double)](93605146-90e9-2f9a-b699-068ab16a3595.htm) |  |
| 公共方法 | [SetSequenceLoopCountFinite](d2e499db-00af-935b-f5e0-e2cfa33f4a9d.htm) |  |
| 公共方法 | [SetSequenceStepDeltaTime](d3398b01-dbd4-c7a0-5313-d8526abea7e8.htm) |  |
| 公共方法 | [SetSequenceStepDeltaTimeEnabled](f6d58daf-3618-111b-b9eb-80e4b544ac62.htm) |  |
| 公共方法 | [SetSourceDelay](539bca22-270e-a5e0-5501-0c1feaa700b3.htm) |  |
| 公共方法 | [SetSourceMode](10a0ed45-fcc7-af9e-8359-661e899a2b21.htm) |  |
| 公共方法 | [SetTransientResponse](0b19ee05-d1aa-655b-7ef5-7fd582bb6556.htm) |  |
| 公共方法 | [SetVClamp](f365c354-156f-ceaa-928f-92511120b80a.htm) |  |
| 公共方法 | [SetVClampAutorange](fb89e179-1088-7dd2-8fc4-0793319db786.htm) |  |
| 公共方法 | [SetVClampHigh](9d8cdd3f-e619-e768-89e4-a4bf2a7d5937.htm) |  |
| 公共方法 | [SetVClampLow](3c023b20-2f3e-63c4-0424-b1c7d51e3b95.htm) |  |
| 公共方法 | [SetVClampRange](0a10b45e-bd48-8c36-c23d-e31cc34fe6e8.htm) |  |
| 公共方法 | [SetVLevel](ee056303-4ba6-6ce5-3b37-f0ab8e43baf4.htm) |  |
| 公共方法 | [SetVLevelAutorange](b43b8979-b425-4a58-470a-75b6dfa7623b.htm) |  |
| 公共方法 | [SetVLevelRange](88f3ad10-89a5-4ab1-8177-da0a624444e7.htm) |  |
| 公共方法 | [VForce(String, Double)](e51fbd2f-f9fd-ff2f-51a9-7aad835cbafc.htm) |  |
| 公共方法 | [VForce(String, Double, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, String, String)](eb70ebd1-b17f-8579-76b2-6d4026d05399.htm) |  |
| 公共方法 | [VForceIMeasure](69da4a98-be2c-396a-951f-981d6957ed97.htm) |  |
| 公共方法 | [VForceVMeasure](1f3d6fe8-b20c-6237-ad87-293d9392ce14.htm) |  |
| 公共方法 | [VIMeasure](e28ee4b0-eaeb-08b7-f6a7-8cc35bf392cc.htm) |  |
| 公共方法 | [VMeasure](e6912eaf-920f-1765-3487-df32639f36b3.htm) |  |
| 公共方法 | [VPulse](4e20eb43-0e0c-b9da-aefc-bdd066a749c0.htm) |  |
| 公共方法 | [VPulseIMeasure](cd4e9007-eff1-8cd0-c8c2-26a1378f8789.htm) |  |
| 公共方法 | [VPulseVMeasure](58d545c9-3750-b663-757b-7133d13898e2.htm) |  |
| 公共方法 | [WaitForEvent](37a93bc3-625b-3f99-f1a2-cf8fd586b0e4.htm) |  |
| 公共方法 | [WriteString](00f0057f-4c74-8302-a886-b9721cd42771.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### Abort 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrAbort 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Abort()
```

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### Commit 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrCommit 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Commit()
```

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### ConfigureDigitalEdgeTrigger 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrConfigureDigitalEdgeTrigger 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureDigitalEdgeTrigger(
	string triggerClass,
	string source,
	string edgeType
)
```

###### 参数

triggerClass  String

source  String

edgeType  String

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### ConfigureSoftwareTrigger 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrConfigureSoftwareTrigger 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureSoftwareTrigger(
	string triggerClass
)
```

###### 参数

triggerClass  String

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### Disable 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrDisable 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Disable()
```

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### DisableTrigger 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrDisableTrigger 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void DisableTrigger(
	string triggerClass
)
```

###### 参数

triggerClass  String

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### ExportSignal 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrExportSignal 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ExportSignal(
	string signalSource,
	string outputTerminal
)
```

###### 参数

signalSource  String

outputTerminal  String

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### Fetch 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrFetch 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
(double[] , double[] , bool[] ) Fetch(
	string channelNumber,
	double timeout,
	int pointsToFetch
)
```

###### 参数

channelNumber  String

timeout  Double

pointsToFetch  Int32

###### 返回值

ValueTupleDouble, Double, Boolean

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetApertureTime 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetApertureTime 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetApertureTime(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetAutoZero 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetAutoZero 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetAutoZero(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

String

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetBufferSize 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetBufferSize 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetBufferSize(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetIClamp 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetIClamp 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetIClamp(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetIClampAutorange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetIClampAutorange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool GetIClampAutorange(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Boolean

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetIClampHigh 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetIClampHigh 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetIClampHigh(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetIClampLow 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetIClampLow 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetIClampLow(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetIClampRange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetIClampRange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetIClampRange(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetILevel 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetILevel 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetILevel(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetILevelAutorange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetILevelAutorange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool GetILevelAutorange(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Boolean

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetILevelRange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetILevelRange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetILevelRange(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetIsRecordLengthFinite 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetIsRecordLengthFinite 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool GetIsRecordLengthFinite()
```

###### 返回值

Boolean

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetMeasureDelay 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetMeasureDelay 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetMeasureDelay()
```

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetMeasureWhen 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetMeasureWhen 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetMeasureWhen()
```

###### 返回值

String

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetOutputConnected 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetOutputConnected 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool GetOutputConnected(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Boolean

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetOutputEnabled 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetOutputEnabled 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool GetOutputEnabled(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Boolean

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetOutputFunction 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetOutputFunction 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetOutputFunction(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

String

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetOutputResistance 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetOutputResistance 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetOutputResistance(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetOvpEnabled 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetOvpEnabled 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool GetOvpEnabled(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Boolean

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetOvpLimit 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetOvpLimit 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetOvpLimit(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseBiasDelay 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetPulseBiasDelay 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetPulseBiasDelay(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseBiasIClamp 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetPulseBiasIClamp 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetPulseBiasIClamp(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseBiasIClampHigh 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetPulseBiasIClampHigh 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetPulseBiasIClampHigh(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseBiasIClampLow 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetPulseBiasIClampLow 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetPulseBiasIClampLow(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseBiasILevel 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetPulseBiasILevel 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetPulseBiasILevel(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseBiasVClamp 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetPulseBiasVClamp 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetPulseBiasVClamp(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseBiasVClampHigh 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetPulseBiasVClampHigh 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetPulseBiasVClampHigh(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseBiasVClampLow 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetPulseBiasVClampLow 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetPulseBiasVClampLow(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseBiasVLevel 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetPulseBiasVLevel 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetPulseBiasVLevel(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseIClamp 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetPulseIClamp 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetPulseIClamp(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseIClampHigh 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetPulseIClampHigh 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetPulseIClampHigh(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseIClampLow 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetPulseIClampLow 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetPulseIClampLow(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseIClampRange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetPulseIClampRange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetPulseIClampRange(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseILevel 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetPulseILevel 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetPulseILevel(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseILevelRange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetPulseILevelRange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetPulseILevelRange(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseOffTime 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetPulseOffTime 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetPulseOffTime(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseOnTime 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetPulseOnTime 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetPulseOnTime(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseVClamp 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetPulseVClamp 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetPulseVClamp(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseVClampHigh 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetPulseVClampHigh 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetPulseVClampHigh(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseVClampLow 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetPulseVClampLow 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetPulseVClampLow(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseVClampRange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetPulseVClampRange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetPulseVClampRange(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseVLevel 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetPulseVLevel 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetPulseVLevel(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetPulseVLevelRange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetPulseVLevelRange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetPulseVLevelRange(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetRecordLength 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetRecordLength 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetRecordLength(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Int32

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetSamplesToAverage 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetSamplesToAverage 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetSamplesToAverage(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Int32

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetSense 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetSense 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetSense(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

String

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetSequenceLoopCountFinite 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetSequenceLoopCountFinite 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool GetSequenceLoopCountFinite()
```

###### 返回值

Boolean

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetSequenceStepDeltaTime 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetSequenceStepDeltaTime 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetSequenceStepDeltaTime(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetSequenceStepDeltaTimeEnabled 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetSequenceStepDeltaTimeEnabled 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool GetSequenceStepDeltaTimeEnabled(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Boolean

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetSourceDelay 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetSourceDelay 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetSourceDelay(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetSourceMode 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetSourceMode 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetSourceMode()
```

###### 返回值

String

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetTransientResponse 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetTransientResponse 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetTransientResponse(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

String

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetVClamp 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetVClamp 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetVClamp(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetVClampAutorange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetVClampAutorange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool GetVClampAutorange(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Boolean

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetVClampHigh 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetVClampHigh 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetVClampHigh(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetVClampLow 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetVClampLow 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetVClampLow(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetVClampRange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetVClampRange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetVClampRange(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetVLevel 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetVLevel 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetVLevel(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetVLevelAutorange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetVLevelAutorange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool GetVLevelAutorange(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Boolean

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### GetVLevelRange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrGetVLevelRange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetVLevelRange(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### IForce 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrIForce 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [IForce(String, Double)](5bc8f260-367a-2799-ba6d-f4bd30b34d07.htm) |  |
| 公共方法 | [IForce(String, Double, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, String, String)](fafedf90-ce21-386e-a9a9-70ac5a33f8ff.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


##### IForce(String, Double) 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrIForce(String, Double) 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void IForce(
	string channelNumber,
	double level
)
```

###### 参数

channelNumber  String

level  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[IForce 重载](90604cb1-fd14-f536-db70-46e1a03d1946.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


##### IForce(String, Double, Nullable&lt;Double&gt;, Nullable&lt;Double&gt;, Nullable&lt;Double&gt;, Nullable&lt;Double&gt;, Nullable&lt;Double&gt;, Nullable&lt;Double&gt;, String, String) 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrIForce(String, Double, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, String, String) 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void IForce(
	string channelNumber,
	double forceLevel,
	double? vClamp,
	double? iLevelRange = null,
	double? vClampRange = null,
	double? vClampLow = null,
	double? vClampHigh = null,
	double? sourceDelay = null,
	string sense = null,
	string forceCompleteEventOutputTerminal = null
)
```

###### 参数

channelNumber  String

forceLevel  Double

vClamp  NullableDouble

iLevelRange  NullableDouble  (Optional)

vClampRange  NullableDouble  (Optional)

vClampLow  NullableDouble  (Optional)

vClampHigh  NullableDouble  (Optional)

sourceDelay  NullableDouble  (Optional)

sense  String  (Optional)

forceCompleteEventOutputTerminal  String  (Optional)

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[IForce 重载](90604cb1-fd14-f536-db70-46e1a03d1946.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### IForceIMeasure 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrIForceIMeasure 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] IForceIMeasure(
	string channelNumber,
	double forceLevel,
	double? vClamp = null,
	double? iLevelRange = null,
	double? vClampRange = null,
	double? vClampLow = null,
	double? vClampHigh = null,
	double? apertureTime = null,
	double? sourceDelay = null,
	double? measureDelay = null,
	string sense = null,
	string forceCompleteEventOutputTerminal = null,
	string measureCompleteEventOutputTerminal = null
)
```

###### 参数

channelNumber  String

forceLevel  Double

vClamp  NullableDouble  (Optional)

iLevelRange  NullableDouble  (Optional)

vClampRange  NullableDouble  (Optional)

vClampLow  NullableDouble  (Optional)

vClampHigh  NullableDouble  (Optional)

apertureTime  NullableDouble  (Optional)

sourceDelay  NullableDouble  (Optional)

measureDelay  NullableDouble  (Optional)

sense  String  (Optional)

forceCompleteEventOutputTerminal  String  (Optional)

measureCompleteEventOutputTerminal  String  (Optional)

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### IForceVMeasure 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrIForceVMeasure 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] IForceVMeasure(
	string channelNumber,
	double forceLevel,
	double? vClamp = null,
	double? iLevelRange = null,
	double? vClampRange = null,
	double? vClampLow = null,
	double? vClampHigh = null,
	double? apertureTime = null,
	double? sourceDelay = null,
	double? measureDelay = null,
	string sense = null,
	string forceCompleteEventOutputTerminal = null,
	string measureCompleteEventOutputTerminal = null
)
```

###### 参数

channelNumber  String

forceLevel  Double

vClamp  NullableDouble  (Optional)

iLevelRange  NullableDouble  (Optional)

vClampRange  NullableDouble  (Optional)

vClampLow  NullableDouble  (Optional)

vClampHigh  NullableDouble  (Optional)

apertureTime  NullableDouble  (Optional)

sourceDelay  NullableDouble  (Optional)

measureDelay  NullableDouble  (Optional)

sense  String  (Optional)

forceCompleteEventOutputTerminal  String  (Optional)

measureCompleteEventOutputTerminal  String  (Optional)

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### IMeasure 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrIMeasure 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] IMeasure(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### Initiate 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrInitiate 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Initiate()
```

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### IPulse 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrIPulse 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void IPulse(
	string channelNumber,
	double level
)
```

###### 参数

channelNumber  String

level  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### IPulseIMeasure 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrIPulseIMeasure 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] IPulseIMeasure(
	string channelNumber,
	double pulseLevel
)
```

###### 参数

channelNumber  String

pulseLevel  Double

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### IPulseVMeasure 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrIPulseVMeasure 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] IPulseVMeasure(
	string channelNumber,
	double pulseLevel
)
```

###### 参数

channelNumber  String

pulseLevel  Double

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### QueryInCompliance 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrQueryInCompliance 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool QueryInCompliance(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Boolean

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### QueryOutputState 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrQueryOutputState 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string QueryOutputState(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

String

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### ReadState 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrReadState 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] ReadState(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### ReadString 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrReadString 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

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

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### Reset 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrReset 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Reset()
```

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### ResetDevice 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrResetDevice 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ResetDevice()
```

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SelfCalibrate 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSelfCalibrate 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SelfCalibrate(
	string channelNumber
)
```

###### 参数

channelNumber  String

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SelfTest 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSelfTest 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SelfTest()
```

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SendSoftwareTrigger 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSendSoftwareTrigger 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SendSoftwareTrigger(
	string triggerClass
)
```

###### 参数

triggerClass  String

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetApertureTime 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetApertureTime 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetApertureTime(
	string channelNumber,
	double apertureTime
)
```

###### 参数

channelNumber  String

apertureTime  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetAutoZero 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetAutoZero 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetAutoZero(
	string channelNumber,
	string autoZero
)
```

###### 参数

channelNumber  String

autoZero  String

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetBufferSize 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetBufferSize 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetBufferSize(
	string channelNumber,
	ulong Size
)
```

###### 参数

channelNumber  String

Size  UInt64

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetIClamp 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetIClamp 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetIClamp(
	string channelNumber,
	double limit
)
```

###### 参数

channelNumber  String

limit  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetIClampAutorange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetIClampAutorange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetIClampAutorange(
	string channelNumber,
	bool autorange
)
```

###### 参数

channelNumber  String

autorange  Boolean

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetIClampHigh 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetIClampHigh 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetIClampHigh(
	string channelNumber,
	double high
)
```

###### 参数

channelNumber  String

high  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetIClampLow 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetIClampLow 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetIClampLow(
	string channelNumber,
	double low
)
```

###### 参数

channelNumber  String

low  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetIClampRange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetIClampRange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetIClampRange(
	string channelNumber,
	double range
)
```

###### 参数

channelNumber  String

range  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetILevel 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetILevel 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetILevel(
	string channelNumber,
	double level
)
```

###### 参数

channelNumber  String

level  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetILevelAutorange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetILevelAutorange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetILevelAutorange(
	string channelNumber,
	bool autorange
)
```

###### 参数

channelNumber  String

autorange  Boolean

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetILevelRange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetILevelRange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetILevelRange(
	string channelNumber,
	double range
)
```

###### 参数

channelNumber  String

range  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetIsRecordLengthFinite 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetIsRecordLengthFinite 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetIsRecordLengthFinite(
	bool value
)
```

###### 参数

value  Boolean

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetMeasureDelay 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetMeasureDelay 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetMeasureDelay(
	double delay
)
```

###### 参数

delay  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetMeasureWhen 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetMeasureWhen 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetMeasureWhen(
	string measureWhen
)
```

###### 参数

measureWhen  String

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetOutputConnected 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetOutputConnected 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetOutputConnected(
	string channelNumber,
	bool connected
)
```

###### 参数

channelNumber  String

connected  Boolean

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetOutputEnabled 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetOutputEnabled 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetOutputEnabled(
	string channelNumber,
	bool enabled
)
```

###### 参数

channelNumber  String

enabled  Boolean

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetOutputFunction 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetOutputFunction 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetOutputFunction(
	string channelNumber,
	string outputFunction
)
```

###### 参数

channelNumber  String

outputFunction  String

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetOutputResistance 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetOutputResistance 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetOutputResistance(
	string channelNumber,
	double resistance
)
```

###### 参数

channelNumber  String

resistance  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetOvpEnabled 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetOvpEnabled 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetOvpEnabled(
	string channelNumber,
	bool OvpEnabled
)
```

###### 参数

channelNumber  String

OvpEnabled  Boolean

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetOvpLimit 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetOvpLimit 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetOvpLimit(
	string channelNumber,
	double limit
)
```

###### 参数

channelNumber  String

limit  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseBiasDelay 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetPulseBiasDelay 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPulseBiasDelay(
	string channelNumber,
	double delay
)
```

###### 参数

channelNumber  String

delay  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseBiasIClamp 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetPulseBiasIClamp 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPulseBiasIClamp(
	string channelNumber,
	double limit
)
```

###### 参数

channelNumber  String

limit  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseBiasIClampHigh 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetPulseBiasIClampHigh 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPulseBiasIClampHigh(
	string channelNumber,
	double high
)
```

###### 参数

channelNumber  String

high  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseBiasIClampLow 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetPulseBiasIClampLow 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPulseBiasIClampLow(
	string channelNumber,
	double low
)
```

###### 参数

channelNumber  String

low  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseBiasILevel 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetPulseBiasILevel 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPulseBiasILevel(
	string channelNumber,
	double level
)
```

###### 参数

channelNumber  String

level  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseBiasVClamp 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetPulseBiasVClamp 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPulseBiasVClamp(
	string channelNumber,
	double limit
)
```

###### 参数

channelNumber  String

limit  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseBiasVClampHigh 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetPulseBiasVClampHigh 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPulseBiasVClampHigh(
	string channelNumber,
	double high
)
```

###### 参数

channelNumber  String

high  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseBiasVClampLow 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetPulseBiasVClampLow 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPulseBiasVClampLow(
	string channelNumber,
	double low
)
```

###### 参数

channelNumber  String

low  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseBiasVLevel 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetPulseBiasVLevel 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPulseBiasVLevel(
	string channelNumber,
	double level
)
```

###### 参数

channelNumber  String

level  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseIClamp 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetPulseIClamp 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPulseIClamp(
	string channelNumber,
	double limit
)
```

###### 参数

channelNumber  String

limit  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseIClampHigh 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetPulseIClampHigh 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPulseIClampHigh(
	string channelNumber,
	double high
)
```

###### 参数

channelNumber  String

high  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseIClampLow 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetPulseIClampLow 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPulseIClampLow(
	string channelNumber,
	double low
)
```

###### 参数

channelNumber  String

low  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseIClampRange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetPulseIClampRange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPulseIClampRange(
	string channelNumber,
	double range
)
```

###### 参数

channelNumber  String

range  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseILevel 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetPulseILevel 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPulseILevel(
	string channelNumber,
	double level
)
```

###### 参数

channelNumber  String

level  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseILevelRange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetPulseILevelRange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPulseILevelRange(
	string channelNumber,
	double range
)
```

###### 参数

channelNumber  String

range  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseOffTime 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetPulseOffTime 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPulseOffTime(
	string channelNumber,
	double time
)
```

###### 参数

channelNumber  String

time  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseOnTime 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetPulseOnTime 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPulseOnTime(
	string channelNumber,
	double time
)
```

###### 参数

channelNumber  String

time  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseVClamp 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetPulseVClamp 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPulseVClamp(
	string channelNumber,
	double limit
)
```

###### 参数

channelNumber  String

limit  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseVClampHigh 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetPulseVClampHigh 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPulseVClampHigh(
	string channelNumber,
	double high
)
```

###### 参数

channelNumber  String

high  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseVClampLow 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetPulseVClampLow 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPulseVClampLow(
	string channelNumber,
	double low
)
```

###### 参数

channelNumber  String

low  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseVClampRange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetPulseVClampRange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPulseVClampRange(
	string channelNumber,
	double range
)
```

###### 参数

channelNumber  String

range  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseVLevel 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetPulseVLevel 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPulseVLevel(
	string channelNumber,
	double level
)
```

###### 参数

channelNumber  String

level  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetPulseVLevelRange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetPulseVLevelRange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPulseVLevelRange(
	string channelNumber,
	double range
)
```

###### 参数

channelNumber  String

range  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetRecordLength 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetRecordLength 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetRecordLength(
	string channelNumber,
	int recordLength
)
```

###### 参数

channelNumber  String

recordLength  Int32

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetSamplesToAverage 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetSamplesToAverage 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSamplesToAverage(
	string channelNumber,
	int samples
)
```

###### 参数

channelNumber  String

samples  Int32

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetSense 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetSense 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSense(
	string channelNumber,
	string sense
)
```

###### 参数

channelNumber  String

sense  String

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetSequence 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetSequence 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [SetSequence(String, Double)](ae3e9c56-2e32-092b-1dc2-2bfa946aeb57.htm) |  |
| 公共方法 | [SetSequence(String, Double, Double)](93605146-90e9-2f9a-b699-068ab16a3595.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


##### SetSequence(String, Double[]) 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetSequence(String, Double) 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSequence(
	string channelNumber,
	double[] values
)
```

###### 参数

channelNumber  String

values  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[SetSequence 重载](b4da7dcd-e8ab-5939-5a58-ef7e0c096037.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


##### SetSequence(String, Double[], Double[]) 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetSequence(String, Double, Double) 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSequence(
	string channelNumber,
	double[] values,
	double[] sourceDelays
)
```

###### 参数

channelNumber  String

values  Double

sourceDelays  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[SetSequence 重载](b4da7dcd-e8ab-5939-5a58-ef7e0c096037.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetSequenceLoopCountFinite 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetSequenceLoopCountFinite 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSequenceLoopCountFinite(
	bool isFinite
)
```

###### 参数

isFinite  Boolean

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetSequenceStepDeltaTime 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetSequenceStepDeltaTime 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSequenceStepDeltaTime(
	string channelNumber,
	double time
)
```

###### 参数

channelNumber  String

time  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetSequenceStepDeltaTimeEnabled 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetSequenceStepDeltaTimeEnabled 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSequenceStepDeltaTimeEnabled(
	string channelNumber,
	bool deltaTimeEnabled
)
```

###### 参数

channelNumber  String

deltaTimeEnabled  Boolean

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetSourceDelay 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetSourceDelay 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSourceDelay(
	string channelNumber,
	double delay
)
```

###### 参数

channelNumber  String

delay  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetSourceMode 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetSourceMode 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSourceMode(
	string sourceMode
)
```

###### 参数

sourceMode  String

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetTransientResponse 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetTransientResponse 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetTransientResponse(
	string channelNumber,
	string response
)
```

###### 参数

channelNumber  String

response  String

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetVClamp 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetVClamp 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetVClamp(
	string channelNumber,
	double limit
)
```

###### 参数

channelNumber  String

limit  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetVClampAutorange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetVClampAutorange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetVClampAutorange(
	string channelNumber,
	bool autorange
)
```

###### 参数

channelNumber  String

autorange  Boolean

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetVClampHigh 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetVClampHigh 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetVClampHigh(
	string channelNumber,
	double high
)
```

###### 参数

channelNumber  String

high  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetVClampLow 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetVClampLow 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetVClampLow(
	string channelNumber,
	double low
)
```

###### 参数

channelNumber  String

low  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetVClampRange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetVClampRange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetVClampRange(
	string channelNumber,
	double range
)
```

###### 参数

channelNumber  String

range  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetVLevel 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetVLevel 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetVLevel(
	string channelNumber,
	double level
)
```

###### 参数

channelNumber  String

level  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetVLevelAutorange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetVLevelAutorange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetVLevelAutorange(
	string channelNumber,
	bool autorange
)
```

###### 参数

channelNumber  String

autorange  Boolean

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### SetVLevelRange 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrSetVLevelRange 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetVLevelRange(
	string channelNumber,
	double range
)
```

###### 参数

channelNumber  String

range  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### VForce 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrVForce 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [VForce(String, Double)](e51fbd2f-f9fd-ff2f-51a9-7aad835cbafc.htm) |  |
| 公共方法 | [VForce(String, Double, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, String, String)](eb70ebd1-b17f-8579-76b2-6d4026d05399.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


##### VForce(String, Double) 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrVForce(String, Double) 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void VForce(
	string channelNumber,
	double level
)
```

###### 参数

channelNumber  String

level  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[VForce 重载](15438159-dae9-6713-6223-3b2bf9fe04d8.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


##### VForce(String, Double, Nullable&lt;Double&gt;, Nullable&lt;Double&gt;, Nullable&lt;Double&gt;, Nullable&lt;Double&gt;, Nullable&lt;Double&gt;, Nullable&lt;Double&gt;, String, String) 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrVForce(String, Double, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, NullableDouble, String, String) 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void VForce(
	string channelNumber,
	double forceLevel,
	double? iClamp,
	double? vLevelRange = null,
	double? iClampRange = null,
	double? iClampLow = null,
	double? iClampHigh = null,
	double? sourceDelay = null,
	string sense = null,
	string forceCompleteEventOutputTerminal = null
)
```

###### 参数

channelNumber  String

forceLevel  Double

iClamp  NullableDouble

vLevelRange  NullableDouble  (Optional)

iClampRange  NullableDouble  (Optional)

iClampLow  NullableDouble  (Optional)

iClampHigh  NullableDouble  (Optional)

sourceDelay  NullableDouble  (Optional)

sense  String  (Optional)

forceCompleteEventOutputTerminal  String  (Optional)

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[VForce 重载](15438159-dae9-6713-6223-3b2bf9fe04d8.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### VForceIMeasure 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrVForceIMeasure 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] VForceIMeasure(
	string channelNumber,
	double forceLevel,
	double? iClamp = null,
	double? vLevelRange = null,
	double? iClampRange = null,
	double? iClampLow = null,
	double? iClampHigh = null,
	double? apertureTime = null,
	double? sourceDelay = null,
	double? measureDelay = null,
	string sense = null,
	string forceCompleteEventOutputTerminal = null,
	string measureCompleteEventOutputTerminal = null
)
```

###### 参数

channelNumber  String

forceLevel  Double

iClamp  NullableDouble  (Optional)

vLevelRange  NullableDouble  (Optional)

iClampRange  NullableDouble  (Optional)

iClampLow  NullableDouble  (Optional)

iClampHigh  NullableDouble  (Optional)

apertureTime  NullableDouble  (Optional)

sourceDelay  NullableDouble  (Optional)

measureDelay  NullableDouble  (Optional)

sense  String  (Optional)

forceCompleteEventOutputTerminal  String  (Optional)

measureCompleteEventOutputTerminal  String  (Optional)

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### VForceVMeasure 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrVForceVMeasure 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] VForceVMeasure(
	string channelNumber,
	double forceLevel,
	double? iClamp = null,
	double? vLevelRange = null,
	double? iClampRange = null,
	double? iClampLow = null,
	double? iClampHigh = null,
	double? apertureTime = null,
	double? sourceDelay = null,
	double? measureDelay = null,
	string sense = null,
	string forceCompleteEventOutputTerminal = null,
	string measureCompleteEventOutputTerminal = null
)
```

###### 参数

channelNumber  String

forceLevel  Double

iClamp  NullableDouble  (Optional)

vLevelRange  NullableDouble  (Optional)

iClampRange  NullableDouble  (Optional)

iClampLow  NullableDouble  (Optional)

iClampHigh  NullableDouble  (Optional)

apertureTime  NullableDouble  (Optional)

sourceDelay  NullableDouble  (Optional)

measureDelay  NullableDouble  (Optional)

sense  String  (Optional)

forceCompleteEventOutputTerminal  String  (Optional)

measureCompleteEventOutputTerminal  String  (Optional)

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### VIMeasure 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrVIMeasure 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
(double[] , double[] ) VIMeasure(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

ValueTupleDouble, Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### VMeasure 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrVMeasure 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] VMeasure(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### VPulse 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrVPulse 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void VPulse(
	string channelNumber,
	double level
)
```

###### 参数

channelNumber  String

level  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### VPulseIMeasure 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrVPulseIMeasure 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] VPulseIMeasure(
	string channelNumber,
	double pulseLevel
)
```

###### 参数

channelNumber  String

pulseLevel  Double

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### VPulseVMeasure 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrVPulseVMeasure 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] VPulseVMeasure(
	string channelNumber,
	double pulseLevel
)
```

###### 参数

channelNumber  String

pulseLevel  Double

###### 返回值

Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### WaitForEvent 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrWaitForEvent 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WaitForEvent(
	string eventSource,
	double timeout
)
```

###### 参数

eventSource  String

timeout  Double

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)


#### WriteString 方法

|  |  |
| --- | --- |
|  | IDCVI\_InstrWriteString 方法 |

  
**命名空间：** [DCVIParent](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)  
**程序集：** DCVIMeasStation (在 DCVIMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteString(
	string cmd
)
```

###### 参数

cmd  String

参见

###### 引用

[IDCVI\_Instr 接口](e23f526c-5aed-4c07-459b-eccfe9e5e2ac.htm)

[DCVIParent 命名空间](e4ebc076-dc74-fa82-abf7-063ed9d0d14e.htm)

