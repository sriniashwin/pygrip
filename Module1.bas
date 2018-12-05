Attribute VB_Name = "Module1"
Sub RefreshList2()
Attribute RefreshList2.VB_ProcData.VB_Invoke_Func = "k\n14"
'
' RefreshList2 Macro
'
' Keyboard Shortcut: Ctrl+k
'
    Dim sht As Worksheet
    Dim LastRow As Long
    Dim DataRange As Range
    
    Set sht = ActiveSheet
    
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
    'ActiveCell.FormulaR1C1 = "RawStatus"
    ActiveCell.FormulaR1C1 = "Status"
    Range("D1").Select
    'ActiveCell.FormulaR1C1 = "Status"
    ActiveCell.FormulaR1C1 = "RawStatus"
    Range("B2").Select
    ActiveCell.FormulaR1C1 = "=LEFT(RC[-1],16)"
    Range("D2").Select
    ActiveCell.FormulaR1C1 = "=RIGHT(RC[-3],1)"
    Range("C2").Select
    'ActiveCell.FormulaR1C1 = "=RIGHT(RC[-2],1)"
    ActiveCell.FormulaR1C1 = "=IF(RC[+1]=""1"",1,0)"
    
    'ActiveCell.FormulaR1C1 = "=IF(RC[-1]=""1"",1,0)"
    
    'Range("B2:D2").Select
    'Selection.Copy
    Range("A2").Select
    LastRow = sht.Range("A1").CurrentRegion.Rows.Count
    
    Debug.Print LastRow
    'Range("B2:D" & LastRow).Select
    'Selection.End(xlDown).Select
    'Range("B98:D98").Select
    'Range(Selection, Selection.End(xlUp)).Select
    'Range("B3:D98").Select
    'Range("B98").Activate
    'ActiveSheet.Paste
    Range("B2:D2").Copy Range("B3:D" & LastRow)
    ActiveWindow.SmallScroll Down:=-93
    'Range("B:B,D:D").Select
    Range("B1:C" & LastRow).Select
    Range("C1").Activate
    ActiveSheet.Shapes.AddChart2(227, xlLine).Select
    'ActiveChart.SetSourceData Source:=Range("Sheet6!$B:$B,Sheet6!$D:$D")
    ActiveChart.SetSourceData Source:=Range("B2:C" & LastRow)
    ActiveChart.Axes(xlValue).Select
    ActiveChart.Axes(xlValue).MaximumScale = 1
    ActiveChart.Axes(xlValue).MajorUnit = 1
    ActiveChart.Axes(xlValue).MinorUnit = 1
    Application.CommandBars("Format Object").Visible = False
End Sub
