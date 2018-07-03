# coding=utf-8

from util.get_case_data import GetCaseData
from util.action_mothod import ActionMothod
from util.server import Server


class RunMain:
    def run_method(self):
        print "start runmethod..."
        server = Server()
        server.main()
        case_data = GetCaseData(0)
        action_method = ActionMothod(0)
        lines = case_data.get_case_lines()
        for i in range(1, lines):
            handle_step = case_data.get_handle_step(i)
            element_key = case_data.get_element_key(i)
            handle_value = case_data.get_handle_value(i)
            expect_element = case_data.get_except_element(i)
            expect_step = case_data.get_except_step(i)
            handle_method = getattr(action_method, handle_step)
            if element_key != '':
                handle_method(element_key, handle_value)
            else:
                handle_method(handle_value)
            print u"预期步骤是：" + expect_step
            if expect_step != '':
                expect_result = getattr(action_method, expect_step)
                result = expect_result(expect_element)
                print result
                if result:
                    case_data.write_value(i, "pass")
                    print "------------------pass--------------------"
                else:
                    case_data.write_value(i, "fail")
                    print "------------------fail--------------------"


if __name__ == "__main__":
    run = RunMain()
    run.run_method()
