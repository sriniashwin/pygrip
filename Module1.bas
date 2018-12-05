Attribute VB_Name = "Module1"
Sub RefreshFile()
Attribute RefreshFile.VB_ProcData.VB_Invoke_Func = "j\n14"
'
' RefreshFile Macro
'
' Keyboard Shortcut: Ctrl+j
'
    With ActiveSheet.QueryTables.Add(Connection:= _
        "TEXT;C:\Users\asrinivasan.SATURN\Desktop\connectionstatus.txt", Destination _
        :=Range("$A$2"))
        .Name = "connectionstatus"
        .FieldNames = True
        .RowNumbers = False
        .FillAdjacentFormulas = False
        .PreserveFormatting = True
        .RefreshOnFileOpen = False
        .RefreshStyle = xlInsertDeleteCells
        .SavePassword = False
        .SaveData = True
        .AdjustColumnWidth = True
        .RefreshPeriod = 0
        .TextFilePromptOnRefresh = False
        .TextFilePlatform = 850
        .TextFileStartRow = 1
        .TextFileParseType = xlDelimited
        .TextFileTextQualifier = xlTextQualifierDoubleQuote
        .TextFileConsecutiveDelimiter = False
        .TextFileTabDelimiter = True
        .TextFileSemicolonDelimiter = False
        .TextFileCommaDelimiter = False
        .TextFileSpaceDelimiter = False
        .TextFileColumnDataTypes = Array(1)
        .TextFileTrailingMinusNumbers = True
        .Refresh BackgroundQuery:=False
    End With
    ActiveCell.FormulaR1C1 = "RawData"
    Range("B1").Select
    ActiveCell.FormulaR1C1 = "Time"
    Range("C1").Select
    ActiveCell.FormulaR1C1 = "RawStatus"
    Range("D1").Select
    ActiveCell.FormulaR1C1 = "Status"
    Range("B2").Select
    ActiveCell.FormulaR1C1 = "=LEFT(RC[-1],16)"
    Range("C2").Select
    ActiveCell.FormulaR1C1 = "=RIGHT(RC[-2],1)"
    Range("D2").Select
    ActiveCell.FormulaR1C1 = "=IF(RC[-1]=""1"",1,0)"
    Range("B2:D2").Select
    Selection.AutoFill Destination:=Range("B2:D95")
    Range("B2:D95").Select
    Range("B2").Select
    ActiveSheet.Shapes.AddChart2(227, xlLine).Select
    ActiveChart.SetSourceData Source:=Range("Sheet2!$A$1:$D$95")
    Application.CutCopyMode = False
    ActiveChart.FullSeriesCollection(1).XValues = "=Sheet2!$B$2:$B$95"
End Sub
