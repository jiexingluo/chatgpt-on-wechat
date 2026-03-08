|  |  |
| --- | --- |
|  | DmmParent 命名空间 |

类

|  | 类 | 说明 |
| --- | --- | --- |
| 公共类 | [Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm) |  |

接口

|  | 接口 | 说明 |
| --- | --- | --- |
| 公共接口 | [IDmm\_Instr](fd964376-5682-d647-6f9b-65b503f82e00.htm) |  |


## Dmm 类

|  |  |
| --- | --- |
|  | Dmm 类 |

继承层次

SystemObject
  
  MeasStation  
    DmmParentDmm

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public class Dmm : MeasStation
```

Dmm 类型公开以下成员。

构造函数

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Dmm](9aa13bf4-1dd1-7336-1d8e-9002cb301977.htm) | 初始化 Dmm 类的一个新实例 |

[Top](#PageHeader)

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Abort](24dea5c5-a16d-bbae-93f4-a469c4ab4634.htm) | Aborts a previously initiated measurement and returns the DMM to the idle state. |
| 公共方法 | [ConfigureACBandwidth](2959f406-c347-cf7f-326b-b8e6ac5912aa.htm) | Configures FrequencyMin and FrequencyMax for AC measurements. |
| 公共方法 | [ConfigureMeasurement(String, Double, Double)](eb90a008-b2e5-aae1-0a39-0256ece3835f.htm) | Configures measurements by setting Range value. The configured properties include MeasurementFunction, Range, and Resolution in digits. |
| 公共方法 | [ConfigureMeasurement(String, String, Double)](abb91d26-d712-73ce-dd54-4a911b28ff0a.htm) | Configures measurements with AutoRange on. The configured properties include MeasurementFunction, Range, and Resolution in digits. |
| 公共方法 | [ConfigureMeasurementTrigger(String, Boolean)](df804e06-9218-8ca5-5a82-7c99c8835cb7.htm) | Configures trigger-related properties. The properties include Source and DelayAuto. |
| 公共方法 | [ConfigureMeasurementTrigger(String, Double)](f500d975-e22c-6141-b361-8c5b79800b7d.htm) | Configures trigger-related properties. The properties include Source and Delay. |
| 受保护的方法 | [ConfigureMeasurementTriggerPyProxy](f3fb19a7-152d-37ff-9a1e-8dc9dd872681.htm) |  |
| 公共方法 | [ConfigureMultiPoint](c70fa656-b0b9-a4c3-ec25-33860791149f.htm) | Configures properties related to multipoint acquisition. |
| 公共方法 | [ConfigureOpenCableCompensation](142088de-040f-a48b-24f6-4cf8d326b1d9.htm) | Configure the open cable compensation. |
| 公共方法 | [ConfigureRTDCustom](3328bf5c-b76b-30a8-ec87-07ace131d924.htm) | Configures the A, B, and C parameters for a custom RTD. |
| 公共方法 | [ConfigureRTDType](0003f8a9-b5ea-a9c5-5fe1-963d11c68579.htm) | Configures the RTD type and RTD resistance parameters for an RTD. |
| 公共方法 | [ConfigureShortCableCompensation](fb452937-3061-4569-a058-23f44b6e98a4.htm) | Configure the shrot cable compensation. |
| 公共方法 | [ConfigureThermistorCustom](23ecd5cd-716a-5537-5ba5-0c14233b563f.htm) | Configures the A, B, and C parameters for a custom thermistor. |
| 公共方法 | [ConfigureThermocouple](324c890a-e5be-ef18-e127-41e4e99f91a6.htm) | Configures the thermocouple type and reference junction type for a chosen thermocouple. |
| 公共方法 | [ConfigureWaveformAcquisition](4f06b3f4-a2fc-9a0b-70e1-1575c77a323c.htm) | Configures the NI 4070/4071/4072 for waveform acquisitions. |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 公共方法 | [Fetch](e7f251aa-ffbf-29f8-d5a8-e40f222e7a21.htm) | Returns the value from a previously initiated measurement. You must call Initiate before calling this method. |
| 公共方法 | [FetchMultiPoint(Double)](0e71ef51-e3ba-f864-d9f6-3ee37b30563c.htm) | Returns an array of values from a previously initiated multipoint measurement. |
| 公共方法 | [FetchMultiPoint(Double, Int64)](347bc2cb-981b-27da-cc99-a0f745383fda.htm) | Returns an array of values from a previously initiated multipoint measurement. |
| 公共方法 | [FetchWaveform](1afa87f3-5020-b8f0-708f-27003c65e5bb.htm) | Returns an array of values in the form of a waveform datatype from a previously initiated waveform acquisition. |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | [GetAbsoluteResolution](01ca78cc-e2c8-2a22-a30e-15b73f378550.htm) | Gets the measurement resolution in absolute units. |
| 公共方法 | [GetACMaxFrequency](472ff3f8-6010-a2f4-96a4-a05f45583307.htm) | Gets the maximum frequency component of the input signal for AC measurements. |
| 公共方法 | [GetACMinFrequency](7107fbf9-fef8-dc6d-d913-3ab7a5fe88d2.htm) | Gets the minimum frequency component of the input signal for AC measurements. |
| 公共方法 | [GetApertureTime](e4322617-23f0-fca8-1b07-449cb23866cc.htm) | Gets the measurement aperture time for the current configuration. |
| 公共方法 | [GetAttributeBool](90a8941c-cdb7-cf77-0148-8d8c89c4f86e.htm) | Get specific value by attribute identifier. |
| 公共方法 | [GetAttributeDouble](b0de3b96-19de-4f1d-8876-d20a96c8e1c7.htm) | Get specific value by attribute identifier. |
| 公共方法 | [GetAttributeInt](f15f4c49-27a2-f9a2-f1db-909854962e89.htm) | Get specific value by attribute identifier. |
| 公共方法 | [GetAttributeLong](29993667-6db6-40ff-acd5-e217ae544c3e.htm) | Get specific value by attribute identifier. |
| 公共方法 | [GetAttributeString](9d8988b5-71b2-4e95-4461-e21f505102e0.htm) | Get specific value by attribute identifier. |
| 公共方法 | [GetAutoRange](bd4713e1-b232-25f8-d0cd-53ea90cecb59.htm) | Gets whether the range is set automatically by the instrument. |
| 公共方法 | [GetAutoRangeValue](0ed25b65-072f-657e-2bf7-9ea8fc021698.htm) | Gets measurement auto range value. |
| 公共方法 | [GetAutoZero](caa63e4d-4677-cb32-a1ec-77b2a44eed68.htm) | Gets the AutoZero mode. |
| 公共方法 | [GetCableCompensationType](40c7d216-ee64-bde1-2083-2c6b41992993.htm) | Gets the type of cable compensation that is applied to the current capacitance or inductance measurement for the current range. |
| 公共方法 | [GetDiodeCurrentSource](e9df7d55-f257-ba46-5f3a-d4cad731bf98.htm) | Gets the current source provided during diode measurements. |
| 公共方法 | [GetFixedReferenceJunction](aa498882-2010-6008-09f2-c11d7bfb2b9a.htm) | Gets the reference junction temperature when a fixed reference junction is used to take a thermocouple measurement. |
| 公共方法 | [GetFrequencyMeasurementVoltageAutoRange](38db002e-a8fe-1dee-6aea-a64cbeee33f8.htm) | Gets a value indicating whether the frequency voltage is auto-ranging. |
| 公共方法 | [GetFrequencyMeasurementVoltageRange](49bbde56-66c6-0b6d-d2a8-666a4cdfbcd8.htm) | Gets the maximum amplitude of the input signal for frequency measurements. |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | [GetInputResistance](1c29ed99-9aaa-ff07-48ae-933de86cce19.htm) | Gets the input resistance of the instrument. |
| 公共方法 | [GetMeasurementCompleteDestination](febc9c30-312f-87ee-21c8-4f85ea6d2597.htm) | Gets the destination of the measurement complete (MC) signal. |
| 公共方法 | [GetMeasurementCompleteSlope](66eac7d0-2cc5-8ee9-25e1-d6cc0e81b30c.htm) | Gets the polarity of the generated measurement complete signal. |
| 公共方法 | [GetMeasurementFunction](de16ee39-8c70-0d49-b520-cb66a06c548c.htm) | Gets the measurement function. |
| 公共方法 | [GetMeasurementPeriod](df6356ad-4214-a14b-139a-203b9c2c4487.htm) | Gets the number of seconds it takes to make one measurement. |
| 公共方法 | [GetMeasurementTriggerDelay](1e3a11df-f923-e202-9bc1-2e784b658a70.htm) | Gets the time (in seconds) that the DMM waits after it has received a trigger before taking a measurement. |
| 公共方法 | [GetMeasurementTriggerDelayAuto](e01cb992-aa22-7867-b665-318d61c3437b.htm) | Gets a value indicating whether the DMM selects the trigger delay automatically. |
| 公共方法 | [GetMeasurementTriggerSlope](b6ed3f01-c3e5-41a7-c207-faaf03b1b791.htm) | Gets the edge of the signal from the specified trigger source on which the DMM is triggered. |
| 公共方法 | [GetMeasurementTriggerSource](9e0082d3-c1a4-8b6f-9f45-87dd02d92ff3.htm) | Gets the trigger source. |
| 公共方法 | [GetOffsetCompensatedOhmEnabled](9fb4f8da-4443-7a75-5ce2-5517a32a41cc.htm) | Gets whether the compensated ohms are offset. |
| 公共方法 | [GetOperationMode](343b886c-7aba-37a5-13c7-086b31c0de3c.htm) | Gets how the NI 4065 and NI 4070/4071/4072 acquire data. |
| 公共方法 | [GetRange](c7c0f29d-f600-f78b-dea0-51912a93af11.htm) | Gets the measurement range. |
| 公共方法 | [GetResolution](62e9a83d-6ce3-9b13-53c3-bda78c9198c7.htm) | Gets the measurement resolution in digits. |
| 公共方法 | [GetSampleCount](1faa8b0e-8be6-38cc-f76e-26b684323bad.htm) | Gets the number of measurements the DMM takes each time it receives a trigger in a multiple point acquisition. |
| 公共方法 | [GetSampleInterval](c1cd1d03-165f-c172-b38b-a0dbc5a636a2.htm) | Gets the amount of time in seconds the DMM waits between measurement cycles. |
| 公共方法 | [GetSampleTriggerCount](633ed4be-6cd7-6852-a49a-2be0294fd057.htm) | Gets the number of triggers the DMM receives before returning to the Idle state. |
| 公共方法 | [GetSampleTriggerSlope](2d94d2c3-10b2-68e3-0ce4-51012f061262.htm) | Gets the edge of the signal from the specified sample trigger source on which the DMM is triggered. |
| 公共方法 | [GetSampleTriggerSource](ceeee6fa-8566-c29b-d1f4-97778769a509.htm) | Gets the sample trigger source. |
| 公共方法 | [GetThermistorType](64d627b9-6a13-2ec6-cf23-96bd67c56180.htm) | Gets the type of thermistor used to measure the temperature. |
| 公共方法 | [GetTransducerType](c4839581-b58b-3219-4314-b441cb34bc70.htm) | Gets the type of transducer. |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | [GetWaveformCoupling](12b23510-c0cb-fa3a-4122-a3be4f1bf8a2.htm) | Gets the coupling during a waveform acquisition. |
| 公共方法 | [Initiate](3fdd7ee1-3bfb-1898-8400-403a0cb71216.htm) | Initiates an acquisition. |
| 公共方法 | [IsOverRange](055a6807-6dad-5dd3-b1dc-c4f1e09272ff.htm) | Takes a measurement value and determines if the value is a valid measurement or a value indicating that an overrange condition occurred. |
| 公共方法 | [IsUnderRange](207fe455-365c-8528-f322-41b762849bb4.htm) | Takes a measurement value and determines if the value is a valid measurement or a value indicating that an underrange condition occurred. |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [PerformOpenCableCompensation](0f9951fa-c59a-78f2-3225-5682215aac83.htm) | Performs the open cable compensation measurements for the current capacitance/inductance range, and returns open cable compensation conductance and susceptance values. You can use the return values of this method as inputs to ConfigureOpenCableCompensation. |
| 公共方法 | [PerformShortCableCompensation](610ad837-4358-6730-b11b-6ad443350eeb.htm) | Performs the short cable compensation measurements for the current capacitance/inductance range, and returns short cable compensation resistance and reactance values. You can use the return values of this function as inputs to ConfigureShortCableCompensation. |
| 公共方法 | [Read](fd3e75b3-e070-5b64-d4fe-20e7c65b87eb.htm) | Acquires a single measurement and returns the measured value. |
| 公共方法 | [ReadMultiPoint(Double)](323da636-e4b8-b61a-4275-4a2dc1f1dee6.htm) | Acquires multiple measurements and returns an array of values. |
| 公共方法 | [ReadMultiPoint(Double, Int64)](9104eeac-19fc-a522-659f-b41f4aa23104.htm) | Acquires multiple measurements and returns an array of values. |
| 公共方法 | [ReadWaveform](acb5edc3-a20c-3a2e-cc61-50013617e9f7.htm) | Acquires and returns a waveform buffer with values. |
| 公共方法 | [Reset](8b2ebd1b-bb7f-b8f9-1b22-04ccdd3fec07.htm) | Reset the instrument session. |
| 公共方法 | [SendSoftwareTrigger](8027b3a1-4f27-ff95-3599-8fa239ed0eb3.htm) | Sends a command to trigger the DMM. |
| 公共方法 | [SetAbsoluteResolution](344d558c-41ba-a1c2-7bb7-321ddefa12c0.htm) | Sets the measurement resolution in absolute units. |
| 公共方法 | [SetACMaxFrequency](aa2cb351-6354-7379-eb60-066c2e46ac73.htm) | Sets the maximum frequency component of the input signal for AC measurements. |
| 公共方法 | [SetACMinFrequency](61ee5b08-b86c-8bfd-9981-b754c56c68d5.htm) | Sets the minimum frequency component of the input signal for AC measurements. |
| 公共方法 | [SetApertureTime](10c0688c-530f-90bb-7f8b-de40a63b19c6.htm) | Sets the measurement aperture time for the current configuration. |
| 公共方法 | [SetAttributeBool](304b81f5-58e8-3cd4-5736-a00b94e105b0.htm) | Set specific value by attribute identifier. |
| 公共方法 | [SetAttributeDouble](54411e24-944b-1a64-6c41-d0ab68d80e44.htm) | Set specific value by attribute identifier. |
| 公共方法 | [SetAttributeInt](5f5c0523-dfb7-154c-9c60-80391250cf5f.htm) | Set specific value by attribute identifier. |
| 公共方法 | [SetAttributeLong](309f2d1f-9ae1-7252-0236-7d525bffc82c.htm) | Set specific value by attribute identifier. |
| 公共方法 | [SetAttributeString](b84ec545-75b0-220d-d241-1b7a03aa1c65.htm) | Set specific value by attribute identifier. |
| 公共方法 | [SetAutoRange](0708a985-9ef4-2a39-60ad-e37699658b51.htm) | Sets whether the range is set automatically by the instrument. |
| 公共方法 | [SetAutoZero](77672318-9215-11a9-5398-44d212a2140c.htm) | Sets the AutoZero mode. |
| 公共方法 | [SetCableCompensationType](4cd3d5f8-30f7-7514-1b81-35b5a0b72f18.htm) | Sets the type of cable compensation that is applied to the current capacitance or inductance measurement for the current range. |
| 公共方法 | [SetDiodeCurrentSource](203bb930-7ff6-cb75-8944-f42b5f07fb5f.htm) | Sets the current source provided during diode measurements. |
| 公共方法 | [SetFixedReferenceJunction](5476eec0-4627-8d71-8bf3-aac06523f305.htm) | Sets the reference junction temperature when a fixed reference junction is used to take a thermocouple measurement. |
| 公共方法 | [SetFrequencyMeasurementVoltageRange](f439d49b-cdc1-41d6-4ada-bd5b23a6fc01.htm) | Sets the maximum amplitude of the input signal for frequency measurements. If VoltageAutoRange is set to true or if VoltageRange is set to -1.0, the DMM is configured to take an auto-range measurement to calculate the voltage range before each frequency or period measurement. If VoltageAutoRange is set to false or if VoltageRange is set to -2.0, auto-ranging is disabled, and NI-DMM sets the voltage range to the last calculated voltage range. |
| 公共方法 | [SetInputResistance](45950a7d-7b90-75c0-af40-1865c63b90c9.htm) | Sets the input resistance of the instrument. |
| 公共方法 | [SetMeasurementCompleteDestination](3a60f4e2-4ebe-21ad-485d-c8a662bff0be.htm) | Sets the destination of the measurement complete (MC) signal. |
| 公共方法 | [SetMeasurementCompleteSlope](821c155d-1971-7793-809c-1b03bd50b375.htm) | Sets the polarity of the generated measurement complete signal. |
| 公共方法 | [SetMeasurementFunction](0ab46391-b738-93d0-3dc5-17b06b089065.htm) | Sets the measurement function. |
| 公共方法 | [SetMeasurementTriggerDelay](cfa6fb54-26c4-224b-a831-e125ca42e509.htm) | Sets the time (in seconds) that the DMM waits after it has received a trigger before taking a measurement. |
| 公共方法 | [SetMeasurementTriggerDelayAuto](fafeb72b-609f-c567-db48-8a7781e392cb.htm) | Sets a value indicating whether the DMM selects the trigger delay automatically. |
| 公共方法 | [SetMeasurementTriggerSlope](f552c6a6-2f74-dfe7-eb72-78115c07b8c1.htm) | Sets the edge of the signal from the specified trigger source on which the DMM is triggered. |
| 公共方法 | [SetMeasurementTriggerSource](c14783ab-739b-1864-e0c7-d1e44142355c.htm) | Sets the trigger source. |
| 公共方法 | [SetOffsetCompensatedOhmEnabled](20bd0615-ebc6-a0c1-6ab8-c1e2e71a8234.htm) | Sets whether the compensated ohms are offset. |
| 公共方法 | [SetOperationMode](31047bd0-c25b-c0ba-d438-9691ec0b2f3a.htm) | Sets how the NI 4065 and NI 4070/4071/4072 acquire data. When you call ConfigureMeasurement or ConfigureMeasurementDigits, NI-DMM sets this property to IviDmmMode. When you call ConfigureWaveformAcquisition, NI-DMM sets this property to WaveformMode. The default value is IviDmmMode. |
| 公共方法 | [SetRange](5ca22649-6c50-2a37-549e-c3347b31e164.htm) | Sets the measurement range. |
| 公共方法 | [SetResolution](d526b62c-aab7-756b-4aa0-d5e7d4681ae0.htm) | Sets the measurement resolution in digits. |
| 公共方法 | [SetSampleCount](78a6e061-a24c-1531-5b7e-e68371c38acc.htm) | Sets the number of measurements the DMM takes each time it receives a trigger in a multiple point acquisition. |
| 公共方法 | [SetSampleInterval](bff8d2a7-e27c-bb1e-9c79-878c8f62978b.htm) | Sets the amount of time in seconds the DMM waits between measurement cycles. |
| 公共方法 | [SetSampleTriggerCount](ba69fc3e-e820-6e41-58af-1834444693fc.htm) | Sets the number of triggers the DMM receives before returning to the Idle state. |
| 公共方法 | [SetSampleTriggerSlope](b0dee1f4-a523-8e70-95c7-9581edc42746.htm) | Sets the edge of the signal from the specified sample trigger source on which the DMM is triggered. |
| 公共方法 | [SetSampleTriggerSource](587da5cc-c2cb-0e46-d1d6-3f9615d130df.htm) | Sets the sample trigger source. |
| 公共方法 | [SetThermistorType](2c05bd90-94ac-e7f9-0065-fba6823ca15a.htm) | Sets the type of thermistor used to measure the temperature. |
| 公共方法 | [SetTransducerType](e783bec9-39ae-1a98-4f1e-a134503755ec.htm) | Sets the type of transducer. |
| 公共方法 | [SetWaveformCoupling](0d191945-8ba8-2622-6670-0dcfd01b8b58.htm) | Sets the coupling during a waveform acquisition. |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |

[Top](#PageHeader)

参见

##### 引用

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


### Dmm 构造函数

|  |  |
| --- | --- |
|  | Dmm 构造函数 |

初始化 [Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm) 类的一个新实例

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm()
```

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


### Dmm 方法

|  |  |
| --- | --- |
|  | Dmm 方法 |

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Abort](24dea5c5-a16d-bbae-93f4-a469c4ab4634.htm) | Aborts a previously initiated measurement and returns the DMM to the idle state. |
| 公共方法 | [ConfigureACBandwidth](2959f406-c347-cf7f-326b-b8e6ac5912aa.htm) | Configures FrequencyMin and FrequencyMax for AC measurements. |
| 公共方法 | [ConfigureMeasurement(String, Double, Double)](eb90a008-b2e5-aae1-0a39-0256ece3835f.htm) | Configures measurements by setting Range value. The configured properties include MeasurementFunction, Range, and Resolution in digits. |
| 公共方法 | [ConfigureMeasurement(String, String, Double)](abb91d26-d712-73ce-dd54-4a911b28ff0a.htm) | Configures measurements with AutoRange on. The configured properties include MeasurementFunction, Range, and Resolution in digits. |
| 公共方法 | [ConfigureMeasurementTrigger(String, Boolean)](df804e06-9218-8ca5-5a82-7c99c8835cb7.htm) | Configures trigger-related properties. The properties include Source and DelayAuto. |
| 公共方法 | [ConfigureMeasurementTrigger(String, Double)](f500d975-e22c-6141-b361-8c5b79800b7d.htm) | Configures trigger-related properties. The properties include Source and Delay. |
| 受保护的方法 | [ConfigureMeasurementTriggerPyProxy](f3fb19a7-152d-37ff-9a1e-8dc9dd872681.htm) |  |
| 公共方法 | [ConfigureMultiPoint](c70fa656-b0b9-a4c3-ec25-33860791149f.htm) | Configures properties related to multipoint acquisition. |
| 公共方法 | [ConfigureOpenCableCompensation](142088de-040f-a48b-24f6-4cf8d326b1d9.htm) | Configure the open cable compensation. |
| 公共方法 | [ConfigureRTDCustom](3328bf5c-b76b-30a8-ec87-07ace131d924.htm) | Configures the A, B, and C parameters for a custom RTD. |
| 公共方法 | [ConfigureRTDType](0003f8a9-b5ea-a9c5-5fe1-963d11c68579.htm) | Configures the RTD type and RTD resistance parameters for an RTD. |
| 公共方法 | [ConfigureShortCableCompensation](fb452937-3061-4569-a058-23f44b6e98a4.htm) | Configure the shrot cable compensation. |
| 公共方法 | [ConfigureThermistorCustom](23ecd5cd-716a-5537-5ba5-0c14233b563f.htm) | Configures the A, B, and C parameters for a custom thermistor. |
| 公共方法 | [ConfigureThermocouple](324c890a-e5be-ef18-e127-41e4e99f91a6.htm) | Configures the thermocouple type and reference junction type for a chosen thermocouple. |
| 公共方法 | [ConfigureWaveformAcquisition](4f06b3f4-a2fc-9a0b-70e1-1575c77a323c.htm) | Configures the NI 4070/4071/4072 for waveform acquisitions. |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 公共方法 | [Fetch](e7f251aa-ffbf-29f8-d5a8-e40f222e7a21.htm) | Returns the value from a previously initiated measurement. You must call Initiate before calling this method. |
| 公共方法 | [FetchMultiPoint(Double)](0e71ef51-e3ba-f864-d9f6-3ee37b30563c.htm) | Returns an array of values from a previously initiated multipoint measurement. |
| 公共方法 | [FetchMultiPoint(Double, Int64)](347bc2cb-981b-27da-cc99-a0f745383fda.htm) | Returns an array of values from a previously initiated multipoint measurement. |
| 公共方法 | [FetchWaveform](1afa87f3-5020-b8f0-708f-27003c65e5bb.htm) | Returns an array of values in the form of a waveform datatype from a previously initiated waveform acquisition. |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | [GetAbsoluteResolution](01ca78cc-e2c8-2a22-a30e-15b73f378550.htm) | Gets the measurement resolution in absolute units. |
| 公共方法 | [GetACMaxFrequency](472ff3f8-6010-a2f4-96a4-a05f45583307.htm) | Gets the maximum frequency component of the input signal for AC measurements. |
| 公共方法 | [GetACMinFrequency](7107fbf9-fef8-dc6d-d913-3ab7a5fe88d2.htm) | Gets the minimum frequency component of the input signal for AC measurements. |
| 公共方法 | [GetApertureTime](e4322617-23f0-fca8-1b07-449cb23866cc.htm) | Gets the measurement aperture time for the current configuration. |
| 公共方法 | [GetAttributeBool](90a8941c-cdb7-cf77-0148-8d8c89c4f86e.htm) | Get specific value by attribute identifier. |
| 公共方法 | [GetAttributeDouble](b0de3b96-19de-4f1d-8876-d20a96c8e1c7.htm) | Get specific value by attribute identifier. |
| 公共方法 | [GetAttributeInt](f15f4c49-27a2-f9a2-f1db-909854962e89.htm) | Get specific value by attribute identifier. |
| 公共方法 | [GetAttributeLong](29993667-6db6-40ff-acd5-e217ae544c3e.htm) | Get specific value by attribute identifier. |
| 公共方法 | [GetAttributeString](9d8988b5-71b2-4e95-4461-e21f505102e0.htm) | Get specific value by attribute identifier. |
| 公共方法 | [GetAutoRange](bd4713e1-b232-25f8-d0cd-53ea90cecb59.htm) | Gets whether the range is set automatically by the instrument. |
| 公共方法 | [GetAutoRangeValue](0ed25b65-072f-657e-2bf7-9ea8fc021698.htm) | Gets measurement auto range value. |
| 公共方法 | [GetAutoZero](caa63e4d-4677-cb32-a1ec-77b2a44eed68.htm) | Gets the AutoZero mode. |
| 公共方法 | [GetCableCompensationType](40c7d216-ee64-bde1-2083-2c6b41992993.htm) | Gets the type of cable compensation that is applied to the current capacitance or inductance measurement for the current range. |
| 公共方法 | [GetDiodeCurrentSource](e9df7d55-f257-ba46-5f3a-d4cad731bf98.htm) | Gets the current source provided during diode measurements. |
| 公共方法 | [GetFixedReferenceJunction](aa498882-2010-6008-09f2-c11d7bfb2b9a.htm) | Gets the reference junction temperature when a fixed reference junction is used to take a thermocouple measurement. |
| 公共方法 | [GetFrequencyMeasurementVoltageAutoRange](38db002e-a8fe-1dee-6aea-a64cbeee33f8.htm) | Gets a value indicating whether the frequency voltage is auto-ranging. |
| 公共方法 | [GetFrequencyMeasurementVoltageRange](49bbde56-66c6-0b6d-d2a8-666a4cdfbcd8.htm) | Gets the maximum amplitude of the input signal for frequency measurements. |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | [GetInputResistance](1c29ed99-9aaa-ff07-48ae-933de86cce19.htm) | Gets the input resistance of the instrument. |
| 公共方法 | [GetMeasurementCompleteDestination](febc9c30-312f-87ee-21c8-4f85ea6d2597.htm) | Gets the destination of the measurement complete (MC) signal. |
| 公共方法 | [GetMeasurementCompleteSlope](66eac7d0-2cc5-8ee9-25e1-d6cc0e81b30c.htm) | Gets the polarity of the generated measurement complete signal. |
| 公共方法 | [GetMeasurementFunction](de16ee39-8c70-0d49-b520-cb66a06c548c.htm) | Gets the measurement function. |
| 公共方法 | [GetMeasurementPeriod](df6356ad-4214-a14b-139a-203b9c2c4487.htm) | Gets the number of seconds it takes to make one measurement. |
| 公共方法 | [GetMeasurementTriggerDelay](1e3a11df-f923-e202-9bc1-2e784b658a70.htm) | Gets the time (in seconds) that the DMM waits after it has received a trigger before taking a measurement. |
| 公共方法 | [GetMeasurementTriggerDelayAuto](e01cb992-aa22-7867-b665-318d61c3437b.htm) | Gets a value indicating whether the DMM selects the trigger delay automatically. |
| 公共方法 | [GetMeasurementTriggerSlope](b6ed3f01-c3e5-41a7-c207-faaf03b1b791.htm) | Gets the edge of the signal from the specified trigger source on which the DMM is triggered. |
| 公共方法 | [GetMeasurementTriggerSource](9e0082d3-c1a4-8b6f-9f45-87dd02d92ff3.htm) | Gets the trigger source. |
| 公共方法 | [GetOffsetCompensatedOhmEnabled](9fb4f8da-4443-7a75-5ce2-5517a32a41cc.htm) | Gets whether the compensated ohms are offset. |
| 公共方法 | [GetOperationMode](343b886c-7aba-37a5-13c7-086b31c0de3c.htm) | Gets how the NI 4065 and NI 4070/4071/4072 acquire data. |
| 公共方法 | [GetRange](c7c0f29d-f600-f78b-dea0-51912a93af11.htm) | Gets the measurement range. |
| 公共方法 | [GetResolution](62e9a83d-6ce3-9b13-53c3-bda78c9198c7.htm) | Gets the measurement resolution in digits. |
| 公共方法 | [GetSampleCount](1faa8b0e-8be6-38cc-f76e-26b684323bad.htm) | Gets the number of measurements the DMM takes each time it receives a trigger in a multiple point acquisition. |
| 公共方法 | [GetSampleInterval](c1cd1d03-165f-c172-b38b-a0dbc5a636a2.htm) | Gets the amount of time in seconds the DMM waits between measurement cycles. |
| 公共方法 | [GetSampleTriggerCount](633ed4be-6cd7-6852-a49a-2be0294fd057.htm) | Gets the number of triggers the DMM receives before returning to the Idle state. |
| 公共方法 | [GetSampleTriggerSlope](2d94d2c3-10b2-68e3-0ce4-51012f061262.htm) | Gets the edge of the signal from the specified sample trigger source on which the DMM is triggered. |
| 公共方法 | [GetSampleTriggerSource](ceeee6fa-8566-c29b-d1f4-97778769a509.htm) | Gets the sample trigger source. |
| 公共方法 | [GetThermistorType](64d627b9-6a13-2ec6-cf23-96bd67c56180.htm) | Gets the type of thermistor used to measure the temperature. |
| 公共方法 | [GetTransducerType](c4839581-b58b-3219-4314-b441cb34bc70.htm) | Gets the type of transducer. |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | [GetWaveformCoupling](12b23510-c0cb-fa3a-4122-a3be4f1bf8a2.htm) | Gets the coupling during a waveform acquisition. |
| 公共方法 | [Initiate](3fdd7ee1-3bfb-1898-8400-403a0cb71216.htm) | Initiates an acquisition. |
| 公共方法 | [IsOverRange](055a6807-6dad-5dd3-b1dc-c4f1e09272ff.htm) | Takes a measurement value and determines if the value is a valid measurement or a value indicating that an overrange condition occurred. |
| 公共方法 | [IsUnderRange](207fe455-365c-8528-f322-41b762849bb4.htm) | Takes a measurement value and determines if the value is a valid measurement or a value indicating that an underrange condition occurred. |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [PerformOpenCableCompensation](0f9951fa-c59a-78f2-3225-5682215aac83.htm) | Performs the open cable compensation measurements for the current capacitance/inductance range, and returns open cable compensation conductance and susceptance values. You can use the return values of this method as inputs to ConfigureOpenCableCompensation. |
| 公共方法 | [PerformShortCableCompensation](610ad837-4358-6730-b11b-6ad443350eeb.htm) | Performs the short cable compensation measurements for the current capacitance/inductance range, and returns short cable compensation resistance and reactance values. You can use the return values of this function as inputs to ConfigureShortCableCompensation. |
| 公共方法 | [Read](fd3e75b3-e070-5b64-d4fe-20e7c65b87eb.htm) | Acquires a single measurement and returns the measured value. |
| 公共方法 | [ReadMultiPoint(Double)](323da636-e4b8-b61a-4275-4a2dc1f1dee6.htm) | Acquires multiple measurements and returns an array of values. |
| 公共方法 | [ReadMultiPoint(Double, Int64)](9104eeac-19fc-a522-659f-b41f4aa23104.htm) | Acquires multiple measurements and returns an array of values. |
| 公共方法 | [ReadWaveform](acb5edc3-a20c-3a2e-cc61-50013617e9f7.htm) | Acquires and returns a waveform buffer with values. |
| 公共方法 | [Reset](8b2ebd1b-bb7f-b8f9-1b22-04ccdd3fec07.htm) | Reset the instrument session. |
| 公共方法 | [SendSoftwareTrigger](8027b3a1-4f27-ff95-3599-8fa239ed0eb3.htm) | Sends a command to trigger the DMM. |
| 公共方法 | [SetAbsoluteResolution](344d558c-41ba-a1c2-7bb7-321ddefa12c0.htm) | Sets the measurement resolution in absolute units. |
| 公共方法 | [SetACMaxFrequency](aa2cb351-6354-7379-eb60-066c2e46ac73.htm) | Sets the maximum frequency component of the input signal for AC measurements. |
| 公共方法 | [SetACMinFrequency](61ee5b08-b86c-8bfd-9981-b754c56c68d5.htm) | Sets the minimum frequency component of the input signal for AC measurements. |
| 公共方法 | [SetApertureTime](10c0688c-530f-90bb-7f8b-de40a63b19c6.htm) | Sets the measurement aperture time for the current configuration. |
| 公共方法 | [SetAttributeBool](304b81f5-58e8-3cd4-5736-a00b94e105b0.htm) | Set specific value by attribute identifier. |
| 公共方法 | [SetAttributeDouble](54411e24-944b-1a64-6c41-d0ab68d80e44.htm) | Set specific value by attribute identifier. |
| 公共方法 | [SetAttributeInt](5f5c0523-dfb7-154c-9c60-80391250cf5f.htm) | Set specific value by attribute identifier. |
| 公共方法 | [SetAttributeLong](309f2d1f-9ae1-7252-0236-7d525bffc82c.htm) | Set specific value by attribute identifier. |
| 公共方法 | [SetAttributeString](b84ec545-75b0-220d-d241-1b7a03aa1c65.htm) | Set specific value by attribute identifier. |
| 公共方法 | [SetAutoRange](0708a985-9ef4-2a39-60ad-e37699658b51.htm) | Sets whether the range is set automatically by the instrument. |
| 公共方法 | [SetAutoZero](77672318-9215-11a9-5398-44d212a2140c.htm) | Sets the AutoZero mode. |
| 公共方法 | [SetCableCompensationType](4cd3d5f8-30f7-7514-1b81-35b5a0b72f18.htm) | Sets the type of cable compensation that is applied to the current capacitance or inductance measurement for the current range. |
| 公共方法 | [SetDiodeCurrentSource](203bb930-7ff6-cb75-8944-f42b5f07fb5f.htm) | Sets the current source provided during diode measurements. |
| 公共方法 | [SetFixedReferenceJunction](5476eec0-4627-8d71-8bf3-aac06523f305.htm) | Sets the reference junction temperature when a fixed reference junction is used to take a thermocouple measurement. |
| 公共方法 | [SetFrequencyMeasurementVoltageRange](f439d49b-cdc1-41d6-4ada-bd5b23a6fc01.htm) | Sets the maximum amplitude of the input signal for frequency measurements. If VoltageAutoRange is set to true or if VoltageRange is set to -1.0, the DMM is configured to take an auto-range measurement to calculate the voltage range before each frequency or period measurement. If VoltageAutoRange is set to false or if VoltageRange is set to -2.0, auto-ranging is disabled, and NI-DMM sets the voltage range to the last calculated voltage range. |
| 公共方法 | [SetInputResistance](45950a7d-7b90-75c0-af40-1865c63b90c9.htm) | Sets the input resistance of the instrument. |
| 公共方法 | [SetMeasurementCompleteDestination](3a60f4e2-4ebe-21ad-485d-c8a662bff0be.htm) | Sets the destination of the measurement complete (MC) signal. |
| 公共方法 | [SetMeasurementCompleteSlope](821c155d-1971-7793-809c-1b03bd50b375.htm) | Sets the polarity of the generated measurement complete signal. |
| 公共方法 | [SetMeasurementFunction](0ab46391-b738-93d0-3dc5-17b06b089065.htm) | Sets the measurement function. |
| 公共方法 | [SetMeasurementTriggerDelay](cfa6fb54-26c4-224b-a831-e125ca42e509.htm) | Sets the time (in seconds) that the DMM waits after it has received a trigger before taking a measurement. |
| 公共方法 | [SetMeasurementTriggerDelayAuto](fafeb72b-609f-c567-db48-8a7781e392cb.htm) | Sets a value indicating whether the DMM selects the trigger delay automatically. |
| 公共方法 | [SetMeasurementTriggerSlope](f552c6a6-2f74-dfe7-eb72-78115c07b8c1.htm) | Sets the edge of the signal from the specified trigger source on which the DMM is triggered. |
| 公共方法 | [SetMeasurementTriggerSource](c14783ab-739b-1864-e0c7-d1e44142355c.htm) | Sets the trigger source. |
| 公共方法 | [SetOffsetCompensatedOhmEnabled](20bd0615-ebc6-a0c1-6ab8-c1e2e71a8234.htm) | Sets whether the compensated ohms are offset. |
| 公共方法 | [SetOperationMode](31047bd0-c25b-c0ba-d438-9691ec0b2f3a.htm) | Sets how the NI 4065 and NI 4070/4071/4072 acquire data. When you call ConfigureMeasurement or ConfigureMeasurementDigits, NI-DMM sets this property to IviDmmMode. When you call ConfigureWaveformAcquisition, NI-DMM sets this property to WaveformMode. The default value is IviDmmMode. |
| 公共方法 | [SetRange](5ca22649-6c50-2a37-549e-c3347b31e164.htm) | Sets the measurement range. |
| 公共方法 | [SetResolution](d526b62c-aab7-756b-4aa0-d5e7d4681ae0.htm) | Sets the measurement resolution in digits. |
| 公共方法 | [SetSampleCount](78a6e061-a24c-1531-5b7e-e68371c38acc.htm) | Sets the number of measurements the DMM takes each time it receives a trigger in a multiple point acquisition. |
| 公共方法 | [SetSampleInterval](bff8d2a7-e27c-bb1e-9c79-878c8f62978b.htm) | Sets the amount of time in seconds the DMM waits between measurement cycles. |
| 公共方法 | [SetSampleTriggerCount](ba69fc3e-e820-6e41-58af-1834444693fc.htm) | Sets the number of triggers the DMM receives before returning to the Idle state. |
| 公共方法 | [SetSampleTriggerSlope](b0dee1f4-a523-8e70-95c7-9581edc42746.htm) | Sets the edge of the signal from the specified sample trigger source on which the DMM is triggered. |
| 公共方法 | [SetSampleTriggerSource](587da5cc-c2cb-0e46-d1d6-3f9615d130df.htm) | Sets the sample trigger source. |
| 公共方法 | [SetThermistorType](2c05bd90-94ac-e7f9-0065-fba6823ca15a.htm) | Sets the type of thermistor used to measure the temperature. |
| 公共方法 | [SetTransducerType](e783bec9-39ae-1a98-4f1e-a134503755ec.htm) | Sets the type of transducer. |
| 公共方法 | [SetWaveformCoupling](0d191945-8ba8-2622-6670-0dcfd01b8b58.htm) | Sets the coupling during a waveform acquisition. |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |

[Top](#PageHeader)

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### Abort 方法

|  |  |
| --- | --- |
|  | DmmAbort 方法 |

Aborts a previously initiated measurement and returns the DMM to the idle state.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm Abort()
```

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ConfigureACBandwidth 方法

|  |  |
| --- | --- |
|  | DmmConfigureACBandwidth 方法 |

Configures FrequencyMin and FrequencyMax for AC measurements.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm ConfigureACBandwidth(
	double minFreq,
	double maxFreq
)
```

###### 参数

minFreq  Double
:   The minimum expected frequency component of the input signal in hertz.

maxFreq  Double
:   The maximum expected frequency component of the input signal in hertz within the device limits.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ConfigureMeasurement 方法

|  |  |
| --- | --- |
|  | DmmConfigureMeasurement 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [ConfigureMeasurement(String, Double, Double)](eb90a008-b2e5-aae1-0a39-0256ece3835f.htm) | Configures measurements by setting Range value. The configured properties include MeasurementFunction, Range, and Resolution in digits. |
| 公共方法 | [ConfigureMeasurement(String, String, Double)](abb91d26-d712-73ce-dd54-4a911b28ff0a.htm) | Configures measurements with AutoRange on. The configured properties include MeasurementFunction, Range, and Resolution in digits. |

[Top](#PageHeader)

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


##### ConfigureMeasurement(String, Double, Double) 方法

|  |  |
| --- | --- |
|  | DmmConfigureMeasurement(String, Double, Double) 方法 |

Configures measurements by setting Range value. The configured properties include MeasurementFunction, Range, and Resolution in digits.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm ConfigureMeasurement(
	string measurementFunction,
	double range,
	double resolutionDigits
)
```

###### 参数

measurementFunction  String
:   Specifies the MeasurementFunction used to acquire the measurement.

range  Double
:   Specifies the Range for the function specified in the measurementFunction parameter.

resolutionDigits  Double
:   Specifies the Resolution for the measurement in digits. The default is 0.001 V.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[ConfigureMeasurement 重载](8439fa97-836b-34e3-4b4e-9162e3b3e389.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


##### ConfigureMeasurement(String, String, Double) 方法

|  |  |
| --- | --- |
|  | DmmConfigureMeasurement(String, String, Double) 方法 |

Configures measurements with AutoRange on. The configured properties include MeasurementFunction, Range, and Resolution in digits.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm ConfigureMeasurement(
	string measurementFunction,
	string autoRange,
	double resolutionDigits
)
```

###### 参数

measurementFunction  String
:   Specifies the MeasurementFunction used to acquire the measurement.

autoRange  String
:   Indicates whether the range is set automatically by the instrument. AutoRange is set to this value.

resolutionDigits  Double
:   Specifies the Resolution for the measurement in digits. This parameter is ignored when the range parameter is set to On or Once. The default is 0.001 V.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[ConfigureMeasurement 重载](8439fa97-836b-34e3-4b4e-9162e3b3e389.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ConfigureMeasurementTrigger 方法

|  |  |
| --- | --- |
|  | DmmConfigureMeasurementTrigger 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [ConfigureMeasurementTrigger(String, Boolean)](df804e06-9218-8ca5-5a82-7c99c8835cb7.htm) | Configures trigger-related properties. The properties include Source and DelayAuto. |
| 公共方法 | [ConfigureMeasurementTrigger(String, Double)](f500d975-e22c-6141-b361-8c5b79800b7d.htm) | Configures trigger-related properties. The properties include Source and Delay. |

[Top](#PageHeader)

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


##### ConfigureMeasurementTrigger(String, Boolean) 方法

|  |  |
| --- | --- |
|  | DmmConfigureMeasurementTrigger(String, Boolean) 方法 |

Configures trigger-related properties. The properties include Source and DelayAuto.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm ConfigureMeasurementTrigger(
	string triggerSource,
	bool autoTriggerDelay
)
```

###### 参数

triggerSource  String
:   "Immediate", "External", "SoftwareTrigger", "Interval", "Ttl0", "Ttl1", "Ttl2", "Ttl3", "Ttl4", "Ttl5", "Ttl6", "Ttl7", "PxiStar", "LbrTrig1", "AuxTrig1".

autoTriggerDelay  Boolean
:   Indicates whether the driver automatically calculates the appropriate settling time before taking the measurement.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[ConfigureMeasurementTrigger 重载](99f03d6b-f6f0-9be4-0ee1-2a4113761d6a.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


##### ConfigureMeasurementTrigger(String, Double) 方法

|  |  |
| --- | --- |
|  | DmmConfigureMeasurementTrigger(String, Double) 方法 |

Configures trigger-related properties. The properties include Source and Delay.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm ConfigureMeasurementTrigger(
	string triggerSource,
	double triggerDelay
)
```

###### 参数

triggerSource  String
:   "Immediate", "External", "SoftwareTrigger", "Interval", "Ttl0", "Ttl1", "Ttl2", "Ttl3", "Ttl4", "Ttl5", "Ttl6", "Ttl7", "PxiStar", "LbrTrig1", "AuxTrig1".

triggerDelay  Double
:   Specifies the time that the DMM waits after it has received a trigger before taking a measurement.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[ConfigureMeasurementTrigger 重载](99f03d6b-f6f0-9be4-0ee1-2a4113761d6a.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ConfigureMeasurementTriggerPyProxy 方法

|  |  |
| --- | --- |
|  | DmmConfigureMeasurementTriggerPyProxy 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
protected Dmm ConfigureMeasurementTriggerPyProxy(
	string triggerSource,
	int autoTriggerDelay
)
```

###### 参数

triggerSource  String

autoTriggerDelay  Int32

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ConfigureMultiPoint 方法

|  |  |
| --- | --- |
|  | DmmConfigureMultiPoint 方法 |

Configures properties related to multipoint acquisition.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm ConfigureMultiPoint(
	long triggerCount,
	long sampleCount,
	string sampleTrigger,
	double sampleInterval
)
```

###### 参数

triggerCount  Int64
:   Sets the number of triggers you want the DMM to receive before returning to the Idle state. The default value is 1.

sampleCount  Int64
:   Sets the number of measurements the DMM makes in each measurement sequence initiated by a trigger. The default value is 1.

sampleTrigger  String
:   Specifies the sample trigger source you want to use. The default is Immediate.

sampleInterval  Double
:   Sets the amount of time in seconds the DMM waits between measurements.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ConfigureOpenCableCompensation 方法

|  |  |
| --- | --- |
|  | DmmConfigureOpenCableCompensation 方法 |

Configure the open cable compensation.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm ConfigureOpenCableCompensation(
	double conductance,
	double susceptance
)
```

###### 参数

conductance  Double
:   The active part (conductance) of the open cable compensation.

susceptance  Double
:   The reactive part (susceptance) of the open cable compensation.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ConfigureRTDCustom 方法

|  |  |
| --- | --- |
|  | DmmConfigureRTDCustom 方法 |

Configures the A, B, and C parameters for a custom RTD.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm ConfigureRTDCustom(
	double rtdA,
	double rtdB,
	double rtdC
)
```

###### 参数

rtdA  Double
:   The default is 3.9083e-3 (Pt3851).

rtdB  Double
:   The default is -5.775e-7 (Pt3851).

rtdC  Double
:   The default is -4.183e-12 (Pt3851).

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ConfigureRTDType 方法

|  |  |
| --- | --- |
|  | DmmConfigureRTDType 方法 |

Configures the RTD type and RTD resistance parameters for an RTD.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm ConfigureRTDType(
	string rtdType,
	double rtdResistance
)
```

###### 参数

rtdType  String
:   The default is "PT3851".
    "Custom", "PT3750", "PT3851", "PT3911", "PT3916", "PT3920", "PT3928".

rtdResistance  Double
:   Specifies the RTD resistance in ohms at 0 deg C.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ConfigureShortCableCompensation 方法

|  |  |
| --- | --- |
|  | DmmConfigureShortCableCompensation 方法 |

Configure the shrot cable compensation.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm ConfigureShortCableCompensation(
	double resistance,
	double reactance
)
```

###### 参数

resistance  Double
:   The active part (resistance) of the short cable compensation.

reactance  Double
:   The reactive part (reactance) of the short cable compensation.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ConfigureThermistorCustom 方法

|  |  |
| --- | --- |
|  | DmmConfigureThermistorCustom 方法 |

Configures the A, B, and C parameters for a custom thermistor.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm ConfigureThermistorCustom(
	double thermistorA,
	double thermistorB,
	double thermistorC
)
```

###### 参数

thermistorA  Double
:   The default is 1.0295e-3 (44006).

thermistorB  Double
:   The default is 2.391e-4 (44006).

thermistorC  Double
:   The default is 1.568e-7 (44006).

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ConfigureThermocouple 方法

|  |  |
| --- | --- |
|  | DmmConfigureThermocouple 方法 |

Configures the thermocouple type and reference junction type for a chosen thermocouple.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm ConfigureThermocouple(
	string thermocoupleType,
	string refJunctionType
)
```

###### 参数

thermocoupleType  String
:   "B", "E", "J", "K", "N", "R", "S", "T". The default is "J".

refJunctionType  String
:   "Fixed"

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ConfigureWaveformAcquisition 方法

|  |  |
| --- | --- |
|  | DmmConfigureWaveformAcquisition 方法 |

Configures the NI 4070/4071/4072 for waveform acquisitions.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm ConfigureWaveformAcquisition(
	string measurementFunction,
	double range,
	double rate,
	long waveformPoints
)
```

###### 参数

measurementFunction  String
:   "WaveformCurrent" and "WaveformVoltage".

range  Double
:   Specifies the expected maximum amplitude of the input signal and sets the range for the measurementFunction.Range values are coerced up to the closest input range. The default is 10.0.

rate  Double
:   Specifies the rate of the acquisition in samples per second. The valid range is 10.0-1,800,000 S/s. Rate values are coerced to the closest integer divisor of 1,800,000. The default value is 1,800,000.

waveformPoints  Int64
:   Specifies the number of points to acquire before the waveform acquisition completes. The default value is 500.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### Fetch 方法

|  |  |
| --- | --- |
|  | DmmFetch 方法 |

Returns the value from a previously initiated measurement. You must call Initiate before calling this method.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> Fetch(
	double timeout
)
```

###### 参数

timeout  Double
:   Timeout values in seconds. The valid range is 0–86400 seconds.

###### 返回值

DictionaryString, Double  
A dictionary collection of the measured value returned from the DMM. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### FetchMultiPoint 方法

|  |  |
| --- | --- |
|  | DmmFetchMultiPoint 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [FetchMultiPoint(Double)](0e71ef51-e3ba-f864-d9f6-3ee37b30563c.htm) | Returns an array of values from a previously initiated multipoint measurement. |
| 公共方法 | [FetchMultiPoint(Double, Int64)](347bc2cb-981b-27da-cc99-a0f745383fda.htm) | Returns an array of values from a previously initiated multipoint measurement. |

[Top](#PageHeader)

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


##### FetchMultiPoint(Double) 方法

|  |  |
| --- | --- |
|  | DmmFetchMultiPoint(Double) 方法 |

Returns an array of values from a previously initiated multipoint measurement.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double[]> FetchMultiPoint(
	double timeout
)
```

###### 参数

timeout  Double
:   Timeout values in seconds. The valid range is 0–86400 seconds.

###### 返回值

DictionaryString, Double  
A dictionary collection of a double array of measured values. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[FetchMultiPoint 重载](30b69830-7c13-dc4c-fa7c-99abdede525c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


##### FetchMultiPoint(Double, Int64) 方法

|  |  |
| --- | --- |
|  | DmmFetchMultiPoint(Double, Int64) 方法 |

Returns an array of values from a previously initiated multipoint measurement.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double[]> FetchMultiPoint(
	double timeout,
	long pointsToFetch
)
```

###### 参数

timeout  Double
:   Timeout values in seconds. The valid range is 0–86400 seconds.

pointsToFetch  Int64
:   Specifies the number of measurements to acquire.

###### 返回值

DictionaryString, Double  
A dictionary collection of a double array of measured values. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[FetchMultiPoint 重载](30b69830-7c13-dc4c-fa7c-99abdede525c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### FetchWaveform 方法

|  |  |
| --- | --- |
|  | DmmFetchWaveform 方法 |

Returns an array of values in the form of a waveform datatype from a previously initiated waveform acquisition.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double[]> FetchWaveform(
	long pointsToFetch,
	double timeout
)
```

###### 参数

pointsToFetch  Int64
:   Specifies the number of waveform points to return. The default value is 1.

timeout  Double
:   Specifies the maximum time allowed for this method to complete. The valid range is 0–86400 seconds.

###### 返回值

DictionaryString, Double  
A dictionary collection of the array of values from a previously initiated waveform acquisition. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetAbsoluteResolution 方法

|  |  |
| --- | --- |
|  | DmmGetAbsoluteResolution 方法 |

Gets the measurement resolution in absolute units.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetAbsoluteResolution()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of measurement resolution in absolute units. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetACMaxFrequency 方法

|  |  |
| --- | --- |
|  | DmmGetACMaxFrequency 方法 |

Gets the maximum frequency component of the input signal for AC measurements.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetACMaxFrequency()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of the maximum frequency. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetACMinFrequency 方法

|  |  |
| --- | --- |
|  | DmmGetACMinFrequency 方法 |

Gets the minimum frequency component of the input signal for AC measurements.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetACMinFrequency()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of the minimum frequency. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetApertureTime 方法

|  |  |
| --- | --- |
|  | DmmGetApertureTime 方法 |

Gets the measurement aperture time for the current configuration.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetApertureTime()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of the measurement aperture time. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetAttributeBool 方法

|  |  |
| --- | --- |
|  | DmmGetAttributeBool 方法 |

Get specific value by attribute identifier.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> GetAttributeBool(
	long attributeId
)
```

###### 参数

attributeId  Int64
:   The attribute identifier.

###### 返回值

DictionaryString, Boolean  
A dictionary collection.The key of the collection is pin name.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetAttributeDouble 方法

|  |  |
| --- | --- |
|  | DmmGetAttributeDouble 方法 |

Get specific value by attribute identifier.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetAttributeDouble(
	long attributeId
)
```

###### 参数

attributeId  Int64
:   The attribute identifier.

###### 返回值

DictionaryString, Double  
A dictionary collection.The key of the collection is pin name.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetAttributeInt 方法

|  |  |
| --- | --- |
|  | DmmGetAttributeInt 方法 |

Get specific value by attribute identifier.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetAttributeInt(
	long attributeId
)
```

###### 参数

attributeId  Int64
:   The attribute identifier.

###### 返回值

DictionaryString, Int64  
A dictionary collection.The key of the collection is pin name.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetAttributeLong 方法

|  |  |
| --- | --- |
|  | DmmGetAttributeLong 方法 |

Get specific value by attribute identifier.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetAttributeLong(
	long attributeId
)
```

###### 参数

attributeId  Int64
:   The attribute identifier.

###### 返回值

DictionaryString, Int64  
A dictionary collection.The key of the collection is pin name.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetAttributeString 方法

|  |  |
| --- | --- |
|  | DmmGetAttributeString 方法 |

Get specific value by attribute identifier.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetAttributeString(
	long attributeId
)
```

###### 参数

attributeId  Int64
:   The attribute identifier.

###### 返回值

DictionaryString, String  
A dictionary collection.The key of the collection is pin name.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetAutoRange 方法

|  |  |
| --- | --- |
|  | DmmGetAutoRange 方法 |

Gets whether the range is set automatically by the instrument.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetAutoRange()
```

###### 返回值

DictionaryString, String  
A dictionary collection. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetAutoRangeValue 方法

|  |  |
| --- | --- |
|  | DmmGetAutoRangeValue 方法 |

Gets measurement auto range value.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetAutoRangeValue()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of measurement auto range value. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetAutoZero 方法

|  |  |
| --- | --- |
|  | DmmGetAutoZero 方法 |

Gets the AutoZero mode.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetAutoZero()
```

###### 返回值

DictionaryString, String  
A dictionary collection of the AutoZero mode. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetCableCompensationType 方法

|  |  |
| --- | --- |
|  | DmmGetCableCompensationType 方法 |

Gets the type of cable compensation that is applied to the current capacitance or inductance measurement for the current range.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetCableCompensationType()
```

###### 返回值

DictionaryString, String  
A dictionary collection of the type of cable compensation. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetDiodeCurrentSource 方法

|  |  |
| --- | --- |
|  | DmmGetDiodeCurrentSource 方法 |

Gets the current source provided during diode measurements.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetDiodeCurrentSource()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of current source. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetFixedReferenceJunction 方法

|  |  |
| --- | --- |
|  | DmmGetFixedReferenceJunction 方法 |

Gets the reference junction temperature when a fixed reference junction is used to take a thermocouple measurement.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetFixedReferenceJunction()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of reference junction temperature. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetFrequencyMeasurementVoltageAutoRange 方法

|  |  |
| --- | --- |
|  | DmmGetFrequencyMeasurementVoltageAutoRange 方法 |

Gets a value indicating whether the frequency voltage is auto-ranging.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetFrequencyMeasurementVoltageAutoRange()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of boolean values. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetFrequencyMeasurementVoltageRange 方法

|  |  |
| --- | --- |
|  | DmmGetFrequencyMeasurementVoltageRange 方法 |

Gets the maximum amplitude of the input signal for frequency measurements.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetFrequencyMeasurementVoltageRange()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of maximum amplitude. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetInputResistance 方法

|  |  |
| --- | --- |
|  | DmmGetInputResistance 方法 |

Gets the input resistance of the instrument.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetInputResistance()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of input resistance. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetMeasurementCompleteDestination 方法

|  |  |
| --- | --- |
|  | DmmGetMeasurementCompleteDestination 方法 |

Gets the destination of the measurement complete (MC) signal.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetMeasurementCompleteDestination()
```

###### 返回值

DictionaryString, String  
A dictionary collection of the destination. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetMeasurementCompleteSlope 方法

|  |  |
| --- | --- |
|  | DmmGetMeasurementCompleteSlope 方法 |

Gets the polarity of the generated measurement complete signal.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetMeasurementCompleteSlope()
```

###### 返回值

DictionaryString, String  
A dictionary collection of the polarity of the signal. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetMeasurementFunction 方法

|  |  |
| --- | --- |
|  | DmmGetMeasurementFunction 方法 |

Gets the measurement function.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetMeasurementFunction()
```

###### 返回值

DictionaryString, String  
A dictionary collection of measurement function. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetMeasurementPeriod 方法

|  |  |
| --- | --- |
|  | DmmGetMeasurementPeriod 方法 |

Gets the number of seconds it takes to make one measurement.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetMeasurementPeriod()
```

###### 返回值

DictionaryString, Double  
The value is the amount of time in seconds it takes to complete one measurement with the current configuration.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetMeasurementTriggerDelay 方法

|  |  |
| --- | --- |
|  | DmmGetMeasurementTriggerDelay 方法 |

Gets the time (in seconds) that the DMM waits after it has received a trigger before taking a measurement.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetMeasurementTriggerDelay()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of delay. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetMeasurementTriggerDelayAuto 方法

|  |  |
| --- | --- |
|  | DmmGetMeasurementTriggerDelayAuto 方法 |

Gets a value indicating whether the DMM selects the trigger delay automatically.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> GetMeasurementTriggerDelayAuto()
```

###### 返回值

DictionaryString, Boolean  
A dictionary collection of boolean values indicating whether the DMM selects the trigger delay automatically. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetMeasurementTriggerSlope 方法

|  |  |
| --- | --- |
|  | DmmGetMeasurementTriggerSlope 方法 |

Gets the edge of the signal from the specified trigger source on which the DMM is triggered.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetMeasurementTriggerSlope()
```

###### 返回值

DictionaryString, String  
A dictionary collection of the edge of the signal. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetMeasurementTriggerSource 方法

|  |  |
| --- | --- |
|  | DmmGetMeasurementTriggerSource 方法 |

Gets the trigger source.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetMeasurementTriggerSource()
```

###### 返回值

DictionaryString, String  
A dictionary collection of trigger source. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetOffsetCompensatedOhmEnabled 方法

|  |  |
| --- | --- |
|  | DmmGetOffsetCompensatedOhmEnabled 方法 |

Gets whether the compensated ohms are offset.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> GetOffsetCompensatedOhmEnabled()
```

###### 返回值

DictionaryString, Boolean  
A dictionary collection of boolean values. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetOperationMode 方法

|  |  |
| --- | --- |
|  | DmmGetOperationMode 方法 |

Gets how the NI 4065 and NI 4070/4071/4072 acquire data.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetOperationMode()
```

###### 返回值

DictionaryString, String  
A dictionary collection of operation mode. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetRange 方法

|  |  |
| --- | --- |
|  | DmmGetRange 方法 |

Gets the measurement range.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetRange()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of measurement range. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetResolution 方法

|  |  |
| --- | --- |
|  | DmmGetResolution 方法 |

Gets the measurement resolution in digits.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetResolution()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of measurement resolution in digits. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetSampleCount 方法

|  |  |
| --- | --- |
|  | DmmGetSampleCount 方法 |

Gets the number of measurements the DMM takes each time it receives a trigger in a multiple point acquisition.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetSampleCount()
```

###### 返回值

DictionaryString, Int64  
A dictionary collection of the number of measurements. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetSampleInterval 方法

|  |  |
| --- | --- |
|  | DmmGetSampleInterval 方法 |

Gets the amount of time in seconds the DMM waits between measurement cycles.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetSampleInterval()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of the amount of time. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetSampleTriggerCount 方法

|  |  |
| --- | --- |
|  | DmmGetSampleTriggerCount 方法 |

Gets the number of triggers the DMM receives before returning to the Idle state.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetSampleTriggerCount()
```

###### 返回值

DictionaryString, Int64  
A dictionary collection of the number of triggers. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetSampleTriggerSlope 方法

|  |  |
| --- | --- |
|  | DmmGetSampleTriggerSlope 方法 |

Gets the edge of the signal from the specified sample trigger source on which the DMM is triggered.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetSampleTriggerSlope()
```

###### 返回值

DictionaryString, String  
A dictionary collection of the edge of the signal. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetSampleTriggerSource 方法

|  |  |
| --- | --- |
|  | DmmGetSampleTriggerSource 方法 |

Gets the sample trigger source.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetSampleTriggerSource()
```

###### 返回值

DictionaryString, String  
A dictionary collection of the trigger source. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetThermistorType 方法

|  |  |
| --- | --- |
|  | DmmGetThermistorType 方法 |

Gets the type of thermistor used to measure the temperature.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetThermistorType()
```

###### 返回值

DictionaryString, String  
A dictionary collection of thermistor type. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetTransducerType 方法

|  |  |
| --- | --- |
|  | DmmGetTransducerType 方法 |

Gets the type of transducer.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetTransducerType()
```

###### 返回值

DictionaryString, String  
A dictionary collection of transducer type. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetWaveformCoupling 方法

|  |  |
| --- | --- |
|  | DmmGetWaveformCoupling 方法 |

Gets the coupling during a waveform acquisition.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetWaveformCoupling()
```

###### 返回值

DictionaryString, String  
A dictionary collection of coupling. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### Initiate 方法

|  |  |
| --- | --- |
|  | DmmInitiate 方法 |

Initiates an acquisition.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm Initiate()
```

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### IsOverRange 方法

|  |  |
| --- | --- |
|  | DmmIsOverRange 方法 |

Takes a measurement value and determines if the value is a valid measurement or a value indicating that an overrange condition occurred.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> IsOverRange(
	double measurementValue
)
```

###### 参数

measurementValue  Double
:   The measured value returned from the DMM.

###### 返回值

DictionaryString, Boolean  
A dictionary collection of a boolean indicating whether the measurement value is valid or overrange. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### IsUnderRange 方法

|  |  |
| --- | --- |
|  | DmmIsUnderRange 方法 |

Takes a measurement value and determines if the value is a valid measurement or a value indicating that an underrange condition occurred.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> IsUnderRange(
	double measurementValue
)
```

###### 参数

measurementValue  Double
:   The measured value returned from the DMM.

###### 返回值

DictionaryString, Boolean  
A dictionary collection of a boolean indicating whether the measurement value is valid or underrange. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### PerformOpenCableCompensation 方法

|  |  |
| --- | --- |
|  | DmmPerformOpenCableCompensation 方法 |

Performs the open cable compensation measurements for the current capacitance/inductance range, and returns open cable compensation conductance and susceptance values. You can use the return values of this method as inputs to ConfigureOpenCableCompensation.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double[]> PerformOpenCableCompensation()
```

###### 返回值

DictionaryString, Double  
A dictionary collection. The key of the collection is pin name, the value: double[0] is conductance, double[1] is susceptance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### PerformShortCableCompensation 方法

|  |  |
| --- | --- |
|  | DmmPerformShortCableCompensation 方法 |

Performs the short cable compensation measurements for the current capacitance/inductance range, and returns short cable compensation resistance and reactance values. You can use the return values of this function as inputs to ConfigureShortCableCompensation.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double[]> PerformShortCableCompensation()
```

###### 返回值

DictionaryString, Double  
 dictionary collection. The key of the collection is pin name, the value: double[0] is resistance, double[1] is reactance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### Read 方法

|  |  |
| --- | --- |
|  | DmmRead 方法 |

Acquires a single measurement and returns the measured value.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> Read(
	double timeout
)
```

###### 参数

timeout  Double
:   Timeout values in seconds. The valid range is 0-86400 seconds.

###### 返回值

DictionaryString, Double  
A dictionary collection of the measured value returned from the DMM. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ReadMultiPoint 方法

|  |  |
| --- | --- |
|  | DmmReadMultiPoint 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [ReadMultiPoint(Double)](323da636-e4b8-b61a-4275-4a2dc1f1dee6.htm) | Acquires multiple measurements and returns an array of values. |
| 公共方法 | [ReadMultiPoint(Double, Int64)](9104eeac-19fc-a522-659f-b41f4aa23104.htm) | Acquires multiple measurements and returns an array of values. |

[Top](#PageHeader)

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


##### ReadMultiPoint(Double) 方法

|  |  |
| --- | --- |
|  | DmmReadMultiPoint(Double) 方法 |

Acquires multiple measurements and returns an array of values.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double[]> ReadMultiPoint(
	double timeout
)
```

###### 参数

timeout  Double
:   Timeout values in seconds. The valid range is 0–86400 seconds.

###### 返回值

DictionaryString, Double  
A dictionary collection of an array of measurement values. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[ReadMultiPoint 重载](40ca9c22-c327-c29d-d9fc-120cfd0a13ae.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


##### ReadMultiPoint(Double, Int64) 方法

|  |  |
| --- | --- |
|  | DmmReadMultiPoint(Double, Int64) 方法 |

Acquires multiple measurements and returns an array of values.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double[]> ReadMultiPoint(
	double timeout,
	long pointsToFetch
)
```

###### 参数

timeout  Double
:   Timeout values in seconds. The valid range is 0–86400 seconds.

pointsToFetch  Int64
:   Specifies the number of measurements to acquire. The default value is 1.

###### 返回值

DictionaryString, Double  
A dictionary collection of an array of measurement values. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[ReadMultiPoint 重载](40ca9c22-c327-c29d-d9fc-120cfd0a13ae.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ReadWaveform 方法

|  |  |
| --- | --- |
|  | DmmReadWaveform 方法 |

Acquires and returns a waveform buffer with values.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double[]> ReadWaveform(
	long pointsToFetch,
	double timeout
)
```

###### 参数

pointsToFetch  Int64
:   Specifies the number of waveform points to return. The default value is 1.

timeout  Double
:   Specifies the maximum time allowed for this method to complete. The valid range is 0-86400 seconds.

###### 返回值

DictionaryString, Double  
A dictionary collection of the array of values from a previously initiated waveform acquisition. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### Reset 方法

|  |  |
| --- | --- |
|  | DmmReset 方法 |

Reset the instrument session.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm Reset()
```

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SendSoftwareTrigger 方法

|  |  |
| --- | --- |
|  | DmmSendSoftwareTrigger 方法 |

Sends a command to trigger the DMM.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SendSoftwareTrigger()
```

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetAbsoluteResolution 方法

|  |  |
| --- | --- |
|  | DmmSetAbsoluteResolution 方法 |

Sets the measurement resolution in absolute units.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetAbsoluteResolution(
	double resolution
)
```

###### 参数

resolution  Double
:   The measurement resolution in absolute units.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetACMaxFrequency 方法

|  |  |
| --- | --- |
|  | DmmSetACMaxFrequency 方法 |

Sets the maximum frequency component of the input signal for AC measurements.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetACMaxFrequency(
	double frequency
)
```

###### 参数

frequency  Double
:   The maximum frequency.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetACMinFrequency 方法

|  |  |
| --- | --- |
|  | DmmSetACMinFrequency 方法 |

Sets the minimum frequency component of the input signal for AC measurements.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetACMinFrequency(
	double frequency
)
```

###### 参数

frequency  Double
:   The minimum frequency.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetApertureTime 方法

|  |  |
| --- | --- |
|  | DmmSetApertureTime 方法 |

Sets the measurement aperture time for the current configuration.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetApertureTime(
	double apertureTime
)
```

###### 参数

apertureTime  Double
:   To override the default aperture, set this property to the desired aperture time after calling ConfigureMeasurement. To return to the default, set this property to -1.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetAttributeBool 方法

|  |  |
| --- | --- |
|  | DmmSetAttributeBool 方法 |

Set specific value by attribute identifier.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetAttributeBool(
	long attributeId,
	bool value
)
```

###### 参数

attributeId  Int64
:   The attribute identifier.

value  Boolean
:   The value to set.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetAttributeDouble 方法

|  |  |
| --- | --- |
|  | DmmSetAttributeDouble 方法 |

Set specific value by attribute identifier.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetAttributeDouble(
	long attributeId,
	double value
)
```

###### 参数

attributeId  Int64
:   The attribute identifier.

value  Double
:   The value to set.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetAttributeInt 方法

|  |  |
| --- | --- |
|  | DmmSetAttributeInt 方法 |

Set specific value by attribute identifier.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetAttributeInt(
	long attributeId,
	long value
)
```

###### 参数

attributeId  Int64
:   The attribute identifier.

value  Int64
:   The value to set.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetAttributeLong 方法

|  |  |
| --- | --- |
|  | DmmSetAttributeLong 方法 |

Set specific value by attribute identifier.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetAttributeLong(
	long attributeId,
	long value
)
```

###### 参数

attributeId  Int64
:   The attribute identifier.

value  Int64
:   The value to set.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetAttributeString 方法

|  |  |
| --- | --- |
|  | DmmSetAttributeString 方法 |

Set specific value by attribute identifier.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetAttributeString(
	long attributeId,
	string value
)
```

###### 参数

attributeId  Int64
:   The attribute identifier.

value  String
:   The value to set.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetAutoRange 方法

|  |  |
| --- | --- |
|  | DmmSetAutoRange 方法 |

Sets whether the range is set automatically by the instrument.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetAutoRange(
	string autoRange
)
```

###### 参数

autoRange  String
:   "On", "Off" and "Once".

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetAutoZero 方法

|  |  |
| --- | --- |
|  | DmmSetAutoZero 方法 |

Sets the AutoZero mode.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetAutoZero(
	string autoZero
)
```

###### 参数

autoZero  String
:   "Auto", "Off", "On", "Once". The default value is "Auto".

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetCableCompensationType 方法

|  |  |
| --- | --- |
|  | DmmSetCableCompensationType 方法 |

Sets the type of cable compensation that is applied to the current capacitance or inductance measurement for the current range.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetCableCompensationType(
	string typeOfCompensation
)
```

###### 参数

typeOfCompensation  String
:   "None", "Open", "OpenAndShort", "Short". The default value is "None".

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetDiodeCurrentSource 方法

|  |  |
| --- | --- |
|  | DmmSetDiodeCurrentSource 方法 |

Sets the current source provided during diode measurements.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetDiodeCurrentSource(
	double diodeCurrentSource
)
```

###### 参数

diodeCurrentSource  Double
:   The supported values are 1 microAmp, 10 microAmps, 100 microAmps, and 1 milliAmp.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetFixedReferenceJunction 方法

|  |  |
| --- | --- |
|  | DmmSetFixedReferenceJunction 方法 |

Sets the reference junction temperature when a fixed reference junction is used to take a thermocouple measurement.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetFixedReferenceJunction(
	double fixedRefJunction
)
```

###### 参数

fixedRefJunction  Double
:   The default value is 25.0 (°C).

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetFrequencyMeasurementVoltageRange 方法

|  |  |
| --- | --- |
|  | DmmSetFrequencyMeasurementVoltageRange 方法 |

Sets the maximum amplitude of the input signal for frequency measurements.
If VoltageAutoRange is set to true or if VoltageRange is set to -1.0, the DMM is configured to take an auto-range measurement to calculate the voltage range before each frequency or period measurement.
If VoltageAutoRange is set to false or if VoltageRange is set to -2.0, auto-ranging is disabled, and NI-DMM sets the voltage range to the last calculated voltage range.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetFrequencyMeasurementVoltageRange(
	double voltageRange
)
```

###### 参数

voltageRange  Double
:   The maximum amplitude of the input signal for frequency measurements.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetInputResistance 方法

|  |  |
| --- | --- |
|  | DmmSetInputResistance 方法 |

Sets the input resistance of the instrument.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetInputResistance(
	double resistance
)
```

###### 参数

resistance  Double
:   The supported values are 1.000000E+6 (1M Ohm), 1.000000E+7 (10M Ohm), and 1.000000E+10 (input resistance greater than 10 G Ohm).

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetMeasurementCompleteDestination 方法

|  |  |
| --- | --- |
|  | DmmSetMeasurementCompleteDestination 方法 |

Sets the destination of the measurement complete (MC) signal.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetMeasurementCompleteDestination(
	string destination
)
```

###### 参数

destination  String
:   "None", "External", "Ttl0", "Ttl1", "Ttl2", "Ttl3", "Ttl4", "Ttl5", "Ttl6", "Ttl7", "LbrTrig0".

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetMeasurementCompleteSlope 方法

|  |  |
| --- | --- |
|  | DmmSetMeasurementCompleteSlope 方法 |

Sets the polarity of the generated measurement complete signal.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetMeasurementCompleteSlope(
	string slope
)
```

###### 参数

slope  String
:   "Positive", "Negative".

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetMeasurementFunction 方法

|  |  |
| --- | --- |
|  | DmmSetMeasurementFunction 方法 |

Sets the measurement function.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetMeasurementFunction(
	string function
)
```

###### 参数

function  String
:   "ACCurrent", "ACVolts", "ACVoltsDCCoupled", "Capacitance", "DCCurrent", "DCVolts", "Diode", "FourWireResistance", "Frequency", "Inductance", "Period", "Temperature", "TwoWireResistance", "WaveformCurrent" and "WaveformVoltage".

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetMeasurementTriggerDelay 方法

|  |  |
| --- | --- |
|  | DmmSetMeasurementTriggerDelay 方法 |

Sets the time (in seconds) that the DMM waits after it has received a trigger before taking a measurement.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetMeasurementTriggerDelay(
	double delay
)
```

###### 参数

delay  Double
:   The amount of time.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetMeasurementTriggerDelayAuto 方法

|  |  |
| --- | --- |
|  | DmmSetMeasurementTriggerDelayAuto 方法 |

Sets a value indicating whether the DMM selects the trigger delay automatically.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetMeasurementTriggerDelayAuto(
	bool auto
)
```

###### 参数

auto  Boolean
:   The default value is true, true or false.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetMeasurementTriggerSlope 方法

|  |  |
| --- | --- |
|  | DmmSetMeasurementTriggerSlope 方法 |

Sets the edge of the signal from the specified trigger source on which the DMM is triggered.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetMeasurementTriggerSlope(
	string triggerSlope
)
```

###### 参数

triggerSlope  String
:   "Positive", "Negative".

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetMeasurementTriggerSource 方法

|  |  |
| --- | --- |
|  | DmmSetMeasurementTriggerSource 方法 |

Sets the trigger source.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetMeasurementTriggerSource(
	string source
)
```

###### 参数

source  String
:   "Immediate", "External", "SoftwareTrigger", "Interval", "Ttl0", "Ttl1", "Ttl2", "Ttl3", "Ttl4", "Ttl5", "Ttl6", "Ttl7", "PxiStar", "LbrTrig1", "AuxTrig1".

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetOffsetCompensatedOhmEnabled 方法

|  |  |
| --- | --- |
|  | DmmSetOffsetCompensatedOhmEnabled 方法 |

Sets whether the compensated ohms are offset.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetOffsetCompensatedOhmEnabled(
	bool enable
)
```

###### 参数

enable  Boolean
:   true or false.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetOperationMode 方法

|  |  |
| --- | --- |
|  | DmmSetOperationMode 方法 |

Sets how the NI 4065 and NI 4070/4071/4072 acquire data.
When you call ConfigureMeasurement or ConfigureMeasurementDigits, NI-DMM sets this property to IviDmmMode.
When you call ConfigureWaveformAcquisition, NI-DMM sets this property to WaveformMode.
The default value is IviDmmMode.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetOperationMode(
	string operationMode
)
```

###### 参数

operationMode  String
:   "IviDmmMode", "WaveformMode".

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetRange 方法

|  |  |
| --- | --- |
|  | DmmSetRange 方法 |

Sets the measurement range.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetRange(
	double range
)
```

###### 参数

range  Double
:   Use positive values to represent the absolute value of the maximum expected measurement.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetResolution 方法

|  |  |
| --- | --- |
|  | DmmSetResolution 方法 |

Sets the measurement resolution in digits.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetResolution(
	double resolution
)
```

###### 参数

resolution  Double
:   3.5, 4.5, 5.5, 6.5, 7.5.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetSampleCount 方法

|  |  |
| --- | --- |
|  | DmmSetSampleCount 方法 |

Sets the number of measurements the DMM takes each time it receives a trigger in a multiple point acquisition.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetSampleCount(
	long sampleCount
)
```

###### 参数

sampleCount  Int64
:   The number of measurements the DMM makes in each measurement sequence initiated by a trigger. The default is 1.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetSampleInterval 方法

|  |  |
| --- | --- |
|  | DmmSetSampleInterval 方法 |

Sets the amount of time in seconds the DMM waits between measurement cycles.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetSampleInterval(
	double sampleInterval
)
```

###### 参数

sampleInterval  Double
:   The amount of time.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetSampleTriggerCount 方法

|  |  |
| --- | --- |
|  | DmmSetSampleTriggerCount 方法 |

Sets the number of triggers the DMM receives before returning to the Idle state.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetSampleTriggerCount(
	long triggerCount
)
```

###### 参数

triggerCount  Int64
:   The numbers of triggers.

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetSampleTriggerSlope 方法

|  |  |
| --- | --- |
|  | DmmSetSampleTriggerSlope 方法 |

Sets the edge of the signal from the specified sample trigger source on which the DMM is triggered.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetSampleTriggerSlope(
	string slope
)
```

###### 参数

slope  String
:   "Positive", "Negative".

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetSampleTriggerSource 方法

|  |  |
| --- | --- |
|  | DmmSetSampleTriggerSource 方法 |

Sets the sample trigger source.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetSampleTriggerSource(
	string sampleTrigger
)
```

###### 参数

sampleTrigger  String
:   "Immediate", "External", "SoftwareTrigger", "Interval", "Ttl0", "Ttl1", "Ttl2", "Ttl3", "Ttl4", "Ttl5", "Ttl6", "Ttl7", "PxiStar", "LbrTrig1", "AuxTrig1".

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetThermistorType 方法

|  |  |
| --- | --- |
|  | DmmSetThermistorType 方法 |

Sets the type of thermistor used to measure the temperature.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetThermistorType(
	string thermistorType
)
```

###### 参数

thermistorType  String
:   "Custom", "Thermistor44004", "Thermistor44006", "Thermistor44007".

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetTransducerType 方法

|  |  |
| --- | --- |
|  | DmmSetTransducerType 方法 |

Sets the type of transducer.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetTransducerType(
	string transducerType
)
```

###### 参数

transducerType  String
:   "FourWireRtd", "Thermistor", "Thermocouple", "TwoWireRtd".

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetWaveformCoupling 方法

|  |  |
| --- | --- |
|  | DmmSetWaveformCoupling 方法 |

Sets the coupling during a waveform acquisition.

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dmm SetWaveformCoupling(
	string coupling
)
```

###### 参数

coupling  String
:   "AC", "DC".

###### 返回值

[Dmm](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)  
Return DmmParent.Dmm instance.

参见

###### 引用

[Dmm 类](e628d2ee-4455-9dc6-d645-c7ebe90d270c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


## IDmm_Instr 接口

|  |  |
| --- | --- |
|  | IDmm\_Instr 接口 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public interface IDmm_Instr
```

IDmm\_Instr 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Abort](94f5cbfb-5fce-78c1-49d1-9d979998105b.htm) |  |
| 公共方法 | [ConfigureACBandwidth](8550f639-87c3-6ea5-f6e8-145cfb8297dc.htm) |  |
| 公共方法 | [ConfigureMeasurement(String, Double, Double)](0ff519c7-7ffa-d5c4-6863-5b6196b25729.htm) |  |
| 公共方法 | [ConfigureMeasurement(String, String, Double)](71d37520-5e82-7c07-cfa7-8a0ff0675aa1.htm) |  |
| 公共方法 | [ConfigureMeasurementTrigger(String, Boolean)](5e9657db-2b05-2099-f262-726ce3e2bb3b.htm) |  |
| 公共方法 | [ConfigureMeasurementTrigger(String, Double)](dbf8e85d-a7ee-d756-f9ac-d9bb7013eba5.htm) |  |
| 公共方法 | [ConfigureMultiPoint](80d30313-9300-8c3a-cc89-be2c19417ebf.htm) |  |
| 公共方法 | [ConfigureOpenCableCompensation](db7ce82f-b538-2953-7fb3-7f3e2cb340ee.htm) |  |
| 公共方法 | [ConfigureRTDCustom](3216c872-8e0a-8233-36c3-84a4f74d6ff9.htm) |  |
| 公共方法 | [ConfigureRTDType](c04eaf7c-3ea1-d05e-2469-da7f23b5dc31.htm) |  |
| 公共方法 | [ConfigureShortCableCompensation](b3a31dfc-5199-2f91-a02b-719cdb735e57.htm) |  |
| 公共方法 | [ConfigureThermistorCustom](3f86382f-5bb0-fa27-2ca7-d8a1eb3f3d9b.htm) |  |
| 公共方法 | [ConfigureThermocouple](40d6a89d-51f1-2565-8463-432e6c23a886.htm) |  |
| 公共方法 | [ConfigureWaveformAcquisition](7a8e2ecc-a3d1-85a0-1dba-5dcf71343272.htm) |  |
| 公共方法 | [Fetch](6424ec9e-f337-69a8-2a39-07af962c0575.htm) |  |
| 公共方法 | [FetchMultiPoint(Double)](25e502bd-3154-cccc-b983-fa383398619d.htm) |  |
| 公共方法 | [FetchMultiPoint(Double, Int32)](b4a39410-b0e8-eea2-6285-ee0768aace25.htm) |  |
| 公共方法 | [FetchWaveform](c05220fd-313f-9523-e25e-8423af29d4ca.htm) |  |
| 公共方法 | [GetAbsoluteResolution](3e61cfc4-2eb4-8cda-e4b2-15a16b883d95.htm) |  |
| 公共方法 | [GetACMaxFrequency](2b762ce0-c49e-6877-771d-73812e179520.htm) |  |
| 公共方法 | [GetACMinFrequency](a01e128b-1dcb-3a20-b9f0-c3816811b330.htm) |  |
| 公共方法 | [GetApertureTime](2920fd85-7ad3-3b07-b111-3f70f7b9d24d.htm) |  |
| 公共方法 | [GetAttributeT](4e2f4004-7435-95ab-61fb-8214f00cb397.htm) |  |
| 公共方法 | [GetAutoRange](b69d6fdb-2403-348b-197e-6afa61c49259.htm) |  |
| 公共方法 | [GetAutoRangeValue](062a1cad-fbf0-e064-6417-19c0848e934b.htm) |  |
| 公共方法 | [GetAutoZero](e38774ad-a112-f8d9-79e7-debe50d4ead8.htm) |  |
| 公共方法 | [GetCableCompensationType](709c4a39-3694-db47-5d57-9e0c1dbd83b9.htm) |  |
| 公共方法 | [GetDiodeCurrentSource](d0946e14-d596-b4db-82a5-6946d8ff157d.htm) |  |
| 公共方法 | [GetFixedReferenceJunction](833e8b6d-3be9-6322-2917-037fe8da4958.htm) |  |
| 公共方法 | [GetFrequencyMeasurementVoltageAutoRange](b6b01752-db93-6550-d052-8417cce81203.htm) |  |
| 公共方法 | [GetFrequencyMeasurementVoltageRange](f7414824-b585-ec8c-1868-ab3ebf5aba82.htm) |  |
| 公共方法 | [GetInputResistance](6984c99b-7291-0d24-004b-9729b91b656a.htm) |  |
| 公共方法 | [GetMeasurementCompleteDestination](e443b954-008e-68a2-e624-496378f3a8b1.htm) |  |
| 公共方法 | [GetMeasurementCompleteSlope](e6119d8e-c2cb-2a18-24d0-86067281c8d0.htm) |  |
| 公共方法 | [GetMeasurementFunction](11e00c9a-3fe8-30c0-034e-64869fe07ad7.htm) |  |
| 公共方法 | [GetMeasurementPeriod](a67f5250-ae9d-fc67-1fef-bd842dfbe6a6.htm) |  |
| 公共方法 | [GetMeasurementTriggerDelay](d852d11f-e943-4784-7040-b9bd929b32af.htm) |  |
| 公共方法 | [GetMeasurementTriggerDelayAuto](f740bc7b-9af9-796b-b00a-d89c5c6243b7.htm) |  |
| 公共方法 | [GetMeasurementTriggerSlope](8ddd4a73-a6cf-6962-26f8-267ca1079cae.htm) |  |
| 公共方法 | [GetMeasurementTriggerSource](94d24505-3409-d0e4-ca01-26c1c2675099.htm) |  |
| 公共方法 | [GetOffsetCompensatedOhmEnabled](23a5711a-4fa8-aa71-1961-a11942c4c97e.htm) |  |
| 公共方法 | [GetOperationMode](e875ef90-3241-e276-8817-8d6b2e13e33f.htm) |  |
| 公共方法 | [GetRange](ce4d00d8-7b2b-e751-8c05-e7263a0c01e4.htm) |  |
| 公共方法 | [GetResolution](53c41db2-c3b1-efca-d6e8-530f3fbfa33e.htm) |  |
| 公共方法 | [GetSampleCount](d4dfad54-5f1b-8462-3bf5-bb9b8d265f85.htm) |  |
| 公共方法 | [GetSampleInterval](3726b08b-cc95-e912-2dc1-fbf8becffe91.htm) |  |
| 公共方法 | [GetSampleTriggerCount](1c612c08-583e-10ea-1212-3808cf9c82b0.htm) |  |
| 公共方法 | [GetSampleTriggerSlope](e9d6f22a-3c9f-9f6b-c1e0-faf56e355b40.htm) |  |
| 公共方法 | [GetSampleTriggerSource](c406bc36-fed9-de50-dc81-13e085d87d98.htm) |  |
| 公共方法 | [GetThermistorType](9e463582-a648-094d-3319-e4f716d9eeee.htm) |  |
| 公共方法 | [GetTransducerType](24d42c16-7f1b-8a62-b187-b951a4681a15.htm) |  |
| 公共方法 | [GetWaveformCoupling](2549c0a4-2df3-372e-bfcf-8d1a760f0096.htm) |  |
| 公共方法 | [Initiate](2a4d1938-3699-34f2-529c-7f2723276fa9.htm) |  |
| 公共方法 | [IsOverRange](e6b870d9-ff34-f12d-2454-a7b5bf3e34fa.htm) |  |
| 公共方法 | [IsUnderRange](5b4b82e1-49a5-c6e1-0225-1768c1ed162d.htm) |  |
| 公共方法 | [PerformOpenCableCompensation](3d4f5147-bf05-ec24-1fea-a1fd34a2e994.htm) |  |
| 公共方法 | [PerformShortCableCompensation](91d9242d-6604-addd-dcbf-ab61ebe97744.htm) |  |
| 公共方法 | [Read](be6290b0-990b-fd06-804b-255f512d0f0b.htm) |  |
| 公共方法 | [ReadMultiPoint(Double)](bca0451d-94dc-505b-f6ed-beed255871d1.htm) |  |
| 公共方法 | [ReadMultiPoint(Double, Int32)](8cbf572e-a12f-5046-bfc6-ececc592c211.htm) |  |
| 公共方法 | [ReadWaveform](240484c3-1793-dd9c-2ad7-d7fbf038873d.htm) |  |
| 公共方法 | [Reset](7c62eb70-73d6-6c5d-d941-4aef79e61bd1.htm) |  |
| 公共方法 | [SendSoftwareTrigger](57602041-ed22-2ee5-82b5-c03f87cf44e7.htm) |  |
| 公共方法 | [SetAbsoluteResolution](3a593648-74cd-e716-43ee-3f9c611efcaa.htm) |  |
| 公共方法 | [SetACMaxFrequency](5a7a3a9d-0512-35d1-8d27-4e4539f2ea9e.htm) |  |
| 公共方法 | [SetACMinFrequency](15b405aa-5cab-2592-01ca-a1edf1620028.htm) |  |
| 公共方法 | [SetApertureTime](46643f36-e051-1925-0af1-669fae3449e7.htm) |  |
| 公共方法 | [SetAttribute](fcdfc860-4923-da58-a88e-3fa2b4e2adf2.htm) |  |
| 公共方法 | [SetAutoRange](ba32e97b-0cca-d7bc-4ae3-de53e99b5d03.htm) |  |
| 公共方法 | [SetAutoZero](d09fab85-b45e-3f56-b5a5-f2ab7ff2aa56.htm) |  |
| 公共方法 | [SetCableCompensationType](b1d14e8d-78c9-69c0-bc3e-682395da168f.htm) |  |
| 公共方法 | [SetDiodeCurrentSource](5a4222d6-0152-8abe-3c56-6b4d9189beed.htm) |  |
| 公共方法 | [SetFixedReferenceJunction](0f365e12-5537-4c27-f801-775eebf9a358.htm) |  |
| 公共方法 | [SetFrequencyMeasurementVoltageRange](deae71f4-83bd-2b51-96ef-d4b69c83eca8.htm) |  |
| 公共方法 | [SetInputResistance](1f94f89d-ef39-2133-df51-f6ceda29a675.htm) |  |
| 公共方法 | [SetMeasurementCompleteDestination](428a8d7f-915c-7be9-2914-db042a9de102.htm) |  |
| 公共方法 | [SetMeasurementCompleteSlope](7de22611-20b4-b57a-4dfe-faec68bba21b.htm) |  |
| 公共方法 | [SetMeasurementFunction](6fe8893c-a3d1-2116-ab8e-a7e043f69f7d.htm) |  |
| 公共方法 | [SetMeasurementTriggerDelay](9efd1d14-75a3-5722-bf6d-42fb01a1196e.htm) |  |
| 公共方法 | [SetMeasurementTriggerDelayAuto](2a6c7128-d03e-599f-2cd2-29aef61250f8.htm) |  |
| 公共方法 | [SetMeasurementTriggerSlope](078c992c-6df9-a4dd-65c5-2ad42fd69e35.htm) |  |
| 公共方法 | [SetMeasurementTriggerSource](142c6082-c4c8-f9b6-292d-22cf7add4148.htm) |  |
| 公共方法 | [SetOffsetCompensatedOhmEnabled](da68fb8e-c2b9-9e91-cd16-add24ef34dcf.htm) |  |
| 公共方法 | [SetOperationMode](e0167fcb-3ea8-d250-0f31-972c08833452.htm) |  |
| 公共方法 | [SetRange](542a99bd-63c9-853c-f119-adbe3715a484.htm) |  |
| 公共方法 | [SetResolution](96bc3284-48f1-9a06-ce65-1f01c9f8ca2a.htm) |  |
| 公共方法 | [SetSampleCount](72f71972-a4a9-135e-ac5c-d56b5e2db4a1.htm) |  |
| 公共方法 | [SetSampleInterval](bb6e0a0d-4442-c306-aaf7-48560314777b.htm) |  |
| 公共方法 | [SetSampleTriggerCount](25c771ea-458f-4011-15a3-e8bd05a19186.htm) |  |
| 公共方法 | [SetSampleTriggerSlope](870de269-a6c6-95c7-4ee2-6e2f0ab70c59.htm) |  |
| 公共方法 | [SetSampleTriggerSource](ffda0700-7f99-d49e-e00b-723490147f1b.htm) |  |
| 公共方法 | [SetThermistorType](c468c870-0c62-6eb2-a04b-210b0545b8c3.htm) |  |
| 公共方法 | [SetTransducerType](f42985d4-5d33-dbf0-0c7a-e966435abd7b.htm) |  |
| 公共方法 | [SetWaveformCoupling](e29df7b1-b66a-2109-f6b5-c2e88966806d.htm) |  |

[Top](#PageHeader)

参见

##### 引用

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


### IDmm_Instr 方法

|  |  |
| --- | --- |
|  | IDmm\_Instr 方法 |

[IDmm\_Instr](fd964376-5682-d647-6f9b-65b503f82e00.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Abort](94f5cbfb-5fce-78c1-49d1-9d979998105b.htm) |  |
| 公共方法 | [ConfigureACBandwidth](8550f639-87c3-6ea5-f6e8-145cfb8297dc.htm) |  |
| 公共方法 | [ConfigureMeasurement(String, Double, Double)](0ff519c7-7ffa-d5c4-6863-5b6196b25729.htm) |  |
| 公共方法 | [ConfigureMeasurement(String, String, Double)](71d37520-5e82-7c07-cfa7-8a0ff0675aa1.htm) |  |
| 公共方法 | [ConfigureMeasurementTrigger(String, Boolean)](5e9657db-2b05-2099-f262-726ce3e2bb3b.htm) |  |
| 公共方法 | [ConfigureMeasurementTrigger(String, Double)](dbf8e85d-a7ee-d756-f9ac-d9bb7013eba5.htm) |  |
| 公共方法 | [ConfigureMultiPoint](80d30313-9300-8c3a-cc89-be2c19417ebf.htm) |  |
| 公共方法 | [ConfigureOpenCableCompensation](db7ce82f-b538-2953-7fb3-7f3e2cb340ee.htm) |  |
| 公共方法 | [ConfigureRTDCustom](3216c872-8e0a-8233-36c3-84a4f74d6ff9.htm) |  |
| 公共方法 | [ConfigureRTDType](c04eaf7c-3ea1-d05e-2469-da7f23b5dc31.htm) |  |
| 公共方法 | [ConfigureShortCableCompensation](b3a31dfc-5199-2f91-a02b-719cdb735e57.htm) |  |
| 公共方法 | [ConfigureThermistorCustom](3f86382f-5bb0-fa27-2ca7-d8a1eb3f3d9b.htm) |  |
| 公共方法 | [ConfigureThermocouple](40d6a89d-51f1-2565-8463-432e6c23a886.htm) |  |
| 公共方法 | [ConfigureWaveformAcquisition](7a8e2ecc-a3d1-85a0-1dba-5dcf71343272.htm) |  |
| 公共方法 | [Fetch](6424ec9e-f337-69a8-2a39-07af962c0575.htm) |  |
| 公共方法 | [FetchMultiPoint(Double)](25e502bd-3154-cccc-b983-fa383398619d.htm) |  |
| 公共方法 | [FetchMultiPoint(Double, Int32)](b4a39410-b0e8-eea2-6285-ee0768aace25.htm) |  |
| 公共方法 | [FetchWaveform](c05220fd-313f-9523-e25e-8423af29d4ca.htm) |  |
| 公共方法 | [GetAbsoluteResolution](3e61cfc4-2eb4-8cda-e4b2-15a16b883d95.htm) |  |
| 公共方法 | [GetACMaxFrequency](2b762ce0-c49e-6877-771d-73812e179520.htm) |  |
| 公共方法 | [GetACMinFrequency](a01e128b-1dcb-3a20-b9f0-c3816811b330.htm) |  |
| 公共方法 | [GetApertureTime](2920fd85-7ad3-3b07-b111-3f70f7b9d24d.htm) |  |
| 公共方法 | [GetAttributeT](4e2f4004-7435-95ab-61fb-8214f00cb397.htm) |  |
| 公共方法 | [GetAutoRange](b69d6fdb-2403-348b-197e-6afa61c49259.htm) |  |
| 公共方法 | [GetAutoRangeValue](062a1cad-fbf0-e064-6417-19c0848e934b.htm) |  |
| 公共方法 | [GetAutoZero](e38774ad-a112-f8d9-79e7-debe50d4ead8.htm) |  |
| 公共方法 | [GetCableCompensationType](709c4a39-3694-db47-5d57-9e0c1dbd83b9.htm) |  |
| 公共方法 | [GetDiodeCurrentSource](d0946e14-d596-b4db-82a5-6946d8ff157d.htm) |  |
| 公共方法 | [GetFixedReferenceJunction](833e8b6d-3be9-6322-2917-037fe8da4958.htm) |  |
| 公共方法 | [GetFrequencyMeasurementVoltageAutoRange](b6b01752-db93-6550-d052-8417cce81203.htm) |  |
| 公共方法 | [GetFrequencyMeasurementVoltageRange](f7414824-b585-ec8c-1868-ab3ebf5aba82.htm) |  |
| 公共方法 | [GetInputResistance](6984c99b-7291-0d24-004b-9729b91b656a.htm) |  |
| 公共方法 | [GetMeasurementCompleteDestination](e443b954-008e-68a2-e624-496378f3a8b1.htm) |  |
| 公共方法 | [GetMeasurementCompleteSlope](e6119d8e-c2cb-2a18-24d0-86067281c8d0.htm) |  |
| 公共方法 | [GetMeasurementFunction](11e00c9a-3fe8-30c0-034e-64869fe07ad7.htm) |  |
| 公共方法 | [GetMeasurementPeriod](a67f5250-ae9d-fc67-1fef-bd842dfbe6a6.htm) |  |
| 公共方法 | [GetMeasurementTriggerDelay](d852d11f-e943-4784-7040-b9bd929b32af.htm) |  |
| 公共方法 | [GetMeasurementTriggerDelayAuto](f740bc7b-9af9-796b-b00a-d89c5c6243b7.htm) |  |
| 公共方法 | [GetMeasurementTriggerSlope](8ddd4a73-a6cf-6962-26f8-267ca1079cae.htm) |  |
| 公共方法 | [GetMeasurementTriggerSource](94d24505-3409-d0e4-ca01-26c1c2675099.htm) |  |
| 公共方法 | [GetOffsetCompensatedOhmEnabled](23a5711a-4fa8-aa71-1961-a11942c4c97e.htm) |  |
| 公共方法 | [GetOperationMode](e875ef90-3241-e276-8817-8d6b2e13e33f.htm) |  |
| 公共方法 | [GetRange](ce4d00d8-7b2b-e751-8c05-e7263a0c01e4.htm) |  |
| 公共方法 | [GetResolution](53c41db2-c3b1-efca-d6e8-530f3fbfa33e.htm) |  |
| 公共方法 | [GetSampleCount](d4dfad54-5f1b-8462-3bf5-bb9b8d265f85.htm) |  |
| 公共方法 | [GetSampleInterval](3726b08b-cc95-e912-2dc1-fbf8becffe91.htm) |  |
| 公共方法 | [GetSampleTriggerCount](1c612c08-583e-10ea-1212-3808cf9c82b0.htm) |  |
| 公共方法 | [GetSampleTriggerSlope](e9d6f22a-3c9f-9f6b-c1e0-faf56e355b40.htm) |  |
| 公共方法 | [GetSampleTriggerSource](c406bc36-fed9-de50-dc81-13e085d87d98.htm) |  |
| 公共方法 | [GetThermistorType](9e463582-a648-094d-3319-e4f716d9eeee.htm) |  |
| 公共方法 | [GetTransducerType](24d42c16-7f1b-8a62-b187-b951a4681a15.htm) |  |
| 公共方法 | [GetWaveformCoupling](2549c0a4-2df3-372e-bfcf-8d1a760f0096.htm) |  |
| 公共方法 | [Initiate](2a4d1938-3699-34f2-529c-7f2723276fa9.htm) |  |
| 公共方法 | [IsOverRange](e6b870d9-ff34-f12d-2454-a7b5bf3e34fa.htm) |  |
| 公共方法 | [IsUnderRange](5b4b82e1-49a5-c6e1-0225-1768c1ed162d.htm) |  |
| 公共方法 | [PerformOpenCableCompensation](3d4f5147-bf05-ec24-1fea-a1fd34a2e994.htm) |  |
| 公共方法 | [PerformShortCableCompensation](91d9242d-6604-addd-dcbf-ab61ebe97744.htm) |  |
| 公共方法 | [Read](be6290b0-990b-fd06-804b-255f512d0f0b.htm) |  |
| 公共方法 | [ReadMultiPoint(Double)](bca0451d-94dc-505b-f6ed-beed255871d1.htm) |  |
| 公共方法 | [ReadMultiPoint(Double, Int32)](8cbf572e-a12f-5046-bfc6-ececc592c211.htm) |  |
| 公共方法 | [ReadWaveform](240484c3-1793-dd9c-2ad7-d7fbf038873d.htm) |  |
| 公共方法 | [Reset](7c62eb70-73d6-6c5d-d941-4aef79e61bd1.htm) |  |
| 公共方法 | [SendSoftwareTrigger](57602041-ed22-2ee5-82b5-c03f87cf44e7.htm) |  |
| 公共方法 | [SetAbsoluteResolution](3a593648-74cd-e716-43ee-3f9c611efcaa.htm) |  |
| 公共方法 | [SetACMaxFrequency](5a7a3a9d-0512-35d1-8d27-4e4539f2ea9e.htm) |  |
| 公共方法 | [SetACMinFrequency](15b405aa-5cab-2592-01ca-a1edf1620028.htm) |  |
| 公共方法 | [SetApertureTime](46643f36-e051-1925-0af1-669fae3449e7.htm) |  |
| 公共方法 | [SetAttribute](fcdfc860-4923-da58-a88e-3fa2b4e2adf2.htm) |  |
| 公共方法 | [SetAutoRange](ba32e97b-0cca-d7bc-4ae3-de53e99b5d03.htm) |  |
| 公共方法 | [SetAutoZero](d09fab85-b45e-3f56-b5a5-f2ab7ff2aa56.htm) |  |
| 公共方法 | [SetCableCompensationType](b1d14e8d-78c9-69c0-bc3e-682395da168f.htm) |  |
| 公共方法 | [SetDiodeCurrentSource](5a4222d6-0152-8abe-3c56-6b4d9189beed.htm) |  |
| 公共方法 | [SetFixedReferenceJunction](0f365e12-5537-4c27-f801-775eebf9a358.htm) |  |
| 公共方法 | [SetFrequencyMeasurementVoltageRange](deae71f4-83bd-2b51-96ef-d4b69c83eca8.htm) |  |
| 公共方法 | [SetInputResistance](1f94f89d-ef39-2133-df51-f6ceda29a675.htm) |  |
| 公共方法 | [SetMeasurementCompleteDestination](428a8d7f-915c-7be9-2914-db042a9de102.htm) |  |
| 公共方法 | [SetMeasurementCompleteSlope](7de22611-20b4-b57a-4dfe-faec68bba21b.htm) |  |
| 公共方法 | [SetMeasurementFunction](6fe8893c-a3d1-2116-ab8e-a7e043f69f7d.htm) |  |
| 公共方法 | [SetMeasurementTriggerDelay](9efd1d14-75a3-5722-bf6d-42fb01a1196e.htm) |  |
| 公共方法 | [SetMeasurementTriggerDelayAuto](2a6c7128-d03e-599f-2cd2-29aef61250f8.htm) |  |
| 公共方法 | [SetMeasurementTriggerSlope](078c992c-6df9-a4dd-65c5-2ad42fd69e35.htm) |  |
| 公共方法 | [SetMeasurementTriggerSource](142c6082-c4c8-f9b6-292d-22cf7add4148.htm) |  |
| 公共方法 | [SetOffsetCompensatedOhmEnabled](da68fb8e-c2b9-9e91-cd16-add24ef34dcf.htm) |  |
| 公共方法 | [SetOperationMode](e0167fcb-3ea8-d250-0f31-972c08833452.htm) |  |
| 公共方法 | [SetRange](542a99bd-63c9-853c-f119-adbe3715a484.htm) |  |
| 公共方法 | [SetResolution](96bc3284-48f1-9a06-ce65-1f01c9f8ca2a.htm) |  |
| 公共方法 | [SetSampleCount](72f71972-a4a9-135e-ac5c-d56b5e2db4a1.htm) |  |
| 公共方法 | [SetSampleInterval](bb6e0a0d-4442-c306-aaf7-48560314777b.htm) |  |
| 公共方法 | [SetSampleTriggerCount](25c771ea-458f-4011-15a3-e8bd05a19186.htm) |  |
| 公共方法 | [SetSampleTriggerSlope](870de269-a6c6-95c7-4ee2-6e2f0ab70c59.htm) |  |
| 公共方法 | [SetSampleTriggerSource](ffda0700-7f99-d49e-e00b-723490147f1b.htm) |  |
| 公共方法 | [SetThermistorType](c468c870-0c62-6eb2-a04b-210b0545b8c3.htm) |  |
| 公共方法 | [SetTransducerType](f42985d4-5d33-dbf0-0c7a-e966435abd7b.htm) |  |
| 公共方法 | [SetWaveformCoupling](e29df7b1-b66a-2109-f6b5-c2e88966806d.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### Abort 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrAbort 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Abort()
```

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ConfigureACBandwidth 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrConfigureACBandwidth 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureACBandwidth(
	double minFreq,
	double maxFreq
)
```

###### 参数

minFreq  Double

maxFreq  Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ConfigureMeasurement 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrConfigureMeasurement 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [ConfigureMeasurement(String, Double, Double)](0ff519c7-7ffa-d5c4-6863-5b6196b25729.htm) |  |
| 公共方法 | [ConfigureMeasurement(String, String, Double)](71d37520-5e82-7c07-cfa7-8a0ff0675aa1.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


##### ConfigureMeasurement(String, Double, Double) 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrConfigureMeasurement(String, Double, Double) 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureMeasurement(
	string measurementFunction,
	double range,
	double resolutionDigits
)
```

###### 参数

measurementFunction  String

range  Double

resolutionDigits  Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[ConfigureMeasurement 重载](570f9430-26d3-e072-980e-1a3ef633764b.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


##### ConfigureMeasurement(String, String, Double) 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrConfigureMeasurement(String, String, Double) 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureMeasurement(
	string measurementFunction,
	string autoRange,
	double resolutionDigits
)
```

###### 参数

measurementFunction  String

autoRange  String

resolutionDigits  Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[ConfigureMeasurement 重载](570f9430-26d3-e072-980e-1a3ef633764b.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ConfigureMeasurementTrigger 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrConfigureMeasurementTrigger 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [ConfigureMeasurementTrigger(String, Boolean)](5e9657db-2b05-2099-f262-726ce3e2bb3b.htm) |  |
| 公共方法 | [ConfigureMeasurementTrigger(String, Double)](dbf8e85d-a7ee-d756-f9ac-d9bb7013eba5.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


##### ConfigureMeasurementTrigger(String, Boolean) 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrConfigureMeasurementTrigger(String, Boolean) 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureMeasurementTrigger(
	string triggerSource,
	bool autoTriggerDelay
)
```

###### 参数

triggerSource  String

autoTriggerDelay  Boolean

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[ConfigureMeasurementTrigger 重载](f02d2a35-dd12-67ad-d6fc-2229f59ab09c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


##### ConfigureMeasurementTrigger(String, Double) 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrConfigureMeasurementTrigger(String, Double) 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureMeasurementTrigger(
	string triggerSource,
	double triggerDelay
)
```

###### 参数

triggerSource  String

triggerDelay  Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[ConfigureMeasurementTrigger 重载](f02d2a35-dd12-67ad-d6fc-2229f59ab09c.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ConfigureMultiPoint 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrConfigureMultiPoint 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureMultiPoint(
	int triggerCount,
	int sampleCount,
	string sampleTrigger,
	double sampleInterval
)
```

###### 参数

triggerCount  Int32

sampleCount  Int32

sampleTrigger  String

sampleInterval  Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ConfigureOpenCableCompensation 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrConfigureOpenCableCompensation 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureOpenCableCompensation(
	double conductance,
	double susceptance
)
```

###### 参数

conductance  Double

susceptance  Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ConfigureRTDCustom 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrConfigureRTDCustom 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureRTDCustom(
	double rtdA,
	double rtdB,
	double rtdC
)
```

###### 参数

rtdA  Double

rtdB  Double

rtdC  Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ConfigureRTDType 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrConfigureRTDType 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureRTDType(
	string rtdType,
	double rtdResistance
)
```

###### 参数

rtdType  String

rtdResistance  Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ConfigureShortCableCompensation 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrConfigureShortCableCompensation 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureShortCableCompensation(
	double resistance,
	double reactance
)
```

###### 参数

resistance  Double

reactance  Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ConfigureThermistorCustom 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrConfigureThermistorCustom 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureThermistorCustom(
	double thermistorA,
	double thermistorB,
	double thermistorC
)
```

###### 参数

thermistorA  Double

thermistorB  Double

thermistorC  Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ConfigureThermocouple 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrConfigureThermocouple 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureThermocouple(
	string thermocoupleType,
	string refJunctionType
)
```

###### 参数

thermocoupleType  String

refJunctionType  String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ConfigureWaveformAcquisition 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrConfigureWaveformAcquisition 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureWaveformAcquisition(
	string measurementFunction,
	double range,
	double rate,
	int waveformPoints
)
```

###### 参数

measurementFunction  String

range  Double

rate  Double

waveformPoints  Int32

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### Fetch 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrFetch 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double Fetch(
	double timeout
)
```

###### 参数

timeout  Double

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### FetchMultiPoint 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrFetchMultiPoint 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [FetchMultiPoint(Double)](25e502bd-3154-cccc-b983-fa383398619d.htm) |  |
| 公共方法 | [FetchMultiPoint(Double, Int32)](b4a39410-b0e8-eea2-6285-ee0768aace25.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


##### FetchMultiPoint(Double) 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrFetchMultiPoint(Double) 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] FetchMultiPoint(
	double timeout
)
```

###### 参数

timeout  Double

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[FetchMultiPoint 重载](07ee904f-cf69-603c-4855-bed98f9b5350.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


##### FetchMultiPoint(Double, Int32) 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrFetchMultiPoint(Double, Int32) 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] FetchMultiPoint(
	double timeout,
	int pointsToFetch
)
```

###### 参数

timeout  Double

pointsToFetch  Int32

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[FetchMultiPoint 重载](07ee904f-cf69-603c-4855-bed98f9b5350.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### FetchWaveform 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrFetchWaveform 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] FetchWaveform(
	int pointsToFetch,
	double timeout
)
```

###### 参数

pointsToFetch  Int32

timeout  Double

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetAbsoluteResolution 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetAbsoluteResolution 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetAbsoluteResolution()
```

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetACMaxFrequency 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetACMaxFrequency 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetACMaxFrequency()
```

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetACMinFrequency 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetACMinFrequency 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetACMinFrequency()
```

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetApertureTime 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetApertureTime 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetApertureTime()
```

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetAttribute&lt;T&gt; 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetAttributeT 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
Object GetAttribute<T>(
	long id,
	string channelNumber
)
```

###### 参数

id  Int64

channelNumber  String

###### 类型参数

T

###### 返回值

Object

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetAutoRange 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetAutoRange 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetAutoRange()
```

###### 返回值

String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetAutoRangeValue 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetAutoRangeValue 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetAutoRangeValue()
```

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetAutoZero 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetAutoZero 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetAutoZero()
```

###### 返回值

String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetCableCompensationType 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetCableCompensationType 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetCableCompensationType()
```

###### 返回值

String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetDiodeCurrentSource 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetDiodeCurrentSource 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetDiodeCurrentSource()
```

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetFixedReferenceJunction 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetFixedReferenceJunction 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetFixedReferenceJunction()
```

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetFrequencyMeasurementVoltageAutoRange 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetFrequencyMeasurementVoltageAutoRange 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetFrequencyMeasurementVoltageAutoRange()
```

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetFrequencyMeasurementVoltageRange 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetFrequencyMeasurementVoltageRange 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetFrequencyMeasurementVoltageRange()
```

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetInputResistance 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetInputResistance 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetInputResistance()
```

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetMeasurementCompleteDestination 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetMeasurementCompleteDestination 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetMeasurementCompleteDestination()
```

###### 返回值

String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetMeasurementCompleteSlope 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetMeasurementCompleteSlope 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetMeasurementCompleteSlope()
```

###### 返回值

String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetMeasurementFunction 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetMeasurementFunction 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetMeasurementFunction()
```

###### 返回值

String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetMeasurementPeriod 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetMeasurementPeriod 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetMeasurementPeriod()
```

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetMeasurementTriggerDelay 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetMeasurementTriggerDelay 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetMeasurementTriggerDelay()
```

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetMeasurementTriggerDelayAuto 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetMeasurementTriggerDelayAuto 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool GetMeasurementTriggerDelayAuto()
```

###### 返回值

Boolean

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetMeasurementTriggerSlope 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetMeasurementTriggerSlope 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetMeasurementTriggerSlope()
```

###### 返回值

String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetMeasurementTriggerSource 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetMeasurementTriggerSource 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetMeasurementTriggerSource()
```

###### 返回值

String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetOffsetCompensatedOhmEnabled 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetOffsetCompensatedOhmEnabled 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool GetOffsetCompensatedOhmEnabled()
```

###### 返回值

Boolean

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetOperationMode 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetOperationMode 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetOperationMode()
```

###### 返回值

String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetRange 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetRange 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetRange()
```

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetResolution 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetResolution 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetResolution()
```

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetSampleCount 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetSampleCount 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetSampleCount()
```

###### 返回值

Int32

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetSampleInterval 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetSampleInterval 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetSampleInterval()
```

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetSampleTriggerCount 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetSampleTriggerCount 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetSampleTriggerCount()
```

###### 返回值

Int32

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetSampleTriggerSlope 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetSampleTriggerSlope 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetSampleTriggerSlope()
```

###### 返回值

String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetSampleTriggerSource 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetSampleTriggerSource 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetSampleTriggerSource()
```

###### 返回值

String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetThermistorType 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetThermistorType 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetThermistorType()
```

###### 返回值

String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetTransducerType 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetTransducerType 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetTransducerType()
```

###### 返回值

String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### GetWaveformCoupling 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrGetWaveformCoupling 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetWaveformCoupling()
```

###### 返回值

String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### Initiate 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrInitiate 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Initiate()
```

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### IsOverRange 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrIsOverRange 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool IsOverRange(
	double measurementValue
)
```

###### 参数

measurementValue  Double

###### 返回值

Boolean

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### IsUnderRange 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrIsUnderRange 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool IsUnderRange(
	double measurementValue
)
```

###### 参数

measurementValue  Double

###### 返回值

Boolean

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### PerformOpenCableCompensation 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrPerformOpenCableCompensation 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] PerformOpenCableCompensation()
```

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### PerformShortCableCompensation 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrPerformShortCableCompensation 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] PerformShortCableCompensation()
```

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### Read 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrRead 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double Read(
	double timeout
)
```

###### 参数

timeout  Double

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ReadMultiPoint 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrReadMultiPoint 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [ReadMultiPoint(Double)](bca0451d-94dc-505b-f6ed-beed255871d1.htm) |  |
| 公共方法 | [ReadMultiPoint(Double, Int32)](8cbf572e-a12f-5046-bfc6-ececc592c211.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


##### ReadMultiPoint(Double) 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrReadMultiPoint(Double) 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] ReadMultiPoint(
	double timeout
)
```

###### 参数

timeout  Double

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[ReadMultiPoint 重载](70c320e8-af40-95af-ae56-3cecd1f4f4e0.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


##### ReadMultiPoint(Double, Int32) 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrReadMultiPoint(Double, Int32) 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] ReadMultiPoint(
	double timeout,
	int pointsToFetch
)
```

###### 参数

timeout  Double

pointsToFetch  Int32

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[ReadMultiPoint 重载](70c320e8-af40-95af-ae56-3cecd1f4f4e0.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### ReadWaveform 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrReadWaveform 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] ReadWaveform(
	int pointsToFetch,
	double timeout
)
```

###### 参数

pointsToFetch  Int32

timeout  Double

###### 返回值

Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### Reset 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrReset 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Reset()
```

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SendSoftwareTrigger 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSendSoftwareTrigger 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SendSoftwareTrigger()
```

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetAbsoluteResolution 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetAbsoluteResolution 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetAbsoluteResolution(
	double resolution
)
```

###### 参数

resolution  Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetACMaxFrequency 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetACMaxFrequency 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetACMaxFrequency(
	double frequency
)
```

###### 参数

frequency  Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetACMinFrequency 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetACMinFrequency 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetACMinFrequency(
	double frequency
)
```

###### 参数

frequency  Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetApertureTime 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetApertureTime 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetApertureTime(
	double apertureTime
)
```

###### 参数

apertureTime  Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetAttribute 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetAttribute 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetAttribute(
	long id,
	string channelNumber,
	Object value
)
```

###### 参数

id  Int64

channelNumber  String

value  Object

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetAutoRange 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetAutoRange 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetAutoRange(
	string autoRange
)
```

###### 参数

autoRange  String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetAutoZero 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetAutoZero 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetAutoZero(
	string autoZero
)
```

###### 参数

autoZero  String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetCableCompensationType 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetCableCompensationType 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetCableCompensationType(
	string typeOfCompensation
)
```

###### 参数

typeOfCompensation  String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetDiodeCurrentSource 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetDiodeCurrentSource 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetDiodeCurrentSource(
	double diodeCurrentSource
)
```

###### 参数

diodeCurrentSource  Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetFixedReferenceJunction 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetFixedReferenceJunction 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetFixedReferenceJunction(
	double fixedRefJunction
)
```

###### 参数

fixedRefJunction  Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetFrequencyMeasurementVoltageRange 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetFrequencyMeasurementVoltageRange 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetFrequencyMeasurementVoltageRange(
	double voltageRange
)
```

###### 参数

voltageRange  Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetInputResistance 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetInputResistance 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetInputResistance(
	double resistance
)
```

###### 参数

resistance  Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetMeasurementCompleteDestination 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetMeasurementCompleteDestination 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetMeasurementCompleteDestination(
	string destination
)
```

###### 参数

destination  String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetMeasurementCompleteSlope 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetMeasurementCompleteSlope 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetMeasurementCompleteSlope(
	string slope
)
```

###### 参数

slope  String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetMeasurementFunction 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetMeasurementFunction 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetMeasurementFunction(
	string function
)
```

###### 参数

function  String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetMeasurementTriggerDelay 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetMeasurementTriggerDelay 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetMeasurementTriggerDelay(
	double delay
)
```

###### 参数

delay  Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetMeasurementTriggerDelayAuto 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetMeasurementTriggerDelayAuto 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetMeasurementTriggerDelayAuto(
	bool auto
)
```

###### 参数

auto  Boolean

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetMeasurementTriggerSlope 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetMeasurementTriggerSlope 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetMeasurementTriggerSlope(
	string triggerSlope
)
```

###### 参数

triggerSlope  String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetMeasurementTriggerSource 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetMeasurementTriggerSource 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetMeasurementTriggerSource(
	string source
)
```

###### 参数

source  String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetOffsetCompensatedOhmEnabled 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetOffsetCompensatedOhmEnabled 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetOffsetCompensatedOhmEnabled(
	bool enable
)
```

###### 参数

enable  Boolean

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetOperationMode 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetOperationMode 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetOperationMode(
	string operationMode
)
```

###### 参数

operationMode  String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetRange 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetRange 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetRange(
	double range
)
```

###### 参数

range  Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetResolution 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetResolution 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetResolution(
	double resolution
)
```

###### 参数

resolution  Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetSampleCount 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetSampleCount 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSampleCount(
	int sampleCount
)
```

###### 参数

sampleCount  Int32

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetSampleInterval 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetSampleInterval 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSampleInterval(
	double sampleInterval
)
```

###### 参数

sampleInterval  Double

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetSampleTriggerCount 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetSampleTriggerCount 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSampleTriggerCount(
	int triggerCount
)
```

###### 参数

triggerCount  Int32

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetSampleTriggerSlope 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetSampleTriggerSlope 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSampleTriggerSlope(
	string slope
)
```

###### 参数

slope  String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetSampleTriggerSource 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetSampleTriggerSource 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSampleTriggerSource(
	string sampleTrigger
)
```

###### 参数

sampleTrigger  String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetThermistorType 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetThermistorType 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetThermistorType(
	string thermistorType
)
```

###### 参数

thermistorType  String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetTransducerType 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetTransducerType 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetTransducerType(
	string transducerType
)
```

###### 参数

transducerType  String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)


#### SetWaveformCoupling 方法

|  |  |
| --- | --- |
|  | IDmm\_InstrSetWaveformCoupling 方法 |

  
**命名空间：** [DmmParent](f174b464-2f1b-0ec0-f305-d1478c888077.htm)  
**程序集：** DmmMeasStation (在 DmmMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetWaveformCoupling(
	string coupling
)
```

###### 参数

coupling  String

参见

###### 引用

[IDmm\_Instr 接口](fd964376-5682-d647-6f9b-65b503f82e00.htm)

[DmmParent 命名空间](f174b464-2f1b-0ec0-f305-d1478c888077.htm)

