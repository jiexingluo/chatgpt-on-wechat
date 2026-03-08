|  |  |
| --- | --- |
|  | FgenParent 命名空间 |

类

|  | 类 | 说明 |
| --- | --- | --- |
| 公共类 | [Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm) |  |

接口

|  | 接口 | 说明 |
| --- | --- | --- |
| 公共接口 | [IFgen\_Instr](38633742-c0b8-a5f5-8b69-2f6127289703.htm) |  |


## Fgen 类

|  |  |
| --- | --- |
|  | Fgen 类 |

继承层次

SystemObject
  
  MeasStation  
    FgenParentFgen

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public class Fgen : MeasStation
```

Fgen 类型公开以下成员。

构造函数

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Fgen](a2b747cd-2d0a-abbe-0cf4-c1a9d7d1b81a.htm) | 初始化 Fgen 类的一个新实例 |

[Top](#PageHeader)

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [AbortGeneration](87d56c03-6ebf-999f-bfe8-1be88bcb7f0f.htm) | Aborts any previously initiated signal generation. |
| 公共方法 | [AdjustRelativeDelay](6a2ac2e7-4782-862d-f5a4-59d01e5508c4.htm) | Delays (or phase shifts) the sample clock, which delays the output of the module. |
| 公共方法 | [AllocateArbWaveform](02c34733-ca62-566b-a2a3-cae7a19085e0.htm) | Specifies the size of a waveform and allocates it in onboard memory before loading the associated data. Data can be loaded in smaller blocks with the Write methods. |
| 公共方法 | [AllocateNamedWaveform](5ff4e50b-1da7-5ecb-1183-3150a784b340.htm) | Sets the initial size of a named waveform so that it can be allocated in onboard memory before loading the associated data. After you allocate, call WriteNamedWaveform to load data in smaller blocks. |
| 公共方法 | [ClearArbMemory](c1991769-27d9-4435-1235-a4052cd199da.htm) | Removes all previously created arbitrary waveforms, sequences, and scripts from the signal generator memory, and invalidates all waveform handles, sequence handles, and waveform names. |
| 公共方法 | [ClearArbSequence](18df42dd-ed38-f5a2-06ca-39c92973c50f.htm) | Removes a previously created arbitrary sequence from the function generator's memory and invalidates the sequence’s handle. |
| 公共方法 | [ClearArbWaveform](596064f2-abe2-a808-7781-bbf6ddab3334.htm) | Removes a previously created arbitrary waveform from the signal generator memory and invalidates the waveform handle. |
| 公共方法 | [ClearFrequencyList](d5b65c20-48d9-63cd-b8a6-43e15668ffe0.htm) | Removes a previously created frequency list from the signal generator memory and invalidates the frequency list handle. |
| 公共方法 | [ClearUserStandardWaveform](17dd1104-4532-855c-9fee-012b55c5d044.htm) | Clears the user-defined waveform created using DefineUserStandardWaveform. |
| 公共方法 | [Commit](3e8ab0f4-ecca-36e7-223a-0adce1f3a480.htm) | Causes a transition to the committed state. |
| 公共方法 | [ConfigureArbSequence](2f7a88cc-27b3-ecfa-250c-ba874ad62a8c.htm) | Configures the signal generator properties that affect arbitrary sequence generation. |
| 公共方法 | [ConfigureArbWaveform](b9b0996d-5ba2-7d1f-08ee-00b1e02dd6f8.htm) | Configures the properties of the signal generator that affect arbitrary waveform generation, selects the arbitrary waveform to produce, and sets the gain and offset. |
| 公共方法 | [ConfigureDigitalEdgeTrigger](45f6012e-f319-90bc-143e-005235175440.htm) | Configures the trigger for digital edge triggering. |
| 公共方法 | [ConfigureDigitalLevelScriptTrigger](c0079aaf-0023-b47c-c360-9715294f1637.htm) | Configures the script trigger for digital level triggering. |
| 公共方法 | [ConfigureFrequencyList](6c25fd1f-5dbc-c200-d39c-d7d39cefb935.htm) | Configures the amplitude, DC offset, and start phase for the specified frequency list. |
| 公共方法 | [ConfigureReferenceClock](d2687c41-82ba-0555-8510-b075f0e72a3a.htm) | Configures the signal generator reference clock source and frequency. The signal generator uses the reference clock to tune the sample clock timebase of the signal generator so that the frequency, stability, and accuracy of the sample clock timebase matches that of the reference clock. |
| 公共方法 | [ConfigureSampleClock](8911b6e1-7048-a986-b346-4b83ec151517.htm) | Configure sample clock, the smaplesPerChannel is not necessary. |
| 公共方法 | [ConfigureSoftwareEdgeTrigger](f25c964f-2884-8772-a862-b81c766e354b.htm) | Configures the trigger for software edge triggering. |
| 公共方法 | [ConfigureStandardWavaform](bdac2a81-83e5-88ec-046d-b1ff7241dd2f.htm) | Configures the properties of the signal generator that affect standard waveform generation. |
| 公共方法 | [CreateArbSequence(Int64, Int64)](ae6c7974-ddf8-94de-b56c-72552935934a.htm) | Creates an arbitrary waveform sequence from an array of waveform handles and a corresponding array of loop counts. |
| 公共方法 | [CreateArbSequence(Int64, Int64, Int64, Int64)](4139cbb2-a4c4-93be-9363-f56048813e46.htm) | Creates an arbitrary sequence from an array of waveform handles and an array of corresponding loop counts and returns a handle that identifies the sequence. |
| 公共方法 | [CreateChannelArbWaveform](31cc1bbb-af97-3be3-557e-0fe3abc38307.htm) | Creates an onboard waveform from the waveform parameter for use in Arbitrary or Sequence. |
| 公共方法 | [CreateChannelArbWaveformFromFile](7f4941c6-6e60-f7ce-e66b-97014f0ac5d3.htm) | Creates an onboard waveform from the file read from the filePath parameter for use in Arbitrary or Sequence. |
| 公共方法 | [CreateFrequencyList](35fb08ee-ee87-fc62-ebe8-721b033f0490.htm) | Creates a frequency list from an array of frequencies and an array of durations for the specified waveform. |
| 公共方法 | [DefineUsetStandardWaveform](9ef3fcd9-5b60-0f40-d384-62b8dff89bb7.htm) | Defines a user waveform for either Function or FrequencyList. The waveform data must be scaled between -1.0 and 1.0. |
| 公共方法 | [DeleteNamedWaveform](fbcaa820-6d1c-d146-2678-53b3ff849c3a.htm) | Deletes the specified named waveform from onboard memory. The waveform specified by waveformName must be allocated using Allocate on the channel specified by channelName. |
| 公共方法 | [DeleteScript](0a1d9e50-803a-694f-25ca-83c521e18c8a.htm) | Deletes the specified script from onboard memory. |
| 公共方法 | [DisableTrigger](5e4a43bf-0edf-a52c-e849-9a18a7196920.htm) | Disables the specified trigger. |
| 公共方法 | [EnableAnalogFilter](4ac7a925-e375-dcaf-b011-59b612bee91a.htm) | Enables the analog filter for the device. |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 公共方法 | [ExportSignal](f46b39c7-589a-10d9-6690-a1dab7184b93.htm) | Routes signals (clocks, triggers, and events) to the output terminal you specify. |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | [GetAmplitude](3478f1a7-8c5b-ba60-01b8-173988b1ecab.htm) | Gets the amplitude of the standard waveform the function generator produces. When the Waveform attribute is set to Waveform DC, this attribute does not affect signal output.The units are volts. |
| 公共方法 | [GetAnalogFilterEnabled](6283eabe-b35a-90e3-3b26-5c775d993682.htm) | Gets a value indicating whether the signal generator applies an analog filter to the output signal. |
| 公共方法 | [GetAnalogPath](31f0a1b0-9f6d-32a1-0394-d3c6402755e8.htm) | Gets the analog signal path. The default valut is "Main". |
| 公共方法 | [GetArbGain](e79d716c-055f-6c7b-5168-2e93f9706cc7.htm) | Gets the factor by which the signal generator scales the arbitrary waveform data. |
| 公共方法 | [GetArbOffset](c7c5c6b6-c462-7cda-7f88-15e9b67bc0a5.htm) | Gets the value the signal generator adds to the arbitrary waveform data. |
| 公共方法 | [GetArbSampleRate](7e57b824-2bde-a279-5968-68731b981665.htm) | Gets the rate, in samples per second, at which the signal generator generates the points in arbitrary waveforms. |
| 公共方法 | [GetArbSequenceHandle](6383189b-e0c0-cc6c-c10a-ce734f8a354b.htm) | Get the handle which arbitrary sequence the function generator produces. |
| 公共方法 | [GetArbSequenceMaxLength](dfb49dd6-5ee1-9b01-eee0-e9a806b61525.htm) | Returns the maximum number of arbitrary waveforms that the function generator allows in an arbitrary sequence. |
| 公共方法 | [GetArbSequenceMaxLoopCount](478ed2ec-5b1b-b2d9-a0d9-ed0a18c433bb.htm) | Returns the maximum number of times that the function generator can repeat a waveform in a sequence. |
| 公共方法 | [GetArbSequenceMinLength](c9b710e7-4341-3e82-c7d8-01b32577c8b1.htm) | Returns the minimum number of arbitrary waveforms that the function generator allows in an arbitrary sequence. |
| 公共方法 | [GetArbSequencesMaxNumber](6c7a34fe-3dfd-b8f7-ecc2-29ede90104f6.htm) | Returns the maximum number of arbitrary sequences that the function generator allows. |
| 公共方法 | [GetArbWaveformHandle](dcc6b38c-3639-1603-3d03-8279376dcc6a.htm) | Returns the handle representing which arbitrary waveform the signal generator produces. |
| 公共方法 | [GetArbWaveformMarkerPosition](e75014de-2ea8-7592-2ba5-bc791a834ff2.htm) | Gets the position for a marker to be asserted in the arbitrary waveform. |
| 公共方法 | [GetArbWaveformMaxSize](23aa022b-5158-647c-af9e-9e9298563a84.htm) | Gets the maximum number of points the signal generator allows in an arbitrary waveform. On some signal generators, this value may vary with remaining onboard memory. |
| 公共方法 | [GetArbWaveformMinSize](1ad8051c-8ca9-7b60-4aa0-57a4d44ea4fa.htm) | Gets the minimum number of points the signal generator allows in an arbitrary waveform. |
| 公共方法 | [GetArbWaveformQuantum](a62ed50b-bf05-8ff7-c085-8eac47f7bc4f.htm) | Gets the quantum value the signal generator allows. The size of each arbitrary waveform must be a multiple of this quantum value. |
| 公共方法 | [GetArbWaveformRepeatCount](39cd7cb3-1233-fadc-4d7d-9bc3e7b43721.htm) | Gets the number of times to repeat the arbitrary waveform when the trigger mode has been set to to Single or Stepped. |
| 公共方法 | [GetArbWaveformsMaxNumber](8ce3e014-b52b-f5b8-c786-1a7ef028dbf3.htm) | Gets the maximum number of arbitrary waveforms that the signal generator allows. On some signal generators, this value may vary with remaining onboard memory. |
| 公共方法 | [GetAttributeBool](6c0cf119-d4fb-21cd-d1c8-10480c60fc65.htm) | Get specific value by attribute identifier. |
| 公共方法 | [GetAttributeDouble](23adde04-28b0-df83-d628-7a9e632dcde9.htm) | Get specific value by attribute identifier. |
| 公共方法 | [GetAttributeInt](c80fd3a9-da04-6c50-0b82-d86e8ca4cab7.htm) | Get specific value by attribute identifier. |
| 公共方法 | [GetAttributeLong](8b4bdd86-a3e3-9201-2c45-d89af2555901.htm) | Get specific value by attribute identifier. |
| 公共方法 | [GetAttributeString](a34240e2-9da4-d5bb-7066-92fa98f636dd.htm) | Get specific value by attribute identifier. |
| 公共方法 | [GetChannelDelay](c920965d-91c4-14a2-fd6a-46fcae99e8b1.htm) | Gets the delay to apply to the analog output of the channel specified by the channel string. |
| 公共方法 | [GetCommonModeOffset](eb8c146e-b967-6a2b-424c-572ce3603224.htm) | Gets the value that the signal generator adds to or subtracts from the arbitrary waveform data. |
| 公共方法 | [GetDCOffset](55301f64-f8d6-7c7d-0225-65721959cbf9.htm) | Gets the DC offset of the standard waveform the function generator produces. If the Waveform attribute is set to Waveform DC, this attribute specifies the DC level the function generator produces.The units are volts. |
| 公共方法 | [GetDigitalFilterEnabled](16e703fd-9055-79d2-d2cf-fbfa73b1b318.htm) | Gets a value indicating whether the signal generator applies a digital filter to the output signal. |
| 公共方法 | [GetDigitalFilterInterpolationFactor](da66fb90-9526-99a0-8dd3-e21144d04b75.htm) | Gets the interpolation factor when the digital filter is enabled. |
| 公共方法 | [GetDigitalGain](997c4523-b7ab-b81d-983d-068ec40b1114.htm) | Gets a factor by which the signal generator digitally multiplies generated data before converting it to an analog signal in the digital-to-analog converter. |
| 公共方法 | [GetDigitalPatternEnabled](be8b9bbf-6802-6cac-e1c6-b5a53daf928a.htm) | Fetches a value indicating whether the signal generator generates a digital pattern corresponding to the output signal. |
| 公共方法 | [GetDutyCycleHigh](d361851b-692f-4197-940b-ef9c45f6fba5.htm) | Gets the duty cycle of the square wave in units of percentage of time the waveform is high. |
| 公共方法 | [GetExternalMultiplier](0b255cad-82ec-9a65-e500-3de320d188dc.htm) | Gets a multiplication factor to use to obtain a desired sample rate from an external Sample Clock. The resulting sample rate is equal to this factor multiplied by the external Sample Clock rate. You can use this property to generate samples at a rate higher than your external clock rate. When using this property, you do not need to explicitly set the external clock rate. |
| 公共方法 | [GetFlatnessCorrectionEnabled](5f5e3deb-da74-2b13-67aa-b5ba26ea9f07.htm) | Gets a value indicating whether flatness correction is enabled. |
| 公共方法 | [GetFrequency](f2b5ee26-f4ca-daa0-9b31-fd7e814bc967.htm) | Gets the frequency of the standard waveform the function generator produces. When the Waveform attribute is set to Waveform DC, this attribute does not affect signal output.The units are Hertz. |
| 公共方法 | [GetFrequencyListDurationQuantum](cd3342fa-3a63-a5ec-aa25-971166a80508.htm) | Gets the quantum of which all durations must be a multiple in a frequency list. |
| 公共方法 | [GetFrequencyListHandle](954d6aa7-d36e-a61f-ddaf-2257922feeff.htm) | Gets which frequency list the signal generator produces. |
| 公共方法 | [GetFrequencyListMaxDuratinon](2cabec75-27ae-92d5-f5b2-159ec40e186b.htm) | Gets the maximum duration of any one step in the frequency list. |
| 公共方法 | [GetFrequencyListMaxLength](402eb4f4-da7a-3b81-0cb8-b26a805af775.htm) | Gets the maximum number of steps that can be in a frequency list. |
| 公共方法 | [GetFrequencyListMaxNumber](687f28ea-5411-8468-7763-ca43313f4814.htm) | Gets the maximum number of frequency lists the signal generator allows. |
| 公共方法 | [GetFrequencyListMinDuration](764a956d-3c1b-4b00-8771-1922304cb012.htm) | Gets the minimum duration of any one step in a frequency list. |
| 公共方法 | [GetFrequencyListMinLength](c3f54159-a6da-51dc-fd38-ba1996348aee.htm) | Gets the minimum number of frequency lists for the specified channel. |
| 公共方法 | [GetHardwareState](9caa3ec8-672b-cdde-977d-16daa9e51893.htm) | Gets a value indicating the hardware state of the signal generator currently in use. |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | [GetIdleValue](b5ac08e2-9509-1205-53c6-d8664a1724a2.htm) | Fetches the value to generate in the Idle state. You must set IdleBehavior to JumpToValue to use this property. |
| 公共方法 | [GetLoadImpedance](6ecb89f3-259d-d4e6-02c5-85c405a751cf.htm) | Gets the load impedance connected to the analog output of the channel. |
| 公共方法 | [GetOutputEnabled](54d0252d-3e0e-a625-72c2-8578787bfa89.htm) | Gets a value indicating whether the output is enabled for a specified channel. |
| 公共方法 | [GetOutputIdleBehavior](7a56b64d-572b-b439-eef6-2b88977839bb.htm) | Gets the behavior of the output signal during the Idle state. |
| 公共方法 | [GetOutputImpedance](bf7232f2-832f-1532-6add-7df52ef0c5eb.htm) | Gets the output impedance of the signal generator at the specified channel. |
| 公共方法 | [GetOutputMode](1769e4c5-8349-d64d-0cff-d252cb6f1cf2.htm) | Gets the output mode of the signal generator. |
| 公共方法 | [GetOutputWaitBehavior](8cdc63dd-243d-2aba-251d-ff09d1db109c.htm) | Gets the behavior of the output while the device is waiting for a Script trigger or executing a wait instruction. |
| 公共方法 | [GetReferenceClockFrequency](77f472d8-ced2-ce38-c020-77e70addc4eb.htm) | Gets the reference clock frequency in hertz (Hz). The signal generator uses the reference clock to derive frequencies and sample rates when generating output. |
| 公共方法 | [GetReferenceClockSource](b04f2e5b-5e47-66bf-981c-a71f55e10980.htm) | Gets the reference clock source used by the signal generator. The function generator derives frequencies and sample rates that it uses to generate waveforms from the reference clock. |
| 公共方法 | [GetSampleClockAbsoluteDelay](b5ac0cd3-5d9d-c196-0c78-51df642e2ab1.htm) | Gets the delay in seconds to apply to an external Sample Clock. This property is useful when trying to align the output of two devices. |
| 公共方法 | [GetSampleClockExportedDivisor](ef5a2f3d-ba2f-0c09-ff6a-5f9b6f032a81.htm) | Gets the factor by which to divide the sample clock, also known as an update clock, before it is exported. To export the sample clock, use ExportSignal or SetSampleClockOutputTerminal. |
| 公共方法 | [GetSampleClockMode](f4b69fc9-84c6-aeb8-e16a-662481b6dab3.htm) | Gets the sample clock mode for the signal generator. |
| 公共方法 | [GetSampleClockRate](49c74502-ab66-3a65-8232-eaf582417304.htm) | Gets the rate, in samples per second, at which the signal generator generates the points |
| 公共方法 | [GetSampleClockSource](d53a793d-485f-9311-14c9-6b806c4a6471.htm) | Gets the sample clock source. |
| 公共方法 | [GetSampleClockTimebaseExportedDivisor](003d3872-de2c-dfa2-e834-5f1a57eb30cb.htm) | Gets the factor by which to divide the device clock (sample clock timebase) before it is exported. To export the sample clock timebase, use ExportSignal or SetSampleClockTimebaseOutputTerminal. |
| 公共方法 | [GetSampleClockTimebaseRate](5761983a-9fbc-aecd-ddf2-9a56480c9baf.htm) | Gets the sample clock timebase rate. This property applies only to an external sample clock timebase. |
| 公共方法 | [GetSampleClockTimebaseSource](507bc28b-7eef-4300-c5a0-db0b267cb418.htm) | Gets the sample clock timebase source. |
| 公共方法 | [GetScriptToGenerate](24285e5c-f375-0db0-6cd8-ce3d459b7f2a.htm) | Gets a value indicating the name of the script that the generator produces. |
| 公共方法 | [GetStartPhase](89d7b115-951a-be0b-6362-837ee80fd91f.htm) | Gets the start phase of the standard waveform the function generator produces. When the Waveform attribute is set to Waveform DC, this attribute does not affect signal output.The units are degrees. |
| 公共方法 | [GetTerminalConfiguration](a2432b6b-924d-1910-1d92-9b1c7241b4bb.htm) | Get the generator terminal configuration information. |
| 公共方法 | [GetTriggerMode](1580a2a7-b130-4182-cc5f-ab2400f07a11.htm) | Gets the trigger mode for the signal generator. |
| 公共方法 | [GetTriggerType](ca26d333-4180-56d6-7bc4-b9ba46b3d027.htm) | Gets the type of trigger for specified triggerId if triggerClass is Script. |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | [GetWaitValue](7b8ddf53-ae82-b95e-1623-2d8c9cd809a9.htm) | Gets the value to generate while waiting. You must set WaitBehavior to JumpToValue to use this method. |
| 公共方法 | [GetWaveformFuntion](468a43cf-4318-cd7b-788e-4dfefb1c19cd.htm) | Gets which standard waveform the function generator produces. |
| 公共方法 | [InitiateGeneration](7feafedf-88cd-ea00-6428-d4386baae29d.htm) | Initiates signal generation |
| 公共方法 | [IsGenerationDone](d463a855-0e53-f88b-6b6d-a8224c5e178d.htm) | Gets a value indicating whether the current generation is complete. |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [Reset](87780fdb-1801-12f8-33b1-80088e0dc79e.htm) | Reset the instrument session. |
| 公共方法 | [SendSoftwareEdgeTrigger](66fec53b-e107-40fd-61e8-18be229175b7.htm) | Sends a command to trigger. |
| 公共方法 | [SetAmplitude](7002eaf5-6d29-4446-2984-545a03634ce4.htm) | Sets the amplitude of the standard waveform the function generator produces. When the Waveform attribute is set to Waveform DC, this attribute does not affect signal output.The units are volts. |
| 公共方法 | [SetAnalogFilterEnabled](2269dd12-1bee-a6de-08bf-1a55dff40e18.htm) | Sets a value indicating whether the signal generator applies an analog filter to the output signal. |
| 公共方法 | [SetAnalogPath](769be0f3-9775-602b-2286-ef1fbf669192.htm) | Sets the analog signal path. The default valut is "Main". The Main path allows the user to configure gain, offset, analog filter status, output impedance, and output enable. The Direct path presents a much smaller gain range, and you cannot adjust offset or the filter status. The Direct path provides a smaller output range but lower distortion. The Main path has two amplifier options, high and low gain. Setting this value to Main allows NI-FGEN to choose the amplifier based on the user-specified gain. |
| 公共方法 | [SetArbGain](c036e714-31dd-c770-6c95-9ec2ce030f35.htm) | Sets the factor by which the signal generator scales the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use the gain to scale the arbitrary waveform to other ranges. |
| 公共方法 | [SetArbOffset](06e48fdd-a981-4f52-82bc-05a35d8686b8.htm) | Sets the value the signal generator adds to the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use the offset to shift the arbitrary waveform range. |
| 公共方法 | [SetArbSampleRate](5b680018-dd06-7084-d6ee-af4193ed636b.htm) | Sets the rate, in samples per second, at which the signal generator generates the points in arbitrary waveforms. Use this property when OutputMode is set to Arbitrary or Sequence. |
| 公共方法 | [SetArbSequenceHandle](eabe0b3e-52c5-4898-7e76-9097ee34b11b.htm) | Identifies which arbitrary sequence the function generator produces. |
| 公共方法 | [SetArbWaveformHandle](b691a70e-662c-e088-9712-309e8c3101c6.htm) | Identifies which arbitrary waveform the function generator produces. |
| 公共方法 | [SetArbWaveformMarkerPosition](4254c589-f348-a0f6-7ce8-4510a83046df.htm) | Sets the position for a marker to be asserted in the arbitrary waveform. Use this property when OutputMode is set to Arbitrary. Use ExportSignal method to export the marker signal. |
| 公共方法 | [SetArbWaveformRepeatCount](ef05a9b7-ea31-42b6-fd49-49f9acb01f31.htm) | Sets the number of times to repeat the arbitrary waveform when the trigger mode has been set to to Single or Stepped. |
| 公共方法 | [SetAttributeBool](471d16eb-9db6-d4ca-1ff0-56aa5df91ee7.htm) | Set specific value by attribute identifier. |
| 公共方法 | [SetAttributeDouble](83946754-0122-9c05-5ffa-2859df8d2be6.htm) | Set specific value by attribute identifier. |
| 公共方法 | [SetAttributeInt](39977dfc-3038-c4aa-7fff-528013cd0f8f.htm) | Set specific value by attribute identifier. |
| 公共方法 | [SetAttributeLong](7ab6f58c-c033-71c6-eec6-5596a672430d.htm) | Set specific value by attribute identifier. |
| 公共方法 | [SetAttributeString](9ffae37c-cb14-cba8-1c1b-06b66722030e.htm) | Set specific value by attribute identifier. |
| 公共方法 | [SetChannelDelay](64b57dc1-2b8c-fd98-e3f3-48f5b050d98b.htm) | Sets the delay to apply to the analog output of the channel specified by the channel string. You can use the output delay to configure the timing relationship between channels on a multichannel device. Values for this property can be zero or positive. A value of zero indicates that the channels are aligned. A positive value delays the analog output by the specified number of seconds. |
| 公共方法 | [SetCommonModeOffset](75e76472-72b4-306b-3380-26c7a68bad01.htm) | Sets the value that the signal generator adds to or subtracts from the arbitrary waveform data. Common-mode offset is applicable only when you set the terminal configuration to Differential. Common-mode offset is applied to the signals generated at each differential output terminal. |
| 公共方法 | [SetDCOffset](a142c4c8-67ff-ae46-6357-d63c7fab1ef1.htm) | Sets the DC offset of the standard waveform the function generator produces. If the Waveform attribute is set to Waveform DC, this attribute specifies the DC level the function generator produces.The units are volts. |
| 公共方法 | [SetDigitalFilterEnabled](38e58151-33f0-5c69-a2e0-ea7ec4c49d7b.htm) | Sets a value indicating whether the signal generator applies a digital filter to the output signal. |
| 公共方法 | [SetDigitalFilterInterpolationFactor](cd7069d3-c81a-4ec0-b356-082413803643.htm) | Sets the interpolation factor when the digital filter is enabled. |
| 公共方法 | [SetDigitalGain](7fe72645-c821-3b9f-1f51-b1cd8295e9bb.htm) | Sets a factor by which the signal generator digitally multiplies generated data before converting it to an analog signal in the digital-to-analog converter. |
| 公共方法 | [SetDigitalPatternEnabled](f0351229-eca0-7476-e1f9-2aca8dfc0c03.htm) | Sets a value indicating whether the signal generator generates a digital pattern corresponding to the output signal. |
| 公共方法 | [SetDutyCycleHigh](94dbe092-c05a-4bb5-8df4-f27c8a069a5f.htm) | Sets the duty cycle of the square wave in units of percentage of time the waveform is high. |
| 公共方法 | [SetExternalMultiplier](e2fb0f48-a929-a56c-dfc5-b96f9d01f9eb.htm) | Sets a multiplication factor to use to obtain a desired sample rate from an external Sample Clock. The resulting sample rate is equal to this factor multiplied by the external Sample Clock rate. You can use this property to generate samples at a rate higher than your external clock rate. When using this property, you do not need to explicitly set the external clock rate. |
| 公共方法 | [SetFlatnessCorrectionEnabled](0f5149f5-58f6-07eb-6b5d-8635e1c397df.htm) | Sets a value indicating whether flatness correction is enabled. |
| 公共方法 | [SetFrequency](01bf70ae-186d-82aa-ba75-23ae9e490733.htm) | Sets the frequency of the standard waveform the function generator produces. When the Waveform attribute is set to Waveform DC, this attribute does not affect signal output.The units are Hertz. |
| 公共方法 | [SetFrequencyListHandle](39341270-8ca1-530a-9710-3b6925e92e8c.htm) | Sets which frequency list the signal generator produces. |
| 公共方法 | [SetIdleValue](c0a538bd-74d1-ae0f-e7b5-ab0f5a35d76c.htm) | Sets the value to generate in the Idle state. You must set IdleBehavior to JumpToValue to use this property. |
| 公共方法 | [SetLoadImpedance](f6ac1c59-0d62-6196-bd5b-90d920f9ed7a.htm) | Sets the load impedance connected to the analog output of the channel. If you set the load impedance to –1.0, NI-FGEN assumes that the load impedance matches the value of the output impedance. |
| 公共方法 | [SetNextWritePosition](d5fbeed5-7fee-d1ce-8e2a-c308e533735d.htm) | Sets the position in the named waveform to which data was written at the next write. |
| 公共方法 | [SetOutputEnabled](33475e2b-f394-3aca-20c2-95fca0fea5ec.htm) | Sets a value indicating whether the output is enabled for a specified channel. |
| 公共方法 | [SetOutputIdleBehavior](51f4ed3b-869e-8c7d-3232-b9080cd9d73f.htm) | Sets the behavior of the output signal during the Idle state. |
| 公共方法 | [SetOutputImpedance](7744893c-4ad4-b558-0c28-ad15b511a249.htm) | Sets the output impedance of the signal generator at the specified channel. This method specifies the output impedance of the signal generator at the output connector. NI signal generators have an output impedance of 50 Ω and an optional 75 Ω on select modules. |
| 公共方法 | [SetOutputMode](fb988af4-5a33-7c59-67c4-6f69cf648bec.htm) | Sets the output mode of the signal generator. |
| 公共方法 | [SetOutputWaitBehavior](c8ccda18-3711-9b54-c1e9-34af2ec423db.htm) | Sets the behavior of the output while the device is waiting for a Script trigger or executing a wait instruction. |
| 公共方法 | [SetReferenceClockFrequency](235c465d-370f-8aae-45fa-49490abc932e.htm) | Sets the reference clock frequency in hertz (Hz). The signal generator uses the reference clock to derive frequencies and sample rates when generating output. |
| 公共方法 | [SetReferenceClockSource](63579d9a-901c-4d3a-4bbd-af404453b9ea.htm) | Sets the reference clock source used by the signal generator. The function generator derives frequencies and sample rates that it uses to generate waveforms from the reference clock. |
| 公共方法 | [SetSampleClockAbsoluteDelay](8d3d70f2-13e9-3787-47f3-dcddb13f8f93.htm) | Sets the delay in seconds to apply to an external Sample Clock. This property is useful when trying to align the output of two devices. |
| 公共方法 | [SetSampleClockExportedDivisor](56f99cbd-8ffb-0e91-9661-ae6c5f718c1f.htm) | Sets the factor by which to divide the sample clock, also known as an update clock, before it is exported. To export the sample clock, use ExportSignal or SetSampleClockOutputTerminal. |
| 公共方法 | [SetSampleClockMode](12759ffd-2a16-57da-ef20-129e33d04ca6.htm) | Sets the sample clock mode for the signal generator. When in DivideDown sampling mode, the sample rate can only be set to certain frequencies, based on dividing down the sample clock. However, in HighResolution mode, the sample rate may be set to any value. |
| 公共方法 | [SetSampleClockRate](8a4463d7-8338-8d00-25cc-cd3f9b7dc61e.htm) | Sets the rate, in samples per second, at which the signal generator generates the points |
| 公共方法 | [SetSampleClockSource](787342e5-b467-323a-8b4b-3af6993c988b.htm) | Sets the sample clock source. |
| 公共方法 | [SetSampleClockTimebaseExportedDivisor](d1cfe2ab-aec9-f7ab-a619-83bce55b8221.htm) | Sets the factor by which to divide the device clock (sample clock timebase) before it is exported. To export the sample clock timebase, use ExportSignal or SetSampleClockTimebaseOutputTerminal. |
| 公共方法 | [SetSampleClockTimebaseRate](34317a4d-3b36-e9c8-6e0b-7486256fa4af.htm) | Sets the sample clock timebase rate. This property applies only to an external sample clock timebase. |
| 公共方法 | [SetSampleClockTimebaseSource](790e4c54-8cc2-05e8-8034-926d0f785750.htm) | Sets the sample clock timebase source. |
| 公共方法 | [SetScriptToGenerate](b4524756-2280-07e1-4fe7-8ba2e6c9262b.htm) | Sets a value indicating the name of the script that the generator produces. OutputMode should be set to Script to call this property. |
| 公共方法 | [SetStartPhase](1c35ca1f-4d23-80d5-47e3-e59d39b2e6a4.htm) | Sets the start phase of the standard waveform the function generator produces. When the Waveform attribute is set to Waveform DC, this attribute does not affect signal output.The units are degrees. |
| 公共方法 | [SetTerminalConfiguration](786aef5f-1090-73f9-cb58-7c7ffff40885.htm) | Determines whether the generator will run in single-ended or differential mode, and whether the output gain and offset values will be analyzed based on single-ended or differential operation. |
| 公共方法 | [SetTriggerMode](af877a4b-67e6-7b15-2373-2c9bbb2db8af.htm) | Sets the trigger mode for the signal generator. |
| 公共方法 | [SetTriggerType](333733bc-9403-9455-ff2b-3c72e8d63b93.htm) | Sets the type of trigger for specified triggerId if triggerClass is Script. |
| 公共方法 | [SetWaitValue](62787996-81fc-e867-239d-a0b70c6b4932.htm) | Sets the value to generate while waiting. You must set WaitBehavior to JumpToValue to use this method. |
| 公共方法 | [SetWaveformFunction](6e6e5d38-c625-40b5-5e73-daab17e39050.htm) | Sets which standard waveform the function generator produces. |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |
| 公共方法 | [WaitUntilDone](45074e21-99f9-8af9-8fc4-46335fa88a89.htm) | Waits until the device is done generating or until the maximum time has expired. Call this method after calling InitiateGeneration. |
| 公共方法 | [WriteArbWaveform](88baa5e1-67a0-707e-263c-0c9837877aab.htm) | Writes data to a waveform in onboard memory. |
| 公共方法 | [WriteNamedWaveform](eac6b396-2134-5ee2-ff1f-7fd805ecd2a1.htm) | Writes floating point data to the named waveform in onboard memory. |
| 公共方法 | [WriteScript](a0a92594-e5c9-e58b-7990-11fafa172168.htm) | Writes a string containing one or more scripts that govern the generation of waveforms. |

[Top](#PageHeader)

参见

##### 引用

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


### Fgen 构造函数

|  |  |
| --- | --- |
|  | Fgen 构造函数 |

初始化 [Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm) 类的一个新实例

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen()
```

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


### Fgen 方法

|  |  |
| --- | --- |
|  | Fgen 方法 |

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [AbortGeneration](87d56c03-6ebf-999f-bfe8-1be88bcb7f0f.htm) | Aborts any previously initiated signal generation. |
| 公共方法 | [AdjustRelativeDelay](6a2ac2e7-4782-862d-f5a4-59d01e5508c4.htm) | Delays (or phase shifts) the sample clock, which delays the output of the module. |
| 公共方法 | [AllocateArbWaveform](02c34733-ca62-566b-a2a3-cae7a19085e0.htm) | Specifies the size of a waveform and allocates it in onboard memory before loading the associated data. Data can be loaded in smaller blocks with the Write methods. |
| 公共方法 | [AllocateNamedWaveform](5ff4e50b-1da7-5ecb-1183-3150a784b340.htm) | Sets the initial size of a named waveform so that it can be allocated in onboard memory before loading the associated data. After you allocate, call WriteNamedWaveform to load data in smaller blocks. |
| 公共方法 | [ClearArbMemory](c1991769-27d9-4435-1235-a4052cd199da.htm) | Removes all previously created arbitrary waveforms, sequences, and scripts from the signal generator memory, and invalidates all waveform handles, sequence handles, and waveform names. |
| 公共方法 | [ClearArbSequence](18df42dd-ed38-f5a2-06ca-39c92973c50f.htm) | Removes a previously created arbitrary sequence from the function generator's memory and invalidates the sequence’s handle. |
| 公共方法 | [ClearArbWaveform](596064f2-abe2-a808-7781-bbf6ddab3334.htm) | Removes a previously created arbitrary waveform from the signal generator memory and invalidates the waveform handle. |
| 公共方法 | [ClearFrequencyList](d5b65c20-48d9-63cd-b8a6-43e15668ffe0.htm) | Removes a previously created frequency list from the signal generator memory and invalidates the frequency list handle. |
| 公共方法 | [ClearUserStandardWaveform](17dd1104-4532-855c-9fee-012b55c5d044.htm) | Clears the user-defined waveform created using DefineUserStandardWaveform. |
| 公共方法 | [Commit](3e8ab0f4-ecca-36e7-223a-0adce1f3a480.htm) | Causes a transition to the committed state. |
| 公共方法 | [ConfigureArbSequence](2f7a88cc-27b3-ecfa-250c-ba874ad62a8c.htm) | Configures the signal generator properties that affect arbitrary sequence generation. |
| 公共方法 | [ConfigureArbWaveform](b9b0996d-5ba2-7d1f-08ee-00b1e02dd6f8.htm) | Configures the properties of the signal generator that affect arbitrary waveform generation, selects the arbitrary waveform to produce, and sets the gain and offset. |
| 公共方法 | [ConfigureDigitalEdgeTrigger](45f6012e-f319-90bc-143e-005235175440.htm) | Configures the trigger for digital edge triggering. |
| 公共方法 | [ConfigureDigitalLevelScriptTrigger](c0079aaf-0023-b47c-c360-9715294f1637.htm) | Configures the script trigger for digital level triggering. |
| 公共方法 | [ConfigureFrequencyList](6c25fd1f-5dbc-c200-d39c-d7d39cefb935.htm) | Configures the amplitude, DC offset, and start phase for the specified frequency list. |
| 公共方法 | [ConfigureReferenceClock](d2687c41-82ba-0555-8510-b075f0e72a3a.htm) | Configures the signal generator reference clock source and frequency. The signal generator uses the reference clock to tune the sample clock timebase of the signal generator so that the frequency, stability, and accuracy of the sample clock timebase matches that of the reference clock. |
| 公共方法 | [ConfigureSampleClock](8911b6e1-7048-a986-b346-4b83ec151517.htm) | Configure sample clock, the smaplesPerChannel is not necessary. |
| 公共方法 | [ConfigureSoftwareEdgeTrigger](f25c964f-2884-8772-a862-b81c766e354b.htm) | Configures the trigger for software edge triggering. |
| 公共方法 | [ConfigureStandardWavaform](bdac2a81-83e5-88ec-046d-b1ff7241dd2f.htm) | Configures the properties of the signal generator that affect standard waveform generation. |
| 公共方法 | [CreateArbSequence(Int64, Int64)](ae6c7974-ddf8-94de-b56c-72552935934a.htm) | Creates an arbitrary waveform sequence from an array of waveform handles and a corresponding array of loop counts. |
| 公共方法 | [CreateArbSequence(Int64, Int64, Int64, Int64)](4139cbb2-a4c4-93be-9363-f56048813e46.htm) | Creates an arbitrary sequence from an array of waveform handles and an array of corresponding loop counts and returns a handle that identifies the sequence. |
| 公共方法 | [CreateChannelArbWaveform](31cc1bbb-af97-3be3-557e-0fe3abc38307.htm) | Creates an onboard waveform from the waveform parameter for use in Arbitrary or Sequence. |
| 公共方法 | [CreateChannelArbWaveformFromFile](7f4941c6-6e60-f7ce-e66b-97014f0ac5d3.htm) | Creates an onboard waveform from the file read from the filePath parameter for use in Arbitrary or Sequence. |
| 公共方法 | [CreateFrequencyList](35fb08ee-ee87-fc62-ebe8-721b033f0490.htm) | Creates a frequency list from an array of frequencies and an array of durations for the specified waveform. |
| 公共方法 | [DefineUsetStandardWaveform](9ef3fcd9-5b60-0f40-d384-62b8dff89bb7.htm) | Defines a user waveform for either Function or FrequencyList. The waveform data must be scaled between -1.0 and 1.0. |
| 公共方法 | [DeleteNamedWaveform](fbcaa820-6d1c-d146-2678-53b3ff849c3a.htm) | Deletes the specified named waveform from onboard memory. The waveform specified by waveformName must be allocated using Allocate on the channel specified by channelName. |
| 公共方法 | [DeleteScript](0a1d9e50-803a-694f-25ca-83c521e18c8a.htm) | Deletes the specified script from onboard memory. |
| 公共方法 | [DisableTrigger](5e4a43bf-0edf-a52c-e849-9a18a7196920.htm) | Disables the specified trigger. |
| 公共方法 | [EnableAnalogFilter](4ac7a925-e375-dcaf-b011-59b612bee91a.htm) | Enables the analog filter for the device. |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 公共方法 | [ExportSignal](f46b39c7-589a-10d9-6690-a1dab7184b93.htm) | Routes signals (clocks, triggers, and events) to the output terminal you specify. |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | [GetAmplitude](3478f1a7-8c5b-ba60-01b8-173988b1ecab.htm) | Gets the amplitude of the standard waveform the function generator produces. When the Waveform attribute is set to Waveform DC, this attribute does not affect signal output.The units are volts. |
| 公共方法 | [GetAnalogFilterEnabled](6283eabe-b35a-90e3-3b26-5c775d993682.htm) | Gets a value indicating whether the signal generator applies an analog filter to the output signal. |
| 公共方法 | [GetAnalogPath](31f0a1b0-9f6d-32a1-0394-d3c6402755e8.htm) | Gets the analog signal path. The default valut is "Main". |
| 公共方法 | [GetArbGain](e79d716c-055f-6c7b-5168-2e93f9706cc7.htm) | Gets the factor by which the signal generator scales the arbitrary waveform data. |
| 公共方法 | [GetArbOffset](c7c5c6b6-c462-7cda-7f88-15e9b67bc0a5.htm) | Gets the value the signal generator adds to the arbitrary waveform data. |
| 公共方法 | [GetArbSampleRate](7e57b824-2bde-a279-5968-68731b981665.htm) | Gets the rate, in samples per second, at which the signal generator generates the points in arbitrary waveforms. |
| 公共方法 | [GetArbSequenceHandle](6383189b-e0c0-cc6c-c10a-ce734f8a354b.htm) | Get the handle which arbitrary sequence the function generator produces. |
| 公共方法 | [GetArbSequenceMaxLength](dfb49dd6-5ee1-9b01-eee0-e9a806b61525.htm) | Returns the maximum number of arbitrary waveforms that the function generator allows in an arbitrary sequence. |
| 公共方法 | [GetArbSequenceMaxLoopCount](478ed2ec-5b1b-b2d9-a0d9-ed0a18c433bb.htm) | Returns the maximum number of times that the function generator can repeat a waveform in a sequence. |
| 公共方法 | [GetArbSequenceMinLength](c9b710e7-4341-3e82-c7d8-01b32577c8b1.htm) | Returns the minimum number of arbitrary waveforms that the function generator allows in an arbitrary sequence. |
| 公共方法 | [GetArbSequencesMaxNumber](6c7a34fe-3dfd-b8f7-ecc2-29ede90104f6.htm) | Returns the maximum number of arbitrary sequences that the function generator allows. |
| 公共方法 | [GetArbWaveformHandle](dcc6b38c-3639-1603-3d03-8279376dcc6a.htm) | Returns the handle representing which arbitrary waveform the signal generator produces. |
| 公共方法 | [GetArbWaveformMarkerPosition](e75014de-2ea8-7592-2ba5-bc791a834ff2.htm) | Gets the position for a marker to be asserted in the arbitrary waveform. |
| 公共方法 | [GetArbWaveformMaxSize](23aa022b-5158-647c-af9e-9e9298563a84.htm) | Gets the maximum number of points the signal generator allows in an arbitrary waveform. On some signal generators, this value may vary with remaining onboard memory. |
| 公共方法 | [GetArbWaveformMinSize](1ad8051c-8ca9-7b60-4aa0-57a4d44ea4fa.htm) | Gets the minimum number of points the signal generator allows in an arbitrary waveform. |
| 公共方法 | [GetArbWaveformQuantum](a62ed50b-bf05-8ff7-c085-8eac47f7bc4f.htm) | Gets the quantum value the signal generator allows. The size of each arbitrary waveform must be a multiple of this quantum value. |
| 公共方法 | [GetArbWaveformRepeatCount](39cd7cb3-1233-fadc-4d7d-9bc3e7b43721.htm) | Gets the number of times to repeat the arbitrary waveform when the trigger mode has been set to to Single or Stepped. |
| 公共方法 | [GetArbWaveformsMaxNumber](8ce3e014-b52b-f5b8-c786-1a7ef028dbf3.htm) | Gets the maximum number of arbitrary waveforms that the signal generator allows. On some signal generators, this value may vary with remaining onboard memory. |
| 公共方法 | [GetAttributeBool](6c0cf119-d4fb-21cd-d1c8-10480c60fc65.htm) | Get specific value by attribute identifier. |
| 公共方法 | [GetAttributeDouble](23adde04-28b0-df83-d628-7a9e632dcde9.htm) | Get specific value by attribute identifier. |
| 公共方法 | [GetAttributeInt](c80fd3a9-da04-6c50-0b82-d86e8ca4cab7.htm) | Get specific value by attribute identifier. |
| 公共方法 | [GetAttributeLong](8b4bdd86-a3e3-9201-2c45-d89af2555901.htm) | Get specific value by attribute identifier. |
| 公共方法 | [GetAttributeString](a34240e2-9da4-d5bb-7066-92fa98f636dd.htm) | Get specific value by attribute identifier. |
| 公共方法 | [GetChannelDelay](c920965d-91c4-14a2-fd6a-46fcae99e8b1.htm) | Gets the delay to apply to the analog output of the channel specified by the channel string. |
| 公共方法 | [GetCommonModeOffset](eb8c146e-b967-6a2b-424c-572ce3603224.htm) | Gets the value that the signal generator adds to or subtracts from the arbitrary waveform data. |
| 公共方法 | [GetDCOffset](55301f64-f8d6-7c7d-0225-65721959cbf9.htm) | Gets the DC offset of the standard waveform the function generator produces. If the Waveform attribute is set to Waveform DC, this attribute specifies the DC level the function generator produces.The units are volts. |
| 公共方法 | [GetDigitalFilterEnabled](16e703fd-9055-79d2-d2cf-fbfa73b1b318.htm) | Gets a value indicating whether the signal generator applies a digital filter to the output signal. |
| 公共方法 | [GetDigitalFilterInterpolationFactor](da66fb90-9526-99a0-8dd3-e21144d04b75.htm) | Gets the interpolation factor when the digital filter is enabled. |
| 公共方法 | [GetDigitalGain](997c4523-b7ab-b81d-983d-068ec40b1114.htm) | Gets a factor by which the signal generator digitally multiplies generated data before converting it to an analog signal in the digital-to-analog converter. |
| 公共方法 | [GetDigitalPatternEnabled](be8b9bbf-6802-6cac-e1c6-b5a53daf928a.htm) | Fetches a value indicating whether the signal generator generates a digital pattern corresponding to the output signal. |
| 公共方法 | [GetDutyCycleHigh](d361851b-692f-4197-940b-ef9c45f6fba5.htm) | Gets the duty cycle of the square wave in units of percentage of time the waveform is high. |
| 公共方法 | [GetExternalMultiplier](0b255cad-82ec-9a65-e500-3de320d188dc.htm) | Gets a multiplication factor to use to obtain a desired sample rate from an external Sample Clock. The resulting sample rate is equal to this factor multiplied by the external Sample Clock rate. You can use this property to generate samples at a rate higher than your external clock rate. When using this property, you do not need to explicitly set the external clock rate. |
| 公共方法 | [GetFlatnessCorrectionEnabled](5f5e3deb-da74-2b13-67aa-b5ba26ea9f07.htm) | Gets a value indicating whether flatness correction is enabled. |
| 公共方法 | [GetFrequency](f2b5ee26-f4ca-daa0-9b31-fd7e814bc967.htm) | Gets the frequency of the standard waveform the function generator produces. When the Waveform attribute is set to Waveform DC, this attribute does not affect signal output.The units are Hertz. |
| 公共方法 | [GetFrequencyListDurationQuantum](cd3342fa-3a63-a5ec-aa25-971166a80508.htm) | Gets the quantum of which all durations must be a multiple in a frequency list. |
| 公共方法 | [GetFrequencyListHandle](954d6aa7-d36e-a61f-ddaf-2257922feeff.htm) | Gets which frequency list the signal generator produces. |
| 公共方法 | [GetFrequencyListMaxDuratinon](2cabec75-27ae-92d5-f5b2-159ec40e186b.htm) | Gets the maximum duration of any one step in the frequency list. |
| 公共方法 | [GetFrequencyListMaxLength](402eb4f4-da7a-3b81-0cb8-b26a805af775.htm) | Gets the maximum number of steps that can be in a frequency list. |
| 公共方法 | [GetFrequencyListMaxNumber](687f28ea-5411-8468-7763-ca43313f4814.htm) | Gets the maximum number of frequency lists the signal generator allows. |
| 公共方法 | [GetFrequencyListMinDuration](764a956d-3c1b-4b00-8771-1922304cb012.htm) | Gets the minimum duration of any one step in a frequency list. |
| 公共方法 | [GetFrequencyListMinLength](c3f54159-a6da-51dc-fd38-ba1996348aee.htm) | Gets the minimum number of frequency lists for the specified channel. |
| 公共方法 | [GetHardwareState](9caa3ec8-672b-cdde-977d-16daa9e51893.htm) | Gets a value indicating the hardware state of the signal generator currently in use. |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | [GetIdleValue](b5ac08e2-9509-1205-53c6-d8664a1724a2.htm) | Fetches the value to generate in the Idle state. You must set IdleBehavior to JumpToValue to use this property. |
| 公共方法 | [GetLoadImpedance](6ecb89f3-259d-d4e6-02c5-85c405a751cf.htm) | Gets the load impedance connected to the analog output of the channel. |
| 公共方法 | [GetOutputEnabled](54d0252d-3e0e-a625-72c2-8578787bfa89.htm) | Gets a value indicating whether the output is enabled for a specified channel. |
| 公共方法 | [GetOutputIdleBehavior](7a56b64d-572b-b439-eef6-2b88977839bb.htm) | Gets the behavior of the output signal during the Idle state. |
| 公共方法 | [GetOutputImpedance](bf7232f2-832f-1532-6add-7df52ef0c5eb.htm) | Gets the output impedance of the signal generator at the specified channel. |
| 公共方法 | [GetOutputMode](1769e4c5-8349-d64d-0cff-d252cb6f1cf2.htm) | Gets the output mode of the signal generator. |
| 公共方法 | [GetOutputWaitBehavior](8cdc63dd-243d-2aba-251d-ff09d1db109c.htm) | Gets the behavior of the output while the device is waiting for a Script trigger or executing a wait instruction. |
| 公共方法 | [GetReferenceClockFrequency](77f472d8-ced2-ce38-c020-77e70addc4eb.htm) | Gets the reference clock frequency in hertz (Hz). The signal generator uses the reference clock to derive frequencies and sample rates when generating output. |
| 公共方法 | [GetReferenceClockSource](b04f2e5b-5e47-66bf-981c-a71f55e10980.htm) | Gets the reference clock source used by the signal generator. The function generator derives frequencies and sample rates that it uses to generate waveforms from the reference clock. |
| 公共方法 | [GetSampleClockAbsoluteDelay](b5ac0cd3-5d9d-c196-0c78-51df642e2ab1.htm) | Gets the delay in seconds to apply to an external Sample Clock. This property is useful when trying to align the output of two devices. |
| 公共方法 | [GetSampleClockExportedDivisor](ef5a2f3d-ba2f-0c09-ff6a-5f9b6f032a81.htm) | Gets the factor by which to divide the sample clock, also known as an update clock, before it is exported. To export the sample clock, use ExportSignal or SetSampleClockOutputTerminal. |
| 公共方法 | [GetSampleClockMode](f4b69fc9-84c6-aeb8-e16a-662481b6dab3.htm) | Gets the sample clock mode for the signal generator. |
| 公共方法 | [GetSampleClockRate](49c74502-ab66-3a65-8232-eaf582417304.htm) | Gets the rate, in samples per second, at which the signal generator generates the points |
| 公共方法 | [GetSampleClockSource](d53a793d-485f-9311-14c9-6b806c4a6471.htm) | Gets the sample clock source. |
| 公共方法 | [GetSampleClockTimebaseExportedDivisor](003d3872-de2c-dfa2-e834-5f1a57eb30cb.htm) | Gets the factor by which to divide the device clock (sample clock timebase) before it is exported. To export the sample clock timebase, use ExportSignal or SetSampleClockTimebaseOutputTerminal. |
| 公共方法 | [GetSampleClockTimebaseRate](5761983a-9fbc-aecd-ddf2-9a56480c9baf.htm) | Gets the sample clock timebase rate. This property applies only to an external sample clock timebase. |
| 公共方法 | [GetSampleClockTimebaseSource](507bc28b-7eef-4300-c5a0-db0b267cb418.htm) | Gets the sample clock timebase source. |
| 公共方法 | [GetScriptToGenerate](24285e5c-f375-0db0-6cd8-ce3d459b7f2a.htm) | Gets a value indicating the name of the script that the generator produces. |
| 公共方法 | [GetStartPhase](89d7b115-951a-be0b-6362-837ee80fd91f.htm) | Gets the start phase of the standard waveform the function generator produces. When the Waveform attribute is set to Waveform DC, this attribute does not affect signal output.The units are degrees. |
| 公共方法 | [GetTerminalConfiguration](a2432b6b-924d-1910-1d92-9b1c7241b4bb.htm) | Get the generator terminal configuration information. |
| 公共方法 | [GetTriggerMode](1580a2a7-b130-4182-cc5f-ab2400f07a11.htm) | Gets the trigger mode for the signal generator. |
| 公共方法 | [GetTriggerType](ca26d333-4180-56d6-7bc4-b9ba46b3d027.htm) | Gets the type of trigger for specified triggerId if triggerClass is Script. |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | [GetWaitValue](7b8ddf53-ae82-b95e-1623-2d8c9cd809a9.htm) | Gets the value to generate while waiting. You must set WaitBehavior to JumpToValue to use this method. |
| 公共方法 | [GetWaveformFuntion](468a43cf-4318-cd7b-788e-4dfefb1c19cd.htm) | Gets which standard waveform the function generator produces. |
| 公共方法 | [InitiateGeneration](7feafedf-88cd-ea00-6428-d4386baae29d.htm) | Initiates signal generation |
| 公共方法 | [IsGenerationDone](d463a855-0e53-f88b-6b6d-a8224c5e178d.htm) | Gets a value indicating whether the current generation is complete. |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [Reset](87780fdb-1801-12f8-33b1-80088e0dc79e.htm) | Reset the instrument session. |
| 公共方法 | [SendSoftwareEdgeTrigger](66fec53b-e107-40fd-61e8-18be229175b7.htm) | Sends a command to trigger. |
| 公共方法 | [SetAmplitude](7002eaf5-6d29-4446-2984-545a03634ce4.htm) | Sets the amplitude of the standard waveform the function generator produces. When the Waveform attribute is set to Waveform DC, this attribute does not affect signal output.The units are volts. |
| 公共方法 | [SetAnalogFilterEnabled](2269dd12-1bee-a6de-08bf-1a55dff40e18.htm) | Sets a value indicating whether the signal generator applies an analog filter to the output signal. |
| 公共方法 | [SetAnalogPath](769be0f3-9775-602b-2286-ef1fbf669192.htm) | Sets the analog signal path. The default valut is "Main". The Main path allows the user to configure gain, offset, analog filter status, output impedance, and output enable. The Direct path presents a much smaller gain range, and you cannot adjust offset or the filter status. The Direct path provides a smaller output range but lower distortion. The Main path has two amplifier options, high and low gain. Setting this value to Main allows NI-FGEN to choose the amplifier based on the user-specified gain. |
| 公共方法 | [SetArbGain](c036e714-31dd-c770-6c95-9ec2ce030f35.htm) | Sets the factor by which the signal generator scales the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use the gain to scale the arbitrary waveform to other ranges. |
| 公共方法 | [SetArbOffset](06e48fdd-a981-4f52-82bc-05a35d8686b8.htm) | Sets the value the signal generator adds to the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use the offset to shift the arbitrary waveform range. |
| 公共方法 | [SetArbSampleRate](5b680018-dd06-7084-d6ee-af4193ed636b.htm) | Sets the rate, in samples per second, at which the signal generator generates the points in arbitrary waveforms. Use this property when OutputMode is set to Arbitrary or Sequence. |
| 公共方法 | [SetArbSequenceHandle](eabe0b3e-52c5-4898-7e76-9097ee34b11b.htm) | Identifies which arbitrary sequence the function generator produces. |
| 公共方法 | [SetArbWaveformHandle](b691a70e-662c-e088-9712-309e8c3101c6.htm) | Identifies which arbitrary waveform the function generator produces. |
| 公共方法 | [SetArbWaveformMarkerPosition](4254c589-f348-a0f6-7ce8-4510a83046df.htm) | Sets the position for a marker to be asserted in the arbitrary waveform. Use this property when OutputMode is set to Arbitrary. Use ExportSignal method to export the marker signal. |
| 公共方法 | [SetArbWaveformRepeatCount](ef05a9b7-ea31-42b6-fd49-49f9acb01f31.htm) | Sets the number of times to repeat the arbitrary waveform when the trigger mode has been set to to Single or Stepped. |
| 公共方法 | [SetAttributeBool](471d16eb-9db6-d4ca-1ff0-56aa5df91ee7.htm) | Set specific value by attribute identifier. |
| 公共方法 | [SetAttributeDouble](83946754-0122-9c05-5ffa-2859df8d2be6.htm) | Set specific value by attribute identifier. |
| 公共方法 | [SetAttributeInt](39977dfc-3038-c4aa-7fff-528013cd0f8f.htm) | Set specific value by attribute identifier. |
| 公共方法 | [SetAttributeLong](7ab6f58c-c033-71c6-eec6-5596a672430d.htm) | Set specific value by attribute identifier. |
| 公共方法 | [SetAttributeString](9ffae37c-cb14-cba8-1c1b-06b66722030e.htm) | Set specific value by attribute identifier. |
| 公共方法 | [SetChannelDelay](64b57dc1-2b8c-fd98-e3f3-48f5b050d98b.htm) | Sets the delay to apply to the analog output of the channel specified by the channel string. You can use the output delay to configure the timing relationship between channels on a multichannel device. Values for this property can be zero or positive. A value of zero indicates that the channels are aligned. A positive value delays the analog output by the specified number of seconds. |
| 公共方法 | [SetCommonModeOffset](75e76472-72b4-306b-3380-26c7a68bad01.htm) | Sets the value that the signal generator adds to or subtracts from the arbitrary waveform data. Common-mode offset is applicable only when you set the terminal configuration to Differential. Common-mode offset is applied to the signals generated at each differential output terminal. |
| 公共方法 | [SetDCOffset](a142c4c8-67ff-ae46-6357-d63c7fab1ef1.htm) | Sets the DC offset of the standard waveform the function generator produces. If the Waveform attribute is set to Waveform DC, this attribute specifies the DC level the function generator produces.The units are volts. |
| 公共方法 | [SetDigitalFilterEnabled](38e58151-33f0-5c69-a2e0-ea7ec4c49d7b.htm) | Sets a value indicating whether the signal generator applies a digital filter to the output signal. |
| 公共方法 | [SetDigitalFilterInterpolationFactor](cd7069d3-c81a-4ec0-b356-082413803643.htm) | Sets the interpolation factor when the digital filter is enabled. |
| 公共方法 | [SetDigitalGain](7fe72645-c821-3b9f-1f51-b1cd8295e9bb.htm) | Sets a factor by which the signal generator digitally multiplies generated data before converting it to an analog signal in the digital-to-analog converter. |
| 公共方法 | [SetDigitalPatternEnabled](f0351229-eca0-7476-e1f9-2aca8dfc0c03.htm) | Sets a value indicating whether the signal generator generates a digital pattern corresponding to the output signal. |
| 公共方法 | [SetDutyCycleHigh](94dbe092-c05a-4bb5-8df4-f27c8a069a5f.htm) | Sets the duty cycle of the square wave in units of percentage of time the waveform is high. |
| 公共方法 | [SetExternalMultiplier](e2fb0f48-a929-a56c-dfc5-b96f9d01f9eb.htm) | Sets a multiplication factor to use to obtain a desired sample rate from an external Sample Clock. The resulting sample rate is equal to this factor multiplied by the external Sample Clock rate. You can use this property to generate samples at a rate higher than your external clock rate. When using this property, you do not need to explicitly set the external clock rate. |
| 公共方法 | [SetFlatnessCorrectionEnabled](0f5149f5-58f6-07eb-6b5d-8635e1c397df.htm) | Sets a value indicating whether flatness correction is enabled. |
| 公共方法 | [SetFrequency](01bf70ae-186d-82aa-ba75-23ae9e490733.htm) | Sets the frequency of the standard waveform the function generator produces. When the Waveform attribute is set to Waveform DC, this attribute does not affect signal output.The units are Hertz. |
| 公共方法 | [SetFrequencyListHandle](39341270-8ca1-530a-9710-3b6925e92e8c.htm) | Sets which frequency list the signal generator produces. |
| 公共方法 | [SetIdleValue](c0a538bd-74d1-ae0f-e7b5-ab0f5a35d76c.htm) | Sets the value to generate in the Idle state. You must set IdleBehavior to JumpToValue to use this property. |
| 公共方法 | [SetLoadImpedance](f6ac1c59-0d62-6196-bd5b-90d920f9ed7a.htm) | Sets the load impedance connected to the analog output of the channel. If you set the load impedance to –1.0, NI-FGEN assumes that the load impedance matches the value of the output impedance. |
| 公共方法 | [SetNextWritePosition](d5fbeed5-7fee-d1ce-8e2a-c308e533735d.htm) | Sets the position in the named waveform to which data was written at the next write. |
| 公共方法 | [SetOutputEnabled](33475e2b-f394-3aca-20c2-95fca0fea5ec.htm) | Sets a value indicating whether the output is enabled for a specified channel. |
| 公共方法 | [SetOutputIdleBehavior](51f4ed3b-869e-8c7d-3232-b9080cd9d73f.htm) | Sets the behavior of the output signal during the Idle state. |
| 公共方法 | [SetOutputImpedance](7744893c-4ad4-b558-0c28-ad15b511a249.htm) | Sets the output impedance of the signal generator at the specified channel. This method specifies the output impedance of the signal generator at the output connector. NI signal generators have an output impedance of 50 Ω and an optional 75 Ω on select modules. |
| 公共方法 | [SetOutputMode](fb988af4-5a33-7c59-67c4-6f69cf648bec.htm) | Sets the output mode of the signal generator. |
| 公共方法 | [SetOutputWaitBehavior](c8ccda18-3711-9b54-c1e9-34af2ec423db.htm) | Sets the behavior of the output while the device is waiting for a Script trigger or executing a wait instruction. |
| 公共方法 | [SetReferenceClockFrequency](235c465d-370f-8aae-45fa-49490abc932e.htm) | Sets the reference clock frequency in hertz (Hz). The signal generator uses the reference clock to derive frequencies and sample rates when generating output. |
| 公共方法 | [SetReferenceClockSource](63579d9a-901c-4d3a-4bbd-af404453b9ea.htm) | Sets the reference clock source used by the signal generator. The function generator derives frequencies and sample rates that it uses to generate waveforms from the reference clock. |
| 公共方法 | [SetSampleClockAbsoluteDelay](8d3d70f2-13e9-3787-47f3-dcddb13f8f93.htm) | Sets the delay in seconds to apply to an external Sample Clock. This property is useful when trying to align the output of two devices. |
| 公共方法 | [SetSampleClockExportedDivisor](56f99cbd-8ffb-0e91-9661-ae6c5f718c1f.htm) | Sets the factor by which to divide the sample clock, also known as an update clock, before it is exported. To export the sample clock, use ExportSignal or SetSampleClockOutputTerminal. |
| 公共方法 | [SetSampleClockMode](12759ffd-2a16-57da-ef20-129e33d04ca6.htm) | Sets the sample clock mode for the signal generator. When in DivideDown sampling mode, the sample rate can only be set to certain frequencies, based on dividing down the sample clock. However, in HighResolution mode, the sample rate may be set to any value. |
| 公共方法 | [SetSampleClockRate](8a4463d7-8338-8d00-25cc-cd3f9b7dc61e.htm) | Sets the rate, in samples per second, at which the signal generator generates the points |
| 公共方法 | [SetSampleClockSource](787342e5-b467-323a-8b4b-3af6993c988b.htm) | Sets the sample clock source. |
| 公共方法 | [SetSampleClockTimebaseExportedDivisor](d1cfe2ab-aec9-f7ab-a619-83bce55b8221.htm) | Sets the factor by which to divide the device clock (sample clock timebase) before it is exported. To export the sample clock timebase, use ExportSignal or SetSampleClockTimebaseOutputTerminal. |
| 公共方法 | [SetSampleClockTimebaseRate](34317a4d-3b36-e9c8-6e0b-7486256fa4af.htm) | Sets the sample clock timebase rate. This property applies only to an external sample clock timebase. |
| 公共方法 | [SetSampleClockTimebaseSource](790e4c54-8cc2-05e8-8034-926d0f785750.htm) | Sets the sample clock timebase source. |
| 公共方法 | [SetScriptToGenerate](b4524756-2280-07e1-4fe7-8ba2e6c9262b.htm) | Sets a value indicating the name of the script that the generator produces. OutputMode should be set to Script to call this property. |
| 公共方法 | [SetStartPhase](1c35ca1f-4d23-80d5-47e3-e59d39b2e6a4.htm) | Sets the start phase of the standard waveform the function generator produces. When the Waveform attribute is set to Waveform DC, this attribute does not affect signal output.The units are degrees. |
| 公共方法 | [SetTerminalConfiguration](786aef5f-1090-73f9-cb58-7c7ffff40885.htm) | Determines whether the generator will run in single-ended or differential mode, and whether the output gain and offset values will be analyzed based on single-ended or differential operation. |
| 公共方法 | [SetTriggerMode](af877a4b-67e6-7b15-2373-2c9bbb2db8af.htm) | Sets the trigger mode for the signal generator. |
| 公共方法 | [SetTriggerType](333733bc-9403-9455-ff2b-3c72e8d63b93.htm) | Sets the type of trigger for specified triggerId if triggerClass is Script. |
| 公共方法 | [SetWaitValue](62787996-81fc-e867-239d-a0b70c6b4932.htm) | Sets the value to generate while waiting. You must set WaitBehavior to JumpToValue to use this method. |
| 公共方法 | [SetWaveformFunction](6e6e5d38-c625-40b5-5e73-daab17e39050.htm) | Sets which standard waveform the function generator produces. |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |
| 公共方法 | [WaitUntilDone](45074e21-99f9-8af9-8fc4-46335fa88a89.htm) | Waits until the device is done generating or until the maximum time has expired. Call this method after calling InitiateGeneration. |
| 公共方法 | [WriteArbWaveform](88baa5e1-67a0-707e-263c-0c9837877aab.htm) | Writes data to a waveform in onboard memory. |
| 公共方法 | [WriteNamedWaveform](eac6b396-2134-5ee2-ff1f-7fd805ecd2a1.htm) | Writes floating point data to the named waveform in onboard memory. |
| 公共方法 | [WriteScript](a0a92594-e5c9-e58b-7990-11fafa172168.htm) | Writes a string containing one or more scripts that govern the generation of waveforms. |

[Top](#PageHeader)

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### AbortGeneration 方法

|  |  |
| --- | --- |
|  | FgenAbortGeneration 方法 |

Aborts any previously initiated signal generation.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen AbortGeneration()
```

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### AdjustRelativeDelay 方法

|  |  |
| --- | --- |
|  | FgenAdjustRelativeDelay 方法 |

Delays (or phase shifts) the sample clock, which delays the output of the module.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen AdjustRelativeDelay(
	double time
)
```

###### 参数

time  Double
:   The amount of time by which to adjust the sample clock delay, in seconds.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### AllocateArbWaveform 方法

|  |  |
| --- | --- |
|  | FgenAllocateArbWaveform 方法 |

Specifies the size of a waveform and allocates it in onboard memory before loading the associated data. Data can be loaded in smaller blocks with the Write methods.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> AllocateArbWaveform(
	long numberOfSamples
)
```

###### 参数

numberOfSamples  Int64
:   The size of the waveform in samples. This value must be an integer multiple of the waveform quantum.

###### 返回值

DictionaryString, Int64  
A dictionary collection of the handle that identifies the waveform. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### AllocateNamedWaveform 方法

|  |  |
| --- | --- |
|  | FgenAllocateNamedWaveform 方法 |

Sets the initial size of a named waveform so that it can be allocated in onboard memory before loading the associated data.
After you allocate, call WriteNamedWaveform to load data in smaller blocks.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen AllocateNamedWaveform(
	string waveformName,
	long numberOfSamples
)
```

###### 参数

waveformName  String
:   The name of waveform.

numberOfSamples  Int64
:   The size of waveform in samples.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ClearArbMemory 方法

|  |  |
| --- | --- |
|  | FgenClearArbMemory 方法 |

Removes all previously created arbitrary waveforms, sequences, and scripts from the signal generator memory, and invalidates all waveform handles, sequence handles, and waveform names.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen ClearArbMemory()
```

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ClearArbSequence 方法

|  |  |
| --- | --- |
|  | FgenClearArbSequence 方法 |

Removes a previously created arbitrary sequence from the function generator's memory and invalidates the sequence’s handle.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen ClearArbSequence(
	long handle
)
```

###### 参数

handle  Int64
:   The handle of the arbitrary sequence to clear.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ClearArbWaveform 方法

|  |  |
| --- | --- |
|  | FgenClearArbWaveform 方法 |

Removes a previously created arbitrary waveform from the signal generator memory and invalidates the waveform handle.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen ClearArbWaveform(
	long handle
)
```

###### 参数

handle  Int64
:   The handle of the arbitrary waveform to clean. Specify a value of -1 to clear all waveforms.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ClearFrequencyList 方法

|  |  |
| --- | --- |
|  | FgenClearFrequencyList 方法 |

Removes a previously created frequency list from the signal generator memory and invalidates the frequency list handle.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen ClearFrequencyList(
	long handle
)
```

###### 参数

handle  Int64
:   The handle of the frequency list you want the signal generator to remove. Specify a value of -1 to clear all frequency lists.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ClearUserStandardWaveform 方法

|  |  |
| --- | --- |
|  | FgenClearUserStandardWaveform 方法 |

Clears the user-defined waveform created using DefineUserStandardWaveform.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen ClearUserStandardWaveform()
```

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### Commit 方法

|  |  |
| --- | --- |
|  | FgenCommit 方法 |

Causes a transition to the committed state.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen Commit()
```

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ConfigureArbSequence 方法

|  |  |
| --- | --- |
|  | FgenConfigureArbSequence 方法 |

Configures the signal generator properties that affect arbitrary sequence generation.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen ConfigureArbSequence(
	long handle,
	double gain,
	double offset
)
```

###### 参数

handle  Int64
:   The handle of the arbitrary sequence to configure.

gain  Double
:   The factor by which the signal generator scales the arbitrary waveforms in the sequence.

offset  Double
:   The value the signal generator adds to the arbitrary waveform data.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ConfigureArbWaveform 方法

|  |  |
| --- | --- |
|  | FgenConfigureArbWaveform 方法 |

Configures the properties of the signal generator that affect arbitrary waveform generation, selects the arbitrary waveform to produce, and sets the gain and offset.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen ConfigureArbWaveform(
	long handle,
	double gain,
	double offset
)
```

###### 参数

handle  Int64
:   The handle of the arbitrary waveform to produce.

gain  Double
:   The factor by which the signal generator scales the arbitrary waveform.

offset  Double
:   The value the signal generator adds to the arbitrary waveform.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ConfigureDigitalEdgeTrigger 方法

|  |  |
| --- | --- |
|  | FgenConfigureDigitalEdgeTrigger 方法 |

Configures the trigger for digital edge triggering.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen ConfigureDigitalEdgeTrigger(
	string triggerClass,
	string triggerId,
	string source,
	string edge
)
```

###### 参数

triggerClass  String
:   "Start", "Script"

triggerId  String
:   The trigger used for triggering. If triggerClass is "Start", input "".

source  String
:   The trigger source for the digital edge script trigger that the signal generator uses.

edge  String
:   "Falling", "Rising".

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ConfigureDigitalLevelScriptTrigger 方法

|  |  |
| --- | --- |
|  | FgenConfigureDigitalLevelScriptTrigger 方法 |

Configures the script trigger for digital level triggering.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen ConfigureDigitalLevelScriptTrigger(
	string triggerId,
	string source,
	string activeLevel
)
```

###### 参数

triggerId  String
:   The trigger used for triggering.

source  String
:   The trigger source for the digital level script trigger.

activeLevel  String
:   "High", "Low".

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ConfigureFrequencyList 方法

|  |  |
| --- | --- |
|  | FgenConfigureFrequencyList 方法 |

Configures the amplitude, DC offset, and start phase for the specified frequency list.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen ConfigureFrequencyList(
	long handle,
	double amplitude,
	double dcOffset,
	double startPhase
)
```

###### 参数

handle  Int64
:   The handle of the frequency list that you want the signal generator to produce.

amplitude  Double
:   The amplitude of the standard waveform that you want the signal generator to produce.

dcOffset  Double
:   The DC offset of the standard waveform that you want the signal generator to produce.

startPhase  Double
:   The horizontal offset of the standard waveform you want the signal generator to produce.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ConfigureReferenceClock 方法

|  |  |
| --- | --- |
|  | FgenConfigureReferenceClock 方法 |

Configures the signal generator reference clock source and frequency.
The signal generator uses the reference clock to tune the sample clock timebase of the signal generator so that the frequency, stability, and accuracy of the sample clock timebase matches that of the reference clock.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen ConfigureReferenceClock(
	string source,
	double frequency
)
```

###### 参数

source  String
:   The reference clock source that you want the signal generator to use.

frequency  Double
:   The reference clock frequency in hertz (Hz).

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ConfigureSampleClock 方法

|  |  |
| --- | --- |
|  | FgenConfigureSampleClock 方法 |

Configure sample clock, the smaplesPerChannel is not necessary.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen ConfigureSampleClock(
	string source,
	double rate,
	long samplesPerChannel = 0
)
```

###### 参数

source  String
:   The sample clock source. The default value is "OnboardClock".

rate  Double
:   The rate, in samples per second, at which the signal generator generates the points.

samplesPerChannel  Int64  (Optional)
:   The number of samples to acquire or generate.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ConfigureSoftwareEdgeTrigger 方法

|  |  |
| --- | --- |
|  | FgenConfigureSoftwareEdgeTrigger 方法 |

Configures the trigger for software edge triggering.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen ConfigureSoftwareEdgeTrigger(
	string triggerClass,
	string triggerId
)
```

###### 参数

triggerClass  String
:   "Start", "Script"

triggerId  String
:   The trigger used for triggering. If triggerClass is "Start", input "".

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ConfigureStandardWavaform 方法

|  |  |
| --- | --- |
|  | FgenConfigureStandardWavaform 方法 |

Configures the properties of the signal generator that affect standard waveform generation.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen ConfigureStandardWavaform(
	string waveformFunction,
	double amplitude,
	double dcOffset,
	double frequency,
	double startPhase
)
```

###### 参数

waveformFunction  String
:   "DC", "Noise", "RampDown", "RampUp", "Sine", "Square", "Triangle", "Uset".
    For NI4463, support "Sine", "DCVoltage", "Square", "Triangle" and "Sawtooth".
    For T3AWG3352, support "Sine", "Ramp", "Square", "Sync", "DC", "Gaussian", "Lorentz", "Haversine", "Exp\_Rise" and "Exp\_Decay".

amplitude  Double
:   The peak-to-peak amplitude of the standard waveform that you want the signal generator to produce.

dcOffset  Double
:   The DC offset of the standard waveform that you want the signal generator to produce.

frequency  Double
:   The frequency of the standard waveform that you want the signal generator to produce.

startPhase  Double
:   The horizontal offset, in degrees of one waveform cycle, of the standard waveform that you want the signal generator to produce.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### CreateArbSequence 方法

|  |  |
| --- | --- |
|  | FgenCreateArbSequence 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [CreateArbSequence(Int64, Int64)](ae6c7974-ddf8-94de-b56c-72552935934a.htm) | Creates an arbitrary waveform sequence from an array of waveform handles and a corresponding array of loop counts. |
| 公共方法 | [CreateArbSequence(Int64, Int64, Int64, Int64)](4139cbb2-a4c4-93be-9363-f56048813e46.htm) | Creates an arbitrary sequence from an array of waveform handles and an array of corresponding loop counts and returns a handle that identifies the sequence. |

[Top](#PageHeader)

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


##### CreateArbSequence(Int64[], Int64[]) 方法

|  |  |
| --- | --- |
|  | FgenCreateArbSequence(Int64, Int64) 方法 |

Creates an arbitrary waveform sequence from an array of waveform handles and a corresponding array of loop counts.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> CreateArbSequence(
	long[] waveformHandle,
	long[] loopCount
)
```

###### 参数

waveformHandle  Int64
:   The array of waveform handles from which you want to create a new arbitrary sequence.

loopCount  Int64
:   The array of loop counts that you want to use to create a new arbitrary sequence.

###### 返回值

DictionaryString, Int64  
A dictionary collection of the handle that identifies the waveform. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[CreateArbSequence 重载](70d479f4-2698-557e-41c4-395fdb6a8422.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


##### CreateArbSequence(Int64[], Int64[], Int64[], Int64[]) 方法

|  |  |
| --- | --- |
|  | FgenCreateArbSequence(Int64, Int64, Int64, Int64) 方法 |

Creates an arbitrary sequence from an array of waveform handles and an array of corresponding loop counts and returns a handle that identifies the sequence.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> CreateArbSequence(
	long[] waveformHandle,
	long[] loopCount,
	long[] sampleCounts,
	long[] markers
)
```

###### 参数

waveformHandle  Int64
:   The array of waveform handles from which you want to create a new arbitrary sequence.

loopCount  Int64
:   The array of loop counts that you want to use to create a new arbitrary sequence.

sampleCounts  Int64
:   The array of sample counts that you want to use to create a new arbitrary waveform. These values indicate the subset, in samples, of the given waveform to generate. Each element must be larger than the minimum waveform size, a multiple of the waveform quantum, and no larger than the number of samples in the corresponding waveform.

markers  Int64
:   The array of marker locations where you want a marker to be generated in the sequence. The marker location must be less than the size of the waveform the marker is in. Use -1 to specify no marker.

###### 返回值

DictionaryString, Int64  
A dictionary collection of the handle that identifies the waveform. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[CreateArbSequence 重载](70d479f4-2698-557e-41c4-395fdb6a8422.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### CreateChannelArbWaveform 方法

|  |  |
| --- | --- |
|  | FgenCreateChannelArbWaveform 方法 |

Creates an onboard waveform from the waveform parameter for use in Arbitrary or Sequence.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> CreateChannelArbWaveform(
	double[] waveform
)
```

###### 参数

waveform  Double
:   The array of data you want to use for the new arbitrary waveform.

###### 返回值

DictionaryString, Int64  
A dictionary collection of the handle that identifies the waveform.. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### CreateChannelArbWaveformFromFile 方法

|  |  |
| --- | --- |
|  | FgenCreateChannelArbWaveformFromFile 方法 |

Creates an onboard waveform from the file read from the filePath parameter for use in Arbitrary or Sequence.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> CreateChannelArbWaveformFromFile(
	string filePath,
	string byteOrder
)
```

###### 参数

filePath  String
:   The full path and name of the file where the waveform data resides.

byteOrder  String
:   The byte order of the data in the file. "BigEndian", "LittleEndian".

###### 返回值

DictionaryString, Int64  
A dictionary collection of the handle that identifies the waveform.. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### CreateFrequencyList 方法

|  |  |
| --- | --- |
|  | FgenCreateFrequencyList 方法 |

Creates a frequency list from an array of frequencies and an array of durations for the specified waveform.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> CreateFrequencyList(
	string waveform,
	double[] frequencies,
	double[] durations
)
```

###### 参数

waveform  String
:   The StandardWaveform that you want the signal generator to produce. "DC", "Noise", "RampDown", "RampUp", "Sine", "Square", "Triangle", "User".

frequencies  Double
:   The array of frequencies to form the frequency list. Each frequencies element has a corresponding durations element that indicates how long that frequency is repeated.

durations  Double
:   The array of durations to form the frequency list.

###### 返回值

DictionaryString, Int64  
A dictionary collection of The handle that identifies the new frequency list. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### DefineUsetStandardWaveform 方法

|  |  |
| --- | --- |
|  | FgenDefineUsetStandardWaveform 方法 |

Defines a user waveform for either Function or FrequencyList.
The waveform data must be scaled between -1.0 and 1.0.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen DefineUsetStandardWaveform(
	double[] data
)
```

###### 参数

data  Double
:   The array of data you want to load into the new waveform.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### DeleteNamedWaveform 方法

|  |  |
| --- | --- |
|  | FgenDeleteNamedWaveform 方法 |

Deletes the specified named waveform from onboard memory.
The waveform specified by waveformName must be allocated using Allocate on the channel specified by channelName.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen DeleteNamedWaveform(
	string waveformName
)
```

###### 参数

waveformName  String
:   The name of waveform.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### DeleteScript 方法

|  |  |
| --- | --- |
|  | FgenDeleteScript 方法 |

Deletes the specified script from onboard memory.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen DeleteScript(
	string scriptName
)
```

###### 参数

scriptName  String
:   The name of the script you want to delete.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### DisableTrigger 方法

|  |  |
| --- | --- |
|  | FgenDisableTrigger 方法 |

Disables the specified trigger.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen DisableTrigger(
	string triggerClass,
	string triggerId
)
```

###### 参数

triggerClass  String
:   "Start", "Script"

triggerId  String
:   The trigger used for triggering. If triggerClass is "Start", input "".

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### EnableAnalogFilter 方法

|  |  |
| --- | --- |
|  | FgenEnableAnalogFilter 方法 |

Enables the analog filter for the device.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen EnableAnalogFilter(
	double filterCorrectionFrequency
)
```

###### 参数

filterCorrectionFrequency  Double
:   The filter correction frequency of the analog filter in hertz.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ExportSignal 方法

|  |  |
| --- | --- |
|  | FgenExportSignal 方法 |

Routes signals (clocks, triggers, and events) to the output terminal you specify.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen ExportSignal(
	string signalSource,
	string signalIdentifier,
	string outputTermianl
)
```

###### 参数

signalSource  String
:   The source of the signal to route. "DataMarkerEvent", "DoneEvent", "MarkerEvent", "OnboardReferenceClock", "ReadyForStartEvent", "ReferenceClock", "SampleClock", "SampleClockTimebase", "ScriptTrigger", "StartedEvent", "StartTrigger" or "SyncOut".

signalIdentifier  String
:   The instance of the selected signal to export.

outputTermianl  String
:   The output terminal to export the signal.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetAmplitude 方法

|  |  |
| --- | --- |
|  | FgenGetAmplitude 方法 |

Gets the amplitude of the standard waveform the function generator produces. When the Waveform attribute is set to Waveform DC, this attribute does not affect signal output.The units are volts.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetAmplitude()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of peak-to-peak amplitude. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetAnalogFilterEnabled 方法

|  |  |
| --- | --- |
|  | FgenGetAnalogFilterEnabled 方法 |

Gets a value indicating whether the signal generator applies an analog filter to the output signal.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> GetAnalogFilterEnabled()
```

###### 返回值

DictionaryString, Boolean  
A dictionary collection indicating whether anlog filter is applied. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetAnalogPath 方法

|  |  |
| --- | --- |
|  | FgenGetAnalogPath 方法 |

Gets the analog signal path. The default valut is "Main".

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetAnalogPath()
```

###### 返回值

DictionaryString, String  
A dictionary collection of analog signal path. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbGain 方法

|  |  |
| --- | --- |
|  | FgenGetArbGain 方法 |

Gets the factor by which the signal generator scales the arbitrary waveform data.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetArbGain()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of factor. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbOffset 方法

|  |  |
| --- | --- |
|  | FgenGetArbOffset 方法 |

Gets the value the signal generator adds to the arbitrary waveform data.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetArbOffset()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of offset. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbSampleRate 方法

|  |  |
| --- | --- |
|  | FgenGetArbSampleRate 方法 |

Gets the rate, in samples per second, at which the signal generator generates the points in arbitrary waveforms.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetArbSampleRate()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of sample rate. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbSequenceHandle 方法

|  |  |
| --- | --- |
|  | FgenGetArbSequenceHandle 方法 |

Get the handle which arbitrary sequence the function generator produces.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetArbSequenceHandle()
```

###### 返回值

DictionaryString, Int64  
A dictionary collection of the handle. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbSequenceMaxLength 方法

|  |  |
| --- | --- |
|  | FgenGetArbSequenceMaxLength 方法 |

Returns the maximum number of arbitrary waveforms that the function generator allows in an arbitrary sequence.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetArbSequenceMaxLength()
```

###### 返回值

DictionaryString, Int64  
A dictionary collection of maximum number of waveforms. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbSequenceMaxLoopCount 方法

|  |  |
| --- | --- |
|  | FgenGetArbSequenceMaxLoopCount 方法 |

Returns the maximum number of times that the function generator can repeat a waveform in a sequence.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetArbSequenceMaxLoopCount()
```

###### 返回值

DictionaryString, Int64  
A dictionary collection of maximum count. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbSequenceMinLength 方法

|  |  |
| --- | --- |
|  | FgenGetArbSequenceMinLength 方法 |

Returns the minimum number of arbitrary waveforms that the function generator allows in an arbitrary sequence.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetArbSequenceMinLength()
```

###### 返回值

DictionaryString, Int64  
A dictionary collection of minimum number of waveforms. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbSequencesMaxNumber 方法

|  |  |
| --- | --- |
|  | FgenGetArbSequencesMaxNumber 方法 |

Returns the maximum number of arbitrary sequences that the function generator allows.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetArbSequencesMaxNumber()
```

###### 返回值

DictionaryString, Int64  
A dictionary collection of the maximum number. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbWaveformHandle 方法

|  |  |
| --- | --- |
|  | FgenGetArbWaveformHandle 方法 |

Returns the handle representing which arbitrary waveform the signal generator produces.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetArbWaveformHandle()
```

###### 返回值

DictionaryString, Int64  
A dictionary collection of the handle. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbWaveformMarkerPosition 方法

|  |  |
| --- | --- |
|  | FgenGetArbWaveformMarkerPosition 方法 |

Gets the position for a marker to be asserted in the arbitrary waveform.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetArbWaveformMarkerPosition()
```

###### 返回值

DictionaryString, Int64  
A dictionary collection of marker position. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbWaveformMaxSize 方法

|  |  |
| --- | --- |
|  | FgenGetArbWaveformMaxSize 方法 |

Gets the maximum number of points the signal generator allows in an arbitrary waveform. On some signal generators, this value may vary with remaining onboard memory.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetArbWaveformMaxSize()
```

###### 返回值

DictionaryString, Int64  
A dictionary collection of maximum number of points. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbWaveformMinSize 方法

|  |  |
| --- | --- |
|  | FgenGetArbWaveformMinSize 方法 |

Gets the minimum number of points the signal generator allows in an arbitrary waveform.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetArbWaveformMinSize()
```

###### 返回值

DictionaryString, Int64  
A dictionary collection of minimum number of points. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbWaveformQuantum 方法

|  |  |
| --- | --- |
|  | FgenGetArbWaveformQuantum 方法 |

Gets the quantum value the signal generator allows. The size of each arbitrary waveform must be a multiple of this quantum value.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetArbWaveformQuantum()
```

###### 返回值

DictionaryString, Int64  
A dictionary collection of the quantum value. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbWaveformRepeatCount 方法

|  |  |
| --- | --- |
|  | FgenGetArbWaveformRepeatCount 方法 |

Gets the number of times to repeat the arbitrary waveform when the trigger mode has been set to to Single or Stepped.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetArbWaveformRepeatCount()
```

###### 返回值

DictionaryString, Int64  
A dictionary collection of repeat count. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbWaveformsMaxNumber 方法

|  |  |
| --- | --- |
|  | FgenGetArbWaveformsMaxNumber 方法 |

Gets the maximum number of arbitrary waveforms that the signal generator allows. On some signal generators, this value may vary with remaining onboard memory.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetArbWaveformsMaxNumber()
```

###### 返回值

DictionaryString, Int64  
A dictionary collection of maximum number of arbitrary waveforms. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetAttributeBool 方法

|  |  |
| --- | --- |
|  | FgenGetAttributeBool 方法 |

Get specific value by attribute identifier.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

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

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetAttributeDouble 方法

|  |  |
| --- | --- |
|  | FgenGetAttributeDouble 方法 |

Get specific value by attribute identifier.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

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

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetAttributeInt 方法

|  |  |
| --- | --- |
|  | FgenGetAttributeInt 方法 |

Get specific value by attribute identifier.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

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

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetAttributeLong 方法

|  |  |
| --- | --- |
|  | FgenGetAttributeLong 方法 |

Get specific value by attribute identifier.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

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

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetAttributeString 方法

|  |  |
| --- | --- |
|  | FgenGetAttributeString 方法 |

Get specific value by attribute identifier.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

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

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetChannelDelay 方法

|  |  |
| --- | --- |
|  | FgenGetChannelDelay 方法 |

Gets the delay to apply to the analog output of the channel specified by the channel string.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetChannelDelay()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of channelDelay. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetCommonModeOffset 方法

|  |  |
| --- | --- |
|  | FgenGetCommonModeOffset 方法 |

Gets the value that the signal generator adds to or subtracts from the arbitrary waveform data.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetCommonModeOffset()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of common mode offset. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetDCOffset 方法

|  |  |
| --- | --- |
|  | FgenGetDCOffset 方法 |

Gets the DC offset of the standard waveform the function generator produces. If the Waveform attribute is set to Waveform DC, this attribute specifies the DC level the function generator produces.The units are volts.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetDCOffset()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of DC offset. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetDigitalFilterEnabled 方法

|  |  |
| --- | --- |
|  | FgenGetDigitalFilterEnabled 方法 |

Gets a value indicating whether the signal generator applies a digital filter to the output signal.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> GetDigitalFilterEnabled()
```

###### 返回值

DictionaryString, Boolean  
A dictionary collection indicating whether digital filter is applied. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetDigitalFilterInterpolationFactor 方法

|  |  |
| --- | --- |
|  | FgenGetDigitalFilterInterpolationFactor 方法 |

Gets the interpolation factor when the digital filter is enabled.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetDigitalFilterInterpolationFactor()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of interpolation factor. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetDigitalGain 方法

|  |  |
| --- | --- |
|  | FgenGetDigitalGain 方法 |

Gets a factor by which the signal generator digitally multiplies generated data before converting it to an analog signal in the digital-to-analog converter.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetDigitalGain()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of gain. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetDigitalPatternEnabled 方法

|  |  |
| --- | --- |
|  | FgenGetDigitalPatternEnabled 方法 |

Fetches a value indicating whether the signal generator generates a digital pattern corresponding to the output signal.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> GetDigitalPatternEnabled()
```

###### 返回值

DictionaryString, Boolean  
A dictionary collection indicating whether to generate digital pattern. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetDutyCycleHigh 方法

|  |  |
| --- | --- |
|  | FgenGetDutyCycleHigh 方法 |

Gets the duty cycle of the square wave in units of percentage of time the waveform is high.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetDutyCycleHigh()
```

###### 返回值

DictionaryString, Double  
A dictionary collection. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetExternalMultiplier 方法

|  |  |
| --- | --- |
|  | FgenGetExternalMultiplier 方法 |

Gets a multiplication factor to use to obtain a desired sample rate from an external Sample Clock.
The resulting sample rate is equal to this factor multiplied by the external Sample Clock rate. You can use this property to generate samples at a rate higher than your external clock rate. When using this property, you do not need to explicitly set the external clock rate.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetExternalMultiplier()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of multiplication factor. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetFlatnessCorrectionEnabled 方法

|  |  |
| --- | --- |
|  | FgenGetFlatnessCorrectionEnabled 方法 |

Gets a value indicating whether flatness correction is enabled.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> GetFlatnessCorrectionEnabled()
```

###### 返回值

DictionaryString, Boolean  
A dictionary collection indicating whether flatness correction is enabled. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetFrequency 方法

|  |  |
| --- | --- |
|  | FgenGetFrequency 方法 |

Gets the frequency of the standard waveform the function generator produces. When the Waveform attribute is set to Waveform DC, this attribute does not affect signal output.The units are Hertz.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetFrequency()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of frequency. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetFrequencyListDurationQuantum 方法

|  |  |
| --- | --- |
|  | FgenGetFrequencyListDurationQuantum 方法 |

Gets the quantum of which all durations must be a multiple in a frequency list.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetFrequencyListDurationQuantum()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of quantum. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetFrequencyListHandle 方法

|  |  |
| --- | --- |
|  | FgenGetFrequencyListHandle 方法 |

Gets which frequency list the signal generator produces.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetFrequencyListHandle()
```

###### 返回值

DictionaryString, Int64  
A dictionary collection of the handle. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetFrequencyListMaxDuratinon 方法

|  |  |
| --- | --- |
|  | FgenGetFrequencyListMaxDuratinon 方法 |

Gets the maximum duration of any one step in the frequency list.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetFrequencyListMaxDuratinon()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of maximum duration. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetFrequencyListMaxLength 方法

|  |  |
| --- | --- |
|  | FgenGetFrequencyListMaxLength 方法 |

Gets the maximum number of steps that can be in a frequency list.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetFrequencyListMaxLength()
```

###### 返回值

DictionaryString, Int64  
A dictionary collection of maximum number of steps. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetFrequencyListMaxNumber 方法

|  |  |
| --- | --- |
|  | FgenGetFrequencyListMaxNumber 方法 |

Gets the maximum number of frequency lists the signal generator allows.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetFrequencyListMaxNumber()
```

###### 返回值

DictionaryString, Int64  
A dictionary collection of maximum number. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetFrequencyListMinDuration 方法

|  |  |
| --- | --- |
|  | FgenGetFrequencyListMinDuration 方法 |

Gets the minimum duration of any one step in a frequency list.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetFrequencyListMinDuration()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of minimum duration. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetFrequencyListMinLength 方法

|  |  |
| --- | --- |
|  | FgenGetFrequencyListMinLength 方法 |

Gets the minimum number of frequency lists for the specified channel.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetFrequencyListMinLength()
```

###### 返回值

DictionaryString, Int64  
A dictionary collection of minimum number of frequency lists. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetHardwareState 方法

|  |  |
| --- | --- |
|  | FgenGetHardwareState 方法 |

Gets a value indicating the hardware state of the signal generator currently in use.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetHardwareState()
```

###### 返回值

DictionaryString, String  
A dictionary collection of hardware state. The key of the collection is pin name, the value is multisite result of one of
"Done", "HardwareError", "Idle", "Running" and "WaitingForStartTrigger".

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetIdleValue 方法

|  |  |
| --- | --- |
|  | FgenGetIdleValue 方法 |

Fetches the value to generate in the Idle state.
You must set IdleBehavior to JumpToValue to use this property.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetIdleValue()
```

###### 返回值

DictionaryString, Int64  
A dictionary collection of value. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetLoadImpedance 方法

|  |  |
| --- | --- |
|  | FgenGetLoadImpedance 方法 |

Gets the load impedance connected to the analog output of the channel.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetLoadImpedance()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of load impedance. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetOutputEnabled 方法

|  |  |
| --- | --- |
|  | FgenGetOutputEnabled 方法 |

Gets a value indicating whether the output is enabled for a specified channel.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> GetOutputEnabled()
```

###### 返回值

DictionaryString, Boolean  
A dictionary collection indicating whether the output is enabled for this channel. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetOutputIdleBehavior 方法

|  |  |
| --- | --- |
|  | FgenGetOutputIdleBehavior 方法 |

Gets the behavior of the output signal during the Idle state.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetOutputIdleBehavior()
```

###### 返回值

DictionaryString, String  
A dictionary collection of behavior. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetOutputImpedance 方法

|  |  |
| --- | --- |
|  | FgenGetOutputImpedance 方法 |

Gets the output impedance of the signal generator at the specified channel.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetOutputImpedance()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of output impedance. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetOutputMode 方法

|  |  |
| --- | --- |
|  | FgenGetOutputMode 方法 |

Gets the output mode of the signal generator.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetOutputMode()
```

###### 返回值

DictionaryString, String  
A dictionary collection of output mode. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetOutputWaitBehavior 方法

|  |  |
| --- | --- |
|  | FgenGetOutputWaitBehavior 方法 |

Gets the behavior of the output while the device is waiting for a Script trigger or executing a wait instruction.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetOutputWaitBehavior()
```

###### 返回值

DictionaryString, String  
A dictionary collection of behavior. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetReferenceClockFrequency 方法

|  |  |
| --- | --- |
|  | FgenGetReferenceClockFrequency 方法 |

Gets the reference clock frequency in hertz (Hz). The signal generator uses the reference clock to derive frequencies and sample rates when generating output.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetReferenceClockFrequency()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of reference clock frequency. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetReferenceClockSource 方法

|  |  |
| --- | --- |
|  | FgenGetReferenceClockSource 方法 |

Gets the reference clock source used by the signal generator.
The function generator derives frequencies and sample rates that it uses to generate waveforms from the reference clock.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetReferenceClockSource()
```

###### 返回值

DictionaryString, String  
A dictionary collection of reference clock source. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetSampleClockAbsoluteDelay 方法

|  |  |
| --- | --- |
|  | FgenGetSampleClockAbsoluteDelay 方法 |

Gets the delay in seconds to apply to an external Sample Clock.
This property is useful when trying to align the output of two devices.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetSampleClockAbsoluteDelay()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of sample clock absolute delay. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetSampleClockExportedDivisor 方法

|  |  |
| --- | --- |
|  | FgenGetSampleClockExportedDivisor 方法 |

Gets the factor by which to divide the sample clock, also known as an update clock, before it is exported.
To export the sample clock, use ExportSignal or SetSampleClockOutputTerminal.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetSampleClockExportedDivisor()
```

###### 返回值

DictionaryString, Int64  
A dictionary collection of sample clock exported divisor. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetSampleClockMode 方法

|  |  |
| --- | --- |
|  | FgenGetSampleClockMode 方法 |

Gets the sample clock mode for the signal generator.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetSampleClockMode()
```

###### 返回值

DictionaryString, String  
A dictionary collection of sample clock mode. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetSampleClockRate 方法

|  |  |
| --- | --- |
|  | FgenGetSampleClockRate 方法 |

Gets the rate, in samples per second, at which the signal generator generates the points

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetSampleClockRate()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of sample clock rate. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetSampleClockSource 方法

|  |  |
| --- | --- |
|  | FgenGetSampleClockSource 方法 |

Gets the sample clock source.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetSampleClockSource()
```

###### 返回值

DictionaryString, String  
A dictionary collection of sample clock source. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetSampleClockTimebaseExportedDivisor 方法

|  |  |
| --- | --- |
|  | FgenGetSampleClockTimebaseExportedDivisor 方法 |

Gets the factor by which to divide the device clock (sample clock timebase) before it is exported.
To export the sample clock timebase, use ExportSignal or SetSampleClockTimebaseOutputTerminal.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetSampleClockTimebaseExportedDivisor()
```

###### 返回值

DictionaryString, Int64  
A dictionary collection of sample clock timebase exported divisor. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetSampleClockTimebaseRate 方法

|  |  |
| --- | --- |
|  | FgenGetSampleClockTimebaseRate 方法 |

Gets the sample clock timebase rate. This property applies only to an external sample clock timebase.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetSampleClockTimebaseRate()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of sample clock timebase rate. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetSampleClockTimebaseSource 方法

|  |  |
| --- | --- |
|  | FgenGetSampleClockTimebaseSource 方法 |

Gets the sample clock timebase source.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetSampleClockTimebaseSource()
```

###### 返回值

DictionaryString, String  
A dictionary collection of sample clock timebase source. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetScriptToGenerate 方法

|  |  |
| --- | --- |
|  | FgenGetScriptToGenerate 方法 |

Gets a value indicating the name of the script that the generator produces.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetScriptToGenerate()
```

###### 返回值

DictionaryString, String  
A dictionary collection of the name of the script. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetStartPhase 方法

|  |  |
| --- | --- |
|  | FgenGetStartPhase 方法 |

Gets the start phase of the standard waveform the function generator produces. When the Waveform attribute is set to Waveform DC, this attribute does not affect signal output.The units are degrees.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetStartPhase()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of start phase. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetTerminalConfiguration 方法

|  |  |
| --- | --- |
|  | FgenGetTerminalConfiguration 方法 |

Get the generator terminal configuration information.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetTerminalConfiguration()
```

###### 返回值

DictionaryString, String  
A dictionary collection of terminal configuration. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetTriggerMode 方法

|  |  |
| --- | --- |
|  | FgenGetTriggerMode 方法 |

Gets the trigger mode for the signal generator.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetTriggerMode()
```

###### 返回值

DictionaryString, String  
A dictionary collection of trigger mode. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetTriggerType 方法

|  |  |
| --- | --- |
|  | FgenGetTriggerType 方法 |

Gets the type of trigger for specified triggerId if triggerClass is Script.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetTriggerType(
	string triggerClass,
	string triggerId
)
```

###### 参数

triggerClass  String
:   "Start", "Script".

triggerId  String
:   The trigger used for triggering. If triggerClass is "Start", input "".

###### 返回值

DictionaryString, String  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetWaitValue 方法

|  |  |
| --- | --- |
|  | FgenGetWaitValue 方法 |

Gets the value to generate while waiting.
You must set WaitBehavior to JumpToValue to use this method.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetWaitValue()
```

###### 返回值

DictionaryString, Int64  
A dictionary collection of behavior. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetWaveformFuntion 方法

|  |  |
| --- | --- |
|  | FgenGetWaveformFuntion 方法 |

Gets which standard waveform the function generator produces.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetWaveformFuntion()
```

###### 返回值

DictionaryString, String  
A dictionary collection of waveform function. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### InitiateGeneration 方法

|  |  |
| --- | --- |
|  | FgenInitiateGeneration 方法 |

Initiates signal generation

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen InitiateGeneration()
```

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### IsGenerationDone 方法

|  |  |
| --- | --- |
|  | FgenIsGenerationDone 方法 |

Gets a value indicating whether the current generation is complete.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> IsGenerationDone()
```

###### 返回值

DictionaryString, Boolean  
A dictionary collection indicating whether generation is done. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### Reset 方法

|  |  |
| --- | --- |
|  | FgenReset 方法 |

Reset the instrument session.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen Reset()
```

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SendSoftwareEdgeTrigger 方法

|  |  |
| --- | --- |
|  | FgenSendSoftwareEdgeTrigger 方法 |

Sends a command to trigger.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SendSoftwareEdgeTrigger(
	string triggeClass,
	string triggerId
)
```

###### 参数

triggeClass  String
:   "Start", "Script"

triggerId  String
:   The trigger used for triggering. If triggerClass is "Start", input "".

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetAmplitude 方法

|  |  |
| --- | --- |
|  | FgenSetAmplitude 方法 |

Sets the amplitude of the standard waveform the function generator produces. When the Waveform attribute is set to Waveform DC, this attribute does not affect signal output.The units are volts.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetAmplitude(
	double amplitude
)
```

###### 参数

amplitude  Double
:   The peak-to-peak amplitude to use.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetAnalogFilterEnabled 方法

|  |  |
| --- | --- |
|  | FgenSetAnalogFilterEnabled 方法 |

Sets a value indicating whether the signal generator applies an analog filter to the output signal.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetAnalogFilterEnabled(
	bool enabled
)
```

###### 参数

enabled  Boolean
:   true or false.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetAnalogPath 方法

|  |  |
| --- | --- |
|  | FgenSetAnalogPath 方法 |

Sets the analog signal path. The default valut is "Main".
The Main path allows the user to configure gain, offset, analog filter status, output impedance, and output enable.
The Direct path presents a much smaller gain range, and you cannot adjust offset or the filter status. The Direct path provides a smaller output range but lower distortion.
The Main path has two amplifier options, high and low gain. Setting this value to Main allows NI-FGEN to choose the amplifier based on the user-specified gain.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetAnalogPath(
	string analogPath
)
```

###### 参数

analogPath  String
:   "Main", "Direct", "FixedHighGain", "FixedLowGain".

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetArbGain 方法

|  |  |
| --- | --- |
|  | FgenSetArbGain 方法 |

Sets the factor by which the signal generator scales the arbitrary waveform data.
When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use the gain to scale the arbitrary waveform to other ranges.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetArbGain(
	double gain
)
```

###### 参数

gain  Double
:   The factor by which the signal generator scales the arbitrary waveform data.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetArbOffset 方法

|  |  |
| --- | --- |
|  | FgenSetArbOffset 方法 |

Sets the value the signal generator adds to the arbitrary waveform data.
When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use the offset to shift the arbitrary waveform range.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetArbOffset(
	double offset
)
```

###### 参数

offset  Double
:   The value the signal generator adds to the arbitrary waveform data.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetArbSampleRate 方法

|  |  |
| --- | --- |
|  | FgenSetArbSampleRate 方法 |

Sets the rate, in samples per second, at which the signal generator generates the points in arbitrary waveforms.
Use this property when OutputMode is set to Arbitrary or Sequence.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetArbSampleRate(
	double sampleRate
)
```

###### 参数

sampleRate  Double
:   The rate, in samples per second, at which the signal generator generates the points.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetArbSequenceHandle 方法

|  |  |
| --- | --- |
|  | FgenSetArbSequenceHandle 方法 |

Identifies which arbitrary sequence the function generator produces.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetArbSequenceHandle(
	long handle
)
```

###### 参数

handle  Int64
:   The handle that identifies the arbitrary sequence.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetArbWaveformHandle 方法

|  |  |
| --- | --- |
|  | FgenSetArbWaveformHandle 方法 |

Identifies which arbitrary waveform the function generator produces.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetArbWaveformHandle(
	long handle
)
```

###### 参数

handle  Int64
:   The handle representing which arbitrary waveform the signal generator produces.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetArbWaveformMarkerPosition 方法

|  |  |
| --- | --- |
|  | FgenSetArbWaveformMarkerPosition 方法 |

Sets the position for a marker to be asserted in the arbitrary waveform.
Use this property when OutputMode is set to Arbitrary. Use ExportSignal method to export the marker signal.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetArbWaveformMarkerPosition(
	long position
)
```

###### 参数

position  Int64
:   The position for a marker to be asserted in the arbitrary waveform. The default value is -1.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetArbWaveformRepeatCount 方法

|  |  |
| --- | --- |
|  | FgenSetArbWaveformRepeatCount 方法 |

Sets the number of times to repeat the arbitrary waveform when the trigger mode has been set to to Single or Stepped.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetArbWaveformRepeatCount(
	long count
)
```

###### 参数

count  Int64
:   The number of times to repeat the arbitrary waveform. The default value is 1.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetAttributeBool 方法

|  |  |
| --- | --- |
|  | FgenSetAttributeBool 方法 |

Set specific value by attribute identifier.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetAttributeBool(
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

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetAttributeDouble 方法

|  |  |
| --- | --- |
|  | FgenSetAttributeDouble 方法 |

Set specific value by attribute identifier.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetAttributeDouble(
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

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetAttributeInt 方法

|  |  |
| --- | --- |
|  | FgenSetAttributeInt 方法 |

Set specific value by attribute identifier.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetAttributeInt(
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

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetAttributeLong 方法

|  |  |
| --- | --- |
|  | FgenSetAttributeLong 方法 |

Set specific value by attribute identifier.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetAttributeLong(
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

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetAttributeString 方法

|  |  |
| --- | --- |
|  | FgenSetAttributeString 方法 |

Set specific value by attribute identifier.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetAttributeString(
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

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return DCVIParent.DCVI instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetChannelDelay 方法

|  |  |
| --- | --- |
|  | FgenSetChannelDelay 方法 |

Sets the delay to apply to the analog output of the channel specified by the channel string.
You can use the output delay to configure the timing relationship between channels on a multichannel device. Values for this property can be zero or positive.
A value of zero indicates that the channels are aligned. A positive value delays the analog output by the specified number of seconds.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetChannelDelay(
	double channelDelay
)
```

###### 参数

channelDelay  Double
:   The delay to apply to the analog output of the specified channel.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetCommonModeOffset 方法

|  |  |
| --- | --- |
|  | FgenSetCommonModeOffset 方法 |

Sets the value that the signal generator adds to or subtracts from the arbitrary waveform data.
Common-mode offset is applicable only when you set the terminal configuration to Differential. Common-mode offset is applied to the signals generated at each differential output terminal.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetCommonModeOffset(
	double commonModeOffset
)
```

###### 参数

commonModeOffset  Double
:   The value the signal generator adds to or subtracts from the arbitrary waveform data.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetDCOffset 方法

|  |  |
| --- | --- |
|  | FgenSetDCOffset 方法 |

Sets the DC offset of the standard waveform the function generator produces. If the Waveform attribute is set to Waveform DC, this attribute specifies the DC level the function generator produces.The units are volts.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetDCOffset(
	double dcOffset
)
```

###### 参数

dcOffset  Double
:   The DC offset of the standard waveform.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetDigitalFilterEnabled 方法

|  |  |
| --- | --- |
|  | FgenSetDigitalFilterEnabled 方法 |

Sets a value indicating whether the signal generator applies a digital filter to the output signal.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetDigitalFilterEnabled(
	bool enabled
)
```

###### 参数

enabled  Boolean
:   true or false.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetDigitalFilterInterpolationFactor 方法

|  |  |
| --- | --- |
|  | FgenSetDigitalFilterInterpolationFactor 方法 |

Sets the interpolation factor when the digital filter is enabled.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetDigitalFilterInterpolationFactor(
	double interpolationFactor
)
```

###### 参数

interpolationFactor  Double
:   The interpolation factor when the digital filter is enabled.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetDigitalGain 方法

|  |  |
| --- | --- |
|  | FgenSetDigitalGain 方法 |

Sets a factor by which the signal generator digitally multiplies generated data before converting it to an analog signal in the digital-to-analog converter.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetDigitalGain(
	double digitalGain
)
```

###### 参数

digitalGain  Double
:   The digital gain value.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetDigitalPatternEnabled 方法

|  |  |
| --- | --- |
|  | FgenSetDigitalPatternEnabled 方法 |

Sets a value indicating whether the signal generator generates a digital pattern corresponding to the output signal.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetDigitalPatternEnabled(
	bool enabled
)
```

###### 参数

enabled  Boolean
:   true or false.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetDutyCycleHigh 方法

|  |  |
| --- | --- |
|  | FgenSetDutyCycleHigh 方法 |

Sets the duty cycle of the square wave in units of percentage of time the waveform is high.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetDutyCycleHigh(
	double dutyCycleHigh
)
```

###### 参数

dutyCycleHigh  Double
:   The duty cycle of the square wave in units of percentage of time the waveform is high.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetExternalMultiplier 方法

|  |  |
| --- | --- |
|  | FgenSetExternalMultiplier 方法 |

Sets a multiplication factor to use to obtain a desired sample rate from an external Sample Clock.
The resulting sample rate is equal to this factor multiplied by the external Sample Clock rate. You can use this property to generate samples at a rate higher than your external clock rate. When using this property, you do not need to explicitly set the external clock rate.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetExternalMultiplier(
	double factor
)
```

###### 参数

factor  Double
:   A multiplication factor to use to obtain a desired sample rate from an external Sample Clock.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetFlatnessCorrectionEnabled 方法

|  |  |
| --- | --- |
|  | FgenSetFlatnessCorrectionEnabled 方法 |

Sets a value indicating whether flatness correction is enabled.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetFlatnessCorrectionEnabled(
	bool enabled
)
```

###### 参数

enabled  Boolean
:   true or false.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetFrequency 方法

|  |  |
| --- | --- |
|  | FgenSetFrequency 方法 |

Sets the frequency of the standard waveform the function generator produces. When the Waveform attribute is set to Waveform DC, this attribute does not affect signal output.The units are Hertz.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetFrequency(
	double frequency
)
```

###### 参数

frequency  Double
:   The frequency of the standard waveform.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetFrequencyListHandle 方法

|  |  |
| --- | --- |
|  | FgenSetFrequencyListHandle 方法 |

Sets which frequency list the signal generator produces.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetFrequencyListHandle(
	long handle
)
```

###### 参数

handle  Int64
:   The identifier of the frequency list that the signal generator produces.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetIdleValue 方法

|  |  |
| --- | --- |
|  | FgenSetIdleValue 方法 |

Sets the value to generate in the Idle state.
You must set IdleBehavior to JumpToValue to use this property.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetIdleValue(
	long idleValue
)
```

###### 参数

idleValue  Int64
:   The value to generate in the Idle state.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetLoadImpedance 方法

|  |  |
| --- | --- |
|  | FgenSetLoadImpedance 方法 |

Sets the load impedance connected to the analog output of the channel.
If you set the load impedance to –1.0, NI-FGEN assumes that the load impedance matches the value of the output impedance.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetLoadImpedance(
	double impedance
)
```

###### 参数

impedance  Double
:   The load impedance value to be set to the analog output of the channel.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetNextWritePosition 方法

|  |  |
| --- | --- |
|  | FgenSetNextWritePosition 方法 |

Sets the position in the named waveform to which data was written at the next write.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetNextWritePosition(
	string waveformName,
	string relativeTo,
	long offset
)
```

###### 参数

waveformName  String
:   The name of the waveform.

relativeTo  String
:   "Current", "Start". The reference position in the waveform.

offset  Int64
:   The offset from the relativeTo at which to start loading the data into the waveform.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetOutputEnabled 方法

|  |  |
| --- | --- |
|  | FgenSetOutputEnabled 方法 |

Sets a value indicating whether the output is enabled for a specified channel.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetOutputEnabled(
	bool enabled
)
```

###### 参数

enabled  Boolean
:   true or false.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetOutputIdleBehavior 方法

|  |  |
| --- | --- |
|  | FgenSetOutputIdleBehavior 方法 |

Sets the behavior of the output signal during the Idle state.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetOutputIdleBehavior(
	string behavior
)
```

###### 参数

behavior  String
:   "HoldLastValue", "JumpToValue".For NI 4463, it's "ZeroVolts", "HighImpedance" or "MaintainExistingValue".

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetOutputImpedance 方法

|  |  |
| --- | --- |
|  | FgenSetOutputImpedance 方法 |

Sets the output impedance of the signal generator at the specified channel.
This method specifies the output impedance of the signal generator at the output connector.
NI signal generators have an output impedance of 50 Ω and an optional 75 Ω on select modules.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetOutputImpedance(
	double impedance
)
```

###### 参数

impedance  Double
:   The output impedance of the signal generator at the specified channel to configure.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetOutputMode 方法

|  |  |
| --- | --- |
|  | FgenSetOutputMode 方法 |

Sets the output mode of the signal generator.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetOutputMode(
	string mode
)
```

###### 参数

mode  String
:   "Arbitrary": Generates waveforms from user-created/provided waveform arrays of numeric data.
    "FrequencyList": Generates a standard function using a list of frequencies you define.
    "Function": Generates standard function waveforms such as sine, square, triangle, etc.
    "Script": Allows you to use scripting to link and loop multiple waveforms in complex combinations.
    "Sequence": Generates downloaded waveforms in an order your specify.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetOutputWaitBehavior 方法

|  |  |
| --- | --- |
|  | FgenSetOutputWaitBehavior 方法 |

Sets the behavior of the output while the device is waiting for a Script trigger or executing a wait instruction.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetOutputWaitBehavior(
	string behavior
)
```

###### 参数

behavior  String
:   "HoldLastValue", "JumpToValue".

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetReferenceClockFrequency 方法

|  |  |
| --- | --- |
|  | FgenSetReferenceClockFrequency 方法 |

Sets the reference clock frequency in hertz (Hz). The signal generator uses the reference clock to derive frequencies and sample rates when generating output.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetReferenceClockFrequency(
	double frequency
)
```

###### 参数

frequency  Double
:   The reference clock frequency in hertz (Hz).

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetReferenceClockSource 方法

|  |  |
| --- | --- |
|  | FgenSetReferenceClockSource 方法 |

Sets the reference clock source used by the signal generator.
The function generator derives frequencies and sample rates that it uses to generate waveforms from the reference clock.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetReferenceClockSource(
	string clockSource
)
```

###### 参数

clockSource  String
:   "None", "PXI\_Clk", "ClkIn", "OnboardRefClk", "RTSI7"

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetSampleClockAbsoluteDelay 方法

|  |  |
| --- | --- |
|  | FgenSetSampleClockAbsoluteDelay 方法 |

Sets the delay in seconds to apply to an external Sample Clock.
This property is useful when trying to align the output of two devices.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetSampleClockAbsoluteDelay(
	double delay
)
```

###### 参数

delay  Double
:   The delay in seconds to apply to an external Sample Clock.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetSampleClockExportedDivisor 方法

|  |  |
| --- | --- |
|  | FgenSetSampleClockExportedDivisor 方法 |

Sets the factor by which to divide the sample clock, also known as an update clock, before it is exported.
To export the sample clock, use ExportSignal or SetSampleClockOutputTerminal.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetSampleClockExportedDivisor(
	long factor
)
```

###### 参数

factor  Int64
:   The factor by which to divide the sample clock before it is exported.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetSampleClockMode 方法

|  |  |
| --- | --- |
|  | FgenSetSampleClockMode 方法 |

Sets the sample clock mode for the signal generator.
When in DivideDown sampling mode, the sample rate can only be set to certain frequencies, based on dividing down the sample clock. However, in HighResolution mode, the sample rate may be set to any value.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetSampleClockMode(
	string mode
)
```

###### 参数

mode  String
:   "Automatic", "DivideDown", "HighResolution".

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetSampleClockRate 方法

|  |  |
| --- | --- |
|  | FgenSetSampleClockRate 方法 |

Sets the rate, in samples per second, at which the signal generator generates the points

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetSampleClockRate(
	double rate
)
```

###### 参数

rate  Double
:   The rate, in samples per second.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetSampleClockSource 方法

|  |  |
| --- | --- |
|  | FgenSetSampleClockSource 方法 |

Sets the sample clock source.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetSampleClockSource(
	string source
)
```

###### 参数

source  String
:   The sample clock source. The default value is "OnboardClock".
    Possible values: "OnboardClock", "ClkIn", "PXI\_Star", "PXI\_Trig0", "PXI\_Trig1", "PXI\_Trig2", "PXI\_Trig3", "PXI\_Trig4", "PXI\_Trig5", "PXI\_Trig6", "PXI\_Trig7", "DDC\_ClkIn".

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetSampleClockTimebaseExportedDivisor 方法

|  |  |
| --- | --- |
|  | FgenSetSampleClockTimebaseExportedDivisor 方法 |

Sets the factor by which to divide the device clock (sample clock timebase) before it is exported.
To export the sample clock timebase, use ExportSignal or SetSampleClockTimebaseOutputTerminal.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetSampleClockTimebaseExportedDivisor(
	long factor
)
```

###### 参数

factor  Int64
:   The factor by which to divide the device clock (sample clock timebase) before it is exported.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetSampleClockTimebaseRate 方法

|  |  |
| --- | --- |
|  | FgenSetSampleClockTimebaseRate 方法 |

Sets the sample clock timebase rate. This property applies only to an external sample clock timebase.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetSampleClockTimebaseRate(
	double rate
)
```

###### 参数

rate  Double
:   The sample clock timebase rate.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetSampleClockTimebaseSource 方法

|  |  |
| --- | --- |
|  | FgenSetSampleClockTimebaseSource 方法 |

Sets the sample clock timebase source.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetSampleClockTimebaseSource(
	string source
)
```

###### 参数

source  String
:   The sample clock timebase source.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetScriptToGenerate 方法

|  |  |
| --- | --- |
|  | FgenSetScriptToGenerate 方法 |

Sets a value indicating the name of the script that the generator produces.
OutputMode should be set to Script to call this property.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetScriptToGenerate(
	string scriptName
)
```

###### 参数

scriptName  String
:   The name of the script that the generator produces.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetStartPhase 方法

|  |  |
| --- | --- |
|  | FgenSetStartPhase 方法 |

Sets the start phase of the standard waveform the function generator produces. When the Waveform attribute is set to Waveform DC, this attribute does not affect signal output.The units are degrees.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetStartPhase(
	double startPhase
)
```

###### 参数

startPhase  Double
:   The horizontal offset, in degrees of one waveform cycle, of the standard waveform.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetTerminalConfiguration 方法

|  |  |
| --- | --- |
|  | FgenSetTerminalConfiguration 方法 |

Determines whether the generator will run in single-ended or differential mode, and whether the output gain and offset values will be analyzed based on single-ended or differential operation.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetTerminalConfiguration(
	string configuration
)
```

###### 参数

configuration  String
:   "SingleEnded" or "Differential". For NI4463, it's "Pseudodifferential" or "Differential".

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetTriggerMode 方法

|  |  |
| --- | --- |
|  | FgenSetTriggerMode 方法 |

Sets the trigger mode for the signal generator.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetTriggerMode(
	string triggerMode
)
```

###### 参数

triggerMode  String
:   The trigger mode to set. "Burst", "Continuous", "Single", "Stepped".

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetTriggerType 方法

|  |  |
| --- | --- |
|  | FgenSetTriggerType 方法 |

Sets the type of trigger for specified triggerId if triggerClass is Script.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetTriggerType(
	string triggerClass,
	string triggerId,
	string triggerType
)
```

###### 参数

triggerClass  String
:   "Start", "Script".

triggerId  String
:   The trigger used for triggering. If triggerClass is "Start", input "".

triggerType  String
:   "DigitalEdge", "None", "SoftwareEdge".

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetWaitValue 方法

|  |  |
| --- | --- |
|  | FgenSetWaitValue 方法 |

Sets the value to generate while waiting.
You must set WaitBehavior to JumpToValue to use this method.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetWaitValue(
	long waitValue
)
```

###### 参数

waitValue  Int64
:   The value to generate in the waiting state.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetWaveformFunction 方法

|  |  |
| --- | --- |
|  | FgenSetWaveformFunction 方法 |

Sets which standard waveform the function generator produces.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen SetWaveformFunction(
	string waveformFunction
)
```

###### 参数

waveformFunction  String
:   The standard waveform the signal generator produces. "DC", "Noise", "RampDown", "RampUp", "Sine", "Square", "Triangle", "User".

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### WaitUntilDone 方法

|  |  |
| --- | --- |
|  | FgenWaitUntilDone 方法 |

Waits until the device is done generating or until the maximum time has expired.
Call this method after calling InitiateGeneration.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen WaitUntilDone(
	double maxTime
)
```

###### 参数

maxTime  Double
:   The timeout value in seconds.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### WriteArbWaveform 方法

|  |  |
| --- | --- |
|  | FgenWriteArbWaveform 方法 |

Writes data to a waveform in onboard memory.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen WriteArbWaveform(
	long handle,
	double[] waveform
)
```

###### 参数

handle  Int64
:   The handle of the arbitrary waveform to use.

waveform  Double
:   The array of data you want to load into the waveform.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### WriteNamedWaveform 方法

|  |  |
| --- | --- |
|  | FgenWriteNamedWaveform 方法 |

Writes floating point data to the named waveform in onboard memory.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen WriteNamedWaveform(
	string waveformName,
	double[] waveform
)
```

###### 参数

waveformName  String
:   The name of the waveform.

waveform  Double
:   The array of floating point values you want to load into the waveform.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### WriteScript 方法

|  |  |
| --- | --- |
|  | FgenWriteScript 方法 |

Writes a string containing one or more scripts that govern the generation of waveforms.

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Fgen WriteScript(
	string script
)
```

###### 参数

script  String
:   The text of the script you want to use for your generation operation.

###### 返回值

[Fgen](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)  
Return FgenParent.Fgen instance.

参见

###### 引用

[Fgen 类](bf8154ce-fb0e-baea-5b6f-84f45c379da5.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


## IFgen_Instr 接口

|  |  |
| --- | --- |
|  | IFgen\_Instr 接口 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public interface IFgen_Instr
```

IFgen\_Instr 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [AbortGeneration](b3c790e8-546d-9bab-faf1-8105d98be364.htm) |  |
| 公共方法 | [AdjustRelativeDelay](ff237758-918f-615e-2651-f9639f1c16b0.htm) |  |
| 公共方法 | [AllocateArbWaveform](cd5797f1-b85c-0268-eeb2-0d6a3b360da1.htm) |  |
| 公共方法 | [AllocateNamedWaveform](95a6558a-b61c-da5a-d6db-9e4a82b46829.htm) |  |
| 公共方法 | [ClearArbMemory](061a03ef-5d99-172a-c1f4-fb00a3fc7dfe.htm) |  |
| 公共方法 | [ClearArbSequence](2e166fe4-12bc-c42d-e72b-8f7ba1fbe285.htm) |  |
| 公共方法 | [ClearArbWaveform](73bb19ab-712e-322d-c983-89f9c783451e.htm) |  |
| 公共方法 | [ClearFrequencyList](3d994d58-6743-9bc9-0cc9-ff6326e0b973.htm) |  |
| 公共方法 | [ClearUserStandardWaveform](29e514b9-540b-878f-aa8e-510785ec8d2f.htm) |  |
| 公共方法 | [Commit](1fa5f2b5-1c24-8907-73bd-a49621584fe4.htm) |  |
| 公共方法 | [ConfigureArbSequence](1209866a-ba6d-1757-80e8-68249477277a.htm) |  |
| 公共方法 | [ConfigureArbWaveform](23f10a97-03eb-f9c1-397b-104c4a63f5f3.htm) |  |
| 公共方法 | [ConfigureDigitalEdgeTrigger](b8341b9b-981a-6bb7-b1f4-a2db1be8a376.htm) |  |
| 公共方法 | [ConfigureDigitalLevelScriptTrigger](1563e1d6-b67c-a235-a3ee-abc3b084cded.htm) |  |
| 公共方法 | [ConfigureFrequencyList](f6666883-a2d9-cd00-18b6-34be0383a1c9.htm) |  |
| 公共方法 | [ConfigureReferenceClock](b49945d5-b7bd-349e-8a4e-217093bf018a.htm) |  |
| 公共方法 | [ConfigureSampleClock](980c2708-d0e1-0b75-9aad-953d502d45d8.htm) |  |
| 公共方法 | [ConfigureSoftwareEdgeTrigger](8e821489-89ff-aba4-7ca4-df35a78e03ef.htm) |  |
| 公共方法 | [ConfigureStandardWavaform](c923bfb6-7963-7ff1-38dc-7085c07d93da.htm) |  |
| 公共方法 | [CreateArbSequence(Int32, Int32)](d9f0e4da-613b-0bbd-12c9-9d1733e0414a.htm) |  |
| 公共方法 | [CreateArbSequence(Int32, Int32, Int32, Int32)](bb9b5489-6ced-5cad-e996-fd226459441e.htm) |  |
| 公共方法 | [CreateChannelArbWaveform](1e0063ad-66c9-0278-e5d6-35a8f1716e42.htm) |  |
| 公共方法 | [CreateChannelArbWaveformFromFile](6a76271f-54a5-d39b-1a8f-5b01c7c04b77.htm) |  |
| 公共方法 | [CreateFrequencyList](4432e709-71cc-7f79-de88-8e9a9ffc0339.htm) |  |
| 公共方法 | [DefineUsetStandardWaveform](9261a42b-c9b4-9d99-cfbc-7c0e6ea10c24.htm) |  |
| 公共方法 | [DeleteNamedWaveform](22bbd442-733b-a0fa-6227-4fa8d9c96efd.htm) |  |
| 公共方法 | [DeleteScript](5d7fce7a-b3b6-684a-a6c2-b3b8c6ba9686.htm) |  |
| 公共方法 | [DisableTrigger](b596ef0c-0bbc-ddce-02bd-4378611025d2.htm) |  |
| 公共方法 | [EnableAnalogFilter](31150b3f-ac06-3434-8eb5-e9b556dbd0a5.htm) |  |
| 公共方法 | [ExportSignal](80ae64f3-925a-1e5e-81f9-bf333a83d6dc.htm) |  |
| 公共方法 | [GetAmplitude](eb954ae4-5827-bc10-7edc-08aa0a9f4229.htm) |  |
| 公共方法 | [GetAnalogFilterEnabled](d217df99-21e7-e50d-c81b-d38c855d64fa.htm) |  |
| 公共方法 | [GetAnalogPath](c57b673d-4b69-e782-ce0f-123785199e65.htm) |  |
| 公共方法 | [GetArbGain](eb6e7e53-d43a-26e0-6cf5-f3c7f0f20d91.htm) |  |
| 公共方法 | [GetArbOffset](555ffeb8-cce3-98a2-2386-820322eacfb7.htm) |  |
| 公共方法 | [GetArbSampleRate](45fbf2e8-81aa-219c-5b40-8201b95f1538.htm) |  |
| 公共方法 | [GetArbSequenceHandle](8a6de733-da32-97e2-913c-03591dc9ed78.htm) |  |
| 公共方法 | [GetArbSequenceMaxLength](d4923faa-039e-424b-1e4b-9ed5319bb909.htm) |  |
| 公共方法 | [GetArbSequenceMaxLoopCount](71efb6ca-9b3f-28c1-a47b-1fca3ce02ca4.htm) |  |
| 公共方法 | [GetArbSequenceMinLength](595ef153-9b4e-104a-9afc-e63970a2fee4.htm) |  |
| 公共方法 | [GetArbSequencesMaxNumber](f1004a3c-6a3f-cb40-3b41-6f0be328caad.htm) |  |
| 公共方法 | [GetArbWaveformHandle](5dbc361b-66f7-77d9-fd2c-970acb9f0e41.htm) |  |
| 公共方法 | [GetArbWaveformMarkerPosition](90d5ea4f-3d68-a06d-fd62-5fe8661f7b55.htm) |  |
| 公共方法 | [GetArbWaveformMaxSize](3b2353c2-86f1-4f4a-d915-16aefb256815.htm) |  |
| 公共方法 | [GetArbWaveformMinSize](461b62a9-d68f-4d40-8b4b-018abf2262da.htm) |  |
| 公共方法 | [GetArbWaveformQuantum](70265fe8-4b53-8e94-2b85-7b818eb84740.htm) |  |
| 公共方法 | [GetArbWaveformRepeatCount](266225cb-5bac-ada5-2883-e6f817aa45d9.htm) |  |
| 公共方法 | [GetArbWaveformsMaxNumber](4e1a37c9-8789-ce76-aba1-387da0c844c4.htm) |  |
| 公共方法 | [GetAttributeT](c85edfd7-7701-96a8-9768-34bdfd9301cf.htm) |  |
| 公共方法 | [GetChannelDelay](59130d9c-3aba-032a-fab6-ca4503596c22.htm) |  |
| 公共方法 | [GetCommonModeOffset](68916e81-4531-ad14-4cbc-dc7920f4fd19.htm) |  |
| 公共方法 | [GetDCOffset](7d898f8f-a485-ec13-1300-774b84e10158.htm) |  |
| 公共方法 | [GetDigitalFilterEnabled](cb462402-1ead-aa08-9de3-d6dca8e9e85d.htm) |  |
| 公共方法 | [GetDigitalFilterInterpolationFactor](9df33939-e484-d59c-2650-3dd95b79d929.htm) |  |
| 公共方法 | [GetDigitalGain](c777e26c-38c1-b55d-2e7d-5f06453c937b.htm) |  |
| 公共方法 | [GetDigitalPatternEnabled](e597b4f1-e0bd-3acf-bb89-498a34d716ce.htm) |  |
| 公共方法 | [GetDutyCycleHigh](9a1a36d4-f9ff-acf5-23bb-f71ee47d2570.htm) |  |
| 公共方法 | [GetExternalMultiplier](c28a9dc8-47ab-8a00-1ad0-b996958db3e1.htm) |  |
| 公共方法 | [GetFlatnessCorrectionEnabled](2352ee41-bc41-9168-e90f-f7ffc288ff58.htm) |  |
| 公共方法 | [GetFrequency](462562e7-f39f-7c0d-9e5b-ff7e02c3e94e.htm) |  |
| 公共方法 | [GetFrequencyListDurationQuantum](a035583c-0ff9-2300-0381-efe9aad83c41.htm) |  |
| 公共方法 | [GetFrequencyListHandle](939cef94-3d88-fc27-4c24-1ca5d53b25fa.htm) |  |
| 公共方法 | [GetFrequencyListMaxDuratinon](094a044b-21d8-9554-15f8-32d5e5217ceb.htm) |  |
| 公共方法 | [GetFrequencyListMaxLength](f8515f4b-d7d6-7715-dd43-e5758d06d473.htm) |  |
| 公共方法 | [GetFrequencyListMaxNumber](ede723c6-c4a8-c527-fba1-d2156a61095b.htm) |  |
| 公共方法 | [GetFrequencyListMinDuration](01275973-fd8d-d7aa-aba4-a388095fecd5.htm) |  |
| 公共方法 | [GetFrequencyListMinLength](8147815a-e680-04c8-d7c2-63ac9d6d86b0.htm) |  |
| 公共方法 | [GetHardwareState](1947d4db-eb42-8130-ac0b-5079549e0681.htm) |  |
| 公共方法 | [GetIdleValue](206acb95-1555-e743-ae1f-d52d890f1b12.htm) |  |
| 公共方法 | [GetLoadImpedance](3884f312-ab59-9596-39e4-c7500b4903c1.htm) |  |
| 公共方法 | [GetOutputEnabled](00869841-6c5a-8b65-e559-c47893203969.htm) |  |
| 公共方法 | [GetOutputIdleBehavior](e851fc52-904d-a825-4607-f26c32548c54.htm) |  |
| 公共方法 | [GetOutputImpedance](878c6f42-aa6b-3b6a-e318-8c6bf730dd05.htm) |  |
| 公共方法 | [GetOutputMode](66302839-5787-1087-602e-2bbd4cf39282.htm) |  |
| 公共方法 | [GetOutputWaitBehavior](aede2049-bca0-e4fe-7c54-800560362547.htm) |  |
| 公共方法 | [GetReferenceClockFrequency](02aa7ecb-df88-b402-d4c5-a840c277db58.htm) |  |
| 公共方法 | [GetReferenceClockSource](80f1a840-0573-9e3e-c8df-10b9fc54ec04.htm) |  |
| 公共方法 | [GetSampleClockAbsoluteDelay](1531f763-c591-a158-669a-fa7bb46c40f9.htm) |  |
| 公共方法 | [GetSampleClockExportedDivisor](5b7ea29c-ccbe-c4bb-6d46-631eccb9929c.htm) |  |
| 公共方法 | [GetSampleClockMode](de82d324-f9c0-efce-f0d9-9242264a9367.htm) |  |
| 公共方法 | [GetSampleClockRate](f16c125c-4505-a853-42b5-1d1cbfc6984c.htm) |  |
| 公共方法 | [GetSampleClockSource](b9dd084a-cfdf-544e-a5db-0f573f7d4215.htm) |  |
| 公共方法 | [GetSampleClockTimebaseExportedDivisor](554776e9-466e-8e0a-1f92-9294a5ee92d7.htm) |  |
| 公共方法 | [GetSampleClockTimebaseRate](afac6a4f-02bd-db7c-8680-d9067088fa0e.htm) |  |
| 公共方法 | [GetSampleClockTimebaseSource](e1292cbb-8385-5b69-fc35-d7165d88a7dd.htm) |  |
| 公共方法 | [GetScriptToGenerate](cc9e754b-93ec-fa90-9ede-b8c6b2f675f3.htm) |  |
| 公共方法 | [GetStartPhase](418707b2-a45f-2943-d162-a6757385256d.htm) |  |
| 公共方法 | [GetTerminalConfiguration](03956560-9a1e-e998-5779-1fd78f03e427.htm) |  |
| 公共方法 | [GetTriggerMode](f95cd92b-974a-7729-e799-51f728d8a1b7.htm) |  |
| 公共方法 | [GetTriggerType](d3d42432-23b1-aad7-dbc1-0f56cd07059e.htm) |  |
| 公共方法 | [GetWaitValue](65b907b8-b126-230c-1730-e85e8f50ea85.htm) |  |
| 公共方法 | [GetWaveformFuntion](6d017609-4c2b-e075-1c15-46aad3f087c3.htm) |  |
| 公共方法 | [InitiateGeneration](3403c117-d0a1-a8e8-ae54-f04496a1cff6.htm) |  |
| 公共方法 | [IsGenerationDone](e5181e05-d38b-042b-bb7b-ad1782f1c682.htm) |  |
| 公共方法 | [Reset](5b5a8dc3-eab6-66ff-2aaf-32511126c77b.htm) |  |
| 公共方法 | [SendSoftwareEdgeTrigger](5a45cb10-dbea-cb93-9f68-5d2cdc31b348.htm) |  |
| 公共方法 | [SetAmplitude](3cdda3c0-101f-2823-779e-5fe54b608576.htm) |  |
| 公共方法 | [SetAnalogFilterEnabled](27de589c-9a94-6487-afe3-01e2a93916a8.htm) |  |
| 公共方法 | [SetAnalogPath](756c305e-9084-36f2-611c-91d38fdae1e9.htm) |  |
| 公共方法 | [SetArbGain](75f44e12-ba36-6892-de8b-b9561a54a659.htm) |  |
| 公共方法 | [SetArbOffset](ae75ef25-0f7c-3fb5-4f5d-73a980ad16af.htm) |  |
| 公共方法 | [SetArbSampleRate](07f51869-cd55-2e70-d3ac-c8a95241e99c.htm) |  |
| 公共方法 | [SetArbSequenceHandle](0a2a82eb-179a-8bba-799b-520ca2bd76e0.htm) |  |
| 公共方法 | [SetArbWaveformHandle](03943aae-e1af-0a13-7826-8821df72ee82.htm) |  |
| 公共方法 | [SetArbWaveformMarkerPosition](a34b425e-de09-a47b-185a-f840df3d395e.htm) |  |
| 公共方法 | [SetArbWaveformRepeatCount](a6575288-4f21-9fc0-acb9-b2dffbcc9747.htm) |  |
| 公共方法 | [SetAttribute](8260fab1-b4da-d5ac-4653-a1a8518167c3.htm) |  |
| 公共方法 | [SetChannelDelay](bec97166-146c-ae0f-a31d-cb439f90c1e6.htm) |  |
| 公共方法 | [SetCommonModeOffset](f8cbdf7b-3526-b5fb-a46d-baf9b9f99a2c.htm) |  |
| 公共方法 | [SetDCOffset](4ebf0e9b-dfb9-9b83-6e2c-8d9e9e8ffc65.htm) |  |
| 公共方法 | [SetDigitalFilterEnabled](5db8f55e-9893-183d-0538-8d4ae9b5f34c.htm) |  |
| 公共方法 | [SetDigitalFilterInterpolationFactor](c2b25fdf-91ab-2de6-488b-4d009f6eb9a4.htm) |  |
| 公共方法 | [SetDigitalGain](bd9d2086-3720-2bb9-a7d3-248aa02be185.htm) |  |
| 公共方法 | [SetDigitalPatternEnabled](f8cd8ac8-23b2-80f3-9b5a-90dde9ceadca.htm) |  |
| 公共方法 | [SetDutyCycleHigh](1ec1d83a-b2aa-9b4c-0739-143197ab955d.htm) |  |
| 公共方法 | [SetExternalMultiplier](c6f96053-a278-345e-d2e9-59929b79a994.htm) |  |
| 公共方法 | [SetFlatnessCorrectionEnabled](44088be8-4789-07fe-9860-3bc889986884.htm) |  |
| 公共方法 | [SetFrequency](480e6bad-2fdc-e6d0-e9d4-7a0fa770583d.htm) |  |
| 公共方法 | [SetFrequencyListHandle](727f9aa5-ebd6-15b6-a162-28546fa7082e.htm) |  |
| 公共方法 | [SetIdleValue](5ba87583-a22a-5fb1-18ee-d744385049c2.htm) |  |
| 公共方法 | [SetLoadImpedance](53a615e1-8181-9778-5919-3830c7da0601.htm) |  |
| 公共方法 | [SetNextWritePosition](1edc83a8-2beb-e90c-9470-54ba2fda94b6.htm) |  |
| 公共方法 | [SetOutputEnabled](b025c0a4-57c3-7740-7cd2-2cfe68d2d8e3.htm) |  |
| 公共方法 | [SetOutputIdleBehavior](0917759c-fa46-34e1-568c-bc7869f4d259.htm) |  |
| 公共方法 | [SetOutputImpedance](5a28a32a-6238-7883-40f7-75025fd4af24.htm) |  |
| 公共方法 | [SetOutputMode](dcfca3ac-8bce-36fa-23cd-18e043b9d5a9.htm) |  |
| 公共方法 | [SetOutputWaitBehavior](e069cd48-04dd-a496-bc25-9ed0caa01213.htm) |  |
| 公共方法 | [SetReferenceClockFrequency](197f160f-e2e3-850c-5c46-ccb2c87279f2.htm) |  |
| 公共方法 | [SetReferenceClockSource](dedf13dd-4416-2a6b-e467-5d646cd513e0.htm) |  |
| 公共方法 | [SetSampleClockAbsoluteDelay](94641598-348a-2ef3-f51c-ab0f566894f9.htm) |  |
| 公共方法 | [SetSampleClockExportedDivisor](d20cdb5f-480f-abf5-62e6-5d0313978aad.htm) |  |
| 公共方法 | [SetSampleClockMode](22216978-0566-2beb-fd3b-fd38d705fc2e.htm) |  |
| 公共方法 | [SetSampleClockRate](dc607ccd-b76d-9cc1-0643-f4f6b231a341.htm) |  |
| 公共方法 | [SetSampleClockSource](5dfacae0-9fb2-9b5d-28fe-2bd056e8e650.htm) |  |
| 公共方法 | [SetSampleClockTimebaseExportedDivisor](543fdb68-5f27-7310-9c7a-1c37546f2764.htm) |  |
| 公共方法 | [SetSampleClockTimebaseRate](afff7ed1-fcde-afe4-18cd-4a8be4d8cb04.htm) |  |
| 公共方法 | [SetSampleClockTimebaseSource](f1e24b74-d548-e6ad-ce2c-3edbf0ce2dae.htm) |  |
| 公共方法 | [SetScriptToGenerate](93e4631e-c521-6712-8b07-e99e2d1c718c.htm) |  |
| 公共方法 | [SetStartPhase](d534a914-6798-70b7-eeba-29fe684e2b54.htm) |  |
| 公共方法 | [SetTerminalConfiguration](7e16deb3-448c-b0d6-ef96-2db5bd877dcc.htm) |  |
| 公共方法 | [SetTriggerMode](253aa1d5-15d0-086c-69eb-83ecb3878614.htm) |  |
| 公共方法 | [SetTriggerType](fd3f25da-9b36-3350-0eef-3a40d7cb9722.htm) |  |
| 公共方法 | [SetWaitValue](729068d8-71b5-db27-2d7c-75d0ca2e74ba.htm) |  |
| 公共方法 | [SetWaveformFunction](cde4e50c-1220-8ea0-da92-8ef11c7e602c.htm) |  |
| 公共方法 | [WaitUntilDone](c0f8f4ce-4c4a-fc5e-3aab-467c4a4f6891.htm) |  |
| 公共方法 | [WriteArbWaveform](5a38a6cb-d0de-5193-a5e0-4075de729e3d.htm) |  |
| 公共方法 | [WriteNamedWaveform](9cb6ec85-00b1-135a-337d-ad0ed81be207.htm) |  |
| 公共方法 | [WriteScript](274bf657-5a90-8e7a-34d5-cee6e5b6d43d.htm) |  |

[Top](#PageHeader)

参见

##### 引用

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


### IFgen_Instr 方法

|  |  |
| --- | --- |
|  | IFgen\_Instr 方法 |

[IFgen\_Instr](38633742-c0b8-a5f5-8b69-2f6127289703.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [AbortGeneration](b3c790e8-546d-9bab-faf1-8105d98be364.htm) |  |
| 公共方法 | [AdjustRelativeDelay](ff237758-918f-615e-2651-f9639f1c16b0.htm) |  |
| 公共方法 | [AllocateArbWaveform](cd5797f1-b85c-0268-eeb2-0d6a3b360da1.htm) |  |
| 公共方法 | [AllocateNamedWaveform](95a6558a-b61c-da5a-d6db-9e4a82b46829.htm) |  |
| 公共方法 | [ClearArbMemory](061a03ef-5d99-172a-c1f4-fb00a3fc7dfe.htm) |  |
| 公共方法 | [ClearArbSequence](2e166fe4-12bc-c42d-e72b-8f7ba1fbe285.htm) |  |
| 公共方法 | [ClearArbWaveform](73bb19ab-712e-322d-c983-89f9c783451e.htm) |  |
| 公共方法 | [ClearFrequencyList](3d994d58-6743-9bc9-0cc9-ff6326e0b973.htm) |  |
| 公共方法 | [ClearUserStandardWaveform](29e514b9-540b-878f-aa8e-510785ec8d2f.htm) |  |
| 公共方法 | [Commit](1fa5f2b5-1c24-8907-73bd-a49621584fe4.htm) |  |
| 公共方法 | [ConfigureArbSequence](1209866a-ba6d-1757-80e8-68249477277a.htm) |  |
| 公共方法 | [ConfigureArbWaveform](23f10a97-03eb-f9c1-397b-104c4a63f5f3.htm) |  |
| 公共方法 | [ConfigureDigitalEdgeTrigger](b8341b9b-981a-6bb7-b1f4-a2db1be8a376.htm) |  |
| 公共方法 | [ConfigureDigitalLevelScriptTrigger](1563e1d6-b67c-a235-a3ee-abc3b084cded.htm) |  |
| 公共方法 | [ConfigureFrequencyList](f6666883-a2d9-cd00-18b6-34be0383a1c9.htm) |  |
| 公共方法 | [ConfigureReferenceClock](b49945d5-b7bd-349e-8a4e-217093bf018a.htm) |  |
| 公共方法 | [ConfigureSampleClock](980c2708-d0e1-0b75-9aad-953d502d45d8.htm) |  |
| 公共方法 | [ConfigureSoftwareEdgeTrigger](8e821489-89ff-aba4-7ca4-df35a78e03ef.htm) |  |
| 公共方法 | [ConfigureStandardWavaform](c923bfb6-7963-7ff1-38dc-7085c07d93da.htm) |  |
| 公共方法 | [CreateArbSequence(Int32, Int32)](d9f0e4da-613b-0bbd-12c9-9d1733e0414a.htm) |  |
| 公共方法 | [CreateArbSequence(Int32, Int32, Int32, Int32)](bb9b5489-6ced-5cad-e996-fd226459441e.htm) |  |
| 公共方法 | [CreateChannelArbWaveform](1e0063ad-66c9-0278-e5d6-35a8f1716e42.htm) |  |
| 公共方法 | [CreateChannelArbWaveformFromFile](6a76271f-54a5-d39b-1a8f-5b01c7c04b77.htm) |  |
| 公共方法 | [CreateFrequencyList](4432e709-71cc-7f79-de88-8e9a9ffc0339.htm) |  |
| 公共方法 | [DefineUsetStandardWaveform](9261a42b-c9b4-9d99-cfbc-7c0e6ea10c24.htm) |  |
| 公共方法 | [DeleteNamedWaveform](22bbd442-733b-a0fa-6227-4fa8d9c96efd.htm) |  |
| 公共方法 | [DeleteScript](5d7fce7a-b3b6-684a-a6c2-b3b8c6ba9686.htm) |  |
| 公共方法 | [DisableTrigger](b596ef0c-0bbc-ddce-02bd-4378611025d2.htm) |  |
| 公共方法 | [EnableAnalogFilter](31150b3f-ac06-3434-8eb5-e9b556dbd0a5.htm) |  |
| 公共方法 | [ExportSignal](80ae64f3-925a-1e5e-81f9-bf333a83d6dc.htm) |  |
| 公共方法 | [GetAmplitude](eb954ae4-5827-bc10-7edc-08aa0a9f4229.htm) |  |
| 公共方法 | [GetAnalogFilterEnabled](d217df99-21e7-e50d-c81b-d38c855d64fa.htm) |  |
| 公共方法 | [GetAnalogPath](c57b673d-4b69-e782-ce0f-123785199e65.htm) |  |
| 公共方法 | [GetArbGain](eb6e7e53-d43a-26e0-6cf5-f3c7f0f20d91.htm) |  |
| 公共方法 | [GetArbOffset](555ffeb8-cce3-98a2-2386-820322eacfb7.htm) |  |
| 公共方法 | [GetArbSampleRate](45fbf2e8-81aa-219c-5b40-8201b95f1538.htm) |  |
| 公共方法 | [GetArbSequenceHandle](8a6de733-da32-97e2-913c-03591dc9ed78.htm) |  |
| 公共方法 | [GetArbSequenceMaxLength](d4923faa-039e-424b-1e4b-9ed5319bb909.htm) |  |
| 公共方法 | [GetArbSequenceMaxLoopCount](71efb6ca-9b3f-28c1-a47b-1fca3ce02ca4.htm) |  |
| 公共方法 | [GetArbSequenceMinLength](595ef153-9b4e-104a-9afc-e63970a2fee4.htm) |  |
| 公共方法 | [GetArbSequencesMaxNumber](f1004a3c-6a3f-cb40-3b41-6f0be328caad.htm) |  |
| 公共方法 | [GetArbWaveformHandle](5dbc361b-66f7-77d9-fd2c-970acb9f0e41.htm) |  |
| 公共方法 | [GetArbWaveformMarkerPosition](90d5ea4f-3d68-a06d-fd62-5fe8661f7b55.htm) |  |
| 公共方法 | [GetArbWaveformMaxSize](3b2353c2-86f1-4f4a-d915-16aefb256815.htm) |  |
| 公共方法 | [GetArbWaveformMinSize](461b62a9-d68f-4d40-8b4b-018abf2262da.htm) |  |
| 公共方法 | [GetArbWaveformQuantum](70265fe8-4b53-8e94-2b85-7b818eb84740.htm) |  |
| 公共方法 | [GetArbWaveformRepeatCount](266225cb-5bac-ada5-2883-e6f817aa45d9.htm) |  |
| 公共方法 | [GetArbWaveformsMaxNumber](4e1a37c9-8789-ce76-aba1-387da0c844c4.htm) |  |
| 公共方法 | [GetAttributeT](c85edfd7-7701-96a8-9768-34bdfd9301cf.htm) |  |
| 公共方法 | [GetChannelDelay](59130d9c-3aba-032a-fab6-ca4503596c22.htm) |  |
| 公共方法 | [GetCommonModeOffset](68916e81-4531-ad14-4cbc-dc7920f4fd19.htm) |  |
| 公共方法 | [GetDCOffset](7d898f8f-a485-ec13-1300-774b84e10158.htm) |  |
| 公共方法 | [GetDigitalFilterEnabled](cb462402-1ead-aa08-9de3-d6dca8e9e85d.htm) |  |
| 公共方法 | [GetDigitalFilterInterpolationFactor](9df33939-e484-d59c-2650-3dd95b79d929.htm) |  |
| 公共方法 | [GetDigitalGain](c777e26c-38c1-b55d-2e7d-5f06453c937b.htm) |  |
| 公共方法 | [GetDigitalPatternEnabled](e597b4f1-e0bd-3acf-bb89-498a34d716ce.htm) |  |
| 公共方法 | [GetDutyCycleHigh](9a1a36d4-f9ff-acf5-23bb-f71ee47d2570.htm) |  |
| 公共方法 | [GetExternalMultiplier](c28a9dc8-47ab-8a00-1ad0-b996958db3e1.htm) |  |
| 公共方法 | [GetFlatnessCorrectionEnabled](2352ee41-bc41-9168-e90f-f7ffc288ff58.htm) |  |
| 公共方法 | [GetFrequency](462562e7-f39f-7c0d-9e5b-ff7e02c3e94e.htm) |  |
| 公共方法 | [GetFrequencyListDurationQuantum](a035583c-0ff9-2300-0381-efe9aad83c41.htm) |  |
| 公共方法 | [GetFrequencyListHandle](939cef94-3d88-fc27-4c24-1ca5d53b25fa.htm) |  |
| 公共方法 | [GetFrequencyListMaxDuratinon](094a044b-21d8-9554-15f8-32d5e5217ceb.htm) |  |
| 公共方法 | [GetFrequencyListMaxLength](f8515f4b-d7d6-7715-dd43-e5758d06d473.htm) |  |
| 公共方法 | [GetFrequencyListMaxNumber](ede723c6-c4a8-c527-fba1-d2156a61095b.htm) |  |
| 公共方法 | [GetFrequencyListMinDuration](01275973-fd8d-d7aa-aba4-a388095fecd5.htm) |  |
| 公共方法 | [GetFrequencyListMinLength](8147815a-e680-04c8-d7c2-63ac9d6d86b0.htm) |  |
| 公共方法 | [GetHardwareState](1947d4db-eb42-8130-ac0b-5079549e0681.htm) |  |
| 公共方法 | [GetIdleValue](206acb95-1555-e743-ae1f-d52d890f1b12.htm) |  |
| 公共方法 | [GetLoadImpedance](3884f312-ab59-9596-39e4-c7500b4903c1.htm) |  |
| 公共方法 | [GetOutputEnabled](00869841-6c5a-8b65-e559-c47893203969.htm) |  |
| 公共方法 | [GetOutputIdleBehavior](e851fc52-904d-a825-4607-f26c32548c54.htm) |  |
| 公共方法 | [GetOutputImpedance](878c6f42-aa6b-3b6a-e318-8c6bf730dd05.htm) |  |
| 公共方法 | [GetOutputMode](66302839-5787-1087-602e-2bbd4cf39282.htm) |  |
| 公共方法 | [GetOutputWaitBehavior](aede2049-bca0-e4fe-7c54-800560362547.htm) |  |
| 公共方法 | [GetReferenceClockFrequency](02aa7ecb-df88-b402-d4c5-a840c277db58.htm) |  |
| 公共方法 | [GetReferenceClockSource](80f1a840-0573-9e3e-c8df-10b9fc54ec04.htm) |  |
| 公共方法 | [GetSampleClockAbsoluteDelay](1531f763-c591-a158-669a-fa7bb46c40f9.htm) |  |
| 公共方法 | [GetSampleClockExportedDivisor](5b7ea29c-ccbe-c4bb-6d46-631eccb9929c.htm) |  |
| 公共方法 | [GetSampleClockMode](de82d324-f9c0-efce-f0d9-9242264a9367.htm) |  |
| 公共方法 | [GetSampleClockRate](f16c125c-4505-a853-42b5-1d1cbfc6984c.htm) |  |
| 公共方法 | [GetSampleClockSource](b9dd084a-cfdf-544e-a5db-0f573f7d4215.htm) |  |
| 公共方法 | [GetSampleClockTimebaseExportedDivisor](554776e9-466e-8e0a-1f92-9294a5ee92d7.htm) |  |
| 公共方法 | [GetSampleClockTimebaseRate](afac6a4f-02bd-db7c-8680-d9067088fa0e.htm) |  |
| 公共方法 | [GetSampleClockTimebaseSource](e1292cbb-8385-5b69-fc35-d7165d88a7dd.htm) |  |
| 公共方法 | [GetScriptToGenerate](cc9e754b-93ec-fa90-9ede-b8c6b2f675f3.htm) |  |
| 公共方法 | [GetStartPhase](418707b2-a45f-2943-d162-a6757385256d.htm) |  |
| 公共方法 | [GetTerminalConfiguration](03956560-9a1e-e998-5779-1fd78f03e427.htm) |  |
| 公共方法 | [GetTriggerMode](f95cd92b-974a-7729-e799-51f728d8a1b7.htm) |  |
| 公共方法 | [GetTriggerType](d3d42432-23b1-aad7-dbc1-0f56cd07059e.htm) |  |
| 公共方法 | [GetWaitValue](65b907b8-b126-230c-1730-e85e8f50ea85.htm) |  |
| 公共方法 | [GetWaveformFuntion](6d017609-4c2b-e075-1c15-46aad3f087c3.htm) |  |
| 公共方法 | [InitiateGeneration](3403c117-d0a1-a8e8-ae54-f04496a1cff6.htm) |  |
| 公共方法 | [IsGenerationDone](e5181e05-d38b-042b-bb7b-ad1782f1c682.htm) |  |
| 公共方法 | [Reset](5b5a8dc3-eab6-66ff-2aaf-32511126c77b.htm) |  |
| 公共方法 | [SendSoftwareEdgeTrigger](5a45cb10-dbea-cb93-9f68-5d2cdc31b348.htm) |  |
| 公共方法 | [SetAmplitude](3cdda3c0-101f-2823-779e-5fe54b608576.htm) |  |
| 公共方法 | [SetAnalogFilterEnabled](27de589c-9a94-6487-afe3-01e2a93916a8.htm) |  |
| 公共方法 | [SetAnalogPath](756c305e-9084-36f2-611c-91d38fdae1e9.htm) |  |
| 公共方法 | [SetArbGain](75f44e12-ba36-6892-de8b-b9561a54a659.htm) |  |
| 公共方法 | [SetArbOffset](ae75ef25-0f7c-3fb5-4f5d-73a980ad16af.htm) |  |
| 公共方法 | [SetArbSampleRate](07f51869-cd55-2e70-d3ac-c8a95241e99c.htm) |  |
| 公共方法 | [SetArbSequenceHandle](0a2a82eb-179a-8bba-799b-520ca2bd76e0.htm) |  |
| 公共方法 | [SetArbWaveformHandle](03943aae-e1af-0a13-7826-8821df72ee82.htm) |  |
| 公共方法 | [SetArbWaveformMarkerPosition](a34b425e-de09-a47b-185a-f840df3d395e.htm) |  |
| 公共方法 | [SetArbWaveformRepeatCount](a6575288-4f21-9fc0-acb9-b2dffbcc9747.htm) |  |
| 公共方法 | [SetAttribute](8260fab1-b4da-d5ac-4653-a1a8518167c3.htm) |  |
| 公共方法 | [SetChannelDelay](bec97166-146c-ae0f-a31d-cb439f90c1e6.htm) |  |
| 公共方法 | [SetCommonModeOffset](f8cbdf7b-3526-b5fb-a46d-baf9b9f99a2c.htm) |  |
| 公共方法 | [SetDCOffset](4ebf0e9b-dfb9-9b83-6e2c-8d9e9e8ffc65.htm) |  |
| 公共方法 | [SetDigitalFilterEnabled](5db8f55e-9893-183d-0538-8d4ae9b5f34c.htm) |  |
| 公共方法 | [SetDigitalFilterInterpolationFactor](c2b25fdf-91ab-2de6-488b-4d009f6eb9a4.htm) |  |
| 公共方法 | [SetDigitalGain](bd9d2086-3720-2bb9-a7d3-248aa02be185.htm) |  |
| 公共方法 | [SetDigitalPatternEnabled](f8cd8ac8-23b2-80f3-9b5a-90dde9ceadca.htm) |  |
| 公共方法 | [SetDutyCycleHigh](1ec1d83a-b2aa-9b4c-0739-143197ab955d.htm) |  |
| 公共方法 | [SetExternalMultiplier](c6f96053-a278-345e-d2e9-59929b79a994.htm) |  |
| 公共方法 | [SetFlatnessCorrectionEnabled](44088be8-4789-07fe-9860-3bc889986884.htm) |  |
| 公共方法 | [SetFrequency](480e6bad-2fdc-e6d0-e9d4-7a0fa770583d.htm) |  |
| 公共方法 | [SetFrequencyListHandle](727f9aa5-ebd6-15b6-a162-28546fa7082e.htm) |  |
| 公共方法 | [SetIdleValue](5ba87583-a22a-5fb1-18ee-d744385049c2.htm) |  |
| 公共方法 | [SetLoadImpedance](53a615e1-8181-9778-5919-3830c7da0601.htm) |  |
| 公共方法 | [SetNextWritePosition](1edc83a8-2beb-e90c-9470-54ba2fda94b6.htm) |  |
| 公共方法 | [SetOutputEnabled](b025c0a4-57c3-7740-7cd2-2cfe68d2d8e3.htm) |  |
| 公共方法 | [SetOutputIdleBehavior](0917759c-fa46-34e1-568c-bc7869f4d259.htm) |  |
| 公共方法 | [SetOutputImpedance](5a28a32a-6238-7883-40f7-75025fd4af24.htm) |  |
| 公共方法 | [SetOutputMode](dcfca3ac-8bce-36fa-23cd-18e043b9d5a9.htm) |  |
| 公共方法 | [SetOutputWaitBehavior](e069cd48-04dd-a496-bc25-9ed0caa01213.htm) |  |
| 公共方法 | [SetReferenceClockFrequency](197f160f-e2e3-850c-5c46-ccb2c87279f2.htm) |  |
| 公共方法 | [SetReferenceClockSource](dedf13dd-4416-2a6b-e467-5d646cd513e0.htm) |  |
| 公共方法 | [SetSampleClockAbsoluteDelay](94641598-348a-2ef3-f51c-ab0f566894f9.htm) |  |
| 公共方法 | [SetSampleClockExportedDivisor](d20cdb5f-480f-abf5-62e6-5d0313978aad.htm) |  |
| 公共方法 | [SetSampleClockMode](22216978-0566-2beb-fd3b-fd38d705fc2e.htm) |  |
| 公共方法 | [SetSampleClockRate](dc607ccd-b76d-9cc1-0643-f4f6b231a341.htm) |  |
| 公共方法 | [SetSampleClockSource](5dfacae0-9fb2-9b5d-28fe-2bd056e8e650.htm) |  |
| 公共方法 | [SetSampleClockTimebaseExportedDivisor](543fdb68-5f27-7310-9c7a-1c37546f2764.htm) |  |
| 公共方法 | [SetSampleClockTimebaseRate](afff7ed1-fcde-afe4-18cd-4a8be4d8cb04.htm) |  |
| 公共方法 | [SetSampleClockTimebaseSource](f1e24b74-d548-e6ad-ce2c-3edbf0ce2dae.htm) |  |
| 公共方法 | [SetScriptToGenerate](93e4631e-c521-6712-8b07-e99e2d1c718c.htm) |  |
| 公共方法 | [SetStartPhase](d534a914-6798-70b7-eeba-29fe684e2b54.htm) |  |
| 公共方法 | [SetTerminalConfiguration](7e16deb3-448c-b0d6-ef96-2db5bd877dcc.htm) |  |
| 公共方法 | [SetTriggerMode](253aa1d5-15d0-086c-69eb-83ecb3878614.htm) |  |
| 公共方法 | [SetTriggerType](fd3f25da-9b36-3350-0eef-3a40d7cb9722.htm) |  |
| 公共方法 | [SetWaitValue](729068d8-71b5-db27-2d7c-75d0ca2e74ba.htm) |  |
| 公共方法 | [SetWaveformFunction](cde4e50c-1220-8ea0-da92-8ef11c7e602c.htm) |  |
| 公共方法 | [WaitUntilDone](c0f8f4ce-4c4a-fc5e-3aab-467c4a4f6891.htm) |  |
| 公共方法 | [WriteArbWaveform](5a38a6cb-d0de-5193-a5e0-4075de729e3d.htm) |  |
| 公共方法 | [WriteNamedWaveform](9cb6ec85-00b1-135a-337d-ad0ed81be207.htm) |  |
| 公共方法 | [WriteScript](274bf657-5a90-8e7a-34d5-cee6e5b6d43d.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### AbortGeneration 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrAbortGeneration 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void AbortGeneration()
```

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### AdjustRelativeDelay 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrAdjustRelativeDelay 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void AdjustRelativeDelay(
	double time
)
```

###### 参数

time  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### AllocateArbWaveform 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrAllocateArbWaveform 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int AllocateArbWaveform(
	string channelNumber,
	int numberOfSamples
)
```

###### 参数

channelNumber  String

numberOfSamples  Int32

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### AllocateNamedWaveform 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrAllocateNamedWaveform 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void AllocateNamedWaveform(
	string channelNumber,
	string waveformName,
	int numberOfSamples
)
```

###### 参数

channelNumber  String

waveformName  String

numberOfSamples  Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ClearArbMemory 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrClearArbMemory 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ClearArbMemory()
```

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ClearArbSequence 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrClearArbSequence 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ClearArbSequence(
	int handle
)
```

###### 参数

handle  Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ClearArbWaveform 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrClearArbWaveform 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ClearArbWaveform(
	int handle
)
```

###### 参数

handle  Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ClearFrequencyList 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrClearFrequencyList 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ClearFrequencyList(
	int handle
)
```

###### 参数

handle  Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ClearUserStandardWaveform 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrClearUserStandardWaveform 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ClearUserStandardWaveform(
	string channelNumber
)
```

###### 参数

channelNumber  String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### Commit 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrCommit 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Commit()
```

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ConfigureArbSequence 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrConfigureArbSequence 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureArbSequence(
	string channelNumber,
	int handle,
	double gain,
	double offset
)
```

###### 参数

channelNumber  String

handle  Int32

gain  Double

offset  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ConfigureArbWaveform 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrConfigureArbWaveform 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureArbWaveform(
	string channelNumber,
	int handle,
	double gain,
	double offset
)
```

###### 参数

channelNumber  String

handle  Int32

gain  Double

offset  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ConfigureDigitalEdgeTrigger 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrConfigureDigitalEdgeTrigger 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureDigitalEdgeTrigger(
	string triggerClass,
	string triggerId,
	string source,
	string edge
)
```

###### 参数

triggerClass  String

triggerId  String

source  String

edge  String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ConfigureDigitalLevelScriptTrigger 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrConfigureDigitalLevelScriptTrigger 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureDigitalLevelScriptTrigger(
	string triggerId,
	string source,
	string activeLevel
)
```

###### 参数

triggerId  String

source  String

activeLevel  String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ConfigureFrequencyList 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrConfigureFrequencyList 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureFrequencyList(
	string channelNumber,
	int handle,
	double amplitude,
	double dcOffset,
	double startPhase
)
```

###### 参数

channelNumber  String

handle  Int32

amplitude  Double

dcOffset  Double

startPhase  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ConfigureReferenceClock 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrConfigureReferenceClock 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureReferenceClock(
	string source,
	double frequency
)
```

###### 参数

source  String

frequency  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ConfigureSampleClock 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrConfigureSampleClock 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureSampleClock(
	string source,
	double rate,
	int? samplesPerChannel = null
)
```

###### 参数

source  String

rate  Double

samplesPerChannel  NullableInt32  (Optional)

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ConfigureSoftwareEdgeTrigger 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrConfigureSoftwareEdgeTrigger 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureSoftwareEdgeTrigger(
	string triggerClass,
	string triggerId
)
```

###### 参数

triggerClass  String

triggerId  String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ConfigureStandardWavaform 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrConfigureStandardWavaform 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureStandardWavaform(
	string channelNumber,
	string waveformFunction,
	double amplitude,
	double dcOffset,
	double frequency,
	double startPhase
)
```

###### 参数

channelNumber  String

waveformFunction  String

amplitude  Double

dcOffset  Double

frequency  Double

startPhase  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### CreateArbSequence 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrCreateArbSequence 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [CreateArbSequence(Int32, Int32)](d9f0e4da-613b-0bbd-12c9-9d1733e0414a.htm) |  |
| 公共方法 | [CreateArbSequence(Int32, Int32, Int32, Int32)](bb9b5489-6ced-5cad-e996-fd226459441e.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


##### CreateArbSequence(Int32[], Int32[]) 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrCreateArbSequence(Int32, Int32) 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int CreateArbSequence(
	int[] waveformHandle,
	int[] loopCount
)
```

###### 参数

waveformHandle  Int32

loopCount  Int32

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[CreateArbSequence 重载](acb973da-1bf8-3d94-134b-ea1a25e4bf16.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


##### CreateArbSequence(Int32[], Int32[], Int32[], Int32[]) 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrCreateArbSequence(Int32, Int32, Int32, Int32) 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int CreateArbSequence(
	int[] waveformHandle,
	int[] loopCount,
	int[] sampleCounts,
	int[] markers
)
```

###### 参数

waveformHandle  Int32

loopCount  Int32

sampleCounts  Int32

markers  Int32

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[CreateArbSequence 重载](acb973da-1bf8-3d94-134b-ea1a25e4bf16.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### CreateChannelArbWaveform 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrCreateChannelArbWaveform 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int CreateChannelArbWaveform(
	string channelNumber,
	double[] waveform
)
```

###### 参数

channelNumber  String

waveform  Double

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### CreateChannelArbWaveformFromFile 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrCreateChannelArbWaveformFromFile 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int CreateChannelArbWaveformFromFile(
	string channelNumber,
	string filePath,
	string byteOrder
)
```

###### 参数

channelNumber  String

filePath  String

byteOrder  String

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### CreateFrequencyList 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrCreateFrequencyList 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int CreateFrequencyList(
	string waveform,
	double[] frequencies,
	double[] durations
)
```

###### 参数

waveform  String

frequencies  Double

durations  Double

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### DefineUsetStandardWaveform 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrDefineUsetStandardWaveform 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void DefineUsetStandardWaveform(
	string channelNumber,
	double[] data
)
```

###### 参数

channelNumber  String

data  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### DeleteNamedWaveform 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrDeleteNamedWaveform 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void DeleteNamedWaveform(
	string channelNumber,
	string waveformName
)
```

###### 参数

channelNumber  String

waveformName  String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### DeleteScript 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrDeleteScript 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void DeleteScript(
	string channelNumber,
	string scriptName
)
```

###### 参数

channelNumber  String

scriptName  String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### DisableTrigger 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrDisableTrigger 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void DisableTrigger(
	string triggerClass,
	string triggerId
)
```

###### 参数

triggerClass  String

triggerId  String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### EnableAnalogFilter 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrEnableAnalogFilter 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void EnableAnalogFilter(
	string channelNumber,
	double filterCorrectionFrequency
)
```

###### 参数

channelNumber  String

filterCorrectionFrequency  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### ExportSignal 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrExportSignal 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ExportSignal(
	string signalSource,
	string signalIdentifier,
	string outputTermianl
)
```

###### 参数

signalSource  String

signalIdentifier  String

outputTermianl  String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetAmplitude 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetAmplitude 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetAmplitude(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetAnalogFilterEnabled 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetAnalogFilterEnabled 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool GetAnalogFilterEnabled(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Boolean

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetAnalogPath 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetAnalogPath 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetAnalogPath(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbGain 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetArbGain 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetArbGain(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbOffset 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetArbOffset 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetArbOffset(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbSampleRate 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetArbSampleRate 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetArbSampleRate()
```

###### 返回值

Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbSequenceHandle 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetArbSequenceHandle 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetArbSequenceHandle(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbSequenceMaxLength 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetArbSequenceMaxLength 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetArbSequenceMaxLength()
```

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbSequenceMaxLoopCount 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetArbSequenceMaxLoopCount 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetArbSequenceMaxLoopCount()
```

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbSequenceMinLength 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetArbSequenceMinLength 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetArbSequenceMinLength()
```

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbSequencesMaxNumber 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetArbSequencesMaxNumber 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetArbSequencesMaxNumber()
```

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbWaveformHandle 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetArbWaveformHandle 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetArbWaveformHandle(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbWaveformMarkerPosition 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetArbWaveformMarkerPosition 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetArbWaveformMarkerPosition()
```

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbWaveformMaxSize 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetArbWaveformMaxSize 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
long GetArbWaveformMaxSize()
```

###### 返回值

Int64

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbWaveformMinSize 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetArbWaveformMinSize 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
long GetArbWaveformMinSize()
```

###### 返回值

Int64

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbWaveformQuantum 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetArbWaveformQuantum 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetArbWaveformQuantum()
```

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbWaveformRepeatCount 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetArbWaveformRepeatCount 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetArbWaveformRepeatCount()
```

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetArbWaveformsMaxNumber 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetArbWaveformsMaxNumber 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetArbWaveformsMaxNumber()
```

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetAttribute&lt;T&gt; 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetAttributeT 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

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

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetChannelDelay 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetChannelDelay 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetChannelDelay(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetCommonModeOffset 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetCommonModeOffset 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetCommonModeOffset(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetDCOffset 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetDCOffset 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetDCOffset(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetDigitalFilterEnabled 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetDigitalFilterEnabled 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool GetDigitalFilterEnabled(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Boolean

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetDigitalFilterInterpolationFactor 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetDigitalFilterInterpolationFactor 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetDigitalFilterInterpolationFactor(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetDigitalGain 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetDigitalGain 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetDigitalGain(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetDigitalPatternEnabled 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetDigitalPatternEnabled 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool GetDigitalPatternEnabled(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Boolean

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetDutyCycleHigh 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetDutyCycleHigh 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetDutyCycleHigh(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetExternalMultiplier 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetExternalMultiplier 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetExternalMultiplier()
```

###### 返回值

Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetFlatnessCorrectionEnabled 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetFlatnessCorrectionEnabled 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool GetFlatnessCorrectionEnabled(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Boolean

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetFrequency 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetFrequency 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetFrequency(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetFrequencyListDurationQuantum 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetFrequencyListDurationQuantum 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetFrequencyListDurationQuantum()
```

###### 返回值

Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetFrequencyListHandle 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetFrequencyListHandle 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetFrequencyListHandle()
```

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetFrequencyListMaxDuratinon 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetFrequencyListMaxDuratinon 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetFrequencyListMaxDuratinon(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetFrequencyListMaxLength 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetFrequencyListMaxLength 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetFrequencyListMaxLength(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetFrequencyListMaxNumber 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetFrequencyListMaxNumber 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetFrequencyListMaxNumber()
```

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetFrequencyListMinDuration 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetFrequencyListMinDuration 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetFrequencyListMinDuration(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetFrequencyListMinLength 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetFrequencyListMinLength 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetFrequencyListMinLength(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetHardwareState 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetHardwareState 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetHardwareState()
```

###### 返回值

String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetIdleValue 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetIdleValue 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetIdleValue(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetLoadImpedance 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetLoadImpedance 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetLoadImpedance(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetOutputEnabled 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetOutputEnabled 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

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

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetOutputIdleBehavior 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetOutputIdleBehavior 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetOutputIdleBehavior()
```

###### 返回值

String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetOutputImpedance 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetOutputImpedance 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetOutputImpedance(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetOutputMode 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetOutputMode 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetOutputMode()
```

###### 返回值

String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetOutputWaitBehavior 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetOutputWaitBehavior 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetOutputWaitBehavior()
```

###### 返回值

String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetReferenceClockFrequency 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetReferenceClockFrequency 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetReferenceClockFrequency()
```

###### 返回值

Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetReferenceClockSource 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetReferenceClockSource 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetReferenceClockSource()
```

###### 返回值

String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetSampleClockAbsoluteDelay 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetSampleClockAbsoluteDelay 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetSampleClockAbsoluteDelay()
```

###### 返回值

Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetSampleClockExportedDivisor 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetSampleClockExportedDivisor 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetSampleClockExportedDivisor()
```

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetSampleClockMode 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetSampleClockMode 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetSampleClockMode()
```

###### 返回值

String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetSampleClockRate 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetSampleClockRate 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetSampleClockRate()
```

###### 返回值

Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetSampleClockSource 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetSampleClockSource 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetSampleClockSource()
```

###### 返回值

String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetSampleClockTimebaseExportedDivisor 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetSampleClockTimebaseExportedDivisor 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetSampleClockTimebaseExportedDivisor()
```

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetSampleClockTimebaseRate 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetSampleClockTimebaseRate 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetSampleClockTimebaseRate()
```

###### 返回值

Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetSampleClockTimebaseSource 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetSampleClockTimebaseSource 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetSampleClockTimebaseSource()
```

###### 返回值

String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetScriptToGenerate 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetScriptToGenerate 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetScriptToGenerate()
```

###### 返回值

String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetStartPhase 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetStartPhase 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetStartPhase(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetTerminalConfiguration 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetTerminalConfiguration 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetTerminalConfiguration(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetTriggerMode 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetTriggerMode 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetTriggerMode(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetTriggerType 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetTriggerType 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetTriggerType(
	string triggerClass,
	string triggerId
)
```

###### 参数

triggerClass  String

triggerId  String

###### 返回值

String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetWaitValue 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetWaitValue 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetWaitValue(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### GetWaveformFuntion 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrGetWaveformFuntion 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetWaveformFuntion(
	string channelNumber
)
```

###### 参数

channelNumber  String

###### 返回值

String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### InitiateGeneration 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrInitiateGeneration 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void InitiateGeneration()
```

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### IsGenerationDone 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrIsGenerationDone 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool IsGenerationDone()
```

###### 返回值

Boolean

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### Reset 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrReset 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Reset()
```

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SendSoftwareEdgeTrigger 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSendSoftwareEdgeTrigger 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SendSoftwareEdgeTrigger(
	string triggeClass,
	string triggerId
)
```

###### 参数

triggeClass  String

triggerId  String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetAmplitude 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetAmplitude 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetAmplitude(
	string channelNumber,
	double amplitude
)
```

###### 参数

channelNumber  String

amplitude  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetAnalogFilterEnabled 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetAnalogFilterEnabled 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetAnalogFilterEnabled(
	string channelNumber,
	bool enabled
)
```

###### 参数

channelNumber  String

enabled  Boolean

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetAnalogPath 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetAnalogPath 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetAnalogPath(
	string channelNumber,
	string analogPath
)
```

###### 参数

channelNumber  String

analogPath  String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetArbGain 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetArbGain 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetArbGain(
	string channelNumber,
	double gain
)
```

###### 参数

channelNumber  String

gain  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetArbOffset 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetArbOffset 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetArbOffset(
	string channelNumber,
	double offset
)
```

###### 参数

channelNumber  String

offset  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetArbSampleRate 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetArbSampleRate 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetArbSampleRate(
	double sampleRate
)
```

###### 参数

sampleRate  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetArbSequenceHandle 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetArbSequenceHandle 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetArbSequenceHandle(
	string channelNumber,
	int handle
)
```

###### 参数

channelNumber  String

handle  Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetArbWaveformHandle 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetArbWaveformHandle 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetArbWaveformHandle(
	string channelNumber,
	int handle
)
```

###### 参数

channelNumber  String

handle  Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetArbWaveformMarkerPosition 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetArbWaveformMarkerPosition 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetArbWaveformMarkerPosition(
	int position
)
```

###### 参数

position  Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetArbWaveformRepeatCount 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetArbWaveformRepeatCount 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetArbWaveformRepeatCount(
	int count
)
```

###### 参数

count  Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetAttribute 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetAttribute 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

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

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetChannelDelay 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetChannelDelay 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetChannelDelay(
	string channelNumber,
	double channelDelay
)
```

###### 参数

channelNumber  String

channelDelay  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetCommonModeOffset 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetCommonModeOffset 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetCommonModeOffset(
	string channelNumber,
	double commonModeOffset
)
```

###### 参数

channelNumber  String

commonModeOffset  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetDCOffset 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetDCOffset 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetDCOffset(
	string channelNumber,
	double dcOffset
)
```

###### 参数

channelNumber  String

dcOffset  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetDigitalFilterEnabled 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetDigitalFilterEnabled 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetDigitalFilterEnabled(
	string channelNumber,
	bool enabled
)
```

###### 参数

channelNumber  String

enabled  Boolean

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetDigitalFilterInterpolationFactor 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetDigitalFilterInterpolationFactor 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetDigitalFilterInterpolationFactor(
	string channelNumber,
	double interpolationFactor
)
```

###### 参数

channelNumber  String

interpolationFactor  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetDigitalGain 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetDigitalGain 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetDigitalGain(
	string channelNumber,
	double digitalGain
)
```

###### 参数

channelNumber  String

digitalGain  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetDigitalPatternEnabled 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetDigitalPatternEnabled 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetDigitalPatternEnabled(
	string channelNumber,
	bool enabled
)
```

###### 参数

channelNumber  String

enabled  Boolean

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetDutyCycleHigh 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetDutyCycleHigh 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetDutyCycleHigh(
	string channelNumber,
	double dutyCycleHigh
)
```

###### 参数

channelNumber  String

dutyCycleHigh  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetExternalMultiplier 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetExternalMultiplier 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetExternalMultiplier(
	double factor
)
```

###### 参数

factor  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetFlatnessCorrectionEnabled 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetFlatnessCorrectionEnabled 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetFlatnessCorrectionEnabled(
	string channelNumber,
	bool enabled
)
```

###### 参数

channelNumber  String

enabled  Boolean

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetFrequency 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetFrequency 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetFrequency(
	string channelNumber,
	double frequency
)
```

###### 参数

channelNumber  String

frequency  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetFrequencyListHandle 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetFrequencyListHandle 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetFrequencyListHandle(
	int handle
)
```

###### 参数

handle  Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetIdleValue 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetIdleValue 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetIdleValue(
	string channelNumber,
	int idleValue
)
```

###### 参数

channelNumber  String

idleValue  Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetLoadImpedance 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetLoadImpedance 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetLoadImpedance(
	string channelNumber,
	double impedance
)
```

###### 参数

channelNumber  String

impedance  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetNextWritePosition 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetNextWritePosition 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetNextWritePosition(
	string channelNumber,
	string waveformName,
	string relativeTo,
	int offset
)
```

###### 参数

channelNumber  String

waveformName  String

relativeTo  String

offset  Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetOutputEnabled 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetOutputEnabled 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

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

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetOutputIdleBehavior 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetOutputIdleBehavior 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetOutputIdleBehavior(
	string behavior
)
```

###### 参数

behavior  String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetOutputImpedance 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetOutputImpedance 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetOutputImpedance(
	string channelNumber,
	double impedance
)
```

###### 参数

channelNumber  String

impedance  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetOutputMode 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetOutputMode 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetOutputMode(
	string mode
)
```

###### 参数

mode  String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetOutputWaitBehavior 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetOutputWaitBehavior 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetOutputWaitBehavior(
	string behavior
)
```

###### 参数

behavior  String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetReferenceClockFrequency 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetReferenceClockFrequency 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetReferenceClockFrequency(
	double frequency
)
```

###### 参数

frequency  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetReferenceClockSource 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetReferenceClockSource 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetReferenceClockSource(
	string clockSource
)
```

###### 参数

clockSource  String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetSampleClockAbsoluteDelay 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetSampleClockAbsoluteDelay 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSampleClockAbsoluteDelay(
	double delay
)
```

###### 参数

delay  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetSampleClockExportedDivisor 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetSampleClockExportedDivisor 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSampleClockExportedDivisor(
	int factor
)
```

###### 参数

factor  Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetSampleClockMode 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetSampleClockMode 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSampleClockMode(
	string mode
)
```

###### 参数

mode  String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetSampleClockRate 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetSampleClockRate 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSampleClockRate(
	double rate
)
```

###### 参数

rate  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetSampleClockSource 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetSampleClockSource 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSampleClockSource(
	string source
)
```

###### 参数

source  String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetSampleClockTimebaseExportedDivisor 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetSampleClockTimebaseExportedDivisor 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSampleClockTimebaseExportedDivisor(
	int factor
)
```

###### 参数

factor  Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetSampleClockTimebaseRate 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetSampleClockTimebaseRate 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSampleClockTimebaseRate(
	double rate
)
```

###### 参数

rate  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetSampleClockTimebaseSource 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetSampleClockTimebaseSource 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSampleClockTimebaseSource(
	string source
)
```

###### 参数

source  String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetScriptToGenerate 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetScriptToGenerate 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetScriptToGenerate(
	string scriptName
)
```

###### 参数

scriptName  String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetStartPhase 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetStartPhase 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetStartPhase(
	string channelNumber,
	double startPhase
)
```

###### 参数

channelNumber  String

startPhase  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetTerminalConfiguration 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetTerminalConfiguration 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetTerminalConfiguration(
	string channelNumber,
	string configuration
)
```

###### 参数

channelNumber  String

configuration  String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetTriggerMode 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetTriggerMode 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetTriggerMode(
	string channelNumber,
	string triggerMode
)
```

###### 参数

channelNumber  String

triggerMode  String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetTriggerType 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetTriggerType 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetTriggerType(
	string triggerClass,
	string triggerId,
	string triggerType
)
```

###### 参数

triggerClass  String

triggerId  String

triggerType  String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetWaitValue 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetWaitValue 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetWaitValue(
	string channelNumber,
	int waitValue
)
```

###### 参数

channelNumber  String

waitValue  Int32

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### SetWaveformFunction 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrSetWaveformFunction 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetWaveformFunction(
	string channelNumber,
	string waveformFunction
)
```

###### 参数

channelNumber  String

waveformFunction  String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### WaitUntilDone 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrWaitUntilDone 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WaitUntilDone(
	double maxTime
)
```

###### 参数

maxTime  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### WriteArbWaveform 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrWriteArbWaveform 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteArbWaveform(
	string channelNumber,
	int handle,
	double[] waveform
)
```

###### 参数

channelNumber  String

handle  Int32

waveform  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### WriteNamedWaveform 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrWriteNamedWaveform 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteNamedWaveform(
	string channelNumber,
	string waveformName,
	double[] waveform
)
```

###### 参数

channelNumber  String

waveformName  String

waveform  Double

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)


#### WriteScript 方法

|  |  |
| --- | --- |
|  | IFgen\_InstrWriteScript 方法 |

  
**命名空间：** [FgenParent](6778fded-2bd1-c33f-c614-b82ab82be476.htm)  
**程序集：** FgenMeasStation (在 FgenMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteScript(
	string channelNumber,
	string script
)
```

###### 参数

channelNumber  String

script  String

参见

###### 引用

[IFgen\_Instr 接口](38633742-c0b8-a5f5-8b69-2f6127289703.htm)

[FgenParent 命名空间](6778fded-2bd1-c33f-c614-b82ab82be476.htm)

