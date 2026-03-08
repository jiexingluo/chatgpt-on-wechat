|  |  |
| --- | --- |
|  | Example\_UpdateInstrumentAddress |

OneTest SDK开发示例

在下方的Example中，演示了如何使用OneTest SDK进行项目的加载、仪表地址的修改

Example\_UpdateInstrumentAddress

[复制](# "复制")

```
public class Example
{
    private static OneTestSdkClient _client;
    private static string _instrumentName = "DPS_4145_1";
    public static void Main()
    {
        _client = new OneTestSdkClient();
        _client.EvaluateResultCallback = EvaluateResultCallback;
        _client.GraphResultCallback = GraphDataCallback;
        _client.TaskFinishedCallback = TaskFinishCallback;
        _client.BatchBinResultCallback = BinResultCallBack;
        _client.TaskExceptionCallback = TaskException;
        _client.EngineLogCallback = CommonLog;
        _client.TimeMetricLogCallback = TimeLog;
        string projectFile = @"D:\OneTestProject\TestSDK\TestSDK.onetest";
        try
        {
            _client.LoadProject(projectFile);
            _client.SetInstrumentAddress(_instrumentName, "DSP_4145_2");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"OneTest SDK Exception: {ex.Message}");
        }
        finally
        {
            _client.CloseInstrument();
            _client.Dispose();
        }
    }
    private static void EvaluateResultCallback(MeasurementResult result)
    {
        Console.WriteLine("EvaluateResult: " + JsonSerializer.Serialize(result));
    }

    private static void GraphDataCallback(GraphResult result)
    {
        Console.WriteLine("GraphData: " + JsonSerializer.Serialize(result));
    }

    private static void TaskFinishCallback(string message)
    {
        Console.WriteLine("Task finished: " + message);
    }
    private static void BinResultCallBack(BatchResult batchResult)
    {
        Console.WriteLine("Bin result: " + JsonSerializer.Serialize(batchResult));
    }

    private static void TaskException(TaskExceptionRequest task)
    {
        Console.WriteLine("TaskException: " + JsonSerializer.Serialize(task));
    }

    private static void CommonLog(string value)
    {
        Console.WriteLine("CommonLog:     " + value);
    }

    private static void TimeLog(string value)
    {
        Console.WriteLine("TimeMetricLog: " + value);
    }
}
```

