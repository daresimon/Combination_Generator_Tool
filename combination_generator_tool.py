'''
Author: Desmond Goh
Date: 2021-03-11 23:37:34
LastEditTime: 2021-03-17 10:01:41
LastEditors: Desmond Goh
FilePath: /Combination_Generator_Tool/combination_generator_tool.py
'''
import tkinter as tk
from tool_interface.common.scrollable_frame import ScrollableFrame
from tool_interface.common.message_box import MessageBox
from tool_interface.interface_parts.generator_type import GeneratorType
from tool_interface.interface_parts.select_input_mode import SelectInputMode
from tool_interface.interface_parts.test_case_statement import TestCaseStatement
from tool_interface.interface_parts.parameter_controller import ParameterController
from tool_interface.interface_parts.action_buttons import ActionButtons
from tool_interface.interface_parts.display_results import DisplayResult
from tool_interface.interface_parts.file_handler import FileHandler
from src.input_processor import InputProcessor

class CombinationGeneratorTool:
    
    def __init__(self, tool_name):
        '''
        setup application window
        setup scrollable canvas
        setup frames for input
        '''
        self.window = tk.Tk()
        self.window.title(tool_name)
        self.window.geometry('1200x800+350+100')

        self.scrollable_frame = ScrollableFrame(self.window)
        self.scrollable_frame.add_vertical_scrollbar()
        self.scrollable_frame.add_horizontal_scrollbar()

        self.frm_generator = tk.Frame(self.scrollable_frame.scrollable_frame)
        self.frm_mode = tk.Frame(self.scrollable_frame.scrollable_frame)
        self.frm_statement = tk.Frame(self.scrollable_frame.scrollable_frame)
        self.frm_input = tk.Frame(self.scrollable_frame.scrollable_frame)
        self.frm_action_buttons = tk.Frame(self.scrollable_frame.scrollable_frame)
        self.frm_results = tk.Frame(self.scrollable_frame.scrollable_frame)

        self.frm_generator.grid(
            row=0, 
            column=0, 
            sticky='w', 
            padx=10, 
            pady=5
        )
        self.frm_mode.grid(
            row=1, 
            column=0, 
            sticky='w', 
            padx=10, 
            pady=5
        )
        self.frm_action_buttons.grid(
            row=4,
            column=0,
            stick='w', 
            padx=10, 
            pady=10
        )
        self.frm_results.grid(
            row=5, 
            column=0, 
            stick='w', 
            padx=10, 
            pady=10
        )

        self.generator_type = GeneratorType(self.frm_generator)

        self.input_mode = SelectInputMode(self.frm_mode)
        self.input_mode.chk_btn_case.configure(command=self.change_mode)
        self.input_mode.chk_btn_data.configure(command=self.change_mode)

        self.action_buttons = ActionButtons(self.frm_action_buttons)
        self.action_buttons.btn_generate.configure(command=self.generate_result)
        self.action_buttons.btn_reset.configure(command=self.reset_all)

        self.display_results = DisplayResult(self.frm_results)
        self.file_handler = FileHandler(self.frm_results, self.display_results.txt_result)
        self.scrollable_frame.unbind_scroll_for_widget(self.display_results.txt_result)

        '''
        test case mode of all pairs by default
        '''
        self.generator_type.selected_generator.set('pairs')
        self.current_mode = 'case'
        self.initiate_test_case_mode()

    def initiate_test_case_mode(self):  
        self.frm_statement = tk.Frame(self.scrollable_frame.scrollable_frame)
        self.case_statement = TestCaseStatement(self.frm_statement)
        self.frm_statement.grid(
            row=2, 
            column=0, 
            sticky='w', 
            padx=10, 
            pady=10
        )
        self.frm_input = tk.Frame(self.scrollable_frame.scrollable_frame)
        self.input_data = ParameterController(self.frm_input, 'case')
        self.frm_input.grid(
            row=3,
            column=0, 
            stick='w',
            padx=10, 
            pady=10
        )

    def initiate_test_data_mode(self):
        self.frm_input = tk.Frame(self.scrollable_frame.scrollable_frame)
        self.input_data = ParameterController(self.frm_input, 'data')
        self.frm_input.grid(
            row=2, 
            column=0, 
            stick='w', 
            padx=10, 
            pady=10
        )

    def generate_result(self):
        input_processor = InputProcessor(
            self.input_data.param_list, 
            self.generator_type.selected_generator.get()
        )
        
        operation_mode = self.input_mode.selected_mode.get()
        results = None
        if operation_mode == 'case':
            test_case_statement = self.case_statement.ent_statement.get()
            results = input_processor.process_test_case(test_case_statement)
        elif operation_mode == 'data':
            results = input_processor.process_test_data()
            
        if results == None:
            results = 'No combination output, please check for errors in input or optimise input data'
        self.display_results.txt_result.delete(1.0, tk.END)
        self.display_results.txt_result.insert(1.0, results)

    def reset_all(self):
        confirmation_message = MessageBox('Confirmation', 'Are you sure? Existing data will be cleared')
        if confirmation_message.ask_yes_no_box():
            self.frm_statement.forget()
            self.frm_statement.destroy()
            self.frm_input.forget()
            self.frm_input.destroy()
            self.display_results.txt_result.delete(1.0, tk.END)
            if self.input_mode.selected_mode.get() == 'case':    
                self.initiate_test_case_mode()
            if self.input_mode.selected_mode.get() == 'data':
                self.initiate_test_data_mode()
            return True
        return False

    def change_mode(self):
        selected_mode = self.input_mode.selected_mode.get()
        if self.current_mode == selected_mode:
            return None
        if self.input_mode.selected_mode.get() == 'case':
            if self.reset_all():
                self.current_mode = selected_mode
            else:
                self.input_mode.selected_mode.set(self.current_mode)
        elif self.input_mode.selected_mode.get() == 'data':
            if self.reset_all():
                self.current_mode = selected_mode
            else:
                self.input_mode.selected_mode.set(self.current_mode)

if __name__ == '__main__':
    input_name = 'Combination Case/Data Generator'
    test = CombinationGeneratorTool(input_name)
    test.window.mainloop()
