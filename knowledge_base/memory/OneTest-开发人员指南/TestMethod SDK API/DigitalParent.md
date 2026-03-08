|  |  |
| --- | --- |
|  | DigitalParent 命名空间 |

类

|  | 类 | 说明 |
| --- | --- | --- |
| 公共类 | [Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm) |  |

接口

|  | 接口 | 说明 |
| --- | --- | --- |
| 公共接口 | [IDigital\_Instr](80776682-5ee7-430a-5608-c219947bae3f.htm) |  |


## Digital 类

|  |  |
| --- | --- |
|  | Digital 类 |

继承层次

SystemObject
  
  MeasStation  
    DigitalParentDigital

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public class Digital : MeasStation
```

Digital 类型公开以下成员。

构造函数

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [Digital](cacb1321-7699-e2d7-e998-f523b10feda0.htm) | 初始化 Digital 类的一个新实例 |

[Top](#PageHeader)

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [AbortBurst](32d8afd7-53dd-fc9d-b694-6f4a4bf01a50.htm) | Stops bursting the pattern. |
| 公共方法 | [AbortClockGenerator](af6955f5-a2b7-8c73-c0ff-d2d6732d303b.htm) | Stops clock generation on the specified channel(s) or pin(s) and pin group(s). |
| 公共方法 | [AbortKeepAlive](772aec94-693f-dc1e-56a3-0da192dde1ed.htm) | Stops the keep alive pattern if it is currently running. If a pattern burst is in progress, this method aborts the pattern burst. If you start a new pattern burst while a keep alive pattern is running, the keep alive pattern runs to the last keep alive vector, and the new pattern burst starts on the next cycle. |
| 公共方法 | [ApplyLevelsAndTiming(String, String)](446e8be1-da3d-4b53-7c9f-30d554790cf3.htm) | Applies digital levels and timing defined in the loaded levels and timing sheets. |
| 公共方法 | [ApplyLevelsAndTiming(String, String, String, String, String)](7b9bde6d-39ac-a0ef-9a05-5426aa4a4d01.htm) | Applies digital levels and timing defined in the loaded levels and timing sheets. |
| 公共方法 | [ApplyTdrOffsets](6c5b156f-ba54-e7bc-e7ed-aff2ffbe1077.htm) | Applies the correction for propagation delay offsets to a digital pattern instrument. |
| 公共方法 | [BurstPattern(String)](6a00d5a5-53d1-7c92-c567-e8556bceed90.htm) | Bursts the pattern on the sites you specify, waits for the burst to complete, and returns comparison results for current site. |
| 公共方法 | [BurstPattern(String, Boolean, Double)](89e23eea-5c46-6273-c333-6f3aed75df49.htm) | Bursts the pattern on the sites you specify, waits for the burst to complete, and returns comparison results for current site. |
| 公共方法 | [BurstPattern(String, Boolean, Boolean, Double)](1bf58a23-7f26-1313-9967-a1cb35bd4ef9.htm) | Bursts the pattern on the site you specify, waits for the burst to complete, and returns comparison results for current site. |
| 公共方法 | [ConfigureActiveLoadLevels](ecf88222-bbfe-efb2-258b-b5e3de3f9fca.htm) | Configures the Ioh, Iol, and Vcom values. The DUT sources or sinks current based on the level values. To enable active load, set the termination mode to ActiveLoad. To disable active load, set the termination mode of the instrument to HighZ or Vterm. These properties are only applicable if the pinset's SelectedFunction is set to Digital and TerminationMode is set to ActiveLoad. |
| 公共方法 | [ConfigureCompareStrobeEdge(String, Double)](b286bb79-e6d1-84d4-38b9-2cf5af248b04.htm) | Configures the strobe edge time for the specified pins. |
| 公共方法 | [ConfigureCompareStrobeEdge(String, Double, Double)](22bf36b4-118b-f056-e4fe-e335669ed9a3.htm) | Configures the strobe edge times for the specified pins. |
| 公共方法 | [ConfigureDigitalEdgeTrigger](8baba7d2-5c73-a9a1-b768-06ec8211da3c.htm) | Configures the TriggerType to DigitalEdge, and configures the source and Edge properties. |
| 公共方法 | [ConfigureDriveEdges](614f4f96-aae6-22d9-a916-82eca07bc0d7.htm) | Configures the drive format and the drive edge placement for the specified pins. |
| 公共方法 | [ConfigureDriveFormat](3ad9f204-f543-a86a-3cf6-fdbd6b6fb442.htm) | Configures the drive format of a time set. |
| 公共方法 | [ConfigureDriverEdges](8f3ebee8-6dd9-368d-9075-e0ef17d28e4d.htm) | Configures the drive format and the drive edge placement for the specified pins. |
| 公共方法 | [ConfigureEdge](e5610029-7d13-1c73-5bfb-55905c814eed.htm) | Configures the edge of a time set. |
| 公共方法 | [ConfigureEdgeMultiplier](63e24596-3d91-099c-bb9f-9176eaaba67c.htm) | Configures the edge multiplier of a time set. |
| 公共方法 | [ConfigureHistoryRamCycleNumberTrigger](245f6339-99e2-cf6c-341f-384714efb69d.htm) | Configures the TriggerType to CycleNumber and configures Number and PretriggerSamples. |
| 公共方法 | [ConfigureHistoryRamFirstFailureTrigger](d84e1110-0b4a-c4ca-5691-e1dc6d058aeb.htm) | Configures the TriggerType to FirstFailure and configures PretriggerSamples. |
| 公共方法 | [ConfigureHistoryRamPatternLabelTrigger](9793d008-acaa-85a4-8358-7fd539568b1f.htm) | Configures the TriggerType to PatternLabel and configures Label, VectorOffset, CycleOffset, and PretriggerSamples. |
| 公共方法 | [ConfigureIClamp](3f1fdfb7-3599-d2bb-adc8-851e3ee95257.htm) | Configure the sourced and sunk current clamp value. |
| 公共方法 | [ConfigureSoftwareTrigger](876990f1-94ad-a0a7-33d4-420d7f5bc374.htm) | Configures the TriggerType for Software triggering. |
| 公共方法 | [ConfigureVClamp](f39ac233-bfdf-19db-45df-b9a6570c9f33.htm) | Configure the maximum and minimum voltage limit. |
| 公共方法 | [ConfigureVoltageLevels](c53628c4-06ec-be92-be9a-2dccc2f275fc.htm) | Configures the high and low logic levels for voltage as well as the termination mode input voltage. These voltages apply to the pin list when the SelectedFunction is Digital. |
| 公共方法 | [CreateCaptureWaveformFromFile](dac55003-b90d-e38d-414f-62d1f0881e66.htm) | Creates a capture waveform using the configuration information from a .digicapture file. |
| 公共方法 | [CreateCaptureWaveformParallel](1e15e50e-3f7e-25d9-98ee-755d0aa94413.htm) | Creates the capture waveform settings for parallel acquisition using a comma-delimited string of pins or channels. |
| 公共方法 | [CreateCaptureWaveformSerial](3a8d22e5-5e67-0786-0568-3968cf7e8600.htm) | Creates the capture waveform settings for serial acquisition using a comma-delimited string of pins or channels. |
| 公共方法 | [CreateChannelMap](b7770175-3d8e-fba1-935f-fd7d67556eda.htm) | Creates a channel map, which translates the pin maps and sites to the instrument channels. You must create the pin map using CreatePinMap() before calling this method. |
| 公共方法 | [CreatePinGroup](7785cda6-7ed5-40b7-bf09-b63f21bd1a40.htm) | Creates a pin group with the specified name. The pin group serves as an alias for a list of pins. |
| 公共方法 | [CreatePinMap](8f109038-9eef-ac15-384c-d75aa50b7a54.htm) | Creates and loads a pin map. Use this method if you are not loading a pin map file using LoadPinMap(). |
| 公共方法 | [CreateSourceWaveformFromFile](99ae6698-cb1c-9e5e-c3e9-92fd06c7e5ed.htm) | Creates the source waveform settings used to source waveforms with configuration information contained in a .tdms file. |
| 公共方法 | [CreateSourceWaveformParallel](0d4f48b7-3386-25e9-99f9-f558303839b5.htm) | Creates source waveform settings used to source parallel data using a comma-delimited string of pins or channels. |
| 公共方法 | [CreateSourceWaveformSerial](9221bb0c-e62d-7816-36e9-bd09fcbc0088.htm) | Creates the source waveform settings used to source serial waveforms using a comma-delimited string of pins or channels. |
| 公共方法 | [CreateTimeSet](cdd750e0-a83d-963c-4807-2e4e4d340deb.htm) | Creates a DigitalTimeSet. Use this method to create time set values after applying a timing sheet with ApplyLevelsAndTiming(), or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to ApplyLevelsAndTiming(), it only affects the values of the current timing context. |
| 公共方法 | [DeleteAllTimeSets](46397e2c-14e3-74ab-560d-12451b0e41f4.htm) | Deletes all loaded and created time sets. |
| 公共方法 | [DisableSites](ef6888bb-eec9-6aa3-7292-ff28b65cb37c.htm) | Disables the specified sites |
| 公共方法 | [DisableTrigger](4a844df7-0bf4-beb7-5d47-4f62b4addc20.htm) | Disables a previously configured trigger and sets TriggerType to None. |
| 公共方法 | [EnableSites](46622cca-be53-2be9-2d0e-8ab1ad924f83.htm) | Enables the specified sites. |
| 公共方法 | [EndChannelMap](66069adf-ffab-55de-f7d7-3b9f23a0bfa1.htm) | Completes the channel map configuration. No further changes can be made to the channel map or connections after calling this method. |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 受保护的方法 | [ExecuteArrayToDictionaryT1, T2](2876e44c-2e79-31b7-2f20-3bc738532d50.htm) | (重写 MeasStation.ExecuteArrayToDictionary``2(MethodDescriptionUMP, UMP, Object)) |
| 受保护的方法 | [ExecuteNoReturnMethodT1, T2](cb817f46-5a3a-4bb3-6e44-14f45677b1a9.htm) | (重写 MeasStation.ExecuteNoReturnMethod``2(NoReturnMethodDescriptionUMP, Object)) |
| 受保护的方法 | [ExecuteSimpleToDictionaryT1, T2](8eb1e067-b08e-07d6-d175-36c31e1526ec.htm) | (重写 MeasStation.ExecuteSimpleToDictionary``2(MethodDescriptionUMP, UMP, Object)) |
| 受保护的方法 | [ExecuteToMeasStationOnceT1, T2](846d9a48-ad7b-4580-2230-bcdbc03493c2.htm) |  |
| 公共方法 | [ExportSignal](6190bc6a-a64c-ff92-f354-7c68ea174b06.htm) | Routes trigger and event signals to the specified outputTerminal. |
| 公共方法 | [FetchCaptureWaveform](59b42875-7726-2d1b-d27b-91d0423db73c.htm) | Fetches a defined number of samples for current site. |
| 公共方法 | [FetchHistoryRamCycleInformation](c4441095-4bc9-709b-eb32-e4cb216c9a71.htm) | Fetches the pattern information acquired for the specified History RAM samples. |
| 公共方法 | [FetchHistoryRamScanCycleNumber](05b7cd6c-0d74-df35-4931-ca63cfde3dbc.htm) | Fetches the scan cycle numbers acquired for the specified History RAM samples. |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | [GenerateClock](f2264cba-844e-6146-7ef5-9091277243ea.htm) | Configures and initiates clock generation on the specified channel(s), or pin(s) and pin group(s). |
| 公共方法 | [GetAllowExtendedVoltageRange](da2ff0ba-a0e9-052a-a585-38655357acd5.htm) | Gets whether the instrument is allowed to operate in the extended voltage range where instrument specifications may differ from standard ranges. |
| 公共方法 | [GetApertureTime](6af16719-f7f6-29ac-83ba-91a8d633ad80.htm) | Gets the measurement aperture time for the PPMU. |
| 公共方法 | [GetDriveFormat](3ace5a44-0dec-e9b1-a6c5-87ff4b3600a7.htm) | Gets the drive format of a time set. |
| 公共方法 | [GetEdge](b1c339fb-31f8-6c5f-d413-d9e32af3ddf4.htm) | Gets the edge time of a time set. |
| 公共方法 | [GetEdgeMultiplier](0b3f5ef7-037d-5c65-5c32-d00ffdfb1065.htm) | Gets the edge multiplier of a time set. |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | [GetHistoryRamBufferSizePerSite](5811885d-1b27-0b93-7443-84b666eeb063.htm) | Gets the size, in samples, of the in-memory History RAM buffer. You can use this property when the instrument is configured for continuous History RAM acquisition. |
| 公共方法 | [GetHistoryRamCyclesToAcquire](a4297696-b3b8-d021-cb70-0bd4fb4b9940.htm) | Gets which cycles History RAM acquires after the trigger conditions are met. If you configure History RAM to acquire only failed samples, you must set the pretrigger samples for History RAM to 0. |
| 公共方法 | [GetHistoryRamFailCount](9274fc5b-0c97-a9e2-0c9f-c91d6cbae124.htm) | Gets the number of samples History RAM acquired on the last pattern burst. |
| 公共方法 | [GetHistoryRamMaxSamplesToAcquire](b7e1c76d-192c-1748-cfdc-602290ef6f78.htm) | Gets the maximum number of History RAM samples to acquire per site. If the property is set to -1, it will acquire until the History RAM buffer is full. |
| 公共方法 | [GetHistoryRamNumberOfSamplesIsFinite](74a9b2a4-31cb-78af-caad-687638252fbe.htm) | Gets whether the instrument acquires a finite number of History RAM samples or acquires samples continuously. When the instrument acquires samples continuously, you can fetch samples during the pattern burst. |
| 公共方法 | [GetIClamp](c9f00b31-f1d3-4331-8d3b-e189fa9585d9.htm) | Gets the valid range, in amps, to which the current limit can be set while the PPMU forces voltage to the DUT. |
| 公共方法 | [GetIClampSink](4253c1a5-15f7-6966-89d1-8ecf09c0acdc.htm) | Gets the clamp value for current sunk by the instrument. |
| 公共方法 | [GetIClampSource](ae630f76-d5df-cefb-64c1-9deefa6404f9.htm) | Gets the clamp value for current sourced by the instrument. |
| 公共方法 | [GetIForceLevel](d063396e-b9dc-4eba-a113-694649627bac.htm) | Gets the current level, in amps, that the PPMU forces to the DUT. |
| 公共方法 | [GetILevelRange](a92ac01b-f3dc-6fc2-686a-babc7887c69b.htm) | Gets the range of valid values for the current level, in amps, that the PPMU forces to the DUT. |
| 公共方法 | [GetIoh](16e3a35f-fbe2-5ba5-fc09-0bf02946ab3f.htm) | Gets the current that the DUT sources to the active load while outputting a voltage above Vcom. |
| 公共方法 | [GetIol](f540e9c1-5ec5-180b-dfd0-022cae6be7ef.htm) | Gets the current that the DUT sinks from the active load while outputting a voltage below Vcom. |
| 公共方法 | [GetOutputFunction](46aa55cc-b123-531f-cc27-581b70204877.htm) | Gets whether the PPMU sources DC voltage or DC current. |
| 公共方法 | [GetPatternIsDone](e5c7112e-a684-fad2-341b-685dcf03f700.htm) | Gets a value that indicates whether the pattern burst completed or if any errors have occurred. |
| 公共方法 | [GetPatternStartLabel](3339c201-27d8-d2b2-3710-a99d0443fea0.htm) | Gets the pattern name or exported pattern label from which to start bursting the pattern. |
| 公共方法 | [GetSelectedFunction](72c91ac1-eeec-a421-f32c-4ffbda464fe2.htm) | Gets the instrument function of this pin list. The changes take effect immediately. |
| 公共方法 | [GetSitePassFail](99551f61-5faf-2934-5ed8-256b1915e6ef.htm) | Returns a value indicating whether the specified sites passed the comparisons in the pattern burst. |
| 公共方法 | [GetTdrOffsets](c7268c85-4fec-a12e-f563-7a2375ea49d4.htm) | Measures propagation delays through cables, connectors, and load boards using Time-Domain Reflectometry (TDR). Optionally, you can apply the offsets to the pins. |
| 公共方法 | [GetTermMode](78279437-2757-52e6-a34a-1dfb050709bb.htm) | Gets the behavior of the pin when pin driver is in a non-drive cycle. |
| 公共方法 | [GetTimeSetFrequency](f3232b17-8c63-05eb-dbec-c4838b08bf48.htm) | Specifies the frequency. The frequency value determines the length of a digital vector. Precondition: property period is not set. |
| 公共方法 | [GetTimeSetPeriod](1aa279f3-8a4c-edbb-c5db-8f8ce603e350.htm) | Gets or sets the period of the time set. The time value determines the length of a digital vector. |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | [GetVClampHigh](d748e771-223e-ae30-a6ad-53b008bde5d3.htm) | Gets the maximum voltage limit, or high clamp voltage (Vch), in volts, at the pin when the PPMU forces current to the DUT. |
| 公共方法 | [GetVClampLow](fafd5d2e-c94d-1fc3-b314-0ee060257d65.htm) | Gets the minimum voltage limit, or low clamp voltage (Vcl), in volts, at the pin when the PPMU forces current to the DUT. |
| 公共方法 | [GetVcom](bb4e0f98-02b7-af5e-3e34-4fe90fffc28f.htm) | Gets the commutating voltage at which the active load circuit switches between between sourcing current and sinking current. |
| 公共方法 | [GetVForceLevel](c668dbe9-b0f9-d017-4e24-6b6a3f736c7b.htm) | Gets the voltage level, in volts, that the PPMU forces to the DUT. |
| 公共方法 | [GetVih](4e03695c-3bcc-39b4-ac9b-9c7e685313b9.htm) | Gets the input voltage that the digital pattern instrument applies to the input of the DUT when the test instrument drives a logic high (1). |
| 公共方法 | [GetVil](ffdb36c0-94a1-f19e-954e-d185bd960739.htm) | Gets the input voltage that the digital pattern instrument applies to the input of the DUT when the test instrument drives a logic low (0). |
| 公共方法 | [GetVoh](3865a649-05f8-2b2e-be83-07606f55ff21.htm) | Gets the output voltage from the DUT above which the comparator on the test instrument interprets a logic high (H). |
| 公共方法 | [GetVol](1384cbb6-dcf6-448e-94fb-c812ba89dd26.htm) | Gets the output voltage from the DUT below which the comparator on the test instrument interprets a logic low (L). |
| 公共方法 | [GetVterm](c41d8971-bee5-0a19-b90c-d928984b2922.htm) | Gets the termination voltage the instrument applies during non-drive cycles when the TerminationMode is set to Vterm. The instrument applies the termination voltage through a 50 Ω parallel termination resistance. |
| 公共方法 | [IForce(Double)](c12024ba-e180-259d-adb5-33dde5bd2ad6.htm) | Set the PPMU to force current to the DUT. You can specify other associated values by properties, such as ILevelRange, VClampHigh and VClampLow. |
| 公共方法 | [IForce(Double, Double)](5ea8c2ec-3487-2a8c-cd2a-bce5ba329a28.htm) | Set the PPMU to force current to the DUI. |
| 公共方法 | [IMeasure](7989f53b-6b5c-6228-6175-6209829c3657.htm) | Measure current while forcing voltage or current with the PPMU. |
| 公共方法 | [Initiate](4421a74a-03ec-39c1-67ce-85370faabab2.htm) | Starts the sourcing voltage or current from the PPMU. |
| 公共方法 | [IsSiteEnabled](64c9d907-1bb1-f6a6-9b8b-8e23040402da.htm) | Returns whether the specified site is enabled or disabled. |
| 公共方法 | [LoadAndApply(String)](08ae4755-63aa-e12b-927e-d76837c28750.htm) | Load PinMap, Specifications, Levels, Timings files and Apply Levels and Timing. |
| 公共方法 | [LoadAndApply(String, String, String, String)](e64124d2-9f73-f90e-5082-a6d83c85a3d5.htm) | Load PinMap, Specifications, Levels, Timings files and Apply Levels and Timing. |
| 公共方法 | [LoadLevels](53c8b521-40fa-96b0-e0cb-2dc17c9a2bf0.htm) | Loads a levels sheet from file. |
| 公共方法 | [LoadPattern](82884f34-2ef5-8cb9-46f3-2ab40f037df8.htm) | Loads a pattern to the hardware from a pattern file. |
| 公共方法 | [LoadPinMap](173f4105-4992-aac1-be4e-71159b2e2ebb.htm) | Loads a pin map file. |
| 公共方法 | [LoadSpecifications](a0cf8491-b585-25a0-ebdc-be0b671085f5.htm) | Loads a specifications sheet from file. |
| 公共方法 | [LoadTiming](c6221d04-41a6-9ba5-27e0-30287ef6c532.htm) | Loads one or more time sets from a timing sheet file. |
| 公共方法 | [MapPinToChannel](e0bccf46-12d9-9e56-085e-242170b02080.htm) | Maps a pin to a digital pattern instrument channel. |
| 公共方法 | [MeasureFrequency](5be10fcf-70b7-8f4e-ef04-80133cce0bad.htm) | Measures the frequency on the specified pins over the measurement time. All pins in the pin list should have the same measurement time. Ensure that all pins have the selected function set to "Digital". |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [ReadSequencerFlag](e992720d-fe2e-8dd4-201a-9231adc2b3a1.htm) | Reads the Boolean state of a pattern sequencer flag. |
| 公共方法 | [ReadSequencerRegister](4ca37d14-3cd7-745e-e673-a53ed844edb7.htm) | Reads the numeric state of a pattern sequencer register. |
| 公共方法 | [ReadStatic](1cfc270f-1eeb-6b33-0477-8f71c87977d7.htm) | Reads the current state of comparators for the specified channels or pins. |
| 公共方法 | [Reset](fb560a17-fa2f-d09c-d657-9b03bc5ff934.htm) | Reset the instrument session. |
| 公共方法 | [ResetDevice](1a9778f2-f83d-69e5-152c-7910a8bc1656.htm) | Performs a hard reset on the device. |
| 公共方法 | [SelfCalibrate](a56efd71-ddd9-cb60-4956-e8c8a12fcb0b.htm) | Performs a self calibrate on the device. |
| 公共方法 | [SelfTest](c80ce17e-1d38-5ff8-79b0-756ff97e1c5e.htm) | Performs a self test on the device. |
| 公共方法 | [SendSoftwareTrigger](4251d2f6-6d4c-1a4c-4ad1-89b4ff9800ce.htm) | Sends the Software Trigger to a digital pattern instrument, forcing the Trigger to assert, regardless of how the Trigger is configured. |
| 公共方法 | [SetAllowExtendedVoltageRange](c277f282-a869-aee8-8176-15f26b43b0ed.htm) | Sets whether the instrument is allowed to operate in the extended voltage range where instrument specifications may differ from standard ranges. |
| 公共方法 | [SetApertureTime](46d058c2-129f-9bee-34d9-7ffdde5f5be0.htm) | Sets the aperture time for the PPMU measurement. |
| 公共方法 | [SetHistoryRamBufferSizePerSite](584d9817-c024-394c-20b6-b8546a7b5c6d.htm) | Sets the size, in samples, of the in-memory History RAM buffer. You can use this property when the instrument is configured for continuous History RAM acquisition. |
| 公共方法 | [SetHistoryRamCyclesToAcquire](d7716c66-6e51-4d16-91e6-89e2d47a7e98.htm) | Sets which cycles History RAM acquires after the trigger conditions are met. If you configure History RAM to acquire only failed samples, you must set the pretrigger samples for History RAM to 0. |
| 公共方法 | [SetHistoryRamMaxSamplesToAcquire](17f8744d-6d91-fc33-63ce-ce98596f18fc.htm) | Sets the maximum number of History RAM samples to acquire per site. If the property is set to -1, it will acquire until the History RAM buffer is full. |
| 公共方法 | [SetHistoryRamNumberOfSamplesIsFinite](e2f95eda-d667-9044-12c7-c0249b079e50.htm) | Sets whether the instrument acquires a finite number of History RAM samples or acquires samples continuously. When the instrument acquires samples continuously, you can fetch samples during the pattern burst. |
| 公共方法 | [SetIClamp](2d86deca-dddb-aa5e-adfb-c8e09d11eb84.htm) | Sets the valid range, in amps, to which the current limit can be set while the PPMU forces voltage to the DUT. |
| 公共方法 | [SetIClampAutoRange](8a779ba6-3ae8-56d8-e5ae-79516e41d69d.htm) | 自动设置Digital仪表的钳位电流，不会直接施加电流。 |
| 公共方法 | [SetIClampSink](85e25fc1-becc-c17a-28b2-7b831d21e7f8.htm) | Specifies the clamp value for current sunk by the instrument. As the direction of the current is out of the DUT into the instrument, the value must be positive. This can be used to set different clamp values for sourcing and sinking current. If the current range is not set explicitly with the irange property, it will be set to the smallest range that covers the specified clamp values to achieve highest possible accuracy. |
| 公共方法 | [SetIClampSource](97ce2698-fc71-3d4e-40b8-cfcab971a761.htm) | Specifies the clamp value for current sourced by the instrument. This can be used to set different clamp values for sourcing and sinking current. If the current range is not set explicitly with the irange property, it will be set to the smallest range that covers the specified clamp values to achieve highest possible accuracy. |
| 公共方法 | [SetIForceLevel](d034f1cd-057b-dae0-2283-49622870fa02.htm) | Sets the current level, in amps, that the PPMU forces to the DUT. |
| 公共方法 | [SetILevelAutoRange](b4b7e7a4-ec00-ff40-70f7-0111c0a5a867.htm) | 自动设置Digital仪表的电流挡位，不会直接施加电流。 |
| 公共方法 | [SetILevelRange](869e02ee-b84b-3a62-6bcb-270e716b6618.htm) | Sets the range of valid values for the current level, in amps, that the PPMU forces to the DUT. |
| 公共方法 | [SetIoh](730b6aa6-5976-a083-23f4-f17fad786058.htm) | Sets the current that the DUT sources to the active load while outputting a voltage above Vcom. |
| 公共方法 | [SetIol](e06717f0-c7e0-101b-9aef-356248123df1.htm) | Sets the current that the DUT sinks from the active load while outputting a voltage below Vcom. |
| 公共方法 | [SetOutputFunction](52f922db-a197-9379-7f10-e0c60ff5e366.htm) | Sets whether the PPMU sources DC voltage or DC current. |
| 公共方法 | [SetPatternStartLabel](6b8d6cb9-86ad-429b-ce7b-15900b70dfb3.htm) | Sets the pattern name or exported pattern label from which to start bursting the pattern. |
| 公共方法 | [SetSelectedFunction](67acace3-dd0d-4536-ebb4-cc1bbbb85bb5.htm) | Sets the instrument function of this pin list. The changes take effect immediately. |
| 公共方法 | [SetTermMode](103b9393-b23d-b1d3-e954-1a5c187f9f3e.htm) | Sets the behavior of the pin when pin driver is in a non-drive cycle. |
| 公共方法 | [SetTimeSetFrequency](e6278b05-0890-49c6-ac76-80dd52c5457e.htm) | Specifies the frequency. The frequency value determines the length of a digital vector. Precondition: property period is not set. |
| 公共方法 | [SetTimeSetPeriod](f7c60800-d874-6993-5a7e-d8d8b677e3ff.htm) | Gets or sets the period of the time set. The time value determines the length of a digital vector. |
| 公共方法 | [SetVClampAutoRange](c1e1674f-bdc3-9e4a-b322-e6c1d04e57dc.htm) | 自动设置Digital仪表的钳位电压值。 |
| 公共方法 | [SetVClampHigh](f72db89d-c568-9752-e873-2a024a85af0b.htm) | Sets the maximum voltage limit, or high clamp voltage (Vch), in volts, at the pin when the PPMU forces current to the DUT. |
| 公共方法 | [SetVClampLow](f5e74e72-4608-50de-76c9-6da3400995b6.htm) | Sets the minimum voltage limit, or low clamp voltage (Vcl), in volts, at the pin when the PPMU forces current to the DUT. |
| 公共方法 | [SetVcom](9a14fe00-dcb7-683e-0278-12812001ae8e.htm) | Sets the commutating voltage at which the active load circuit switches between between sourcing current and sinking current. |
| 公共方法 | [SetVForceLevel](1d528ef1-a325-ac56-8848-58ad6f5923a8.htm) | Sets the voltage level, in volts, that the PPMU forces to the DUT. |
| 公共方法 | [SetVih](9bb67f33-4f12-e327-c372-275568754092.htm) | Sets the input voltage that the digital pattern instrument applies to the input of the DUT when the test instrument drives a logic high (1). |
| 公共方法 | [SetVil](5d3ab7ac-15bc-14f2-26eb-9363c2456d24.htm) | Sets the input voltage that the digital pattern instrument applies to the input of the DUT when the test instrument drives a logic low (0). |
| 公共方法 | [SetVoh](8ff9bf80-c360-e981-a03d-286f4f47f246.htm) | Sets the output voltage from the DUT above which the comparator on the test instrument interprets a logic high (H). |
| 公共方法 | [SetVol](e0ba84a2-1a96-3636-d7af-874649cd6a2c.htm) | Sets the output voltage from the DUT below which the comparator on the test instrument interprets a logic low (L). |
| 公共方法 | [SetVterm](5e02992a-67b9-c4c7-f7a0-063cc8abfbc1.htm) | Sets the termination voltage the instrument applies during non-drive cycles when the TerminationMode is set to Vterm. The instrument applies the termination voltage through a 50 Ω parallel termination resistance. |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |
| 公共方法 | [UnloadAllPatterns](90190be5-da2b-4c96-5a0e-992adb306720.htm) | Unloads all patterns, source waveforms, and capture waveforms from a digital pattern instrument. |
| 公共方法 | [UnloadSpecifications](e58a122f-b33d-f1e6-159a-a0fe1c59bf5e.htm) | Unloads the given specifications sheet present in the previously loaded specifications file that you select. |
| 公共方法 | [VForce(Double)](4ee27b17-9519-4347-3a9c-036e14c86981.htm) | Set the PPMU to force voltage to the DUT. You can specify other associated values by properties, such as IClampRange. |
| 公共方法 | [VForce(Double, Double)](36d62a26-e2e9-c394-4371-aa28903c8945.htm) | Set the PPMU to force voltage to the DUI. |
| 公共方法 | [VMeasure](093951e2-a5d8-15e1-4c71-e5717fd2d8b6.htm) | Perform measurement operations at any time, even if you are not forcing current or voltage with the PPMU. |
| 公共方法 | [WaitUntilDone](e4224f24-ce12-4657-56d7-637aa7a9da13.htm) | Waits until the pattern burst has completed or the specified maxTime has expired. |
| 公共方法 | [WriteSequencerFlag](5ca3da79-0fff-ddbf-a00e-30319786fcb8.htm) | Writes a Boolean value to a pattern sequencer flag. |
| 公共方法 | [WriteSequencerRegister](7b27a2c5-e747-2281-21db-4d83a8b3068c.htm) | Writes a value to a pattern sequencer register. |
| 公共方法 | [WriteSourceWaveformBroadcast](c958d865-ae88-9b93-3ebf-99a4abfb472f.htm) | Writes the same source waveform data to all sites. |
| 公共方法 | [WriteSourceWaveformDataFromFile](1e946e49-4973-c678-64c0-4aa26f003757.htm) | Writes a source waveform based on the waveform data and the configuration information the file contains. |
| 公共方法 | [WriteSourceWaveformSiteUnique](69299666-02e1-fa96-553c-74c9f0a0028b.htm) | Writes one source waveform to current site. |
| 公共方法 | [WriteStatic](5478c171-266d-36b6-bbad-30b33516dffe.htm) | Writes a static state to the channels or pins represented by this pin list. These channels or pins remain in the specified state until the next pattern burst or call to this method. |

[Top](#PageHeader)

参见

##### 引用

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


### Digital 构造函数

|  |  |
| --- | --- |
|  | Digital 构造函数 |

初始化 [Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm) 类的一个新实例

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital()
```

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


### Digital 方法

|  |  |
| --- | --- |
|  | Digital 方法 |

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [AbortBurst](32d8afd7-53dd-fc9d-b694-6f4a4bf01a50.htm) | Stops bursting the pattern. |
| 公共方法 | [AbortClockGenerator](af6955f5-a2b7-8c73-c0ff-d2d6732d303b.htm) | Stops clock generation on the specified channel(s) or pin(s) and pin group(s). |
| 公共方法 | [AbortKeepAlive](772aec94-693f-dc1e-56a3-0da192dde1ed.htm) | Stops the keep alive pattern if it is currently running. If a pattern burst is in progress, this method aborts the pattern burst. If you start a new pattern burst while a keep alive pattern is running, the keep alive pattern runs to the last keep alive vector, and the new pattern burst starts on the next cycle. |
| 公共方法 | [ApplyLevelsAndTiming(String, String)](446e8be1-da3d-4b53-7c9f-30d554790cf3.htm) | Applies digital levels and timing defined in the loaded levels and timing sheets. |
| 公共方法 | [ApplyLevelsAndTiming(String, String, String, String, String)](7b9bde6d-39ac-a0ef-9a05-5426aa4a4d01.htm) | Applies digital levels and timing defined in the loaded levels and timing sheets. |
| 公共方法 | [ApplyTdrOffsets](6c5b156f-ba54-e7bc-e7ed-aff2ffbe1077.htm) | Applies the correction for propagation delay offsets to a digital pattern instrument. |
| 公共方法 | [BurstPattern(String)](6a00d5a5-53d1-7c92-c567-e8556bceed90.htm) | Bursts the pattern on the sites you specify, waits for the burst to complete, and returns comparison results for current site. |
| 公共方法 | [BurstPattern(String, Boolean, Double)](89e23eea-5c46-6273-c333-6f3aed75df49.htm) | Bursts the pattern on the sites you specify, waits for the burst to complete, and returns comparison results for current site. |
| 公共方法 | [BurstPattern(String, Boolean, Boolean, Double)](1bf58a23-7f26-1313-9967-a1cb35bd4ef9.htm) | Bursts the pattern on the site you specify, waits for the burst to complete, and returns comparison results for current site. |
| 公共方法 | [ConfigureActiveLoadLevels](ecf88222-bbfe-efb2-258b-b5e3de3f9fca.htm) | Configures the Ioh, Iol, and Vcom values. The DUT sources or sinks current based on the level values. To enable active load, set the termination mode to ActiveLoad. To disable active load, set the termination mode of the instrument to HighZ or Vterm. These properties are only applicable if the pinset's SelectedFunction is set to Digital and TerminationMode is set to ActiveLoad. |
| 公共方法 | [ConfigureCompareStrobeEdge(String, Double)](b286bb79-e6d1-84d4-38b9-2cf5af248b04.htm) | Configures the strobe edge time for the specified pins. |
| 公共方法 | [ConfigureCompareStrobeEdge(String, Double, Double)](22bf36b4-118b-f056-e4fe-e335669ed9a3.htm) | Configures the strobe edge times for the specified pins. |
| 公共方法 | [ConfigureDigitalEdgeTrigger](8baba7d2-5c73-a9a1-b768-06ec8211da3c.htm) | Configures the TriggerType to DigitalEdge, and configures the source and Edge properties. |
| 公共方法 | [ConfigureDriveEdges](614f4f96-aae6-22d9-a916-82eca07bc0d7.htm) | Configures the drive format and the drive edge placement for the specified pins. |
| 公共方法 | [ConfigureDriveFormat](3ad9f204-f543-a86a-3cf6-fdbd6b6fb442.htm) | Configures the drive format of a time set. |
| 公共方法 | [ConfigureDriverEdges](8f3ebee8-6dd9-368d-9075-e0ef17d28e4d.htm) | Configures the drive format and the drive edge placement for the specified pins. |
| 公共方法 | [ConfigureEdge](e5610029-7d13-1c73-5bfb-55905c814eed.htm) | Configures the edge of a time set. |
| 公共方法 | [ConfigureEdgeMultiplier](63e24596-3d91-099c-bb9f-9176eaaba67c.htm) | Configures the edge multiplier of a time set. |
| 公共方法 | [ConfigureHistoryRamCycleNumberTrigger](245f6339-99e2-cf6c-341f-384714efb69d.htm) | Configures the TriggerType to CycleNumber and configures Number and PretriggerSamples. |
| 公共方法 | [ConfigureHistoryRamFirstFailureTrigger](d84e1110-0b4a-c4ca-5691-e1dc6d058aeb.htm) | Configures the TriggerType to FirstFailure and configures PretriggerSamples. |
| 公共方法 | [ConfigureHistoryRamPatternLabelTrigger](9793d008-acaa-85a4-8358-7fd539568b1f.htm) | Configures the TriggerType to PatternLabel and configures Label, VectorOffset, CycleOffset, and PretriggerSamples. |
| 公共方法 | [ConfigureIClamp](3f1fdfb7-3599-d2bb-adc8-851e3ee95257.htm) | Configure the sourced and sunk current clamp value. |
| 公共方法 | [ConfigureSoftwareTrigger](876990f1-94ad-a0a7-33d4-420d7f5bc374.htm) | Configures the TriggerType for Software triggering. |
| 公共方法 | [ConfigureVClamp](f39ac233-bfdf-19db-45df-b9a6570c9f33.htm) | Configure the maximum and minimum voltage limit. |
| 公共方法 | [ConfigureVoltageLevels](c53628c4-06ec-be92-be9a-2dccc2f275fc.htm) | Configures the high and low logic levels for voltage as well as the termination mode input voltage. These voltages apply to the pin list when the SelectedFunction is Digital. |
| 公共方法 | [CreateCaptureWaveformFromFile](dac55003-b90d-e38d-414f-62d1f0881e66.htm) | Creates a capture waveform using the configuration information from a .digicapture file. |
| 公共方法 | [CreateCaptureWaveformParallel](1e15e50e-3f7e-25d9-98ee-755d0aa94413.htm) | Creates the capture waveform settings for parallel acquisition using a comma-delimited string of pins or channels. |
| 公共方法 | [CreateCaptureWaveformSerial](3a8d22e5-5e67-0786-0568-3968cf7e8600.htm) | Creates the capture waveform settings for serial acquisition using a comma-delimited string of pins or channels. |
| 公共方法 | [CreateChannelMap](b7770175-3d8e-fba1-935f-fd7d67556eda.htm) | Creates a channel map, which translates the pin maps and sites to the instrument channels. You must create the pin map using CreatePinMap() before calling this method. |
| 公共方法 | [CreatePinGroup](7785cda6-7ed5-40b7-bf09-b63f21bd1a40.htm) | Creates a pin group with the specified name. The pin group serves as an alias for a list of pins. |
| 公共方法 | [CreatePinMap](8f109038-9eef-ac15-384c-d75aa50b7a54.htm) | Creates and loads a pin map. Use this method if you are not loading a pin map file using LoadPinMap(). |
| 公共方法 | [CreateSourceWaveformFromFile](99ae6698-cb1c-9e5e-c3e9-92fd06c7e5ed.htm) | Creates the source waveform settings used to source waveforms with configuration information contained in a .tdms file. |
| 公共方法 | [CreateSourceWaveformParallel](0d4f48b7-3386-25e9-99f9-f558303839b5.htm) | Creates source waveform settings used to source parallel data using a comma-delimited string of pins or channels. |
| 公共方法 | [CreateSourceWaveformSerial](9221bb0c-e62d-7816-36e9-bd09fcbc0088.htm) | Creates the source waveform settings used to source serial waveforms using a comma-delimited string of pins or channels. |
| 公共方法 | [CreateTimeSet](cdd750e0-a83d-963c-4807-2e4e4d340deb.htm) | Creates a DigitalTimeSet. Use this method to create time set values after applying a timing sheet with ApplyLevelsAndTiming(), or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to ApplyLevelsAndTiming(), it only affects the values of the current timing context. |
| 公共方法 | [DeleteAllTimeSets](46397e2c-14e3-74ab-560d-12451b0e41f4.htm) | Deletes all loaded and created time sets. |
| 公共方法 | [DisableSites](ef6888bb-eec9-6aa3-7292-ff28b65cb37c.htm) | Disables the specified sites |
| 公共方法 | [DisableTrigger](4a844df7-0bf4-beb7-5d47-4f62b4addc20.htm) | Disables a previously configured trigger and sets TriggerType to None. |
| 公共方法 | [EnableSites](46622cca-be53-2be9-2d0e-8ab1ad924f83.htm) | Enables the specified sites. |
| 公共方法 | [EndChannelMap](66069adf-ffab-55de-f7d7-3b9f23a0bfa1.htm) | Completes the channel map configuration. No further changes can be made to the channel map or connections after calling this method. |
| 公共方法 | Equals | Determines whether the specified object is equal to the current object. (继承自 Object。) |
| 受保护的方法 | [ExecuteArrayToDictionaryT1, T2](2876e44c-2e79-31b7-2f20-3bc738532d50.htm) | (重写 MeasStation.ExecuteArrayToDictionary``2(MethodDescriptionUMP, UMP, Object)) |
| 受保护的方法 | [ExecuteNoReturnMethodT1, T2](cb817f46-5a3a-4bb3-6e44-14f45677b1a9.htm) | (重写 MeasStation.ExecuteNoReturnMethod``2(NoReturnMethodDescriptionUMP, Object)) |
| 受保护的方法 | [ExecuteSimpleToDictionaryT1, T2](8eb1e067-b08e-07d6-d175-36c31e1526ec.htm) | (重写 MeasStation.ExecuteSimpleToDictionary``2(MethodDescriptionUMP, UMP, Object)) |
| 受保护的方法 | [ExecuteToMeasStationOnceT1, T2](846d9a48-ad7b-4580-2230-bcdbc03493c2.htm) |  |
| 公共方法 | [ExportSignal](6190bc6a-a64c-ff92-f354-7c68ea174b06.htm) | Routes trigger and event signals to the specified outputTerminal. |
| 公共方法 | [FetchCaptureWaveform](59b42875-7726-2d1b-d27b-91d0423db73c.htm) | Fetches a defined number of samples for current site. |
| 公共方法 | [FetchHistoryRamCycleInformation](c4441095-4bc9-709b-eb32-e4cb216c9a71.htm) | Fetches the pattern information acquired for the specified History RAM samples. |
| 公共方法 | [FetchHistoryRamScanCycleNumber](05b7cd6c-0d74-df35-4931-ca63cfde3dbc.htm) | Fetches the scan cycle numbers acquired for the specified History RAM samples. |
| 受保护的方法 | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (继承自 Object。) |
| 公共方法 | [GenerateClock](f2264cba-844e-6146-7ef5-9091277243ea.htm) | Configures and initiates clock generation on the specified channel(s), or pin(s) and pin group(s). |
| 公共方法 | [GetAllowExtendedVoltageRange](da2ff0ba-a0e9-052a-a585-38655357acd5.htm) | Gets whether the instrument is allowed to operate in the extended voltage range where instrument specifications may differ from standard ranges. |
| 公共方法 | [GetApertureTime](6af16719-f7f6-29ac-83ba-91a8d633ad80.htm) | Gets the measurement aperture time for the PPMU. |
| 公共方法 | [GetDriveFormat](3ace5a44-0dec-e9b1-a6c5-87ff4b3600a7.htm) | Gets the drive format of a time set. |
| 公共方法 | [GetEdge](b1c339fb-31f8-6c5f-d413-d9e32af3ddf4.htm) | Gets the edge time of a time set. |
| 公共方法 | [GetEdgeMultiplier](0b3f5ef7-037d-5c65-5c32-d00ffdfb1065.htm) | Gets the edge multiplier of a time set. |
| 公共方法 | GetHashCode | Serves as the default hash function. (继承自 Object。) |
| 公共方法 | [GetHistoryRamBufferSizePerSite](5811885d-1b27-0b93-7443-84b666eeb063.htm) | Gets the size, in samples, of the in-memory History RAM buffer. You can use this property when the instrument is configured for continuous History RAM acquisition. |
| 公共方法 | [GetHistoryRamCyclesToAcquire](a4297696-b3b8-d021-cb70-0bd4fb4b9940.htm) | Gets which cycles History RAM acquires after the trigger conditions are met. If you configure History RAM to acquire only failed samples, you must set the pretrigger samples for History RAM to 0. |
| 公共方法 | [GetHistoryRamFailCount](9274fc5b-0c97-a9e2-0c9f-c91d6cbae124.htm) | Gets the number of samples History RAM acquired on the last pattern burst. |
| 公共方法 | [GetHistoryRamMaxSamplesToAcquire](b7e1c76d-192c-1748-cfdc-602290ef6f78.htm) | Gets the maximum number of History RAM samples to acquire per site. If the property is set to -1, it will acquire until the History RAM buffer is full. |
| 公共方法 | [GetHistoryRamNumberOfSamplesIsFinite](74a9b2a4-31cb-78af-caad-687638252fbe.htm) | Gets whether the instrument acquires a finite number of History RAM samples or acquires samples continuously. When the instrument acquires samples continuously, you can fetch samples during the pattern burst. |
| 公共方法 | [GetIClamp](c9f00b31-f1d3-4331-8d3b-e189fa9585d9.htm) | Gets the valid range, in amps, to which the current limit can be set while the PPMU forces voltage to the DUT. |
| 公共方法 | [GetIClampSink](4253c1a5-15f7-6966-89d1-8ecf09c0acdc.htm) | Gets the clamp value for current sunk by the instrument. |
| 公共方法 | [GetIClampSource](ae630f76-d5df-cefb-64c1-9deefa6404f9.htm) | Gets the clamp value for current sourced by the instrument. |
| 公共方法 | [GetIForceLevel](d063396e-b9dc-4eba-a113-694649627bac.htm) | Gets the current level, in amps, that the PPMU forces to the DUT. |
| 公共方法 | [GetILevelRange](a92ac01b-f3dc-6fc2-686a-babc7887c69b.htm) | Gets the range of valid values for the current level, in amps, that the PPMU forces to the DUT. |
| 公共方法 | [GetIoh](16e3a35f-fbe2-5ba5-fc09-0bf02946ab3f.htm) | Gets the current that the DUT sources to the active load while outputting a voltage above Vcom. |
| 公共方法 | [GetIol](f540e9c1-5ec5-180b-dfd0-022cae6be7ef.htm) | Gets the current that the DUT sinks from the active load while outputting a voltage below Vcom. |
| 公共方法 | [GetOutputFunction](46aa55cc-b123-531f-cc27-581b70204877.htm) | Gets whether the PPMU sources DC voltage or DC current. |
| 公共方法 | [GetPatternIsDone](e5c7112e-a684-fad2-341b-685dcf03f700.htm) | Gets a value that indicates whether the pattern burst completed or if any errors have occurred. |
| 公共方法 | [GetPatternStartLabel](3339c201-27d8-d2b2-3710-a99d0443fea0.htm) | Gets the pattern name or exported pattern label from which to start bursting the pattern. |
| 公共方法 | [GetSelectedFunction](72c91ac1-eeec-a421-f32c-4ffbda464fe2.htm) | Gets the instrument function of this pin list. The changes take effect immediately. |
| 公共方法 | [GetSitePassFail](99551f61-5faf-2934-5ed8-256b1915e6ef.htm) | Returns a value indicating whether the specified sites passed the comparisons in the pattern burst. |
| 公共方法 | [GetTdrOffsets](c7268c85-4fec-a12e-f563-7a2375ea49d4.htm) | Measures propagation delays through cables, connectors, and load boards using Time-Domain Reflectometry (TDR). Optionally, you can apply the offsets to the pins. |
| 公共方法 | [GetTermMode](78279437-2757-52e6-a34a-1dfb050709bb.htm) | Gets the behavior of the pin when pin driver is in a non-drive cycle. |
| 公共方法 | [GetTimeSetFrequency](f3232b17-8c63-05eb-dbec-c4838b08bf48.htm) | Specifies the frequency. The frequency value determines the length of a digital vector. Precondition: property period is not set. |
| 公共方法 | [GetTimeSetPeriod](1aa279f3-8a4c-edbb-c5db-8f8ce603e350.htm) | Gets or sets the period of the time set. The time value determines the length of a digital vector. |
| 公共方法 | GetType | Gets the Type of the current instance. (继承自 Object。) |
| 公共方法 | [GetVClampHigh](d748e771-223e-ae30-a6ad-53b008bde5d3.htm) | Gets the maximum voltage limit, or high clamp voltage (Vch), in volts, at the pin when the PPMU forces current to the DUT. |
| 公共方法 | [GetVClampLow](fafd5d2e-c94d-1fc3-b314-0ee060257d65.htm) | Gets the minimum voltage limit, or low clamp voltage (Vcl), in volts, at the pin when the PPMU forces current to the DUT. |
| 公共方法 | [GetVcom](bb4e0f98-02b7-af5e-3e34-4fe90fffc28f.htm) | Gets the commutating voltage at which the active load circuit switches between between sourcing current and sinking current. |
| 公共方法 | [GetVForceLevel](c668dbe9-b0f9-d017-4e24-6b6a3f736c7b.htm) | Gets the voltage level, in volts, that the PPMU forces to the DUT. |
| 公共方法 | [GetVih](4e03695c-3bcc-39b4-ac9b-9c7e685313b9.htm) | Gets the input voltage that the digital pattern instrument applies to the input of the DUT when the test instrument drives a logic high (1). |
| 公共方法 | [GetVil](ffdb36c0-94a1-f19e-954e-d185bd960739.htm) | Gets the input voltage that the digital pattern instrument applies to the input of the DUT when the test instrument drives a logic low (0). |
| 公共方法 | [GetVoh](3865a649-05f8-2b2e-be83-07606f55ff21.htm) | Gets the output voltage from the DUT above which the comparator on the test instrument interprets a logic high (H). |
| 公共方法 | [GetVol](1384cbb6-dcf6-448e-94fb-c812ba89dd26.htm) | Gets the output voltage from the DUT below which the comparator on the test instrument interprets a logic low (L). |
| 公共方法 | [GetVterm](c41d8971-bee5-0a19-b90c-d928984b2922.htm) | Gets the termination voltage the instrument applies during non-drive cycles when the TerminationMode is set to Vterm. The instrument applies the termination voltage through a 50 Ω parallel termination resistance. |
| 公共方法 | [IForce(Double)](c12024ba-e180-259d-adb5-33dde5bd2ad6.htm) | Set the PPMU to force current to the DUT. You can specify other associated values by properties, such as ILevelRange, VClampHigh and VClampLow. |
| 公共方法 | [IForce(Double, Double)](5ea8c2ec-3487-2a8c-cd2a-bce5ba329a28.htm) | Set the PPMU to force current to the DUI. |
| 公共方法 | [IMeasure](7989f53b-6b5c-6228-6175-6209829c3657.htm) | Measure current while forcing voltage or current with the PPMU. |
| 公共方法 | [Initiate](4421a74a-03ec-39c1-67ce-85370faabab2.htm) | Starts the sourcing voltage or current from the PPMU. |
| 公共方法 | [IsSiteEnabled](64c9d907-1bb1-f6a6-9b8b-8e23040402da.htm) | Returns whether the specified site is enabled or disabled. |
| 公共方法 | [LoadAndApply(String)](08ae4755-63aa-e12b-927e-d76837c28750.htm) | Load PinMap, Specifications, Levels, Timings files and Apply Levels and Timing. |
| 公共方法 | [LoadAndApply(String, String, String, String)](e64124d2-9f73-f90e-5082-a6d83c85a3d5.htm) | Load PinMap, Specifications, Levels, Timings files and Apply Levels and Timing. |
| 公共方法 | [LoadLevels](53c8b521-40fa-96b0-e0cb-2dc17c9a2bf0.htm) | Loads a levels sheet from file. |
| 公共方法 | [LoadPattern](82884f34-2ef5-8cb9-46f3-2ab40f037df8.htm) | Loads a pattern to the hardware from a pattern file. |
| 公共方法 | [LoadPinMap](173f4105-4992-aac1-be4e-71159b2e2ebb.htm) | Loads a pin map file. |
| 公共方法 | [LoadSpecifications](a0cf8491-b585-25a0-ebdc-be0b671085f5.htm) | Loads a specifications sheet from file. |
| 公共方法 | [LoadTiming](c6221d04-41a6-9ba5-27e0-30287ef6c532.htm) | Loads one or more time sets from a timing sheet file. |
| 公共方法 | [MapPinToChannel](e0bccf46-12d9-9e56-085e-242170b02080.htm) | Maps a pin to a digital pattern instrument channel. |
| 公共方法 | [MeasureFrequency](5be10fcf-70b7-8f4e-ef04-80133cce0bad.htm) | Measures the frequency on the specified pins over the measurement time. All pins in the pin list should have the same measurement time. Ensure that all pins have the selected function set to "Digital". |
| 受保护的方法 | MemberwiseClone | Creates a shallow copy of the current Object. (继承自 Object。) |
| 公共方法 | [ReadSequencerFlag](e992720d-fe2e-8dd4-201a-9231adc2b3a1.htm) | Reads the Boolean state of a pattern sequencer flag. |
| 公共方法 | [ReadSequencerRegister](4ca37d14-3cd7-745e-e673-a53ed844edb7.htm) | Reads the numeric state of a pattern sequencer register. |
| 公共方法 | [ReadStatic](1cfc270f-1eeb-6b33-0477-8f71c87977d7.htm) | Reads the current state of comparators for the specified channels or pins. |
| 公共方法 | [Reset](fb560a17-fa2f-d09c-d657-9b03bc5ff934.htm) | Reset the instrument session. |
| 公共方法 | [ResetDevice](1a9778f2-f83d-69e5-152c-7910a8bc1656.htm) | Performs a hard reset on the device. |
| 公共方法 | [SelfCalibrate](a56efd71-ddd9-cb60-4956-e8c8a12fcb0b.htm) | Performs a self calibrate on the device. |
| 公共方法 | [SelfTest](c80ce17e-1d38-5ff8-79b0-756ff97e1c5e.htm) | Performs a self test on the device. |
| 公共方法 | [SendSoftwareTrigger](4251d2f6-6d4c-1a4c-4ad1-89b4ff9800ce.htm) | Sends the Software Trigger to a digital pattern instrument, forcing the Trigger to assert, regardless of how the Trigger is configured. |
| 公共方法 | [SetAllowExtendedVoltageRange](c277f282-a869-aee8-8176-15f26b43b0ed.htm) | Sets whether the instrument is allowed to operate in the extended voltage range where instrument specifications may differ from standard ranges. |
| 公共方法 | [SetApertureTime](46d058c2-129f-9bee-34d9-7ffdde5f5be0.htm) | Sets the aperture time for the PPMU measurement. |
| 公共方法 | [SetHistoryRamBufferSizePerSite](584d9817-c024-394c-20b6-b8546a7b5c6d.htm) | Sets the size, in samples, of the in-memory History RAM buffer. You can use this property when the instrument is configured for continuous History RAM acquisition. |
| 公共方法 | [SetHistoryRamCyclesToAcquire](d7716c66-6e51-4d16-91e6-89e2d47a7e98.htm) | Sets which cycles History RAM acquires after the trigger conditions are met. If you configure History RAM to acquire only failed samples, you must set the pretrigger samples for History RAM to 0. |
| 公共方法 | [SetHistoryRamMaxSamplesToAcquire](17f8744d-6d91-fc33-63ce-ce98596f18fc.htm) | Sets the maximum number of History RAM samples to acquire per site. If the property is set to -1, it will acquire until the History RAM buffer is full. |
| 公共方法 | [SetHistoryRamNumberOfSamplesIsFinite](e2f95eda-d667-9044-12c7-c0249b079e50.htm) | Sets whether the instrument acquires a finite number of History RAM samples or acquires samples continuously. When the instrument acquires samples continuously, you can fetch samples during the pattern burst. |
| 公共方法 | [SetIClamp](2d86deca-dddb-aa5e-adfb-c8e09d11eb84.htm) | Sets the valid range, in amps, to which the current limit can be set while the PPMU forces voltage to the DUT. |
| 公共方法 | [SetIClampAutoRange](8a779ba6-3ae8-56d8-e5ae-79516e41d69d.htm) | 自动设置Digital仪表的钳位电流，不会直接施加电流。 |
| 公共方法 | [SetIClampSink](85e25fc1-becc-c17a-28b2-7b831d21e7f8.htm) | Specifies the clamp value for current sunk by the instrument. As the direction of the current is out of the DUT into the instrument, the value must be positive. This can be used to set different clamp values for sourcing and sinking current. If the current range is not set explicitly with the irange property, it will be set to the smallest range that covers the specified clamp values to achieve highest possible accuracy. |
| 公共方法 | [SetIClampSource](97ce2698-fc71-3d4e-40b8-cfcab971a761.htm) | Specifies the clamp value for current sourced by the instrument. This can be used to set different clamp values for sourcing and sinking current. If the current range is not set explicitly with the irange property, it will be set to the smallest range that covers the specified clamp values to achieve highest possible accuracy. |
| 公共方法 | [SetIForceLevel](d034f1cd-057b-dae0-2283-49622870fa02.htm) | Sets the current level, in amps, that the PPMU forces to the DUT. |
| 公共方法 | [SetILevelAutoRange](b4b7e7a4-ec00-ff40-70f7-0111c0a5a867.htm) | 自动设置Digital仪表的电流挡位，不会直接施加电流。 |
| 公共方法 | [SetILevelRange](869e02ee-b84b-3a62-6bcb-270e716b6618.htm) | Sets the range of valid values for the current level, in amps, that the PPMU forces to the DUT. |
| 公共方法 | [SetIoh](730b6aa6-5976-a083-23f4-f17fad786058.htm) | Sets the current that the DUT sources to the active load while outputting a voltage above Vcom. |
| 公共方法 | [SetIol](e06717f0-c7e0-101b-9aef-356248123df1.htm) | Sets the current that the DUT sinks from the active load while outputting a voltage below Vcom. |
| 公共方法 | [SetOutputFunction](52f922db-a197-9379-7f10-e0c60ff5e366.htm) | Sets whether the PPMU sources DC voltage or DC current. |
| 公共方法 | [SetPatternStartLabel](6b8d6cb9-86ad-429b-ce7b-15900b70dfb3.htm) | Sets the pattern name or exported pattern label from which to start bursting the pattern. |
| 公共方法 | [SetSelectedFunction](67acace3-dd0d-4536-ebb4-cc1bbbb85bb5.htm) | Sets the instrument function of this pin list. The changes take effect immediately. |
| 公共方法 | [SetTermMode](103b9393-b23d-b1d3-e954-1a5c187f9f3e.htm) | Sets the behavior of the pin when pin driver is in a non-drive cycle. |
| 公共方法 | [SetTimeSetFrequency](e6278b05-0890-49c6-ac76-80dd52c5457e.htm) | Specifies the frequency. The frequency value determines the length of a digital vector. Precondition: property period is not set. |
| 公共方法 | [SetTimeSetPeriod](f7c60800-d874-6993-5a7e-d8d8b677e3ff.htm) | Gets or sets the period of the time set. The time value determines the length of a digital vector. |
| 公共方法 | [SetVClampAutoRange](c1e1674f-bdc3-9e4a-b322-e6c1d04e57dc.htm) | 自动设置Digital仪表的钳位电压值。 |
| 公共方法 | [SetVClampHigh](f72db89d-c568-9752-e873-2a024a85af0b.htm) | Sets the maximum voltage limit, or high clamp voltage (Vch), in volts, at the pin when the PPMU forces current to the DUT. |
| 公共方法 | [SetVClampLow](f5e74e72-4608-50de-76c9-6da3400995b6.htm) | Sets the minimum voltage limit, or low clamp voltage (Vcl), in volts, at the pin when the PPMU forces current to the DUT. |
| 公共方法 | [SetVcom](9a14fe00-dcb7-683e-0278-12812001ae8e.htm) | Sets the commutating voltage at which the active load circuit switches between between sourcing current and sinking current. |
| 公共方法 | [SetVForceLevel](1d528ef1-a325-ac56-8848-58ad6f5923a8.htm) | Sets the voltage level, in volts, that the PPMU forces to the DUT. |
| 公共方法 | [SetVih](9bb67f33-4f12-e327-c372-275568754092.htm) | Sets the input voltage that the digital pattern instrument applies to the input of the DUT when the test instrument drives a logic high (1). |
| 公共方法 | [SetVil](5d3ab7ac-15bc-14f2-26eb-9363c2456d24.htm) | Sets the input voltage that the digital pattern instrument applies to the input of the DUT when the test instrument drives a logic low (0). |
| 公共方法 | [SetVoh](8ff9bf80-c360-e981-a03d-286f4f47f246.htm) | Sets the output voltage from the DUT above which the comparator on the test instrument interprets a logic high (H). |
| 公共方法 | [SetVol](e0ba84a2-1a96-3636-d7af-874649cd6a2c.htm) | Sets the output voltage from the DUT below which the comparator on the test instrument interprets a logic low (L). |
| 公共方法 | [SetVterm](5e02992a-67b9-c4c7-f7a0-063cc8abfbc1.htm) | Sets the termination voltage the instrument applies during non-drive cycles when the TerminationMode is set to Vterm. The instrument applies the termination voltage through a 50 Ω parallel termination resistance. |
| 公共方法 | ToString | Returns a string that represents the current object. (继承自 Object。) |
| 公共方法 | [UnloadAllPatterns](90190be5-da2b-4c96-5a0e-992adb306720.htm) | Unloads all patterns, source waveforms, and capture waveforms from a digital pattern instrument. |
| 公共方法 | [UnloadSpecifications](e58a122f-b33d-f1e6-159a-a0fe1c59bf5e.htm) | Unloads the given specifications sheet present in the previously loaded specifications file that you select. |
| 公共方法 | [VForce(Double)](4ee27b17-9519-4347-3a9c-036e14c86981.htm) | Set the PPMU to force voltage to the DUT. You can specify other associated values by properties, such as IClampRange. |
| 公共方法 | [VForce(Double, Double)](36d62a26-e2e9-c394-4371-aa28903c8945.htm) | Set the PPMU to force voltage to the DUI. |
| 公共方法 | [VMeasure](093951e2-a5d8-15e1-4c71-e5717fd2d8b6.htm) | Perform measurement operations at any time, even if you are not forcing current or voltage with the PPMU. |
| 公共方法 | [WaitUntilDone](e4224f24-ce12-4657-56d7-637aa7a9da13.htm) | Waits until the pattern burst has completed or the specified maxTime has expired. |
| 公共方法 | [WriteSequencerFlag](5ca3da79-0fff-ddbf-a00e-30319786fcb8.htm) | Writes a Boolean value to a pattern sequencer flag. |
| 公共方法 | [WriteSequencerRegister](7b27a2c5-e747-2281-21db-4d83a8b3068c.htm) | Writes a value to a pattern sequencer register. |
| 公共方法 | [WriteSourceWaveformBroadcast](c958d865-ae88-9b93-3ebf-99a4abfb472f.htm) | Writes the same source waveform data to all sites. |
| 公共方法 | [WriteSourceWaveformDataFromFile](1e946e49-4973-c678-64c0-4aa26f003757.htm) | Writes a source waveform based on the waveform data and the configuration information the file contains. |
| 公共方法 | [WriteSourceWaveformSiteUnique](69299666-02e1-fa96-553c-74c9f0a0028b.htm) | Writes one source waveform to current site. |
| 公共方法 | [WriteStatic](5478c171-266d-36b6-bbad-30b33516dffe.htm) | Writes a static state to the channels or pins represented by this pin list. These channels or pins remain in the specified state until the next pattern burst or call to this method. |

[Top](#PageHeader)

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### AbortBurst 方法

|  |  |
| --- | --- |
|  | DigitalAbortBurst 方法 |

Stops bursting the pattern.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital AbortBurst()
```

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### AbortClockGenerator 方法

|  |  |
| --- | --- |
|  | DigitalAbortClockGenerator 方法 |

Stops clock generation on the specified channel(s) or pin(s) and pin group(s).

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital AbortClockGenerator()
```

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### AbortKeepAlive 方法

|  |  |
| --- | --- |
|  | DigitalAbortKeepAlive 方法 |

Stops the keep alive pattern if it is currently running.
If a pattern burst is in progress, this method aborts the pattern burst.
If you start a new pattern burst while a keep alive pattern is running, the keep alive pattern runs to the last keep alive vector, and the new pattern burst starts on the next cycle.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital AbortKeepAlive()
```

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ApplyLevelsAndTiming 方法

|  |  |
| --- | --- |
|  | DigitalApplyLevelsAndTiming 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [ApplyLevelsAndTiming(String, String)](446e8be1-da3d-4b53-7c9f-30d554790cf3.htm) | Applies digital levels and timing defined in the loaded levels and timing sheets. |
| 公共方法 | [ApplyLevelsAndTiming(String, String, String, String, String)](7b9bde6d-39ac-a0ef-9a05-5426aa4a4d01.htm) | Applies digital levels and timing defined in the loaded levels and timing sheets. |

[Top](#PageHeader)

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### ApplyLevelsAndTiming(String, String) 方法

|  |  |
| --- | --- |
|  | DigitalApplyLevelsAndTiming(String, String) 方法 |

Applies digital levels and timing defined in the loaded levels and timing sheets.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital ApplyLevelsAndTiming(
	string levelsFilePath,
	string timingFilePath
)
```

###### 参数

levelsFilePath  String
:   Use the name of the sheet or pass the absolute file path used in the LoadLevels(String) method. The name of the levels sheet is the file name without the directory and the file extension.

timingFilePath  String
:   Use the name of the sheet or pass the absolute file path that you used in the LoadTiming(String) method. The name of the timing sheet is the file name without the directory and file extension.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[ApplyLevelsAndTiming 重载](fa0dd550-a950-fa19-20e0-3847bc608441.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### ApplyLevelsAndTiming(String, String, String, String, String) 方法

|  |  |
| --- | --- |
|  | DigitalApplyLevelsAndTiming(String, String, String, String, String) 方法 |

Applies digital levels and timing defined in the loaded levels and timing sheets.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital ApplyLevelsAndTiming(
	string levelsFilePath,
	string timingFilePath,
	string initialStateHighPins,
	string initialStateLowPins,
	string initialStateTristatePins
)
```

###### 参数

levelsFilePath  String
:   Use the name of the sheet or pass the absolute file path used in the LoadLevels(String) method. The name of the levels sheet is the file name without the directory and the file extension.

timingFilePath  String
:   Use the name of the sheet or pass the absolute file path that you used in the LoadTiming(String) method. The name of the timing sheet is the file name without the directory and file extension.

initialStateHighPins  String
:   Comma-delimited list of pins, pin groups, or channels to initialize to a high state.

initialStateLowPins  String
:   Comma-delimited list of pins, pin groups, or channels to initialize to a low state.

initialStateTristatePins  String
:   Comma-delimited list of pins, pin groups, or channels to initialize to a non-drive state.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[ApplyLevelsAndTiming 重载](fa0dd550-a950-fa19-20e0-3847bc608441.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ApplyTdrOffsets 方法

|  |  |
| --- | --- |
|  | DigitalApplyTdrOffsets 方法 |

Applies the correction for propagation delay offsets to a digital pattern instrument.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital ApplyTdrOffsets(
	double[] offsets
)
```

###### 参数

offsets  Double
:   The Time-Domain Reflectometry (TDR) offsets to write to the digital pattern instrument.
    you must specify offsets for each site in the channel map per pin.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### BurstPattern 方法

|  |  |
| --- | --- |
|  | DigitalBurstPattern 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [BurstPattern(String)](6a00d5a5-53d1-7c92-c567-e8556bceed90.htm) | Bursts the pattern on the sites you specify, waits for the burst to complete, and returns comparison results for current site. |
| 公共方法 | [BurstPattern(String, Boolean, Double)](89e23eea-5c46-6273-c333-6f3aed75df49.htm) | Bursts the pattern on the sites you specify, waits for the burst to complete, and returns comparison results for current site. |
| 公共方法 | [BurstPattern(String, Boolean, Boolean, Double)](1bf58a23-7f26-1313-9967-a1cb35bd4ef9.htm) | Bursts the pattern on the site you specify, waits for the burst to complete, and returns comparison results for current site. |

[Top](#PageHeader)

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### BurstPattern(String) 方法

|  |  |
| --- | --- |
|  | DigitalBurstPattern(String) 方法 |

Bursts the pattern on the sites you specify, waits for the burst to complete, and returns comparison results for current site.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public bool BurstPattern(
	string startLabel
)
```

###### 参数

startLabel  String
:   The pattern name or exported pattern label from which to start bursting the pattern.

###### 返回值

Boolean  
Boolean value for current site. true, if the site passed; false, if the site failed.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[BurstPattern 重载](2087b755-da22-a92f-4495-e234a24962c7.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### BurstPattern(String, Boolean, Double) 方法

|  |  |
| --- | --- |
|  | DigitalBurstPattern(String, Boolean, Double) 方法 |

Bursts the pattern on the sites you specify, waits for the burst to complete, and returns comparison results for current site.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public bool BurstPattern(
	string startLabel,
	bool selectDigitalFunction,
	double timeout
)
```

###### 参数

startLabel  String
:   The pattern name or exported pattern label from which to start bursting the pattern.

selectDigitalFunction  Boolean
:   If true, sets the SelectedFunction of the pins to Digital.

timeout  Double
:   The maximum time interval allowed for the pattern burst to complete.

###### 返回值

Boolean  
Boolean value for current site. true, if the site passed; false, if the site failed.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[BurstPattern 重载](2087b755-da22-a92f-4495-e234a24962c7.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### BurstPattern(String, Boolean, Boolean, Double) 方法

|  |  |
| --- | --- |
|  | DigitalBurstPattern(String, Boolean, Boolean, Double) 方法 |

Bursts the pattern on the site you specify, waits for the burst to complete, and returns comparison results for current site.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital BurstPattern(
	string startLabel,
	bool selectDigitalFunction,
	bool waitUntilDone,
	double timeout
)
```

###### 参数

startLabel  String
:   The pattern name or exported pattern label from which to start bursting the pattern.

selectDigitalFunction  Boolean
:   If true, sets the SelectedFunction of the pins to Digital.

waitUntilDone  Boolean
:   If true, waits until the pattern burst is completed; otherwise, initiates a pattern burst and returns.

timeout  Double
:   The maximum time interval allowed for the pattern burst to complete.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[BurstPattern 重载](2087b755-da22-a92f-4495-e234a24962c7.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureActiveLoadLevels 方法

|  |  |
| --- | --- |
|  | DigitalConfigureActiveLoadLevels 方法 |

Configures the Ioh, Iol, and Vcom values.
The DUT sources or sinks current based on the level values.
To enable active load, set the termination mode to ActiveLoad.
To disable active load, set the termination mode of the instrument to HighZ or Vterm.
These properties are only applicable if the pinset's SelectedFunction is set to Digital and TerminationMode is set to ActiveLoad.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital ConfigureActiveLoadLevels(
	double iol,
	double ioh,
	double vcom
)
```

###### 参数

iol  Double
:   The current that the DUT sinks from the active load while outputting a voltage below Vcom.

ioh  Double
:   The current that the DUT sources to the active load while outputting a voltage above Vcom.

vcom  Double
:   The commutating voltage at which the active load circuit switches between between sourcing current and sinking current.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureCompareStrobeEdge 方法

|  |  |
| --- | --- |
|  | DigitalConfigureCompareStrobeEdge 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [ConfigureCompareStrobeEdge(String, Double)](b286bb79-e6d1-84d4-38b9-2cf5af248b04.htm) | Configures the strobe edge time for the specified pins. |
| 公共方法 | [ConfigureCompareStrobeEdge(String, Double, Double)](22bf36b4-118b-f056-e4fe-e335669ed9a3.htm) | Configures the strobe edge times for the specified pins. |

[Top](#PageHeader)

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### ConfigureCompareStrobeEdge(String, Double) 方法

|  |  |
| --- | --- |
|  | DigitalConfigureCompareStrobeEdge(String, Double) 方法 |

Configures the strobe edge time for the specified pins.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital ConfigureCompareStrobeEdge(
	string timeSetName,
	double strobeEdge
)
```

###### 参数

timeSetName  String
:   The time set name.

strobeEdge  Double
:   The time within a vector period when the comparison happens.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[ConfigureCompareStrobeEdge 重载](81c0a6bf-0044-b460-90b4-bc9f62e559a6.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### ConfigureCompareStrobeEdge(String, Double, Double) 方法

|  |  |
| --- | --- |
|  | DigitalConfigureCompareStrobeEdge(String, Double, Double) 方法 |

Configures the strobe edge times for the specified pins.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital ConfigureCompareStrobeEdge(
	string timeSetName,
	double strobeEdge,
	double strobe2Edge
)
```

###### 参数

timeSetName  String
:   The time set name.

strobeEdge  Double
:   The time within a vector period when the comparison happens.

strobe2Edge  Double
:   The time when the comparison happens for the second DUT cycle within a vector period.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[ConfigureCompareStrobeEdge 重载](81c0a6bf-0044-b460-90b4-bc9f62e559a6.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureDigitalEdgeTrigger 方法

|  |  |
| --- | --- |
|  | DigitalConfigureDigitalEdgeTrigger 方法 |

Configures the TriggerType to DigitalEdge, and configures the source and Edge properties.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital ConfigureDigitalEdgeTrigger(
	string triggerClass,
	string source,
	string edgeType
)
```

###### 参数

triggerClass  String
:   "Start" or "ConditionalJump",
    "Start" configure and control start triggers,
    "ConditionalJump" configure and control conditional jump triggers.

source  String
:   The default value is an empty string ("").

edgeType  String
:   "Rising" or "Falling". The default value is Rising.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureDriveEdges 方法

|  |  |
| --- | --- |
|  | DigitalConfigureDriveEdges 方法 |

Configures the drive format and the drive edge placement for the specified pins.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital ConfigureDriveEdges(
	string timeSetName,
	string format,
	double driveOnEdge,
	double driveDataEdge,
	double driveReturnEdge,
	double driveOffEdge
)
```

###### 参数

timeSetName  String
:   The time set name.

format  String
:   The drive format of the time set. "NonReturn", "ReturnToLow", "ReturnToHigh" or "SurroundByComplement".

driveOnEdge  Double
:   The delay from the beginning of the vector period for turning on the pin driver.

driveDataEdge  Double
:   The delay from the beginning of the vector period until the pattern data is driven to the pattern value. The ending state from the previous vector persists until this point.

driveReturnEdge  Double
:   The delay from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format.

driveOffEdge  Double
:   The delay from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive PinState (L, H, X, V, M, E).

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureDriveFormat 方法

|  |  |
| --- | --- |
|  | DigitalConfigureDriveFormat 方法 |

Configures the drive format of a time set.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital ConfigureDriveFormat(
	string timeSetName,
	string driveFormat
)
```

###### 参数

timeSetName  String
:   The time set name.

driveFormat  String
:   The drive format of the time set. "NonReturn", "ReturnToLow", "ReturnToHigh" or "SurroundByComplement".

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureDriverEdges 方法

|  |  |
| --- | --- |
|  | DigitalConfigureDriverEdges 方法 |

Configures the drive format and the drive edge placement for the specified pins.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital ConfigureDriverEdges(
	string timeSetName,
	string format,
	double driveOnEdge,
	double driveDataEdge,
	double driveReturnEdge,
	double driveOffEdge,
	double driveData2Edge,
	double driveReturn2Edge
)
```

###### 参数

timeSetName  String
:   The time set name.

format  String
:   The drive format of the time set. "NonReturn", "ReturnToLow", "ReturnToHigh" or "SurroundByComplement".

driveOnEdge  Double
:   The delay from the beginning of the vector period for turning on the pin driver.

driveDataEdge  Double
:   The delay from the beginning of the vector period until the pattern data is driven to the pattern value. The ending state from the previous vector persists until this point.

driveReturnEdge  Double
:   The delay from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format.

driveOffEdge  Double
:   The delay from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive PinState (L, H, X, V, M, E).

driveData2Edge  Double
:   The delay from the beginning of the vector period until the pattern data is driven to the second pattern value.

driveReturn2Edge  Double
:   The delay from the beginning of the vector period until the pin changes from the second pattern data to the return value, as specified in the format.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureEdge 方法

|  |  |
| --- | --- |
|  | DigitalConfigureEdge 方法 |

Configures the edge of a time set.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital ConfigureEdge(
	string timeSetName,
	string edge,
	double time
)
```

###### 参数

timeSetName  String
:   The time set name.

edge  String
:   The edge of the time set to configure.
    "DriveOn", "DriveData", "DriveReturn", "DriveOff", "CompareStrobe", "DriveData2", "DriveReturn2", "CompareStrobe2".

time  Double
:   The time of the edge to configure.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureEdgeMultiplier 方法

|  |  |
| --- | --- |
|  | DigitalConfigureEdgeMultiplier 方法 |

Configures the edge multiplier of a time set.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital ConfigureEdgeMultiplier(
	string timeSetName,
	int edgeMultiplier
)
```

###### 参数

timeSetName  String
:   The time set name.

edgeMultiplier  Int32
:   1 or 2, the edge multiplier of the time set.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureHistoryRamCycleNumberTrigger 方法

|  |  |
| --- | --- |
|  | DigitalConfigureHistoryRamCycleNumberTrigger 方法 |

Configures the TriggerType to CycleNumber and configures Number and PretriggerSamples.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital ConfigureHistoryRamCycleNumberTrigger(
	long cycleNumber,
	int pretriggerSamples
)
```

###### 参数

cycleNumber  Int64
:   The cycle number to execute before the History RAM trigger. Use this property when TriggerType is set to CycleNumber. The default value is 0.

pretriggerSamples  Int32
:   The number of samples to acquire before the History RAM trigger. The default value is 0.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureHistoryRamFirstFailureTrigger 方法

|  |  |
| --- | --- |
|  | DigitalConfigureHistoryRamFirstFailureTrigger 方法 |

Configures the TriggerType to FirstFailure and configures PretriggerSamples.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital ConfigureHistoryRamFirstFailureTrigger(
	int pertriggerSamples
)
```

###### 参数

pertriggerSamples  Int32
:   The number of samples to acquire before the DigitalHistoryRamTrigger.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureHistoryRamPatternLabelTrigger 方法

|  |  |
| --- | --- |
|  | DigitalConfigureHistoryRamPatternLabelTrigger 方法 |

Configures the TriggerType to PatternLabel and configures Label, VectorOffset, CycleOffset, and PretriggerSamples.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital ConfigureHistoryRamPatternLabelTrigger(
	string label,
	long vectorOffset,
	long cycleOffset,
	int pretriggerSamples
)
```

###### 参数

label  String
:   Pattern label to augment by the vector and cycle offset where History RAM will start acquiring pattern information.

vectorOffset  Int64
:   The value at which to set VectorOffset.

cycleOffset  Int64
:   The value at which to set CycleOffset.

pretriggerSamples  Int32
:   The number of samples to acquire before the DigitalHistoryRamTrigger.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureIClamp 方法

|  |  |
| --- | --- |
|  | DigitalConfigureIClamp 方法 |

Configure the sourced and sunk current clamp value.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital ConfigureIClamp(
	double high,
	double low
)
```

###### 参数

high  Double
:   The clamp value for current sourced.

low  Double
:   The clamp value for current sunk.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureSoftwareTrigger 方法

|  |  |
| --- | --- |
|  | DigitalConfigureSoftwareTrigger 方法 |

Configures the TriggerType for Software triggering.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital ConfigureSoftwareTrigger(
	string triggerClass
)
```

###### 参数

triggerClass  String
:   "Start" or "ConditionalJump",
    "Start" configure and control start triggers,
    "ConditionalJump" configure and control conditional jump triggers.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureVClamp 方法

|  |  |
| --- | --- |
|  | DigitalConfigureVClamp 方法 |

Configure the maximum and minimum voltage limit.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital ConfigureVClamp(
	double high,
	double low
)
```

###### 参数

high  Double
:   The maximum voltage limit.

low  Double
:   The minimum voltage limit.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureVoltageLevels 方法

|  |  |
| --- | --- |
|  | DigitalConfigureVoltageLevels 方法 |

Configures the high and low logic levels for voltage as well as the termination mode input voltage.
These voltages apply to the pin list when the SelectedFunction is Digital.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital ConfigureVoltageLevels(
	double vil,
	double vih,
	double vol,
	double voh,
	double vterm
)
```

###### 参数

vil  Double
:   The input voltage that the digital pattern instrument applies to the input of the DUT when the test instrument drives a logic low (0).

vih  Double
:   The input voltage that the digital pattern instrument applies to the input of the DUT when the test instrument drives a logic high (1).

vol  Double
:   The output voltage from the DUT below which the comparator on the test instrument interprets a logic low (L).

voh  Double
:   The output voltage from the DUT above which the comparator on the test instrument interprets a logic high (H).

vterm  Double
:   The termination voltage.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### CreateCaptureWaveformFromFile 方法

|  |  |
| --- | --- |
|  | DigitalCreateCaptureWaveformFromFile 方法 |

Creates a capture waveform using the configuration information from a .digicapture file.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital CreateCaptureWaveformFromFile(
	string waveformName,
	string waveformFilePath
)
```

###### 参数

waveformName  String
:   Specifies the waveform name to use from the file. You must specify a waveform name if the file contains multiple waveforms. Use the waveformName with the capture\_start opcode in your pattern.

waveformFilePath  String
:   Specifies the absolute file path to the capture waveform file (.digicapture) to load.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### CreateCaptureWaveformParallel 方法

|  |  |
| --- | --- |
|  | DigitalCreateCaptureWaveformParallel 方法 |

Creates the capture waveform settings for parallel acquisition using a comma-delimited string of pins or channels.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital CreateCaptureWaveformParallel(
	string waveformName
)
```

###### 参数

waveformName  String
:   Specifies the waveform name to use. Use the waveformName with the capture\_start opcode in your pattern.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### CreateCaptureWaveformSerial 方法

|  |  |
| --- | --- |
|  | DigitalCreateCaptureWaveformSerial 方法 |

Creates the capture waveform settings for serial acquisition using a comma-delimited string of pins or channels.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital CreateCaptureWaveformSerial(
	string waveformName,
	uint sampleWidth,
	string bitOrder
)
```

###### 参数

waveformName  String
:   Specifies the waveform name to use. Use the waveformName with the capture\_start opcode in your pattern.

sampleWidth  UInt32
:   The width in bits of each serial sample. Valid values are between 1 and 32.

bitOrder  String
:   The order in which to shift the bits. This can be most significant bit first or least significant bit first.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### CreateChannelMap 方法

|  |  |
| --- | --- |
|  | DigitalCreateChannelMap 方法 |

Creates a channel map, which translates the pin maps and sites to the instrument channels. You must create the pin map using CreatePinMap() before calling this method.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital CreateChannelMap(
	int numberOfSites
)
```

###### 参数

numberOfSites  Int32
:   Number of sites in the channel map.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### CreatePinGroup 方法

|  |  |
| --- | --- |
|  | DigitalCreatePinGroup 方法 |

Creates a pin group with the specified name. The pin group serves as an alias for a list of pins.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital CreatePinGroup(
	string pinGroupName,
	string[] pins
)
```

###### 参数

pinGroupName  String
:   The name of pin group.

pins  String
:   A one-dimensional array of strings that contains pin(s), pin group(s), and/or channel(s) to include in the pin group.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### CreatePinMap 方法

|  |  |
| --- | --- |
|  | DigitalCreatePinMap 方法 |

Creates and loads a pin map. Use this method if you are not loading a pin map file using LoadPinMap().

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital CreatePinMap(
	string[] dutPins,
	string[] systemPins
)
```

###### 参数

dutPins  String
:   An array of DUT pin names to include in the pin map. DUT pins are duplicated for all sites and are used in patterns.

systemPins  String
:   An array of system pin names to include in the pin map. System pins do not scale with the number of sites and are not used with pattern functions.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### CreateSourceWaveformFromFile 方法

|  |  |
| --- | --- |
|  | DigitalCreateSourceWaveformFromFile 方法 |

Creates the source waveform settings used to source waveforms with configuration information contained in a .tdms file.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital CreateSourceWaveformFromFile(
	string waveformName,
	string waveformFilePath,
	bool writeWaveformData
)
```

###### 参数

waveformName  String
:   Specifies the waveform name to use from the file. You must specify a waveform name if the file contains multiple waveforms. Use the waveformName with the source\_start opcode in your pattern.

waveformFilePath  String
:   Specifies the absolute file path to the source waveform file (.tdms).

writeWaveformData  Boolean
:   Writes waveform data to source memory if true and the waveform data is in the file.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### CreateSourceWaveformParallel 方法

|  |  |
| --- | --- |
|  | DigitalCreateSourceWaveformParallel 方法 |

Creates source waveform settings used to source parallel data using a comma-delimited string of pins or channels.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital CreateSourceWaveformParallel(
	string waveformName,
	string dataMapping
)
```

###### 参数

waveformName  String
:   The name of the waveform to use in the pattern file. Waveform names must be unique. Use this waveformName with the source\_start opcode in your pattern.

dataMapping  String
:   "Broadcast" or "SiteUnique", Specifies whether the waveform is broadcast to all sites or a unique waveform is sourced per site.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### CreateSourceWaveformSerial 方法

|  |  |
| --- | --- |
|  | DigitalCreateSourceWaveformSerial 方法 |

Creates the source waveform settings used to source serial waveforms using a comma-delimited string of pins or channels.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital CreateSourceWaveformSerial(
	string waveformName,
	string dataMapping,
	uint sampleWidth,
	string bitOrder
)
```

###### 参数

waveformName  String
:   The name of the waveform to use in the pattern file. Waveform names must be unique. Use the waveformName with source\_start opcode in your pattern.

dataMapping  String
:   "Broadcast" or "SiteUnique", Specifies whether the waveform is broadcast to all sites or a unique waveform is sourced per site.

sampleWidth  UInt32
:   The width in bits of each serial sample. Valid values are between 1 and 32.

bitOrder  String
:   "MostSignificantBitFirst" or "LeastSignificantBitFirst". "MostSignificantBitFirst" is the default value.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### CreateTimeSet 方法

|  |  |
| --- | --- |
|  | DigitalCreateTimeSet 方法 |

Creates a DigitalTimeSet. Use this method to create time set values after applying a timing sheet with ApplyLevelsAndTiming(), or to create time sets programmatically without the use of timing sheets.
This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to ApplyLevelsAndTiming(), it only affects the values of the current timing context.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital CreateTimeSet(
	string timeSetName
)
```

###### 参数

timeSetName  String
:   The time set name.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### DeleteAllTimeSets 方法

|  |  |
| --- | --- |
|  | DigitalDeleteAllTimeSets 方法 |

Deletes all loaded and created time sets.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital DeleteAllTimeSets()
```

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### DisableSites 方法

|  |  |
| --- | --- |
|  | DigitalDisableSites 方法 |

Disables the specified sites

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital DisableSites(
	string siteList
)
```

###### 参数

siteList  String
:   A comma-delimited list of strings of the form siteN, where N is the site number. All sites are disabled if the string is empty.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### DisableTrigger 方法

|  |  |
| --- | --- |
|  | DigitalDisableTrigger 方法 |

Disables a previously configured trigger and sets TriggerType to None.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital DisableTrigger(
	string triggerClass
)
```

###### 参数

triggerClass  String
:   "Start" or "ConditionalJump",
    "Start" configure and control start triggers,
    "ConditionalJump" configure and control conditional jump triggers.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### EnableSites 方法

|  |  |
| --- | --- |
|  | DigitalEnableSites 方法 |

Enables the specified sites.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital EnableSites(
	string siteList
)
```

###### 参数

siteList  String
:   A comma-delimited list of strings of the form siteN, where N is the site number. All sites are enabled if the string is empty.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### EndChannelMap 方法

|  |  |
| --- | --- |
|  | DigitalEndChannelMap 方法 |

Completes the channel map configuration. No further changes can be made to the channel map or connections after calling this method.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital EndChannelMap()
```

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ExecuteArrayToDictionary&lt;T1, T2&gt; 方法

|  |  |
| --- | --- |
|  | DigitalExecuteArrayToDictionaryT1, T2 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
protected override Dictionary<string, T2> ExecuteArrayToDictionary<T1, T2>(
	MethodDescription<T1, T2[]> method,
	params Object[] args
)
```

###### 参数

method  MethodDescriptionT1, T2

args  Object

###### 类型参数

T1

T2

###### 返回值

DictionaryString, T2

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ExecuteNoReturnMethod&lt;T1, T2&gt; 方法

|  |  |
| --- | --- |
|  | DigitalExecuteNoReturnMethodT1, T2 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
protected override T2 ExecuteNoReturnMethod<T1, T2>(
	NoReturnMethodDescription<T1> method,
	params Object[] args
)
```

###### 参数

method  NoReturnMethodDescriptionT1

args  Object

###### 类型参数

T1

T2

###### 返回值

T2

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ExecuteSimpleToDictionary&lt;T1, T2&gt; 方法

|  |  |
| --- | --- |
|  | DigitalExecuteSimpleToDictionaryT1, T2 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
protected override Dictionary<string, T2> ExecuteSimpleToDictionary<T1, T2>(
	MethodDescription<T1, T2> method,
	params Object[] args
)
```

###### 参数

method  MethodDescriptionT1, T2

args  Object

###### 类型参数

T1

T2

###### 返回值

DictionaryString, T2

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ExecuteToMeasStationOnce&lt;T1, T2&gt; 方法

|  |  |
| --- | --- |
|  | DigitalExecuteToMeasStationOnceT1, T2 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
protected Digital ExecuteToMeasStationOnce<T1, T2>(
	NoReturnMethodDescription<T1> method,
	params Object[] args
)
```

###### 参数

method  NoReturnMethodDescriptionT1

args  Object

###### 类型参数

T1

T2

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ExportSignal 方法

|  |  |
| --- | --- |
|  | DigitalExportSignal 方法 |

Routes trigger and event signals to the specified outputTerminal.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital ExportSignal(
	string signal,
	string signalIdentifier,
	string outputTerminal
)
```

###### 参数

signal  String
:   The type of signal to export. "StartTrigger", "ConditionalJumpTrigger", "PatternOpcodeEvent".

signalIdentifier  String
:   The instance of the selected signal to export. Possible values include "patternOpcodeEvent0", "patternOpcodeEvent1", "patternOpcodeEvent2", or "patternOpcodeEvent3".

outputTerminal  String
:   The terminal to which to export the signal. Possible values include but are not limited to "PXI\_Trig0", "PXI\_Trig1", "PXI\_Trig2", "PXI\_Trig3", "PXI\_Trig4", "PXI\_Trig5", "PXI\_Trig6" or "PXI\_Trig7".

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### FetchCaptureWaveform 方法

|  |  |
| --- | --- |
|  | DigitalFetchCaptureWaveform 方法 |

Fetches a defined number of samples for current site.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public uint[] FetchCaptureWaveform(
	string waveformName,
	int samplesToRead,
	double timeout
)
```

###### 参数

waveformName  String
:   The name of the waveform to fetch. Use the waveformName with the capture\_start opcode in your pattern.

samplesToRead  Int32
:   The number of samples to fetch. Use -1 to fetch all samples after the pattern is finished bursting.

timeout  Double
:   The maximum amount of time allowed for this method to complete in seconds. An exception is thrown if the method does not complete within this time span.

###### 返回值

UInt32  
The captured data for current site. If a site is disabled, not enabled for burst, or the current instrument does not include any capture pins, the method does not return data for that site.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### FetchHistoryRamCycleInformation 方法

|  |  |
| --- | --- |
|  | DigitalFetchHistoryRamCycleInformation 方法 |

Fetches the pattern information acquired for the specified History RAM samples.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string[] FetchHistoryRamCycleInformation(
	long position
)
```

###### 参数

position  Int64
:   The position from which to start fetching pattern information.

###### 返回值

String  
Provides pattern information for the specified History RAM samples.
String format as below
"{PatternName:new\_pattern,TimeSetName:tset0,VectorNumber:0,CycleNumber:1,ExpectedPinStates:[X,X,X,X],ActualPinStates:[L,L,L,L],PerPinPassFail:[true,true,true,true]}".

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### FetchHistoryRamScanCycleNumber 方法

|  |  |
| --- | --- |
|  | DigitalFetchHistoryRamScanCycleNumber 方法 |

Fetches the scan cycle numbers acquired for the specified History RAM samples.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public long[] FetchHistoryRamScanCycleNumber(
	long position
)
```

###### 参数

position  Int64
:   The position from which to start fetching pattern information.

###### 返回值

Int64  
An array of scan cycle numbers for the specified History RAM samples.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GenerateClock 方法

|  |  |
| --- | --- |
|  | DigitalGenerateClock 方法 |

Configures and initiates clock generation on the specified channel(s), or pin(s) and pin group(s).

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital GenerateClock(
	double frequency,
	bool selectDigitalFunction
)
```

###### 参数

frequency  Double
:   Specifies the clock frequency in Hz.

selectDigitalFunction  Boolean
:   If true, sets the SelectedFunction of the pins to Digital.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetAllowExtendedVoltageRange 方法

|  |  |
| --- | --- |
|  | DigitalGetAllowExtendedVoltageRange 方法 |

Gets whether the instrument is allowed to operate in the extended voltage range where instrument specifications may differ from standard ranges.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> GetAllowExtendedVoltageRange()
```

###### 返回值

DictionaryString, Boolean  
Key: pin name.
Value: the value decide whether the instrument is allowed extend voltage range. The default value is false.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetApertureTime 方法

|  |  |
| --- | --- |
|  | DigitalGetApertureTime 方法 |

Gets the measurement aperture time for the PPMU.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetApertureTime()
```

###### 返回值

DictionaryString, Double  
Key: pin name.
Value: The measurement aperture time for the PPMU. The default value is 4e-6.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetDriveFormat 方法

|  |  |
| --- | --- |
|  | DigitalGetDriveFormat 方法 |

Gets the drive format of a time set.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetDriveFormat(
	string timeSetName
)
```

###### 参数

timeSetName  String
:   The time set name.

###### 返回值

DictionaryString, String  
Key: pin name.
Value: The drive format of the time set to get. "NonReturn", "ReturnToLow", "ReturnToHigh" or "SurroundByComplement".

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetEdge 方法

|  |  |
| --- | --- |
|  | DigitalGetEdge 方法 |

Gets the edge time of a time set.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetEdge(
	string timeSetName,
	string edge
)
```

###### 参数

timeSetName  String
:   The time set name.

edge  String
:   The edge of the time set to get.
    "DriveOn", "DriveData", "DriveReturn", "DriveOff", "CompareStrobe", "DriveData2", "DriveReturn2", "CompareStrobe2".

###### 返回值

DictionaryString, Double  
Key: pin name.
Value: seconds.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetEdgeMultiplier 方法

|  |  |
| --- | --- |
|  | DigitalGetEdgeMultiplier 方法 |

Gets the edge multiplier of a time set.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, int> GetEdgeMultiplier(
	string timeSetName
)
```

###### 参数

timeSetName  String
:   The time set name.

###### 返回值

DictionaryString, Int32  
A dictionary collection of the edge multiplier of the time set. The key of the collection is pin name, the value is multisite result of 1 or 2.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetHistoryRamBufferSizePerSite 方法

|  |  |
| --- | --- |
|  | DigitalGetHistoryRamBufferSizePerSite 方法 |

Gets the size, in samples, of the in-memory History RAM buffer. You can use this property when the instrument is configured for continuous History RAM acquisition.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, long> GetHistoryRamBufferSizePerSite()
```

###### 返回值

DictionaryString, Int64  
Key: pin name.
Value: The size of the per-site History RAM sample buffer.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetHistoryRamCyclesToAcquire 方法

|  |  |
| --- | --- |
|  | DigitalGetHistoryRamCyclesToAcquire 方法 |

Gets which cycles History RAM acquires after the trigger conditions are met. If you configure History RAM to acquire only failed samples, you must set the pretrigger samples for History RAM to 0.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetHistoryRamCyclesToAcquire()
```

###### 返回值

DictionaryString, String  
Key: pin name.
Value: "Failed" or "All".

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetHistoryRamFailCount 方法

|  |  |
| --- | --- |
|  | DigitalGetHistoryRamFailCount 方法 |

Gets the number of samples History RAM acquired on the last pattern burst.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public long GetHistoryRamFailCount()
```

###### 返回值

Int64  
The History RAM fail count for the current site.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetHistoryRamMaxSamplesToAcquire 方法

|  |  |
| --- | --- |
|  | DigitalGetHistoryRamMaxSamplesToAcquire 方法 |

Gets the maximum number of History RAM samples to acquire per site. If the property is set to -1, it will acquire until the History RAM buffer is full.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, int> GetHistoryRamMaxSamplesToAcquire()
```

###### 返回值

DictionaryString, Int32  
Key: pin name.
Value: The maximum History RAM samples to acquire per site.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetHistoryRamNumberOfSamplesIsFinite 方法

|  |  |
| --- | --- |
|  | DigitalGetHistoryRamNumberOfSamplesIsFinite 方法 |

Gets whether the instrument acquires a finite number of History RAM samples or acquires samples continuously. When the instrument acquires samples continuously, you can fetch samples during the pattern burst.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, bool> GetHistoryRamNumberOfSamplesIsFinite()
```

###### 返回值

DictionaryString, Boolean  
Key: pin name.
Value: true, if the number of captured History RAM samples is finite; otherwise, false.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetIClamp 方法

|  |  |
| --- | --- |
|  | DigitalGetIClamp 方法 |

Gets the valid range, in amps, to which the current limit can be set while the PPMU forces voltage to the DUT.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetIClamp()
```

###### 返回值

DictionaryString, Double  
Key: pin name.
Value: Maximum current in amps that can be set.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetIClampSink 方法

|  |  |
| --- | --- |
|  | DigitalGetIClampSink 方法 |

Gets the clamp value for current sunk by the instrument.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetIClampSink()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of current sunk clamp value. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetIClampSource 方法

|  |  |
| --- | --- |
|  | DigitalGetIClampSource 方法 |

Gets the clamp value for current sourced by the instrument.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetIClampSource()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of current soured clamp value. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetIForceLevel 方法

|  |  |
| --- | --- |
|  | DigitalGetIForceLevel 方法 |

Gets the current level, in amps, that the PPMU forces to the DUT.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetIForceLevel()
```

###### 返回值

DictionaryString, Double  
Key: pin name.
Value: The current leve in amps, forced to the DUT.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetILevelRange 方法

|  |  |
| --- | --- |
|  | DigitalGetILevelRange 方法 |

Gets the range of valid values for the current level, in amps, that the PPMU forces to the DUT.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetILevelRange()
```

###### 返回值

DictionaryString, Double  
Key: pin name.
Value: The valid range for the current level in amps forced to the DUT.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetIoh 方法

|  |  |
| --- | --- |
|  | DigitalGetIoh 方法 |

Gets the current that the DUT sources to the active load while outputting a voltage above Vcom.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetIoh()
```

###### 返回值

DictionaryString, Double  
Key: pin name.
Value: The current that the DUT sources to the active load while outputting a voltage above Vcom.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetIol 方法

|  |  |
| --- | --- |
|  | DigitalGetIol 方法 |

Gets the current that the DUT sinks from the active load while outputting a voltage below Vcom.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetIol()
```

###### 返回值

DictionaryString, Double  
Key: pin name.
Value: The current that the DUT sinks while outputting voltage below Vcom.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetOutputFunction 方法

|  |  |
| --- | --- |
|  | DigitalGetOutputFunction 方法 |

Gets whether the PPMU sources DC voltage or DC current.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetOutputFunction()
```

###### 返回值

DictionaryString, String  
A dictionary collection of output function. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetPatternIsDone 方法

|  |  |
| --- | --- |
|  | DigitalGetPatternIsDone 方法 |

Gets a value that indicates whether the pattern burst completed or if any errors have occurred.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public bool GetPatternIsDone()
```

###### 返回值

Boolean  
true, if the pattern burst completed; otherwise, false.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetPatternStartLabel 方法

|  |  |
| --- | --- |
|  | DigitalGetPatternStartLabel 方法 |

Gets the pattern name or exported pattern label from which to start bursting the pattern.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public string GetPatternStartLabel()
```

###### 返回值

String  
Multisite result of the pattern name or exported pattern label from which to start bursting the pattern.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetSelectedFunction 方法

|  |  |
| --- | --- |
|  | DigitalGetSelectedFunction 方法 |

Gets the instrument function of this pin list. The changes take effect immediately.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetSelectedFunction()
```

###### 返回值

DictionaryString, String  
Key: pin name.
Value: the function of the pin list.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetSitePassFail 方法

|  |  |
| --- | --- |
|  | DigitalGetSitePassFail 方法 |

Returns a value indicating whether the specified sites passed the comparisons in the pattern burst.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public bool GetSitePassFail()
```

###### 返回值

Boolean  
Boolean value current site, true, if the site passed; false, if the site failed.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetTdrOffsets 方法

|  |  |
| --- | --- |
|  | DigitalGetTdrOffsets 方法 |

Measures propagation delays through cables, connectors, and load boards using Time-Domain Reflectometry (TDR). Optionally, you can apply the offsets to the pins.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double[]> GetTdrOffsets(
	bool applyOffsets,
	string tdrEndpointTermination
)
```

###### 参数

applyOffsets  Boolean
:   Specifies whether to apply the measured TDR offsets. The default value is true. If you need to adjust the measured offsets prior to applying, set this input to false, and call ApplyTdrOffsets() to specify the adjusted TDR offsets values.

tdrEndpointTermination  String
:   "TdrToOpenCircuit" or "TdrToShortToGround".

###### 返回值

DictionaryString, Double  
Key: pin name.
Value: Returns the measured TDR offsets specified in seconds.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetTermMode 方法

|  |  |
| --- | --- |
|  | DigitalGetTermMode 方法 |

Gets the behavior of the pin when pin driver is in a non-drive cycle.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string> GetTermMode()
```

###### 返回值

DictionaryString, String  
A dictionary collection of the behavior. The key of the collection is pin name, the value is multisite result of one of "ActiveLoad", "Vterm", "HighZ".

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetTimeSetFrequency 方法

|  |  |
| --- | --- |
|  | DigitalGetTimeSetFrequency 方法 |

Specifies the frequency. The frequency value determines the length of a digital vector.
Precondition: property period is not set.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetTimeSetFrequency(
	string timeSetName
)
```

###### 参数

timeSetName  String
:   The name of the time set.

###### 返回值

DictionaryString, Double  
A dictionary collection of frequency. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetTimeSetPeriod 方法

|  |  |
| --- | --- |
|  | DigitalGetTimeSetPeriod 方法 |

Gets or sets the period of the time set. The time value determines the length of a digital vector.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetTimeSetPeriod(
	string timeSetName
)
```

###### 参数

timeSetName  String
:   The name of the time set.

###### 返回值

DictionaryString, Double  
Key: pin name.
Value: the period of the time set in seconds.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetVClampHigh 方法

|  |  |
| --- | --- |
|  | DigitalGetVClampHigh 方法 |

Gets the maximum voltage limit, or high clamp voltage (Vch), in volts, at the pin when the PPMU forces current to the DUT.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetVClampHigh()
```

###### 返回值

DictionaryString, Double  
Key: pin name.
Value: maximum voltage limit or high clamp voltage.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetVClampLow 方法

|  |  |
| --- | --- |
|  | DigitalGetVClampLow 方法 |

Gets the minimum voltage limit, or low clamp voltage (Vcl), in volts, at the pin when the PPMU forces current to the DUT.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetVClampLow()
```

###### 返回值

DictionaryString, Double  
Key: pin name.
Value: minimum voltage limit or low clamp voltage

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetVcom 方法

|  |  |
| --- | --- |
|  | DigitalGetVcom 方法 |

Gets the commutating voltage at which the active load circuit switches between between sourcing current and sinking current.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetVcom()
```

###### 返回值

DictionaryString, Double  
Key: pin name.
Value: The commutating voltage at which the DUT switches between Iol and Ioh.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetVForceLevel 方法

|  |  |
| --- | --- |
|  | DigitalGetVForceLevel 方法 |

Gets the voltage level, in volts, that the PPMU forces to the DUT.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetVForceLevel()
```

###### 返回值

DictionaryString, Double  
Key: pin name.
Value: The voltage level in volts forced to the DUT.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetVih 方法

|  |  |
| --- | --- |
|  | DigitalGetVih 方法 |

Gets the input voltage that the digital pattern instrument applies to the input of the DUT when the test instrument drives a logic high (1).

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetVih()
```

###### 返回值

DictionaryString, Double  
Key: pin name.
Value: The input voltage for a logic high input.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetVil 方法

|  |  |
| --- | --- |
|  | DigitalGetVil 方法 |

Gets the input voltage that the digital pattern instrument applies to the input of the DUT when the test instrument drives a logic low (0).

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetVil()
```

###### 返回值

DictionaryString, Double  
Key: pin name.
Value: The input voltage for a logic low output.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetVoh 方法

|  |  |
| --- | --- |
|  | DigitalGetVoh 方法 |

Gets the output voltage from the DUT above which the comparator on the test instrument interprets a logic high (H).

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetVoh()
```

###### 返回值

DictionaryString, Double  
Key: pin name.
Value: The output voltage for a logic high input.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetVol 方法

|  |  |
| --- | --- |
|  | DigitalGetVol 方法 |

Gets the output voltage from the DUT below which the comparator on the test instrument interprets a logic low (L).

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetVol()
```

###### 返回值

DictionaryString, Double  
Key: pin name.
Value: The maximum output voltage for a logic low output.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetVterm 方法

|  |  |
| --- | --- |
|  | DigitalGetVterm 方法 |

Gets the termination voltage the instrument applies during non-drive cycles when the TerminationMode is set to Vterm. The instrument applies the termination voltage through a 50 Ω parallel termination resistance.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> GetVterm()
```

###### 返回值

DictionaryString, Double  
Key: pin name.
Value: The input voltage in Vterm termination mode.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### IForce 方法

|  |  |
| --- | --- |
|  | DigitalIForce 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [IForce(Double)](c12024ba-e180-259d-adb5-33dde5bd2ad6.htm) | Set the PPMU to force current to the DUT. You can specify other associated values by properties, such as ILevelRange, VClampHigh and VClampLow. |
| 公共方法 | [IForce(Double, Double)](5ea8c2ec-3487-2a8c-cd2a-bce5ba329a28.htm) | Set the PPMU to force current to the DUI. |

[Top](#PageHeader)

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### IForce(Double) 方法

|  |  |
| --- | --- |
|  | DigitalIForce(Double) 方法 |

Set the PPMU to force current to the DUT.
You can specify other associated values by properties, such as ILevelRange, VClampHigh and VClampLow.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital IForce(
	double level
)
```

###### 参数

level  Double
:   The current level to force, in amps.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[IForce 重载](199ae5a1-4abc-459b-6bd3-90b8674ec8e3.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### IForce(Double, Double) 方法

|  |  |
| --- | --- |
|  | DigitalIForce(Double, Double) 方法 |

Set the PPMU to force current to the DUI.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital IForce(
	double level,
	double range
)
```

###### 参数

level  Double
:   The current level to force, in amps.

range  Double
:   The range of valid values for the current level, in amps.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[IForce 重载](199ae5a1-4abc-459b-6bd3-90b8674ec8e3.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### IMeasure 方法

|  |  |
| --- | --- |
|  | DigitalIMeasure 方法 |

Measure current while forcing voltage or current with the PPMU.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> IMeasure()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of mesured current. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### Initiate 方法

|  |  |
| --- | --- |
|  | DigitalInitiate 方法 |

Starts the sourcing voltage or current from the PPMU.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital Initiate()
```

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### IsSiteEnabled 方法

|  |  |
| --- | --- |
|  | DigitalIsSiteEnabled 方法 |

Returns whether the specified site is enabled or disabled.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public bool IsSiteEnabled(
	int site
)
```

###### 参数

site  Int32
:   The site to check.

###### 返回值

Boolean  
true, if the site is enabled; false, if the site is disabled.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### LoadAndApply 方法

|  |  |
| --- | --- |
|  | DigitalLoadAndApply 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [LoadAndApply(String)](08ae4755-63aa-e12b-927e-d76837c28750.htm) | Load PinMap, Specifications, Levels, Timings files and Apply Levels and Timing. |
| 公共方法 | [LoadAndApply(String, String, String, String)](e64124d2-9f73-f90e-5082-a6d83c85a3d5.htm) | Load PinMap, Specifications, Levels, Timings files and Apply Levels and Timing. |

[Top](#PageHeader)

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### LoadAndApply(String) 方法

|  |  |
| --- | --- |
|  | DigitalLoadAndApply(String) 方法 |

Load PinMap, Specifications, Levels, Timings files and Apply Levels and Timing.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital LoadAndApply(
	string rootPath
)
```

###### 参数

rootPath  String
:   Provide the root path, which is the digital project path for NI6570.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[LoadAndApply 重载](cbba78e6-3a9f-43cf-8e6d-e092a53ef81a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### LoadAndApply(String, String, String, String) 方法

|  |  |
| --- | --- |
|  | DigitalLoadAndApply(String, String, String, String) 方法 |

Load PinMap, Specifications, Levels, Timings files and Apply Levels and Timing.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital LoadAndApply(
	string pinMapFilePath,
	string specificationsFilePath,
	string levelsFilePath,
	string timingFilePath
)
```

###### 参数

pinMapFilePath  String
:   The absolute file path to the pin map file.

specificationsFilePath  String
:   The absolute file path to the specifications file.

levelsFilePath  String
:   The absolute file path to the pin levels file.

timingFilePath  String
:   The absolute file path to the timing sheet file.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[LoadAndApply 重载](cbba78e6-3a9f-43cf-8e6d-e092a53ef81a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### LoadLevels 方法

|  |  |
| --- | --- |
|  | DigitalLoadLevels 方法 |

Loads a levels sheet from file.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital LoadLevels(
	string levelsFilePath
)
```

###### 参数

levelsFilePath  String
:   The absolute file path to the pin levels file.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### LoadPattern 方法

|  |  |
| --- | --- |
|  | DigitalLoadPattern 方法 |

Loads a pattern to the hardware from a pattern file.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital LoadPattern(
	string filePath
)
```

###### 参数

filePath  String
:   The absolute file path to the pattern file.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### LoadPinMap 方法

|  |  |
| --- | --- |
|  | DigitalLoadPinMap 方法 |

Loads a pin map file.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital LoadPinMap(
	string pinMapFilePath
)
```

###### 参数

pinMapFilePath  String
:   The absolute file path to the pin map file.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### LoadSpecifications 方法

|  |  |
| --- | --- |
|  | DigitalLoadSpecifications 方法 |

Loads a specifications sheet from file.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital LoadSpecifications(
	string specificationsFilePath
)
```

###### 参数

specificationsFilePath  String
:   The absolute file path to the specifications file.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### LoadTiming 方法

|  |  |
| --- | --- |
|  | DigitalLoadTiming 方法 |

Loads one or more time sets from a timing sheet file.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital LoadTiming(
	string timingFilePath
)
```

###### 参数

timingFilePath  String
:   The absolute file path to the timing sheet file.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### MapPinToChannel 方法

|  |  |
| --- | --- |
|  | DigitalMapPinToChannel 方法 |

Maps a pin to a digital pattern instrument channel.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital MapPinToChannel(
	string pin,
	int site,
	string channel
)
```

###### 参数

pin  String
:   The name of the pin.

site  Int32
:   The index of the site of the pin to map. This parameter is ignored if the specified pin is a system pin.

channel  String
:   The name of the channel. Specify channel names using the channel number, for example, "0" or "31." To specify channels used in multi-instrument sessions, use the form PXI1Slot2/0 or PXI1Slot2/31.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### MeasureFrequency 方法

|  |  |
| --- | --- |
|  | DigitalMeasureFrequency 方法 |

Measures the frequency on the specified pins over the measurement time. All pins in the pin list should have the same measurement time.
Ensure that all pins have the selected function set to "Digital".

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> MeasureFrequency(
	double measurementTime
)
```

###### 参数

measurementTime  Double
:   The frequency measurement time. The default value is 1 millisecond.

###### 返回值

DictionaryString, Double  
Key: pin name.
Value: The measurements taken, ordered according to the pinList parameter.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ReadSequencerFlag 方法

|  |  |
| --- | --- |
|  | DigitalReadSequencerFlag 方法 |

Reads the Boolean state of a pattern sequencer flag.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public bool ReadSequencerFlag(
	string flag
)
```

###### 参数

flag  String
:   The name of the pattern sequencer flag to read. Possible values include "seqflag0", "seqflag1", "seqflag2", or "seqflag3".

###### 返回值

Boolean  
The state of the specified pattern sequencer flag.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ReadSequencerRegister 方法

|  |  |
| --- | --- |
|  | DigitalReadSequencerRegister 方法 |

Reads the numeric state of a pattern sequencer register.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public int ReadSequencerRegister(
	string reg
)
```

###### 参数

reg  String
:   Specifies pattern sequencer register to read.

###### 返回值

Int32  
Returns the value read from the specified pattern sequence register.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ReadStatic 方法

|  |  |
| --- | --- |
|  | DigitalReadStatic 方法 |

Reads the current state of comparators for the specified channels or pins.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, string[]> ReadStatic()
```

###### 返回值

DictionaryString, String  
Key: pin name.
Value: An array of digital states in the order specified by the pinList parameter.
Possible values are a logic low pin state (L), a logic high pin state (H), a midband pin state (M), or a value that is above Voh and below Vol, which can occur when you set Vol higher than Voh (V).

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### Reset 方法

|  |  |
| --- | --- |
|  | DigitalReset 方法 |

Reset the instrument session.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital Reset()
```

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ResetDevice 方法

|  |  |
| --- | --- |
|  | DigitalResetDevice 方法 |

Performs a hard reset on the device.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital ResetDevice()
```

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SelfCalibrate 方法

|  |  |
| --- | --- |
|  | DigitalSelfCalibrate 方法 |

Performs a self calibrate on the device.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SelfCalibrate()
```

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SelfTest 方法

|  |  |
| --- | --- |
|  | DigitalSelfTest 方法 |

Performs a self test on the device.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SelfTest()
```

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SendSoftwareTrigger 方法

|  |  |
| --- | --- |
|  | DigitalSendSoftwareTrigger 方法 |

Sends the Software Trigger to a digital pattern instrument, forcing the Trigger to assert, regardless of how the Trigger is configured.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SendSoftwareTrigger(
	string triggerClass
)
```

###### 参数

triggerClass  String
:   "Start" or "ConditionalJump",
    "Start" configure and control start triggers,
    "ConditionalJump" configure and control conditional jump triggers.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetAllowExtendedVoltageRange 方法

|  |  |
| --- | --- |
|  | DigitalSetAllowExtendedVoltageRange 方法 |

Sets whether the instrument is allowed to operate in the extended voltage range where instrument specifications may differ from standard ranges.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetAllowExtendedVoltageRange(
	bool allow
)
```

###### 参数

allow  Boolean
:   true to allow the PPMU to use the extended voltage range, and false to not allow the PPMU to use the extended voltage range. The default value is false.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetApertureTime 方法

|  |  |
| --- | --- |
|  | DigitalSetApertureTime 方法 |

Sets the aperture time for the PPMU measurement.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetApertureTime(
	double apertureTime
)
```

###### 参数

apertureTime  Double
:   The measurement aperture time for the PPMU. The units is seconds.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetHistoryRamBufferSizePerSite 方法

|  |  |
| --- | --- |
|  | DigitalSetHistoryRamBufferSizePerSite 方法 |

Sets the size, in samples, of the in-memory History RAM buffer. You can use this property when the instrument is configured for continuous History RAM acquisition.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetHistoryRamBufferSizePerSite(
	long value
)
```

###### 参数

value  Int64
:   The size of the per-site History RAM sample buffer. The default value is 32000.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetHistoryRamCyclesToAcquire 方法

|  |  |
| --- | --- |
|  | DigitalSetHistoryRamCyclesToAcquire 方法 |

Sets which cycles History RAM acquires after the trigger conditions are met. If you configure History RAM to acquire only failed samples, you must set the pretrigger samples for History RAM to 0.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetHistoryRamCyclesToAcquire(
	string cyclesToAquire
)
```

###### 参数

cyclesToAquire  String
:   "Failed" or "All".

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetHistoryRamMaxSamplesToAcquire 方法

|  |  |
| --- | --- |
|  | DigitalSetHistoryRamMaxSamplesToAcquire 方法 |

Sets the maximum number of History RAM samples to acquire per site. If the property is set to -1, it will acquire until the History RAM buffer is full.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetHistoryRamMaxSamplesToAcquire(
	int value
)
```

###### 参数

value  Int32
:   The maximum History RAM samples to acquire per site. The default value is 0.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetHistoryRamNumberOfSamplesIsFinite 方法

|  |  |
| --- | --- |
|  | DigitalSetHistoryRamNumberOfSamplesIsFinite 方法 |

Sets whether the instrument acquires a finite number of History RAM samples or acquires samples continuously. When the instrument acquires samples continuously, you can fetch samples during the pattern burst.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetHistoryRamNumberOfSamplesIsFinite(
	bool value
)
```

###### 参数

value  Boolean
:   true, if the number of captured History RAM samples is finite; otherwise, false. The default value is true.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetIClamp 方法

|  |  |
| --- | --- |
|  | DigitalSetIClamp 方法 |

Sets the valid range, in amps, to which the current limit can be set while the PPMU forces voltage to the DUT.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetIClamp(
	double range
)
```

###### 参数

range  Double
:   Maximum current in amps that can be set. The default value is 2e-6.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetIClampAutoRange 方法

|  |  |
| --- | --- |
|  | DigitalSetIClampAutoRange 方法 |

自动设置Digital仪表的钳位电流，不会直接施加电流。

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetIClampAutoRange(
	double iForceValue
)
```

###### 参数

iForceValue  Double
:   预计要施加的电流值。

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetIClampSink 方法

|  |  |
| --- | --- |
|  | DigitalSetIClampSink 方法 |

Specifies the clamp value for current sunk by the instrument. As the direction of the current is out of the DUT into the instrument, the value must be positive. This can be used to set different clamp values for sourcing and sinking current.
If the current range is not set explicitly with the irange property, it will be set to the smallest range that covers the specified clamp values to achieve highest possible accuracy.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetIClampSink(
	double value
)
```

###### 参数

value  Double
:   The clamp value for current sunk.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetIClampSource 方法

|  |  |
| --- | --- |
|  | DigitalSetIClampSource 方法 |

Specifies the clamp value for current sourced by the instrument. This can be used to set different clamp values for sourcing and sinking current.
If the current range is not set explicitly with the irange property, it will be set to the smallest range that covers the specified clamp values to achieve highest possible accuracy.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetIClampSource(
	double value
)
```

###### 参数

value  Double
:   The clamp value for current sourced.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetIForceLevel 方法

|  |  |
| --- | --- |
|  | DigitalSetIForceLevel 方法 |

Sets the current level, in amps, that the PPMU forces to the DUT.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetIForceLevel(
	double value
)
```

###### 参数

value  Double
:   The current leve in amps, forced to the DUT. The default value is 0.0.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetILevelAutoRange 方法

|  |  |
| --- | --- |
|  | DigitalSetILevelAutoRange 方法 |

自动设置Digital仪表的电流挡位，不会直接施加电流。

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetILevelAutoRange(
	double iForceValue
)
```

###### 参数

iForceValue  Double
:   预计要施加的电流值。

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetILevelRange 方法

|  |  |
| --- | --- |
|  | DigitalSetILevelRange 方法 |

Sets the range of valid values for the current level, in amps, that the PPMU forces to the DUT.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetILevelRange(
	double range
)
```

###### 参数

range  Double
:   The valid range for the current level in amps forced to the DUT. The default value is 2e-6.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetIoh 方法

|  |  |
| --- | --- |
|  | DigitalSetIoh 方法 |

Sets the current that the DUT sources to the active load while outputting a voltage above Vcom.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetIoh(
	double value
)
```

###### 参数

value  Double
:   The current that the DUT sources to the active load while outputting a voltage above Vcom. The default value is -0.0015.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetIol 方法

|  |  |
| --- | --- |
|  | DigitalSetIol 方法 |

Sets the current that the DUT sinks from the active load while outputting a voltage below Vcom.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetIol(
	double value
)
```

###### 参数

value  Double
:   The current that the DUT sinks while outputting voltage below Vcom.The default value is 0.0015.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetOutputFunction 方法

|  |  |
| --- | --- |
|  | DigitalSetOutputFunction 方法 |

Sets whether the PPMU sources DC voltage or DC current.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetOutputFunction(
	string outputFunction
)
```

###### 参数

outputFunction  String
:   The output of the PPMU as either DC voltage or DC current. The default value is "DCVoltage".

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetPatternStartLabel 方法

|  |  |
| --- | --- |
|  | DigitalSetPatternStartLabel 方法 |

Sets the pattern name or exported pattern label from which to start bursting the pattern.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetPatternStartLabel(
	string label
)
```

###### 参数

label  String
:   The start label used when bursting a pattern.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetSelectedFunction 方法

|  |  |
| --- | --- |
|  | DigitalSetSelectedFunction 方法 |

Sets the instrument function of this pin list. The changes take effect immediately.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetSelectedFunction(
	string function
)
```

###### 参数

function  String
:   The function of this pin list as "Digital", "Ppmu", "Off", or "Disconnect". The default value is "Disconnect".

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetTermMode 方法

|  |  |
| --- | --- |
|  | DigitalSetTermMode 方法 |

Sets the behavior of the pin when pin driver is in a non-drive cycle.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetTermMode(
	string value
)
```

###### 参数

value  String
:   "ActiveLoad", "Vterm", "HighZ"

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetTimeSetFrequency 方法

|  |  |
| --- | --- |
|  | DigitalSetTimeSetFrequency 方法 |

Specifies the frequency. The frequency value determines the length of a digital vector.
Precondition: property period is not set.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetTimeSetFrequency(
	string timeSetName,
	double value
)
```

###### 参数

timeSetName  String
:   The time set name.

value  Double
:   The frequency.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetTimeSetPeriod 方法

|  |  |
| --- | --- |
|  | DigitalSetTimeSetPeriod 方法 |

Gets or sets the period of the time set. The time value determines the length of a digital vector.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetTimeSetPeriod(
	string timeSetName,
	double value
)
```

###### 参数

timeSetName  String
:   The name of the time set.

value  Double
:   The period of the time set in seconds.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetVClampAutoRange 方法

|  |  |
| --- | --- |
|  | DigitalSetVClampAutoRange 方法 |

自动设置Digital仪表的钳位电压值。

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetVClampAutoRange(
	double vClampHigh,
	double vClampLow
)
```

###### 参数

vClampHigh  Double
:   钳位电压高输出。

vClampLow  Double
:   钳位电压低输出。

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetVClampHigh 方法

|  |  |
| --- | --- |
|  | DigitalSetVClampHigh 方法 |

Sets the maximum voltage limit, or high clamp voltage (Vch), in volts, at the pin when the PPMU forces current to the DUT.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetVClampHigh(
	double value
)
```

###### 参数

value  Double
:   Maximum voltage limit or high clamp voltage. The default value is 6.0.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetVClampLow 方法

|  |  |
| --- | --- |
|  | DigitalSetVClampLow 方法 |

Sets the minimum voltage limit, or low clamp voltage (Vcl), in volts, at the pin when the PPMU forces current to the DUT.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetVClampLow(
	double value
)
```

###### 参数

value  Double
:   Minimum voltage limit or low clamp voltage. The default value is -2.0.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetVcom 方法

|  |  |
| --- | --- |
|  | DigitalSetVcom 方法 |

Sets the commutating voltage at which the active load circuit switches between between sourcing current and sinking current.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetVcom(
	double value
)
```

###### 参数

value  Double
:   The commutating voltage at which the DUT switches between Iol and Ioh. The default value is 2.0.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetVForceLevel 方法

|  |  |
| --- | --- |
|  | DigitalSetVForceLevel 方法 |

Sets the voltage level, in volts, that the PPMU forces to the DUT.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetVForceLevel(
	double value
)
```

###### 参数

value  Double
:   The voltage level in volts forced to the DUT. The default value is 0.0.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetVih 方法

|  |  |
| --- | --- |
|  | DigitalSetVih 方法 |

Sets the input voltage that the digital pattern instrument applies to the input of the DUT when the test instrument drives a logic high (1).

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetVih(
	double value
)
```

###### 参数

value  Double
:   The input voltage for a logic high input. The default value is 3.3.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetVil 方法

|  |  |
| --- | --- |
|  | DigitalSetVil 方法 |

Sets the input voltage that the digital pattern instrument applies to the input of the DUT when the test instrument drives a logic low (0).

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetVil(
	double value
)
```

###### 参数

value  Double
:   The input voltage for a logic low output. The default value is 0.0.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetVoh 方法

|  |  |
| --- | --- |
|  | DigitalSetVoh 方法 |

Sets the output voltage from the DUT above which the comparator on the test instrument interprets a logic high (H).

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetVoh(
	double value
)
```

###### 参数

value  Double
:   The output voltage for a logic high input. The default value is 1.7.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetVol 方法

|  |  |
| --- | --- |
|  | DigitalSetVol 方法 |

Sets the output voltage from the DUT below which the comparator on the test instrument interprets a logic low (L).

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetVol(
	double value
)
```

###### 参数

value  Double
:   The maximum output voltage for a logic low output. The default value is 1.6.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetVterm 方法

|  |  |
| --- | --- |
|  | DigitalSetVterm 方法 |

Sets the termination voltage the instrument applies during non-drive cycles when the TerminationMode is set to Vterm. The instrument applies the termination voltage through a 50 Ω parallel termination resistance.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital SetVterm(
	double value
)
```

###### 参数

value  Double
:   The input voltage in Vterm termination mode. The default value is 2.0.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### UnloadAllPatterns 方法

|  |  |
| --- | --- |
|  | DigitalUnloadAllPatterns 方法 |

Unloads all patterns, source waveforms, and capture waveforms from a digital pattern instrument.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital UnloadAllPatterns(
	bool unloadKeepAlivePattern
)
```

###### 参数

unloadKeepAlivePattern  Boolean
:   Specifies whether to unload any loaded keep alive patterns.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### UnloadSpecifications 方法

|  |  |
| --- | --- |
|  | DigitalUnloadSpecifications 方法 |

Unloads the given specifications sheet present in the previously loaded specifications file that you select.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital UnloadSpecifications(
	string specificationsFilePath
)
```

###### 参数

specificationsFilePath  String
:   The absolute file path to a loaded specifications file.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### VForce 方法

|  |  |
| --- | --- |
|  | DigitalVForce 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [VForce(Double)](4ee27b17-9519-4347-3a9c-036e14c86981.htm) | Set the PPMU to force voltage to the DUT. You can specify other associated values by properties, such as IClampRange. |
| 公共方法 | [VForce(Double, Double)](36d62a26-e2e9-c394-4371-aa28903c8945.htm) | Set the PPMU to force voltage to the DUI. |

[Top](#PageHeader)

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### VForce(Double) 方法

|  |  |
| --- | --- |
|  | DigitalVForce(Double) 方法 |

Set the PPMU to force voltage to the DUT.
You can specify other associated values by properties, such as IClampRange.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital VForce(
	double level
)
```

###### 参数

level  Double
:   The voltage level, in volts.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[VForce 重载](5650429f-473e-ac80-27d1-0c516677ea86.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### VForce(Double, Double) 方法

|  |  |
| --- | --- |
|  | DigitalVForce(Double, Double) 方法 |

Set the PPMU to force voltage to the DUI.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital VForce(
	double level,
	double range
)
```

###### 参数

level  Double
:   The voltage level, in volts.

range  Double
:   The range of valid values for the voltage level, in volts.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[VForce 重载](5650429f-473e-ac80-27d1-0c516677ea86.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### VMeasure 方法

|  |  |
| --- | --- |
|  | DigitalVMeasure 方法 |

Perform measurement operations at any time, even if you are not forcing current or voltage with the PPMU.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Dictionary<string, double> VMeasure()
```

###### 返回值

DictionaryString, Double  
A dictionary collection of measured voltage. The key of the collection is pin name, the value is multisite result.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### WaitUntilDone 方法

|  |  |
| --- | --- |
|  | DigitalWaitUntilDone 方法 |

Waits until the pattern burst has completed or the specified maxTime has expired.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital WaitUntilDone(
	double timeout
)
```

###### 参数

timeout  Double
:   The maximum time interval allowed for the pattern burst to complete.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### WriteSequencerFlag 方法

|  |  |
| --- | --- |
|  | DigitalWriteSequencerFlag 方法 |

Writes a Boolean value to a pattern sequencer flag.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital WriteSequencerFlag(
	string flag,
	bool value
)
```

###### 参数

flag  String
:   The name of the pattern sequencer flag to which you would like to write the specified value. Possible values include "seqflag0", "seqflag1", "seqflag2", or "seqflag3".

value  Boolean
:   The state to assign to the specified pattern sequencer flag.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### WriteSequencerRegister 方法

|  |  |
| --- | --- |
|  | DigitalWriteSequencerRegister 方法 |

Writes a value to a pattern sequencer register.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital WriteSequencerRegister(
	string reg,
	int value
)
```

###### 参数

reg  String
:   Specifies the sequencer register to which you would like to write the specified value.

value  Int32
:   The value to write to the specified pattern sequence register.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### WriteSourceWaveformBroadcast 方法

|  |  |
| --- | --- |
|  | DigitalWriteSourceWaveformBroadcast 方法 |

Writes the same source waveform data to all sites.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital WriteSourceWaveformBroadcast(
	string waveformName,
	uint[] waveformData
)
```

###### 参数

waveformName  String
:   Name of the source waveform. Use the waveformName with the source\_start opcode in your pattern.

waveformData  UInt32
:   A 1D array of waveform data samples to use as the source data to apply to all sites.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### WriteSourceWaveformDataFromFile 方法

|  |  |
| --- | --- |
|  | DigitalWriteSourceWaveformDataFromFile 方法 |

Writes a source waveform based on the waveform data and the configuration information the file contains.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital WriteSourceWaveformDataFromFile(
	string waveformName,
	string waveformFilePath
)
```

###### 参数

waveformName  String
:   Specifies the waveform name to use from the file. You must specify the waveform name if the file contains multiple waveforms. Use the waveformName with source\_start opcode in your pattern.

waveformFilePath  String
:   Specifies the absolute file path to the source waveform file (.tdms).

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### WriteSourceWaveformSiteUnique 方法

|  |  |
| --- | --- |
|  | DigitalWriteSourceWaveformSiteUnique 方法 |

Writes one source waveform to current site.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital WriteSourceWaveformSiteUnique(
	string waveformName,
	uint[] waveformData
)
```

###### 参数

waveformName  String
:   Name of the source waveform. Use the waveformName with the source\_start opcode in your pattern.

waveformData  UInt32
:   A 2D jagged array of waveform samples to use as source data.

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### WriteStatic 方法

|  |  |
| --- | --- |
|  | DigitalWriteStatic 方法 |

Writes a static state to the channels or pins represented by this pin list. These channels or pins remain in the specified state until the next pattern burst or call to this method.

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public Digital WriteStatic(
	string state
)
```

###### 参数

state  String
:   The digital state to write to the channels or pins specified. Valid values are "\_0", "\_1", or "X".

###### 返回值

[Digital](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)  
Return DigitalParent.Digital instance.

参见

###### 引用

[Digital 类](872546fd-68ec-6012-ed6c-af9be2401d1a.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


## IDigital_Instr 接口

|  |  |
| --- | --- |
|  | IDigital\_Instr 接口 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
public interface IDigital_Instr
```

IDigital\_Instr 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [AbortBurst](3cae147e-2deb-f6e7-104b-a63038beacec.htm) |  |
| 公共方法 | [AbortClockGenerator](cca18407-9c0a-5d9f-43cc-60ad26ef4eab.htm) |  |
| 公共方法 | [AbortKeepAlive](57eb77fc-1d65-b831-685e-32d277f98667.htm) |  |
| 公共方法 | [ApplyLevelsAndTiming(String, String, String)](c85dc68e-ea9f-1641-7381-712022d53252.htm) |  |
| 公共方法 | [ApplyLevelsAndTiming(String, String, String, String, String, String)](412be939-c29d-df8c-3d0e-ff9ba7acea5b.htm) |  |
| 公共方法 | [ApplyTdrOffsets](4e3374a6-a631-1e12-7e57-ff006ab1ecd7.htm) |  |
| 公共方法 | [BurstPattern(String, String, NullableBoolean, NullableDouble)](c45ee386-4d96-6c44-25a3-4123f1c3927a.htm) |  |
| 公共方法 | [BurstPattern(String, String, Boolean, Boolean, Double)](04f412e1-1d13-57bb-d3e2-5d502a9354fe.htm) |  |
| 公共方法 | [CloseFpga](0f845d8b-fd49-13e7-5ddb-235d171cfcdd.htm) |  |
| 公共方法 | [ConfigureActiveLoadLevels](a2845ee2-5352-4467-4adb-32926b1428cd.htm) |  |
| 公共方法 | [ConfigureCompareStrobeEdge(String, String, Double)](6cde0758-00f3-2545-588b-2b3fd72541c0.htm) |  |
| 公共方法 | [ConfigureCompareStrobeEdge(String, String, Double, Double)](a445da9e-5958-9cb3-8164-6775183d5a72.htm) |  |
| 公共方法 | [ConfigureDigitalEdgeTrigger](80588dc8-80bf-9ac9-4037-c9e8e3840676.htm) |  |
| 公共方法 | [ConfigureDriveEdges](aca99062-7304-b772-b452-ddbae3dccdab.htm) |  |
| 公共方法 | [ConfigureDriveFormat](930137ad-a6f7-a6f7-c3d7-b9d7b7eab7c0.htm) |  |
| 公共方法 | [ConfigureDriverEdges](366cffc3-c0b1-9c0e-3696-e92c96a4ff5b.htm) |  |
| 公共方法 | [ConfigureEdge](c4fe074c-5e7c-74bf-6abe-f859b8ccdfc0.htm) |  |
| 公共方法 | [ConfigureEdgeMultiplier](90d16a64-7cd2-e1ad-bdfc-fb46db78ee6f.htm) |  |
| 公共方法 | [ConfigureHistoryRamCycleNumberTrigger](30501f0a-714c-729a-2afe-1fc29b86d79f.htm) |  |
| 公共方法 | [ConfigureHistoryRamFirstFailureTrigger](1102986b-7bd8-e7de-e651-cc246d183fb8.htm) |  |
| 公共方法 | [ConfigureHistoryRamPatternLabelTrigger](b2eda445-987c-3cca-36ed-044cc07b615c.htm) |  |
| 公共方法 | [ConfigureIClamp](92fd3c86-6b4e-5ffe-ce8d-d91d106d04e9.htm) |  |
| 公共方法 | [ConfigureSoftwareTrigger](2c562dbd-a11f-ef14-39fa-fb19fc9291c7.htm) |  |
| 公共方法 | [ConfigureVClamp](86b2a2dd-f293-4100-ab7f-238baac72514.htm) |  |
| 公共方法 | [ConfigureVoltageLevels](a9a4cc42-7cb2-5e13-ed52-2d77e23174a4.htm) |  |
| 公共方法 | [CppDynamicInvoke](9bd86ed6-26d0-5ca0-4ef4-b1c470a7dfca.htm) |  |
| 公共方法 | [CreateCaptureWaveformFromFile](3a6336e4-45cc-3280-d9dc-14aba4c6d6e8.htm) |  |
| 公共方法 | [CreateCaptureWaveformParallel](5e15ea89-117c-5698-e647-a8335bdae6cb.htm) |  |
| 公共方法 | [CreateCaptureWaveformSerial](0f19f4e5-b08c-9851-0a7a-061b8c6ea4be.htm) |  |
| 公共方法 | [CreateChannelMap](f5f199fb-2a37-631f-b1c5-47eb21bdb050.htm) |  |
| 公共方法 | [CreatePinGroup](4fdeadb4-8a38-6a23-2fca-1eecbbc03109.htm) |  |
| 公共方法 | [CreatePinMap](a593b019-c437-3f30-26f7-6109238d12e1.htm) |  |
| 公共方法 | [CreateSourceWaveformFromFile](ff06d61e-d963-c942-26f7-fb50fc2b72b4.htm) |  |
| 公共方法 | [CreateSourceWaveformParallel](ce76eed3-fdce-ff67-c0a2-fe3ba2f2d14a.htm) |  |
| 公共方法 | [CreateSourceWaveformSerial](f94d1094-23c0-0732-354e-fe46af28829a.htm) |  |
| 公共方法 | [CreateTimeSet](d91cf751-a82d-f808-c14e-a34c9f856fbc.htm) |  |
| 公共方法 | [DeleteAllTimeSets](221107d5-3052-62f4-7c95-2e22a0c8b53e.htm) |  |
| 公共方法 | [DisableSites](763e824c-c8a0-c3ed-3d95-0faf8f901813.htm) |  |
| 公共方法 | [DisableTrigger](fc5053a9-21f5-a9c7-48d4-a2c86c6b246c.htm) |  |
| 公共方法 | [EnableSites](929ab32b-153e-b403-38e9-28984a4a2395.htm) |  |
| 公共方法 | [EndChannelMap](8a23a5ee-a0d3-73bc-707f-b3c867cc3937.htm) |  |
| 公共方法 | [ExportSignal](17deb198-2852-f8f9-5357-d9aa3cf04ad4.htm) |  |
| 公共方法 | [FetchCaptureWaveform](9a6e3165-07bf-38d6-7226-2837e740f099.htm) |  |
| 公共方法 | [FetchHistoryRamCycleInformation](d784173c-42f0-c349-e366-a30e7191de1c.htm) |  |
| 公共方法 | [FetchHistoryRamScanCycleNumber](79ba8d6c-245b-4c74-0dd4-222a93135364.htm) |  |
| 公共方法 | [GenerateClock](a94db185-3e13-161f-df64-ce2298d9e63e.htm) |  |
| 公共方法 | [GetAllowExtendedVoltageRange](e35439de-5815-e7cb-b26b-2aaa5fac247d.htm) |  |
| 公共方法 | [GetApertureTime](154e0d0b-ed76-b398-3fe0-e18697a153d5.htm) |  |
| 公共方法 | [GetDriveFormat](8a6332b2-4401-ab33-b526-208c2d7c1d02.htm) |  |
| 公共方法 | [GetEdge](f6a50508-61c3-7b01-6fba-cc205d9f01b9.htm) |  |
| 公共方法 | [GetEdgeMultiplier](d25d852f-651f-14f4-8eef-bc0a24c05cf5.htm) |  |
| 公共方法 | [GetFpgaStatus](21d51b00-88da-66e2-260f-b840f38e27b2.htm) |  |
| 公共方法 | [GetHistoryRamBufferSizePerSite](af2956c8-08be-016e-57c4-303478df6045.htm) |  |
| 公共方法 | [GetHistoryRamCyclesToAcquire](d132e79b-5ea1-e01a-745b-aada32ad2d1b.htm) |  |
| 公共方法 | [GetHistoryRamFailCount](7a58d5d5-294a-9050-7fd6-ef5297b3c1a3.htm) |  |
| 公共方法 | [GetHistoryRamMaxSamplesToAcquire](6ae9f903-54a6-d512-47ed-280197a62f42.htm) |  |
| 公共方法 | [GetHistoryRamNumberOfSamplesIsFinite](0668a403-5f66-2a9a-3060-9fc32749e5f7.htm) |  |
| 公共方法 | [GetIClamp](56c1542c-ac1e-26c6-e3d4-2ef0c0267c3c.htm) |  |
| 公共方法 | [GetIClampSink](c1a750ce-c6fe-8a80-a774-96f1b4462a66.htm) |  |
| 公共方法 | [GetIClampSource](c4eb1524-c1a8-0ae3-f1d6-e21f379fe8fd.htm) |  |
| 公共方法 | [GetIForceLevel](60afeb2e-f643-a56b-d07d-60476e48c810.htm) |  |
| 公共方法 | [GetILevelRange](96cfea49-84ea-07cd-d239-bc93bc4be020.htm) |  |
| 公共方法 | [GetIoh](9f8980f7-2baf-78dc-cbb0-0c8084e4afd3.htm) |  |
| 公共方法 | [GetIol](12e6dea8-e7a5-ce54-5876-b18592311517.htm) |  |
| 公共方法 | [GetOutputFunction](449274d0-48d1-778b-3dea-75e3e5b2b0d6.htm) |  |
| 公共方法 | [GetPatternIsDone](615f7ed8-3d72-a64f-dd6b-86300228517f.htm) |  |
| 公共方法 | [GetPatternStartLabel](22b83c0d-6b60-65d0-fad1-067ac1de89f4.htm) |  |
| 公共方法 | [GetSelectedFunction](add6e616-2e04-6d16-bed3-2d11bd267c3c.htm) |  |
| 公共方法 | [GetSitePassFail](fee2c952-4c1c-0760-b128-a65eb077b3cc.htm) |  |
| 公共方法 | [GetTdrOffsets](f3ba5cfd-1d8a-9dd3-7362-577aec233978.htm) |  |
| 公共方法 | [GetTermMode](43a4fdde-9379-ec66-5197-13e11a369bd5.htm) |  |
| 公共方法 | [GetTimeSetFrequency](fffb6e73-ab0e-edeb-7815-3601b8a4a6c9.htm) |  |
| 公共方法 | [GetTimeSetPeriod](a6639ec7-6802-e783-1b14-20232b30d456.htm) |  |
| 公共方法 | [GetVClampHigh](ecdc9b71-26b9-fe63-5f89-0ef609f5dd43.htm) |  |
| 公共方法 | [GetVClampLow](08669e5b-7721-b628-a015-f3b67ae62544.htm) |  |
| 公共方法 | [GetVcom](d35e65f5-b20a-628d-89c2-a86737a6e349.htm) |  |
| 公共方法 | [GetVForceLevel](60f66571-8034-f8fd-f417-8bfaad595159.htm) |  |
| 公共方法 | [GetVih](49dc55f7-35b1-285b-bb79-a368bc903933.htm) |  |
| 公共方法 | [GetVil](1baf079a-27d9-463b-104b-1ca73acf72d8.htm) |  |
| 公共方法 | [GetVoh](b26a7538-4996-aa3d-6736-e613ca7b3dc4.htm) |  |
| 公共方法 | [GetVol](4772f28e-16b3-2f38-6959-001ce94d8804.htm) |  |
| 公共方法 | [GetVterm](ce30266f-2bd3-aac1-f79c-26315530d286.htm) |  |
| 公共方法 | [IForce(String, Double)](cf6c0d13-c282-efff-a1d7-df24ef86eba9.htm) |  |
| 公共方法 | [IForce(String, Double, Double)](bf225857-95aa-54a4-6e13-afd7c5763608.htm) |  |
| 公共方法 | [IMeasure](a4836176-4104-d207-68db-1198f84dba01.htm) |  |
| 公共方法 | [InitializeFpga](c7ebf213-3582-2d74-9402-85e97c7f8001.htm) |  |
| 公共方法 | [Initiate](52f054fa-1dae-ff89-a8e0-1990bff236ae.htm) |  |
| 公共方法 | [IsSiteEnabled](ac005c6c-2f0e-e684-f8f7-7dd871c72cd5.htm) |  |
| 公共方法 | [LoadAndApply(String, String)](b4e8b5b3-cda5-7f11-ee02-420062aef4ec.htm) |  |
| 公共方法 | [LoadAndApply(String, String, String, String, String)](03a1bc98-e88d-5979-8ca0-11eaecffa813.htm) |  |
| 公共方法 | [LoadLevels](097b6426-496e-1876-2b47-14e807a03b81.htm) |  |
| 公共方法 | [LoadPattern](b358a60f-8cd7-559c-4860-0c2013ed34e7.htm) |  |
| 公共方法 | [LoadPinMap](ee8c4989-c8b1-126e-d90e-c625c8d6b404.htm) |  |
| 公共方法 | [LoadSpecifications](dd3266f7-c4b3-75a5-83fd-fde97f1f7606.htm) |  |
| 公共方法 | [LoadTiming](daa8d232-b880-e334-5c72-1dd0087bc646.htm) |  |
| 公共方法 | [MapPinToChannel](cc8eb5c1-cac9-5d7c-624b-177121cee13d.htm) |  |
| 公共方法 | [MeasureFrequency](2f07b5ef-83e3-21f0-f883-51f09a39bec1.htm) |  |
| 公共方法 | [ReadSequencerFlag](d638eec0-6deb-fc0b-4e14-129de071de52.htm) |  |
| 公共方法 | [ReadSequencerRegister](fa714e9d-8566-ad10-f6c2-8142214b75cd.htm) |  |
| 公共方法 | [ReadStatic](3eea4d3a-2d93-a0d7-3940-2b2dccffee36.htm) |  |
| 公共方法 | [ReleaseControlPrivilege](77eb0e4c-6dac-6509-9a7d-052953c57cee.htm) |  |
| 公共方法 | [RequestControlPrivilege](d7b9d8f5-eb59-ed80-1c65-7399a8577d1c.htm) |  |
| 公共方法 | [Reset](4c744ec1-6230-8496-8d07-ad948d3293b2.htm) |  |
| 公共方法 | [ResetDevice](c093c7b5-04d8-82a1-bd27-8f27c4643be0.htm) |  |
| 公共方法 | [SelfCalibrate](b37832c1-6ab8-e774-f6c7-32db2059b357.htm) |  |
| 公共方法 | [SelfTest](a203eb4f-4c55-7150-debf-7a3ddd486ea4.htm) |  |
| 公共方法 | [SendSoftwareTrigger](21ab7ae2-33ad-3adb-aee4-bf3167cf66d3.htm) |  |
| 公共方法 | [SetAllowExtendedVoltageRange](96ebbaaf-b447-a02e-aae4-12eb521a75d9.htm) |  |
| 公共方法 | [SetApertureTime](dd968bba-6584-4cd4-aae4-c237ef6041fb.htm) |  |
| 公共方法 | [SetHistoryRamBufferSizePerSite](fb3bc8e6-393a-9493-136f-1e3071a31284.htm) |  |
| 公共方法 | [SetHistoryRamCyclesToAcquire](e068a584-288c-37a0-f74d-f9f4c72ec24a.htm) |  |
| 公共方法 | [SetHistoryRamMaxSamplesToAcquire](f056a8c9-2406-9af8-a7cc-6749a0aaa497.htm) |  |
| 公共方法 | [SetHistoryRamNumberOfSamplesIsFinite](d09f0a66-d86e-7d07-dc6b-5dad691c5d9d.htm) |  |
| 公共方法 | [SetIClamp](e16450e7-ec5e-eaab-d931-2e05113aa6e6.htm) |  |
| 公共方法 | [SetIClampAutoRange](134cf82f-ed0a-4439-4b6f-eb676be5e463.htm) |  |
| 公共方法 | [SetIClampSink](0419f65c-c8a0-f97e-4fe2-d8ef7439ebe4.htm) |  |
| 公共方法 | [SetIClampSource](7bc338ca-99eb-689a-464b-c217022e06ce.htm) |  |
| 公共方法 | [SetIForceLevel](395fe464-db61-338e-3f92-c4d6a38ce958.htm) |  |
| 公共方法 | [SetILevelAutoRange](f64a94d6-824e-120d-3d3a-ed9d06988400.htm) |  |
| 公共方法 | [SetILevelRange](11b52b13-aa67-ba49-81e6-45daae7bc9c6.htm) |  |
| 公共方法 | [SetIoh](284fb598-d7b4-4334-564b-f915ef8cab6f.htm) |  |
| 公共方法 | [SetIol](69505dcf-9def-800f-b908-4aebf398e749.htm) |  |
| 公共方法 | [SetOutputFunction](a83e466b-ab56-6abc-8025-ea5cbbebf8c1.htm) |  |
| 公共方法 | [SetPatternStartLabel](656e9ded-18ba-6e6c-dad3-2de113b20a8e.htm) |  |
| 公共方法 | [SetSelectedFunction](2cd5eeef-211f-c408-cefa-54ddd5b9e523.htm) |  |
| 公共方法 | [SetTermMode](ceef869a-1502-de4d-9339-f1c7f1de3be5.htm) |  |
| 公共方法 | [SetTimeSetFrequency](ffa5cc7c-cc5a-dba5-4a53-c48be31fb62a.htm) |  |
| 公共方法 | [SetTimeSetPeriod](6574d34e-b20f-97b6-42f0-a03e3fe4cb31.htm) |  |
| 公共方法 | [SetVClampAutoRange](f82a4ff4-0e88-7364-e3be-bed22a165c77.htm) |  |
| 公共方法 | [SetVClampHigh](57b7df7d-1a2a-bd02-e676-b2588a4ea58f.htm) |  |
| 公共方法 | [SetVClampLow](0028fe96-e1cb-eae2-4627-2eefbf2c7905.htm) |  |
| 公共方法 | [SetVcom](6864c1fd-4dcb-b101-89d5-72601cfff8b5.htm) |  |
| 公共方法 | [SetVForceLevel](c7e3b146-f00c-f57d-98e2-d983cf8364b9.htm) |  |
| 公共方法 | [SetVih](03f917a6-7be7-7306-3c04-761a27bee35e.htm) |  |
| 公共方法 | [SetVil](c0256824-1c14-551c-c6ee-ff8d6fc83a15.htm) |  |
| 公共方法 | [SetVoh](9e5972d0-9240-0474-60dd-87bcfbdeffa9.htm) |  |
| 公共方法 | [SetVol](9b5469e1-46ec-2b32-b1be-e2f65186615a.htm) |  |
| 公共方法 | [SetVterm](9529ab9f-84c1-99b8-7a3f-4f6042fd0589.htm) |  |
| 公共方法 | [UnloadAllPatterns](1e33fadf-7d74-2cab-eca2-260e6923c0c2.htm) |  |
| 公共方法 | [UnloadSpecifications](66e3a7d5-f866-af0d-acdc-4d73f7235f36.htm) |  |
| 公共方法 | [VForce(String, Double)](197be8f7-6a4b-d1af-14fc-157cac7bf34d.htm) |  |
| 公共方法 | [VForce(String, Double, Double)](af459c08-cd83-62a8-f0a2-a4fb63ee20cb.htm) |  |
| 公共方法 | [VMeasure](b2801bc5-693d-7a99-95ac-865fdcaf8138.htm) |  |
| 公共方法 | [WaitUntilDone](83c3cf81-9f16-80c1-5955-806816d029eb.htm) |  |
| 公共方法 | [WriteSequencerFlag](302d9db1-213d-9e1a-7da1-9a92234592d2.htm) |  |
| 公共方法 | [WriteSequencerRegister](7bcbf5e0-d0f6-490a-fd6e-038dc2a7b5bf.htm) |  |
| 公共方法 | [WriteSourceWaveformBroadcast](9c19c9b2-0b36-e368-aa24-3e67a96643ef.htm) |  |
| 公共方法 | [WriteSourceWaveformDataFromFile](085b6aa3-cc3b-4090-23fc-d8b3fffcde14.htm) |  |
| 公共方法 | [WriteSourceWaveformSiteUnique](3954aa92-2309-7f1a-d5eb-e5be62395edb.htm) |  |
| 公共方法 | [WriteStatic](e302d531-bc3e-e483-a224-cf81379a2af1.htm) |  |

[Top](#PageHeader)

参见

##### 引用

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


### IDigital_Instr 方法

|  |  |
| --- | --- |
|  | IDigital\_Instr 方法 |

[IDigital\_Instr](80776682-5ee7-430a-5608-c219947bae3f.htm) 类型公开以下成员。

方法

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [AbortBurst](3cae147e-2deb-f6e7-104b-a63038beacec.htm) |  |
| 公共方法 | [AbortClockGenerator](cca18407-9c0a-5d9f-43cc-60ad26ef4eab.htm) |  |
| 公共方法 | [AbortKeepAlive](57eb77fc-1d65-b831-685e-32d277f98667.htm) |  |
| 公共方法 | [ApplyLevelsAndTiming(String, String, String)](c85dc68e-ea9f-1641-7381-712022d53252.htm) |  |
| 公共方法 | [ApplyLevelsAndTiming(String, String, String, String, String, String)](412be939-c29d-df8c-3d0e-ff9ba7acea5b.htm) |  |
| 公共方法 | [ApplyTdrOffsets](4e3374a6-a631-1e12-7e57-ff006ab1ecd7.htm) |  |
| 公共方法 | [BurstPattern(String, String, NullableBoolean, NullableDouble)](c45ee386-4d96-6c44-25a3-4123f1c3927a.htm) |  |
| 公共方法 | [BurstPattern(String, String, Boolean, Boolean, Double)](04f412e1-1d13-57bb-d3e2-5d502a9354fe.htm) |  |
| 公共方法 | [CloseFpga](0f845d8b-fd49-13e7-5ddb-235d171cfcdd.htm) |  |
| 公共方法 | [ConfigureActiveLoadLevels](a2845ee2-5352-4467-4adb-32926b1428cd.htm) |  |
| 公共方法 | [ConfigureCompareStrobeEdge(String, String, Double)](6cde0758-00f3-2545-588b-2b3fd72541c0.htm) |  |
| 公共方法 | [ConfigureCompareStrobeEdge(String, String, Double, Double)](a445da9e-5958-9cb3-8164-6775183d5a72.htm) |  |
| 公共方法 | [ConfigureDigitalEdgeTrigger](80588dc8-80bf-9ac9-4037-c9e8e3840676.htm) |  |
| 公共方法 | [ConfigureDriveEdges](aca99062-7304-b772-b452-ddbae3dccdab.htm) |  |
| 公共方法 | [ConfigureDriveFormat](930137ad-a6f7-a6f7-c3d7-b9d7b7eab7c0.htm) |  |
| 公共方法 | [ConfigureDriverEdges](366cffc3-c0b1-9c0e-3696-e92c96a4ff5b.htm) |  |
| 公共方法 | [ConfigureEdge](c4fe074c-5e7c-74bf-6abe-f859b8ccdfc0.htm) |  |
| 公共方法 | [ConfigureEdgeMultiplier](90d16a64-7cd2-e1ad-bdfc-fb46db78ee6f.htm) |  |
| 公共方法 | [ConfigureHistoryRamCycleNumberTrigger](30501f0a-714c-729a-2afe-1fc29b86d79f.htm) |  |
| 公共方法 | [ConfigureHistoryRamFirstFailureTrigger](1102986b-7bd8-e7de-e651-cc246d183fb8.htm) |  |
| 公共方法 | [ConfigureHistoryRamPatternLabelTrigger](b2eda445-987c-3cca-36ed-044cc07b615c.htm) |  |
| 公共方法 | [ConfigureIClamp](92fd3c86-6b4e-5ffe-ce8d-d91d106d04e9.htm) |  |
| 公共方法 | [ConfigureSoftwareTrigger](2c562dbd-a11f-ef14-39fa-fb19fc9291c7.htm) |  |
| 公共方法 | [ConfigureVClamp](86b2a2dd-f293-4100-ab7f-238baac72514.htm) |  |
| 公共方法 | [ConfigureVoltageLevels](a9a4cc42-7cb2-5e13-ed52-2d77e23174a4.htm) |  |
| 公共方法 | [CppDynamicInvoke](9bd86ed6-26d0-5ca0-4ef4-b1c470a7dfca.htm) |  |
| 公共方法 | [CreateCaptureWaveformFromFile](3a6336e4-45cc-3280-d9dc-14aba4c6d6e8.htm) |  |
| 公共方法 | [CreateCaptureWaveformParallel](5e15ea89-117c-5698-e647-a8335bdae6cb.htm) |  |
| 公共方法 | [CreateCaptureWaveformSerial](0f19f4e5-b08c-9851-0a7a-061b8c6ea4be.htm) |  |
| 公共方法 | [CreateChannelMap](f5f199fb-2a37-631f-b1c5-47eb21bdb050.htm) |  |
| 公共方法 | [CreatePinGroup](4fdeadb4-8a38-6a23-2fca-1eecbbc03109.htm) |  |
| 公共方法 | [CreatePinMap](a593b019-c437-3f30-26f7-6109238d12e1.htm) |  |
| 公共方法 | [CreateSourceWaveformFromFile](ff06d61e-d963-c942-26f7-fb50fc2b72b4.htm) |  |
| 公共方法 | [CreateSourceWaveformParallel](ce76eed3-fdce-ff67-c0a2-fe3ba2f2d14a.htm) |  |
| 公共方法 | [CreateSourceWaveformSerial](f94d1094-23c0-0732-354e-fe46af28829a.htm) |  |
| 公共方法 | [CreateTimeSet](d91cf751-a82d-f808-c14e-a34c9f856fbc.htm) |  |
| 公共方法 | [DeleteAllTimeSets](221107d5-3052-62f4-7c95-2e22a0c8b53e.htm) |  |
| 公共方法 | [DisableSites](763e824c-c8a0-c3ed-3d95-0faf8f901813.htm) |  |
| 公共方法 | [DisableTrigger](fc5053a9-21f5-a9c7-48d4-a2c86c6b246c.htm) |  |
| 公共方法 | [EnableSites](929ab32b-153e-b403-38e9-28984a4a2395.htm) |  |
| 公共方法 | [EndChannelMap](8a23a5ee-a0d3-73bc-707f-b3c867cc3937.htm) |  |
| 公共方法 | [ExportSignal](17deb198-2852-f8f9-5357-d9aa3cf04ad4.htm) |  |
| 公共方法 | [FetchCaptureWaveform](9a6e3165-07bf-38d6-7226-2837e740f099.htm) |  |
| 公共方法 | [FetchHistoryRamCycleInformation](d784173c-42f0-c349-e366-a30e7191de1c.htm) |  |
| 公共方法 | [FetchHistoryRamScanCycleNumber](79ba8d6c-245b-4c74-0dd4-222a93135364.htm) |  |
| 公共方法 | [GenerateClock](a94db185-3e13-161f-df64-ce2298d9e63e.htm) |  |
| 公共方法 | [GetAllowExtendedVoltageRange](e35439de-5815-e7cb-b26b-2aaa5fac247d.htm) |  |
| 公共方法 | [GetApertureTime](154e0d0b-ed76-b398-3fe0-e18697a153d5.htm) |  |
| 公共方法 | [GetDriveFormat](8a6332b2-4401-ab33-b526-208c2d7c1d02.htm) |  |
| 公共方法 | [GetEdge](f6a50508-61c3-7b01-6fba-cc205d9f01b9.htm) |  |
| 公共方法 | [GetEdgeMultiplier](d25d852f-651f-14f4-8eef-bc0a24c05cf5.htm) |  |
| 公共方法 | [GetFpgaStatus](21d51b00-88da-66e2-260f-b840f38e27b2.htm) |  |
| 公共方法 | [GetHistoryRamBufferSizePerSite](af2956c8-08be-016e-57c4-303478df6045.htm) |  |
| 公共方法 | [GetHistoryRamCyclesToAcquire](d132e79b-5ea1-e01a-745b-aada32ad2d1b.htm) |  |
| 公共方法 | [GetHistoryRamFailCount](7a58d5d5-294a-9050-7fd6-ef5297b3c1a3.htm) |  |
| 公共方法 | [GetHistoryRamMaxSamplesToAcquire](6ae9f903-54a6-d512-47ed-280197a62f42.htm) |  |
| 公共方法 | [GetHistoryRamNumberOfSamplesIsFinite](0668a403-5f66-2a9a-3060-9fc32749e5f7.htm) |  |
| 公共方法 | [GetIClamp](56c1542c-ac1e-26c6-e3d4-2ef0c0267c3c.htm) |  |
| 公共方法 | [GetIClampSink](c1a750ce-c6fe-8a80-a774-96f1b4462a66.htm) |  |
| 公共方法 | [GetIClampSource](c4eb1524-c1a8-0ae3-f1d6-e21f379fe8fd.htm) |  |
| 公共方法 | [GetIForceLevel](60afeb2e-f643-a56b-d07d-60476e48c810.htm) |  |
| 公共方法 | [GetILevelRange](96cfea49-84ea-07cd-d239-bc93bc4be020.htm) |  |
| 公共方法 | [GetIoh](9f8980f7-2baf-78dc-cbb0-0c8084e4afd3.htm) |  |
| 公共方法 | [GetIol](12e6dea8-e7a5-ce54-5876-b18592311517.htm) |  |
| 公共方法 | [GetOutputFunction](449274d0-48d1-778b-3dea-75e3e5b2b0d6.htm) |  |
| 公共方法 | [GetPatternIsDone](615f7ed8-3d72-a64f-dd6b-86300228517f.htm) |  |
| 公共方法 | [GetPatternStartLabel](22b83c0d-6b60-65d0-fad1-067ac1de89f4.htm) |  |
| 公共方法 | [GetSelectedFunction](add6e616-2e04-6d16-bed3-2d11bd267c3c.htm) |  |
| 公共方法 | [GetSitePassFail](fee2c952-4c1c-0760-b128-a65eb077b3cc.htm) |  |
| 公共方法 | [GetTdrOffsets](f3ba5cfd-1d8a-9dd3-7362-577aec233978.htm) |  |
| 公共方法 | [GetTermMode](43a4fdde-9379-ec66-5197-13e11a369bd5.htm) |  |
| 公共方法 | [GetTimeSetFrequency](fffb6e73-ab0e-edeb-7815-3601b8a4a6c9.htm) |  |
| 公共方法 | [GetTimeSetPeriod](a6639ec7-6802-e783-1b14-20232b30d456.htm) |  |
| 公共方法 | [GetVClampHigh](ecdc9b71-26b9-fe63-5f89-0ef609f5dd43.htm) |  |
| 公共方法 | [GetVClampLow](08669e5b-7721-b628-a015-f3b67ae62544.htm) |  |
| 公共方法 | [GetVcom](d35e65f5-b20a-628d-89c2-a86737a6e349.htm) |  |
| 公共方法 | [GetVForceLevel](60f66571-8034-f8fd-f417-8bfaad595159.htm) |  |
| 公共方法 | [GetVih](49dc55f7-35b1-285b-bb79-a368bc903933.htm) |  |
| 公共方法 | [GetVil](1baf079a-27d9-463b-104b-1ca73acf72d8.htm) |  |
| 公共方法 | [GetVoh](b26a7538-4996-aa3d-6736-e613ca7b3dc4.htm) |  |
| 公共方法 | [GetVol](4772f28e-16b3-2f38-6959-001ce94d8804.htm) |  |
| 公共方法 | [GetVterm](ce30266f-2bd3-aac1-f79c-26315530d286.htm) |  |
| 公共方法 | [IForce(String, Double)](cf6c0d13-c282-efff-a1d7-df24ef86eba9.htm) |  |
| 公共方法 | [IForce(String, Double, Double)](bf225857-95aa-54a4-6e13-afd7c5763608.htm) |  |
| 公共方法 | [IMeasure](a4836176-4104-d207-68db-1198f84dba01.htm) |  |
| 公共方法 | [InitializeFpga](c7ebf213-3582-2d74-9402-85e97c7f8001.htm) |  |
| 公共方法 | [Initiate](52f054fa-1dae-ff89-a8e0-1990bff236ae.htm) |  |
| 公共方法 | [IsSiteEnabled](ac005c6c-2f0e-e684-f8f7-7dd871c72cd5.htm) |  |
| 公共方法 | [LoadAndApply(String, String)](b4e8b5b3-cda5-7f11-ee02-420062aef4ec.htm) |  |
| 公共方法 | [LoadAndApply(String, String, String, String, String)](03a1bc98-e88d-5979-8ca0-11eaecffa813.htm) |  |
| 公共方法 | [LoadLevels](097b6426-496e-1876-2b47-14e807a03b81.htm) |  |
| 公共方法 | [LoadPattern](b358a60f-8cd7-559c-4860-0c2013ed34e7.htm) |  |
| 公共方法 | [LoadPinMap](ee8c4989-c8b1-126e-d90e-c625c8d6b404.htm) |  |
| 公共方法 | [LoadSpecifications](dd3266f7-c4b3-75a5-83fd-fde97f1f7606.htm) |  |
| 公共方法 | [LoadTiming](daa8d232-b880-e334-5c72-1dd0087bc646.htm) |  |
| 公共方法 | [MapPinToChannel](cc8eb5c1-cac9-5d7c-624b-177121cee13d.htm) |  |
| 公共方法 | [MeasureFrequency](2f07b5ef-83e3-21f0-f883-51f09a39bec1.htm) |  |
| 公共方法 | [ReadSequencerFlag](d638eec0-6deb-fc0b-4e14-129de071de52.htm) |  |
| 公共方法 | [ReadSequencerRegister](fa714e9d-8566-ad10-f6c2-8142214b75cd.htm) |  |
| 公共方法 | [ReadStatic](3eea4d3a-2d93-a0d7-3940-2b2dccffee36.htm) |  |
| 公共方法 | [ReleaseControlPrivilege](77eb0e4c-6dac-6509-9a7d-052953c57cee.htm) |  |
| 公共方法 | [RequestControlPrivilege](d7b9d8f5-eb59-ed80-1c65-7399a8577d1c.htm) |  |
| 公共方法 | [Reset](4c744ec1-6230-8496-8d07-ad948d3293b2.htm) |  |
| 公共方法 | [ResetDevice](c093c7b5-04d8-82a1-bd27-8f27c4643be0.htm) |  |
| 公共方法 | [SelfCalibrate](b37832c1-6ab8-e774-f6c7-32db2059b357.htm) |  |
| 公共方法 | [SelfTest](a203eb4f-4c55-7150-debf-7a3ddd486ea4.htm) |  |
| 公共方法 | [SendSoftwareTrigger](21ab7ae2-33ad-3adb-aee4-bf3167cf66d3.htm) |  |
| 公共方法 | [SetAllowExtendedVoltageRange](96ebbaaf-b447-a02e-aae4-12eb521a75d9.htm) |  |
| 公共方法 | [SetApertureTime](dd968bba-6584-4cd4-aae4-c237ef6041fb.htm) |  |
| 公共方法 | [SetHistoryRamBufferSizePerSite](fb3bc8e6-393a-9493-136f-1e3071a31284.htm) |  |
| 公共方法 | [SetHistoryRamCyclesToAcquire](e068a584-288c-37a0-f74d-f9f4c72ec24a.htm) |  |
| 公共方法 | [SetHistoryRamMaxSamplesToAcquire](f056a8c9-2406-9af8-a7cc-6749a0aaa497.htm) |  |
| 公共方法 | [SetHistoryRamNumberOfSamplesIsFinite](d09f0a66-d86e-7d07-dc6b-5dad691c5d9d.htm) |  |
| 公共方法 | [SetIClamp](e16450e7-ec5e-eaab-d931-2e05113aa6e6.htm) |  |
| 公共方法 | [SetIClampAutoRange](134cf82f-ed0a-4439-4b6f-eb676be5e463.htm) |  |
| 公共方法 | [SetIClampSink](0419f65c-c8a0-f97e-4fe2-d8ef7439ebe4.htm) |  |
| 公共方法 | [SetIClampSource](7bc338ca-99eb-689a-464b-c217022e06ce.htm) |  |
| 公共方法 | [SetIForceLevel](395fe464-db61-338e-3f92-c4d6a38ce958.htm) |  |
| 公共方法 | [SetILevelAutoRange](f64a94d6-824e-120d-3d3a-ed9d06988400.htm) |  |
| 公共方法 | [SetILevelRange](11b52b13-aa67-ba49-81e6-45daae7bc9c6.htm) |  |
| 公共方法 | [SetIoh](284fb598-d7b4-4334-564b-f915ef8cab6f.htm) |  |
| 公共方法 | [SetIol](69505dcf-9def-800f-b908-4aebf398e749.htm) |  |
| 公共方法 | [SetOutputFunction](a83e466b-ab56-6abc-8025-ea5cbbebf8c1.htm) |  |
| 公共方法 | [SetPatternStartLabel](656e9ded-18ba-6e6c-dad3-2de113b20a8e.htm) |  |
| 公共方法 | [SetSelectedFunction](2cd5eeef-211f-c408-cefa-54ddd5b9e523.htm) |  |
| 公共方法 | [SetTermMode](ceef869a-1502-de4d-9339-f1c7f1de3be5.htm) |  |
| 公共方法 | [SetTimeSetFrequency](ffa5cc7c-cc5a-dba5-4a53-c48be31fb62a.htm) |  |
| 公共方法 | [SetTimeSetPeriod](6574d34e-b20f-97b6-42f0-a03e3fe4cb31.htm) |  |
| 公共方法 | [SetVClampAutoRange](f82a4ff4-0e88-7364-e3be-bed22a165c77.htm) |  |
| 公共方法 | [SetVClampHigh](57b7df7d-1a2a-bd02-e676-b2588a4ea58f.htm) |  |
| 公共方法 | [SetVClampLow](0028fe96-e1cb-eae2-4627-2eefbf2c7905.htm) |  |
| 公共方法 | [SetVcom](6864c1fd-4dcb-b101-89d5-72601cfff8b5.htm) |  |
| 公共方法 | [SetVForceLevel](c7e3b146-f00c-f57d-98e2-d983cf8364b9.htm) |  |
| 公共方法 | [SetVih](03f917a6-7be7-7306-3c04-761a27bee35e.htm) |  |
| 公共方法 | [SetVil](c0256824-1c14-551c-c6ee-ff8d6fc83a15.htm) |  |
| 公共方法 | [SetVoh](9e5972d0-9240-0474-60dd-87bcfbdeffa9.htm) |  |
| 公共方法 | [SetVol](9b5469e1-46ec-2b32-b1be-e2f65186615a.htm) |  |
| 公共方法 | [SetVterm](9529ab9f-84c1-99b8-7a3f-4f6042fd0589.htm) |  |
| 公共方法 | [UnloadAllPatterns](1e33fadf-7d74-2cab-eca2-260e6923c0c2.htm) |  |
| 公共方法 | [UnloadSpecifications](66e3a7d5-f866-af0d-acdc-4d73f7235f36.htm) |  |
| 公共方法 | [VForce(String, Double)](197be8f7-6a4b-d1af-14fc-157cac7bf34d.htm) |  |
| 公共方法 | [VForce(String, Double, Double)](af459c08-cd83-62a8-f0a2-a4fb63ee20cb.htm) |  |
| 公共方法 | [VMeasure](b2801bc5-693d-7a99-95ac-865fdcaf8138.htm) |  |
| 公共方法 | [WaitUntilDone](83c3cf81-9f16-80c1-5955-806816d029eb.htm) |  |
| 公共方法 | [WriteSequencerFlag](302d9db1-213d-9e1a-7da1-9a92234592d2.htm) |  |
| 公共方法 | [WriteSequencerRegister](7bcbf5e0-d0f6-490a-fd6e-038dc2a7b5bf.htm) |  |
| 公共方法 | [WriteSourceWaveformBroadcast](9c19c9b2-0b36-e368-aa24-3e67a96643ef.htm) |  |
| 公共方法 | [WriteSourceWaveformDataFromFile](085b6aa3-cc3b-4090-23fc-d8b3fffcde14.htm) |  |
| 公共方法 | [WriteSourceWaveformSiteUnique](3954aa92-2309-7f1a-d5eb-e5be62395edb.htm) |  |
| 公共方法 | [WriteStatic](e302d531-bc3e-e483-a224-cf81379a2af1.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### AbortBurst 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrAbortBurst 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void AbortBurst()
```

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### AbortClockGenerator 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrAbortClockGenerator 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void AbortClockGenerator(
	string pinList
)
```

###### 参数

pinList  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### AbortKeepAlive 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrAbortKeepAlive 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void AbortKeepAlive()
```

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ApplyLevelsAndTiming 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrApplyLevelsAndTiming 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [ApplyLevelsAndTiming(String, String, String)](c85dc68e-ea9f-1641-7381-712022d53252.htm) |  |
| 公共方法 | [ApplyLevelsAndTiming(String, String, String, String, String, String)](412be939-c29d-df8c-3d0e-ff9ba7acea5b.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### ApplyLevelsAndTiming(String, String, String) 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrApplyLevelsAndTiming(String, String, String) 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ApplyLevelsAndTiming(
	string siteList,
	string levelsFilePath,
	string timingFilePath
)
```

###### 参数

siteList  String

levelsFilePath  String

timingFilePath  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[ApplyLevelsAndTiming 重载](1dc31ea0-bdde-f8bd-05d6-791e65367c09.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### ApplyLevelsAndTiming(String, String, String, String, String, String) 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrApplyLevelsAndTiming(String, String, String, String, String, String) 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ApplyLevelsAndTiming(
	string siteList,
	string levelsFilePath,
	string timingFilePath,
	string initialStateHighPins,
	string initialStateLowPins,
	string initialStateTristatePins
)
```

###### 参数

siteList  String

levelsFilePath  String

timingFilePath  String

initialStateHighPins  String

initialStateLowPins  String

initialStateTristatePins  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[ApplyLevelsAndTiming 重载](1dc31ea0-bdde-f8bd-05d6-791e65367c09.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ApplyTdrOffsets 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrApplyTdrOffsets 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ApplyTdrOffsets(
	string pinList,
	double[] offsets
)
```

###### 参数

pinList  String

offsets  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### BurstPattern 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrBurstPattern 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [BurstPattern(String, String, NullableBoolean, NullableDouble)](c45ee386-4d96-6c44-25a3-4123f1c3927a.htm) |  |
| 公共方法 | [BurstPattern(String, String, Boolean, Boolean, Double)](04f412e1-1d13-57bb-d3e2-5d502a9354fe.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### BurstPattern(String, String, Nullable&lt;Boolean&gt;, Nullable&lt;Double&gt;) 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrBurstPattern(String, String, NullableBoolean, NullableDouble) 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool[] BurstPattern(
	string siteList,
	string startLabel,
	bool? selectDigitalFunction = null,
	double? timeout = null
)
```

###### 参数

siteList  String

startLabel  String

selectDigitalFunction  NullableBoolean  (Optional)

timeout  NullableDouble  (Optional)

###### 返回值

Boolean

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[BurstPattern 重载](c5f9a6d3-8381-ca2b-20e8-90c630f95c18.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### BurstPattern(String, String, Boolean, Boolean, Double) 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrBurstPattern(String, String, Boolean, Boolean, Double) 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void BurstPattern(
	string siteList,
	string startLabel,
	bool selectDigitalFunction,
	bool waitUntilDone,
	double timeout
)
```

###### 参数

siteList  String

startLabel  String

selectDigitalFunction  Boolean

waitUntilDone  Boolean

timeout  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[BurstPattern 重载](c5f9a6d3-8381-ca2b-20e8-90c630f95c18.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### CloseFpga 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrCloseFpga 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void CloseFpga()
```

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureActiveLoadLevels 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrConfigureActiveLoadLevels 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureActiveLoadLevels(
	string pinList,
	double iol,
	double ioh,
	double vcom
)
```

###### 参数

pinList  String

iol  Double

ioh  Double

vcom  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureCompareStrobeEdge 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrConfigureCompareStrobeEdge 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [ConfigureCompareStrobeEdge(String, String, Double)](6cde0758-00f3-2545-588b-2b3fd72541c0.htm) |  |
| 公共方法 | [ConfigureCompareStrobeEdge(String, String, Double, Double)](a445da9e-5958-9cb3-8164-6775183d5a72.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### ConfigureCompareStrobeEdge(String, String, Double) 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrConfigureCompareStrobeEdge(String, String, Double) 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureCompareStrobeEdge(
	string pinList,
	string timeSetName,
	double strobeEdge
)
```

###### 参数

pinList  String

timeSetName  String

strobeEdge  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[ConfigureCompareStrobeEdge 重载](e3433461-bc36-3696-b4eb-ffd57daf4319.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### ConfigureCompareStrobeEdge(String, String, Double, Double) 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrConfigureCompareStrobeEdge(String, String, Double, Double) 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureCompareStrobeEdge(
	string pinList,
	string timeSetName,
	double strobeEdge,
	double strobe2Edge
)
```

###### 参数

pinList  String

timeSetName  String

strobeEdge  Double

strobe2Edge  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[ConfigureCompareStrobeEdge 重载](e3433461-bc36-3696-b4eb-ffd57daf4319.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureDigitalEdgeTrigger 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrConfigureDigitalEdgeTrigger 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

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

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureDriveEdges 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrConfigureDriveEdges 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureDriveEdges(
	string pinList,
	string timeSetName,
	string format,
	double driveOnEdge,
	double driveDataEdge,
	double driveReturnEdge,
	double driveOffEdge
)
```

###### 参数

pinList  String

timeSetName  String

format  String

driveOnEdge  Double

driveDataEdge  Double

driveReturnEdge  Double

driveOffEdge  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureDriveFormat 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrConfigureDriveFormat 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureDriveFormat(
	string pinList,
	string timeSetName,
	string driveFormat
)
```

###### 参数

pinList  String

timeSetName  String

driveFormat  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureDriverEdges 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrConfigureDriverEdges 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureDriverEdges(
	string pinList,
	string timeSetName,
	string format,
	double driveOnEdge,
	double driveDataEdge,
	double driveReturnEdge,
	double driveOffEdge,
	double driveData2Edge,
	double driveReturn2Edge
)
```

###### 参数

pinList  String

timeSetName  String

format  String

driveOnEdge  Double

driveDataEdge  Double

driveReturnEdge  Double

driveOffEdge  Double

driveData2Edge  Double

driveReturn2Edge  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureEdge 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrConfigureEdge 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureEdge(
	string pinList,
	string timeSetName,
	string edge,
	double time
)
```

###### 参数

pinList  String

timeSetName  String

edge  String

time  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureEdgeMultiplier 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrConfigureEdgeMultiplier 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureEdgeMultiplier(
	string pinList,
	string timeSetName,
	int edgeMultiplier
)
```

###### 参数

pinList  String

timeSetName  String

edgeMultiplier  Int32

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureHistoryRamCycleNumberTrigger 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrConfigureHistoryRamCycleNumberTrigger 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureHistoryRamCycleNumberTrigger(
	long cycleNumber,
	int pretriggerSamples
)
```

###### 参数

cycleNumber  Int64

pretriggerSamples  Int32

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureHistoryRamFirstFailureTrigger 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrConfigureHistoryRamFirstFailureTrigger 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureHistoryRamFirstFailureTrigger(
	int pertriggerSamples
)
```

###### 参数

pertriggerSamples  Int32

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureHistoryRamPatternLabelTrigger 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrConfigureHistoryRamPatternLabelTrigger 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureHistoryRamPatternLabelTrigger(
	string label,
	long vectorOffset,
	long cycleOffset,
	int pretriggerSamples
)
```

###### 参数

label  String

vectorOffset  Int64

cycleOffset  Int64

pretriggerSamples  Int32

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureIClamp 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrConfigureIClamp 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureIClamp(
	string pinList,
	double high,
	double low
)
```

###### 参数

pinList  String

high  Double

low  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureSoftwareTrigger 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrConfigureSoftwareTrigger 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

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

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureVClamp 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrConfigureVClamp 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureVClamp(
	string pinList,
	double high,
	double low
)
```

###### 参数

pinList  String

high  Double

low  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ConfigureVoltageLevels 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrConfigureVoltageLevels 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ConfigureVoltageLevels(
	string pinList,
	double vil,
	double vih,
	double vol,
	double voh,
	double vterm
)
```

###### 参数

pinList  String

vil  Double

vih  Double

vol  Double

voh  Double

vterm  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### CppDynamicInvoke 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrCppDynamicInvoke 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
Object? CppDynamicInvoke(
	Type delegateType,
	params Object[] args
)
```

###### 参数

delegateType  Type

args  Object

###### 返回值

Object

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### CreateCaptureWaveformFromFile 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrCreateCaptureWaveformFromFile 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void CreateCaptureWaveformFromFile(
	string waveformName,
	string waveformFilePath
)
```

###### 参数

waveformName  String

waveformFilePath  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### CreateCaptureWaveformParallel 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrCreateCaptureWaveformParallel 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void CreateCaptureWaveformParallel(
	string pinList,
	string waveformName
)
```

###### 参数

pinList  String

waveformName  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### CreateCaptureWaveformSerial 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrCreateCaptureWaveformSerial 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void CreateCaptureWaveformSerial(
	string pinList,
	string waveformName,
	uint sampleWidth,
	string bitOrder
)
```

###### 参数

pinList  String

waveformName  String

sampleWidth  UInt32

bitOrder  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### CreateChannelMap 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrCreateChannelMap 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void CreateChannelMap(
	int numberOfSites
)
```

###### 参数

numberOfSites  Int32

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### CreatePinGroup 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrCreatePinGroup 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void CreatePinGroup(
	string pinGroupName,
	string[] pins
)
```

###### 参数

pinGroupName  String

pins  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### CreatePinMap 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrCreatePinMap 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void CreatePinMap(
	string[] dutPins,
	string[] systemPins
)
```

###### 参数

dutPins  String

systemPins  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### CreateSourceWaveformFromFile 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrCreateSourceWaveformFromFile 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void CreateSourceWaveformFromFile(
	string waveformName,
	string waveformFilePath,
	bool writeWaveformData
)
```

###### 参数

waveformName  String

waveformFilePath  String

writeWaveformData  Boolean

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### CreateSourceWaveformParallel 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrCreateSourceWaveformParallel 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void CreateSourceWaveformParallel(
	string pinList,
	string waveformName,
	string dataMapping
)
```

###### 参数

pinList  String

waveformName  String

dataMapping  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### CreateSourceWaveformSerial 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrCreateSourceWaveformSerial 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void CreateSourceWaveformSerial(
	string pinList,
	string waveformName,
	string dataMapping,
	uint sampleWidth,
	string bitOrder
)
```

###### 参数

pinList  String

waveformName  String

dataMapping  String

sampleWidth  UInt32

bitOrder  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### CreateTimeSet 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrCreateTimeSet 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void CreateTimeSet(
	string timeSetName
)
```

###### 参数

timeSetName  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### DeleteAllTimeSets 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrDeleteAllTimeSets 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void DeleteAllTimeSets()
```

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### DisableSites 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrDisableSites 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void DisableSites(
	string siteList
)
```

###### 参数

siteList  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### DisableTrigger 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrDisableTrigger 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

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

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### EnableSites 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrEnableSites 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void EnableSites(
	string siteList
)
```

###### 参数

siteList  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### EndChannelMap 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrEndChannelMap 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void EndChannelMap()
```

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ExportSignal 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrExportSignal 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ExportSignal(
	string signal,
	string signalIdentifier,
	string outputTerminal
)
```

###### 参数

signal  String

signalIdentifier  String

outputTerminal  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### FetchCaptureWaveform 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrFetchCaptureWaveform 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
uint[][] FetchCaptureWaveform(
	string siteList,
	string waveformName,
	int samplesToRead,
	double timeout
)
```

###### 参数

siteList  String

waveformName  String

samplesToRead  Int32

timeout  Double

###### 返回值

UInt32

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### FetchHistoryRamCycleInformation 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrFetchHistoryRamCycleInformation 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string[] FetchHistoryRamCycleInformation(
	string pinList,
	int site,
	long position
)
```

###### 参数

pinList  String

site  Int32

position  Int64

###### 返回值

String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### FetchHistoryRamScanCycleNumber 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrFetchHistoryRamScanCycleNumber 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
long[] FetchHistoryRamScanCycleNumber(
	int site,
	long position
)
```

###### 参数

site  Int32

position  Int64

###### 返回值

Int64

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GenerateClock 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGenerateClock 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void GenerateClock(
	string pinList,
	double frequency,
	bool selectDigitalFunction
)
```

###### 参数

pinList  String

frequency  Double

selectDigitalFunction  Boolean

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetAllowExtendedVoltageRange 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetAllowExtendedVoltageRange 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool GetAllowExtendedVoltageRange(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

Boolean

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetApertureTime 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetApertureTime 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetApertureTime(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetDriveFormat 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetDriveFormat 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetDriveFormat(
	string pinList,
	string timeSetName
)
```

###### 参数

pinList  String

timeSetName  String

###### 返回值

String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetEdge 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetEdge 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetEdge(
	string pinList,
	string timeSetName,
	string edge
)
```

###### 参数

pinList  String

timeSetName  String

edge  String

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetEdgeMultiplier 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetEdgeMultiplier 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetEdgeMultiplier(
	string pinList,
	string timeSetName
)
```

###### 参数

pinList  String

timeSetName  String

###### 返回值

Int32

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetFpgaStatus 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetFpgaStatus 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetFpgaStatus()
```

###### 返回值

Int32

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetHistoryRamBufferSizePerSite 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetHistoryRamBufferSizePerSite 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
long GetHistoryRamBufferSizePerSite()
```

###### 返回值

Int64

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetHistoryRamCyclesToAcquire 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetHistoryRamCyclesToAcquire 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetHistoryRamCyclesToAcquire()
```

###### 返回值

String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetHistoryRamFailCount 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetHistoryRamFailCount 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
long GetHistoryRamFailCount(
	int site
)
```

###### 参数

site  Int32

###### 返回值

Int64

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetHistoryRamMaxSamplesToAcquire 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetHistoryRamMaxSamplesToAcquire 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int GetHistoryRamMaxSamplesToAcquire()
```

###### 返回值

Int32

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetHistoryRamNumberOfSamplesIsFinite 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetHistoryRamNumberOfSamplesIsFinite 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool GetHistoryRamNumberOfSamplesIsFinite()
```

###### 返回值

Boolean

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetIClamp 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetIClamp 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetIClamp(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetIClampSink 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetIClampSink 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetIClampSink(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetIClampSource 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetIClampSource 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetIClampSource(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetIForceLevel 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetIForceLevel 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetIForceLevel(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetILevelRange 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetILevelRange 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetILevelRange(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetIoh 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetIoh 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetIoh(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetIol 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetIol 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetIol(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetOutputFunction 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetOutputFunction 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetOutputFunction(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetPatternIsDone 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetPatternIsDone 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool GetPatternIsDone()
```

###### 返回值

Boolean

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetPatternStartLabel 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetPatternStartLabel 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetPatternStartLabel()
```

###### 返回值

String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetSelectedFunction 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetSelectedFunction 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetSelectedFunction(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetSitePassFail 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetSitePassFail 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool[] GetSitePassFail(
	string siteList
)
```

###### 参数

siteList  String

###### 返回值

Boolean

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetTdrOffsets 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetTdrOffsets 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] GetTdrOffsets(
	string pinList,
	bool applyOffsets,
	string tdrEndpointTermination
)
```

###### 参数

pinList  String

applyOffsets  Boolean

tdrEndpointTermination  String

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetTermMode 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetTermMode 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string GetTermMode(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetTimeSetFrequency 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetTimeSetFrequency 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetTimeSetFrequency(
	string timeSetName
)
```

###### 参数

timeSetName  String

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetTimeSetPeriod 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetTimeSetPeriod 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetTimeSetPeriod(
	string timeSetName
)
```

###### 参数

timeSetName  String

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetVClampHigh 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetVClampHigh 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetVClampHigh(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetVClampLow 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetVClampLow 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetVClampLow(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetVcom 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetVcom 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetVcom(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetVForceLevel 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetVForceLevel 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetVForceLevel(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetVih 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetVih 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetVih(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetVil 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetVil 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetVil(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetVoh 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetVoh 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetVoh(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetVol 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetVol 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetVol(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### GetVterm 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrGetVterm 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double GetVterm(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### IForce 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrIForce 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [IForce(String, Double)](cf6c0d13-c282-efff-a1d7-df24ef86eba9.htm) |  |
| 公共方法 | [IForce(String, Double, Double)](bf225857-95aa-54a4-6e13-afd7c5763608.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### IForce(String, Double) 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrIForce(String, Double) 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void IForce(
	string pinList,
	double level
)
```

###### 参数

pinList  String

level  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[IForce 重载](2d769d84-ef4c-b126-db78-961a4e4e17bc.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### IForce(String, Double, Double) 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrIForce(String, Double, Double) 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void IForce(
	string pinList,
	double level,
	double range
)
```

###### 参数

pinList  String

level  Double

range  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[IForce 重载](2d769d84-ef4c-b126-db78-961a4e4e17bc.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### IMeasure 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrIMeasure 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] IMeasure(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### InitializeFpga 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrInitializeFpga 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void InitializeFpga(
	string lvbitFil,
	string dllName,
	string resourceName
)
```

###### 参数

lvbitFil  String

dllName  String

resourceName  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### Initiate 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrInitiate 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Initiate(
	string pinList
)
```

###### 参数

pinList  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### IsSiteEnabled 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrIsSiteEnabled 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool IsSiteEnabled(
	int site
)
```

###### 参数

site  Int32

###### 返回值

Boolean

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### LoadAndApply 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrLoadAndApply 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [LoadAndApply(String, String)](b4e8b5b3-cda5-7f11-ee02-420062aef4ec.htm) |  |
| 公共方法 | [LoadAndApply(String, String, String, String, String)](03a1bc98-e88d-5979-8ca0-11eaecffa813.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### LoadAndApply(String, String) 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrLoadAndApply(String, String) 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void LoadAndApply(
	string siteList,
	string rootPath
)
```

###### 参数

siteList  String

rootPath  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[LoadAndApply 重载](ff03d6cb-2a3f-1d6f-3a3f-27e0dd95fb34.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### LoadAndApply(String, String, String, String, String) 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrLoadAndApply(String, String, String, String, String) 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void LoadAndApply(
	string siteList,
	string pinMapFilePath,
	string specificationsFilePath,
	string levelsFilePath,
	string timingFilePath
)
```

###### 参数

siteList  String

pinMapFilePath  String

specificationsFilePath  String

levelsFilePath  String

timingFilePath  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[LoadAndApply 重载](ff03d6cb-2a3f-1d6f-3a3f-27e0dd95fb34.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### LoadLevels 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrLoadLevels 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void LoadLevels(
	string levelsFilePath
)
```

###### 参数

levelsFilePath  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### LoadPattern 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrLoadPattern 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void LoadPattern(
	string filePath
)
```

###### 参数

filePath  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### LoadPinMap 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrLoadPinMap 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void LoadPinMap(
	string pinMapFilePath
)
```

###### 参数

pinMapFilePath  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### LoadSpecifications 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrLoadSpecifications 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void LoadSpecifications(
	string specificationsFilePath
)
```

###### 参数

specificationsFilePath  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### LoadTiming 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrLoadTiming 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void LoadTiming(
	string timingFilePath
)
```

###### 参数

timingFilePath  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### MapPinToChannel 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrMapPinToChannel 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void MapPinToChannel(
	string pin,
	int site,
	string channel
)
```

###### 参数

pin  String

site  Int32

channel  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### MeasureFrequency 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrMeasureFrequency 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] MeasureFrequency(
	string pinList,
	double measurementTime
)
```

###### 参数

pinList  String

measurementTime  Double

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ReadSequencerFlag 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrReadSequencerFlag 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
bool ReadSequencerFlag(
	string flag
)
```

###### 参数

flag  String

###### 返回值

Boolean

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ReadSequencerRegister 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrReadSequencerRegister 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
int ReadSequencerRegister(
	string reg
)
```

###### 参数

reg  String

###### 返回值

Int32

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ReadStatic 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrReadStatic 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
string[] ReadStatic(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ReleaseControlPrivilege 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrReleaseControlPrivilege 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ReleaseControlPrivilege()
```

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### RequestControlPrivilege 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrRequestControlPrivilege 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void RequestControlPrivilege()
```

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### Reset 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrReset 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void Reset()
```

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### ResetDevice 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrResetDevice 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void ResetDevice()
```

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SelfCalibrate 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSelfCalibrate 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SelfCalibrate()
```

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SelfTest 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSelfTest 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SelfTest()
```

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SendSoftwareTrigger 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSendSoftwareTrigger 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

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

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetAllowExtendedVoltageRange 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetAllowExtendedVoltageRange 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetAllowExtendedVoltageRange(
	string pinList,
	bool allow
)
```

###### 参数

pinList  String

allow  Boolean

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetApertureTime 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetApertureTime 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetApertureTime(
	string pinList,
	double apertureTime
)
```

###### 参数

pinList  String

apertureTime  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetHistoryRamBufferSizePerSite 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetHistoryRamBufferSizePerSite 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetHistoryRamBufferSizePerSite(
	long value
)
```

###### 参数

value  Int64

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetHistoryRamCyclesToAcquire 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetHistoryRamCyclesToAcquire 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetHistoryRamCyclesToAcquire(
	string cyclesToAquire
)
```

###### 参数

cyclesToAquire  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetHistoryRamMaxSamplesToAcquire 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetHistoryRamMaxSamplesToAcquire 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetHistoryRamMaxSamplesToAcquire(
	int value
)
```

###### 参数

value  Int32

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetHistoryRamNumberOfSamplesIsFinite 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetHistoryRamNumberOfSamplesIsFinite 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetHistoryRamNumberOfSamplesIsFinite(
	bool value
)
```

###### 参数

value  Boolean

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetIClamp 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetIClamp 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetIClamp(
	string pinList,
	double value
)
```

###### 参数

pinList  String

value  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetIClampAutoRange 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetIClampAutoRange 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetIClampAutoRange(
	string pinList,
	double? iForceValue
)
```

###### 参数

pinList  String

iForceValue  NullableDouble

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetIClampSink 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetIClampSink 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetIClampSink(
	string pinList,
	double value
)
```

###### 参数

pinList  String

value  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetIClampSource 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetIClampSource 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetIClampSource(
	string pinList,
	double value
)
```

###### 参数

pinList  String

value  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetIForceLevel 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetIForceLevel 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetIForceLevel(
	string pinList,
	double value
)
```

###### 参数

pinList  String

value  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetILevelAutoRange 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetILevelAutoRange 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetILevelAutoRange(
	string pinList,
	double? iForceValue
)
```

###### 参数

pinList  String

iForceValue  NullableDouble

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetILevelRange 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetILevelRange 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetILevelRange(
	string pinList,
	double range
)
```

###### 参数

pinList  String

range  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetIoh 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetIoh 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetIoh(
	string pinList,
	double value
)
```

###### 参数

pinList  String

value  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetIol 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetIol 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetIol(
	string pinList,
	double value
)
```

###### 参数

pinList  String

value  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetOutputFunction 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetOutputFunction 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetOutputFunction(
	string pinList,
	string outputFunction
)
```

###### 参数

pinList  String

outputFunction  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetPatternStartLabel 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetPatternStartLabel 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetPatternStartLabel(
	string label
)
```

###### 参数

label  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetSelectedFunction 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetSelectedFunction 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetSelectedFunction(
	string pinList,
	string function
)
```

###### 参数

pinList  String

function  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetTermMode 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetTermMode 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetTermMode(
	string pinList,
	string value
)
```

###### 参数

pinList  String

value  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetTimeSetFrequency 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetTimeSetFrequency 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetTimeSetFrequency(
	string timeSetName,
	double value
)
```

###### 参数

timeSetName  String

value  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetTimeSetPeriod 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetTimeSetPeriod 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetTimeSetPeriod(
	string timeSetName,
	double value
)
```

###### 参数

timeSetName  String

value  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetVClampAutoRange 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetVClampAutoRange 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetVClampAutoRange(
	string pinList,
	double? vClampHigh,
	double? vClampLow
)
```

###### 参数

pinList  String

vClampHigh  NullableDouble

vClampLow  NullableDouble

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetVClampHigh 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetVClampHigh 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetVClampHigh(
	string pinList,
	double value
)
```

###### 参数

pinList  String

value  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetVClampLow 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetVClampLow 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetVClampLow(
	string pinList,
	double value
)
```

###### 参数

pinList  String

value  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetVcom 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetVcom 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetVcom(
	string pinList,
	double value
)
```

###### 参数

pinList  String

value  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetVForceLevel 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetVForceLevel 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetVForceLevel(
	string pinList,
	double value
)
```

###### 参数

pinList  String

value  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetVih 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetVih 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetVih(
	string pinList,
	double value
)
```

###### 参数

pinList  String

value  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetVil 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetVil 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetVil(
	string pinList,
	double value
)
```

###### 参数

pinList  String

value  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetVoh 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetVoh 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetVoh(
	string pinList,
	double value
)
```

###### 参数

pinList  String

value  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetVol 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetVol 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetVol(
	string pinList,
	double value
)
```

###### 参数

pinList  String

value  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### SetVterm 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrSetVterm 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void SetVterm(
	string pinList,
	double value
)
```

###### 参数

pinList  String

value  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### UnloadAllPatterns 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrUnloadAllPatterns 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void UnloadAllPatterns(
	bool unloadKeepAlivePattern
)
```

###### 参数

unloadKeepAlivePattern  Boolean

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### UnloadSpecifications 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrUnloadSpecifications 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void UnloadSpecifications(
	string specificationsFilePath
)
```

###### 参数

specificationsFilePath  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### VForce 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrVForce 方法 |

重载列表

|  | 名称 | 说明 |
| --- | --- | --- |
| 公共方法 | [VForce(String, Double)](197be8f7-6a4b-d1af-14fc-157cac7bf34d.htm) |  |
| 公共方法 | [VForce(String, Double, Double)](af459c08-cd83-62a8-f0a2-a4fb63ee20cb.htm) |  |

[Top](#PageHeader)

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### VForce(String, Double) 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrVForce(String, Double) 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void VForce(
	string pinList,
	double level
)
```

###### 参数

pinList  String

level  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[VForce 重载](88ffec15-c5c8-a757-1f4f-5d2fab221632.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


##### VForce(String, Double, Double) 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrVForce(String, Double, Double) 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void VForce(
	string pinList,
	double level,
	double range
)
```

###### 参数

pinList  String

level  Double

range  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[VForce 重载](88ffec15-c5c8-a757-1f4f-5d2fab221632.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### VMeasure 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrVMeasure 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
double[] VMeasure(
	string pinList
)
```

###### 参数

pinList  String

###### 返回值

Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### WaitUntilDone 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrWaitUntilDone 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WaitUntilDone(
	double timeout
)
```

###### 参数

timeout  Double

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### WriteSequencerFlag 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrWriteSequencerFlag 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteSequencerFlag(
	string flag,
	bool value
)
```

###### 参数

flag  String

value  Boolean

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### WriteSequencerRegister 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrWriteSequencerRegister 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteSequencerRegister(
	string reg,
	int value
)
```

###### 参数

reg  String

value  Int32

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### WriteSourceWaveformBroadcast 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrWriteSourceWaveformBroadcast 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteSourceWaveformBroadcast(
	string waveformName,
	uint[] waveformData
)
```

###### 参数

waveformName  String

waveformData  UInt32

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### WriteSourceWaveformDataFromFile 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrWriteSourceWaveformDataFromFile 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteSourceWaveformDataFromFile(
	string waveformName,
	string waveformFilePath
)
```

###### 参数

waveformName  String

waveformFilePath  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### WriteSourceWaveformSiteUnique 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrWriteSourceWaveformSiteUnique 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteSourceWaveformSiteUnique(
	string siteList,
	string waveformName,
	uint[][] waveformData
)
```

###### 参数

siteList  String

waveformName  String

waveformData  UInt32

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)


#### WriteStatic 方法

|  |  |
| --- | --- |
|  | IDigital\_InstrWriteStatic 方法 |

  
**命名空间：** [DigitalParent](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)  
**程序集：** DigitalMeasStation (在 DigitalMeasStation.dll 中) 版本：2.0.0.0+a7bc1cebb515af7103d79fec111f1a66ff778f8d

语法

C#

[复制](# "复制")

```
void WriteStatic(
	string pinList,
	string state
)
```

###### 参数

pinList  String

state  String

参见

###### 引用

[IDigital\_Instr 接口](80776682-5ee7-430a-5608-c219947bae3f.htm)

[DigitalParent 命名空间](9dacf5b0-d037-48cc-409a-c5af7a59e011.htm)

