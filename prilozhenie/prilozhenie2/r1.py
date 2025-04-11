from win32com import client
import os
import pythoncom
import time
import sys

def excel_to_pdf_no_headers(excel_path, pdf_output_dir):
    excel = None
    workbook = None
    success_count = 0
    
    try:
        # Verify file exists first
        if not os.path.exists(excel_path):
            raise FileNotFoundError(f"Excel file not found at: {excel_path}")
        
        # Create output directory if it doesn't exist
        os.makedirs(pdf_output_dir, exist_ok=True)
        print(f"Output directory ready: {pdf_output_dir}")
        
        # Initialize COM
        pythoncom.CoInitialize()
        
        # Try to connect to existing Excel instance or create new one
        try:
            excel = client.GetActiveObject("Excel.Application")
            print("Connected to existing Excel instance")
        except:
            excel = client.Dispatch("Excel.Application")
            print("Created new Excel instance")
        
        # Configure Excel
        try:
            excel.Visible = False
            excel.DisplayAlerts = False
        except:
            print("Warning: Could not configure Excel settings - continuing anyway")
        
        # Add delay to allow Excel to initialize
        time.sleep(2)
        
        try:
            print(f"Attempting to open: {excel_path}")
            workbook = excel.Workbooks.Open(excel_path)
            print("Workbook opened successfully")
        except Exception as e:
            raise Exception(f"Could not open workbook: {str(e)}")
        
        # Process each worksheet
        sheet_count = workbook.Worksheets.Count
        print(f"Found {sheet_count} worksheets to process")
        
        for i, worksheet in enumerate(workbook.Worksheets):
            sheet_name = worksheet.Name
            print(f"\nProcessing sheet {i+1}/{sheet_count}: '{sheet_name}'")
            
            try:
                # Create safe filename
                safe_sheet_name = "".join(c for c in sheet_name if c.isalnum() or c in (' ', '_')).rstrip()
                pdf_path = os.path.join(pdf_output_dir, f"{safe_sheet_name}.pdf")
                print(f"Attempting to save as: {pdf_path}")
                
                # Verify we can write to the destination
                test_path = os.path.join(pdf_output_dir, "test_write.tmp")
                with open(test_path, 'w') as f:
                    f.write("test")
                os.remove(test_path)
                print("Write test successful")
                
                # Adjust page setup
                worksheet.PageSetup.CenterHeader = ""
                worksheet.PageSetup.LeftHeader = ""
                worksheet.PageSetup.RightHeader = ""
                
                # Export to PDF with retry logic
                max_retries = 2
                for attempt in range(max_retries):
                    try:
                        worksheet.ExportAsFixedFormat(
                            Type=0,  # PDF format
                            Filename=pdf_path,
                            Quality=0,
                            IncludeDocProperties=True,
                            IgnorePrintAreas=False,
                            OpenAfterPublish=False
                        )
                        print(f"Successfully saved sheet '{sheet_name}'")
                        success_count += 1
                        break
                    except Exception as export_error:
                        if attempt == max_retries - 1:
                            raise export_error
                        print(f"Attempt {attempt+1} failed, retrying...")
                        time.sleep(1)
                
            except Exception as sheet_error:
                error_msg = str(sheet_error)
                if "Ошибка" in error_msg or "Error" in error_msg:
                    print(f"Failed to save sheet '{sheet_name}': {error_msg}")
                    print("Possible causes:")
                    print("- Invalid characters in sheet name")
                    print("- Path too long (try shorter output directory)")
                    print("- Special characters in path")
                    print("- Excel permissions issue")
                else:
                    print(f"Error processing sheet '{sheet_name}': {error_msg}")
                continue
        
        return success_count > 0
        
    except Exception as e:
        print(f"Fatal error: {str(e)}", file=sys.stderr)
        return False
    finally:
        # Close workbook if open
        if workbook:
            try:
                workbook.Close(SaveChanges=False)
                print("Workbook closed")
            except Exception as e:
                print(f"Warning: Could not close workbook: {str(e)}", file=sys.stderr)
        
        # Quit Excel if we created it
        if excel:
            try:
                # Only quit if we created the instance
                if not client.GetActiveObject("Excel.Application"):
                    excel.Quit()
                    print("Excel application quit")
            except Exception as e:
                print(f"Warning: Could not quit Excel: {str(e)}", file=sys.stderr)
        
        # Release COM resources
        pythoncom.CoUninitialize()

# Usage with detailed error reporting
try:
    input_path = 'C:/Users/79133/glavpro/prilozhenie/prilozhenie2/Расчет_modified.xlsx'
    output_dir = 'C:/Users/79133/glavpro/prilozhenie/prilozhenie2'
    
    print(f"\nStarting conversion:\nInput: {input_path}\nOutput: {output_dir}")
    
    success = excel_to_pdf_no_headers(
        excel_path=input_path,
        pdf_output_dir=output_dir
    )
    
    if success:
        print("\nConversion completed successfully!")
    else:
        print("\nConversion completed with errors", file=sys.stderr)
        print("\nTroubleshooting steps:")
        print("1. Verify the Excel file opens manually")
        print("2. Try saving one sheet manually as PDF")
        print("3. Check output directory permissions")
        print("4. Try shorter output path (avoid special chars)")
        print("5. Close all Excel instances before running")
        
except Exception as e:
    print(f"\nCritical failure: {str(e)}", file=sys.stderr)