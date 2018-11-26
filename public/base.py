#!/usr/bin/python3
# coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from public.log import My_Log
from config import globalparam
import time
import os

success = "Success"
fail = "Fail "
logger = My_Log()

class Page():
    # 页面基础类，用于所有类的继承
    def __init__(self, driver, base_url=globalparam.url, parent=None):
        self.driver = driver
        self.base_url = base_url
        self.parent = parent

    # 拼接并进入url站点
    def _open_url(self, url):
        url = self.base_url + url
        self.driver.get(url)

    # 进入url站点
    def open_url(self,url):
        """
        open url.
        Usage:
        driver.open("http://www.fengsulian.com")
        """
        start_time = time.time()
        nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")
        file_name = 'open->%s.jpg' % nowTime
        file_path = globalparam.exception_image_path + "\\" + file_name
        try:
            self._open_url(url)
            self.my_print("{0}navigated to {1}, Spend {2} seconds"
                          "".format(success, self.base_url + url, "%.5f"%(time.time()-start_time)))
        except Exception:
            self.my_print("{0}unable to load {1}, Spend {2} seconds"
                          .format(fail, self.base_url + url, "%.5f"%(time.time()-start_time)))
            self.fail_img()
            raise

    # 浏览器窗口最大化
    def max_window(self):
        start_time = time.time()
        self.driver.maximize_window()
        self.my_print(("{0}set browser window maximized, Spend {1}"
                       "seconds").format(success, "%.5f"%(time.time()-start_time)))

    # 设置浏览器大小
    def set_window(self, width, highth):
        start_time = time.time()
        self.driver.set_window_size(width, highth)
        self.my_print("{0}set browser window width: {1},high: {2}, Spend {3} "
                      "seconds".format(success, width, highth, "%.5f"%(time.time()-start_time)))

    # 获取浏览器窗口大小
    def get_window(self):
        return self.driver.get_window_size()

    # 关闭当前窗口
    def close(self):
        """
        Simulates the user clicking the "close" button in the titlebar of a popup
        window or tab.
        Usage:
        driver.close()
        """
        start_time = time.time()
        self.driver.close()
        self.my_print("{0}closed the current window  the driver, Spend {1} seconds"
                      "".format(success, "%.5f"%(time.time()-start_time)))

    # 关闭浏览器
    def quit_browser(self):
        """
        Quit the driver and close all the windows.
        Usage:
        driver.quit()
        """
        start_time = time.time()
        self.driver.quit()
        self.my_print("{0}exit the browser, Spend {1} seconds"
                      "".format(success, "%.5f"%(time.time()-start_time)))


    # 等待元素出现与元素消失定位方式为：id、name、class、link_text、xpath或css)
    def element_wait_display(self, css, secs=3):
        locate_mode = css[0].strip()            # 获取元素定位方式
        msg = 'Element: {0}not found in {1} seconds'.format(css, secs)
        by_element = ['xpath', 'id', 'link text', 'css selector', 'name', 'class name']
        try:
            if locate_mode in by_element:
                WebDriverWait(self.driver,secs,0.5).until(EC.presence_of_element_located(css), msg)
            else:
                raise NameError("Please in element_wait_display enter the correct targeting "
                                "elements,'id','name','class','link_text','xpath','css.'")
        except NameError as name_error:
            print('...%s'%name_error)

    # 等待元素可见(定位方式为：id,name,class,link_text,xpath,css.)
    def element_wait_visible(self, css, secs=3):
        locate_mode = css[0].strip()        # 获取元素定位方式
        msg = 'Element:{0}not found in {1} secods'.format(css, secs)
        by_element = ['xpath', 'id', 'link text', 'css selector', 'name', 'class name']
        try:
            if locate_mode in by_element:
                WebDriverWait(self.driver,secs,0.5).until(EC.visibility_of_element_located(css),msg)
            else:
                raise NameError("Please in element_wait_display enter the correct targeting elements: "
                                "'id','name','class','link_text','xpath','css.'")
        except NameError as name_error:
            print('...%s'%name_error)

    # 封装定位方式（id,name,class,link_text,xpath,css）
    def get_element(self, css):
        """调用此方法的格式为: elemenr= self.get_element(css=(By.ID,"kw"))"""
        locate_mode = css[0].strip()
        value = css[1].strip()
        by_element=['xpath', 'id', 'link text', 'css selector', 'name', 'class name']
        try:
            if locate_mode in by_element:
                element = self.driver.find_element(locate_mode, value)
            else:
                raise NameError("Please in element_wait_display enter the correct targeting elements: "
                                "'id','name','class','link_text','xpath','css.")
        except NameError as name_error:
            print('...%s'%name_error)
        else:
            return element

    # 打印info日志
    def my_print(self, message):
        logger.info(message)

    def my_error(self, message):
        logger.error(message)


    # 操作输入框
    def input_box(self,css,text):
        """
        Operation input box.
        Usage:
        driver.type("id->kw","selenium")
        """
        start_time = time.time()
        css1 = css[0] + "->" +css[1]
        base_path = os.path.dirname(os.path.abspath(__file__))
        try:
            self.element_wait_display(css)
            self.get_element(css).send_keys(text)
            self.my_print("{0}typed element: <{1}> content: {2}, Spend {3} seconds "
                          "-- from: {4}".format(success,css1,text, time.time()-start_time,base_path))
        except Exception:
            self.my_print("{0}unable to type element: <{1}> content: {2},Spend {3} "
                          "seconds-- from: {4} ->{5}".format(fail, css1, text, "%.5f"%
                                                             (time.time()-start_time), base_path, self))
            self.fail_img()
            raise

    # 清空输入框，再次输入内容
    def clear_box(self, css, text):
        start_time = time.time()
        css1 = css[0] + "->" + css[1]
        base_path = os.path.dirname(os.path.abspath(__file__))
        try:
            self.element_wait_display(css)
            el = self.get_element(css)
            el.clear()
            el.send_keys(text)
            self.my_print("{0}typed element: <{1}> content: {2}, Spend {3} seconds "
                          "-- from: {4}".format(success, css1, text, "%.5f"%(time.time()-start_time),
                                                base_path))
        except Exception:
            self.my_print("{0}unable to type element: <{1}> content: {2},Spend {3} seconds-- "
                          "from: {4} ->{5}".format(fail, css1, text, "%.5f"%(time.time()-start_time),
                                                   base_path, self))
            self.fail_img()
            raise

    # 鼠标点击
    def click(self, css):
        """
        It can click any text / image can be clicked
        Connection, check box and radio buttons etc..
        Usage:
        self.driver.click(css=(By.ID,'kw'))
        """
        start_time = time.time()
        css1 = css[0] + "->" + css[1]
        try:
            self.element_wait_display(css)
            self.get_element(css).click()
            self.my_print("{0}clicked element: <{1}>, Spend {2} seconds"
                          "".format(success, css1, "%.5f"%(time.time()-start_time)))
        except Exception:
            self.my_print("{0}clicked element: <{1}>, Spend {2} seconds ->{3}"
                          "".format(fail, css1, "%.5f"%(time.time()-start_time), self))
            raise

    # 鼠标右键单击
    def right_click(self, css):
        """
        Right click element.
        Usage:
        driver.right_click("id->kw")
        """
        start_time = time.time()
        css1 = css[0] +"->" +css[1]
        try:
            self.element_wait_display(css)
            ActionChains(self.driver).context_click(self.get_element(css)).perform()
            self.my_print("{0}right click element: <{1}>, Spend {2} seconds"
                          "".format(success, css1, "%.5f"%(time.time()-start_time)))
        except Exception:
            self.my_print("{0}right click element: <{1}>, Spend {2} seconds ->{3}"
                          "".format(fail, css1, "%.5f"%(time.time()-start_time), self))
            raise

    # 鼠标悬停
    def move_to_element(self,css):
        """
        Mouse over the element.
        Usage:
        driver.move_to_element("id->kw")
        """
        start_time = time.time()
        css1 = css[0] + "->" + css[1]
        try:
            self.element_wait_display(css)
            ActionChains(self.driver).move_to_element(self.get_element(css))
            self.my_print("{0}move to element:<{1}>, Spend {2} seconds"
                          "".format(success, css1, "%.5f"%(time.time()-start_time)))
        except Exception:
            self.my_print("{0}move to element:<{1}>, Spend {2} seconds ->{3}".
                          format(fail, css1, "%.5f"%(time.time()-start_time), self))
            raise

    # 鼠标双击
    def double_click(self, css):
        """
        Double click element.
        Usage:
        driver.double_click("id->kw")
        """
        start_time = time.time()
        css1 = css[0] + "->" + css[1]
        print(css1)
        try:
            ActionChains(self.driver).double_click(css)
            self.my_print("{0}double click element: <{1}>, Spend {2} seconds"
                          "".format(success, css1, "%.5f"%(time.time()-start_time)))
        except Exception:
            self.my_print("{0}double click element: <{1}>, Spend {2} seconds ->{3}"
                          "".format(fail, css1, "%.5f"%(time.time()-start_time), self))
            raise

    # 鼠标拖拽
    def drag_and_drop(self, drag_css, drop_css):
        """
        Drags an element a certain distance and then drops it.
        Usage:
        driver.drag_and_drop("id->kw","id->su")
        """
        ag_css = drag_css[0]+"->"+ drag_css[1]
        op_css = drop_css[0]+"->"+ drop_css[1]
        start_time = time.time()
        try:
            self.element_wait_display(drag_css)
            ag_element = self.get_element(drag_css)
            self.element_wait_display(drop_css)
            op_element = self.get_element(drop_css)
            ActionChains(self.driver).drag_and_drop(ag_element, op_element).perform()
            self.my_print("{0}drag and drop element: <{1}> to element: <{2}>, Spend {3} seconds"
                          "".format(success, ag_css, op_css, "%.5f"%(time.time()-start_time)))
        except Exception:
            self.my_print("{0}drag and drop element: <{1}> to element: <{2}>, Spend {3} seconds ->{4}"
                          "".format(fail, ag_css, op_css, "%.5f"%(time.time()-start_time), self))
            raise

    # 点击text
    def click_text(self, text):
        """
        Click the element by the link text
        Usage:
        driver.click_text("新闻")
        """
        start_time = time.time()
        try:
            self.driver.find_element_by_partial_link_text(text).click()
            self.my_print("{0}click by text content: {1}, Spend {2} seconds"
                          "".format(success, text, "%.5f"%(time.time()-start_time)))
        except Exception:
            self.my_print("{0}click by text content: {1}, Spend {2} seconds ->{3}"
                          "".format(fail, text, "%.5f"%(time.time()-start_time), self))
            raise

    # 刷新浏览器
    def F5(self):
        """
        Refresh the current page.
        Usage:
        driver.F5()
        """
        start_time = time.time()
        self.driver.refresh()
        self.my_print("{0}refresh the current page, Spend {1} seconds"
                      "".format(success, "%.5f"%(time.time()-start_time)))

    # 获取元素属性的值
    def get_attribute(self, css, attribute):
        """
        Gets the value of an element attribute.
        Usage:
        driver.get_attribute("id->su","href")
        """
        css1 = css[0] + "->" + css[1]
        start_time = time.time()
        try:
            element = self.get_element(css)
            attr = element.get_attribute(attribute)
            if attr is None:
                raise AttributeError
            else:
                self.my_print("{0}get attribute element: <{1}>,attribute: {2}, Spend {3} seconds"
                              "".format(success, css1, attribute, "%.5f"%(time.time()-start_time)))
                return attr
        except Exception:
            self.my_print("{0}to get the attribute ({2}) of the element <{1}>, Spend {3} seconds"
                          " ->{4}".format(fail, css1, attribute, "%.5f"%(time.time()-start_time), self))
            raise

    # 获取操作元素的text
    def get_text(self, css):
        """
        Get element text information.
        Usage:
        driver.get_text("id->kw")
        """
        start_time = time.time()
        css1 = css[0] + "->" + css[1]
        self.element_wait_display(css)
        text = self.get_element(css).text
        self.my_print("{0}get element text element: <{1}>, Spend {2} seconds"
                      "".format(success, css1, "%.5f"%(time.time()-start_time)))
        return text

    # 获取title
    def get_title(self):
        """
        Get window title.
        Usage:
        title = driver.get_title()
        """
        start_time = time.time()
        title = self.driver.title
        self.my_print("{0}get current window title, Spend {1} seconds"
                      "".format(success, "%.5f"%(time.time()-start_time)))
        return title

    # 获取url
    def get_url(self):
        """
        Get the URL address of the current page.
        Usage:
        url = driver.get_url()
        """
        start_time = time.time()
        url = self.driver.current_url
        self.my_print("{0}get current window url, Spend {1} seconds"
                      "".format(success, "%.5f"%(time.time()-start_time)))
        return url

    # 隐性等待
    def wait(self,secs=5):
        """
        Implicitly wait.All elements on the page.
        Usage:
        driver.wait(secs=10)
         """
        self.driver.implicitly_wait(secs)
        self.my_print("{0}set wait all element display in {1} seconds.".format(success, secs))

    # 接受警告弹框
    def accept_alert(self):
        """
        Accept warning box.
        Usage:
        driver.accept_alert()
        """
        start_time = time.time()
        self.driver.switch_to.alert.accept()
        self.my_print("{0}accept warning box, Spend {1} seconds"
                      "".format(success, "%.5f"%(time.time()-start_time)))

    # 解除警告弹框
    def dismiss_alert(self):
        """
        Dismisses the alert available.
        Usage:
        driver.dismiss_alert()
        """
        start_time = time.time()
        self.driver.switch_to.alert.dismiss()
        self.my_print("{0}dismisses the alert available, Spend {1} seconds"
                      "".format(success, "%.5f"%(time.time()-start_time)))

    # 切换到指定的frame
    def switch_to_frame(self, css='default', index='default'):
        """
        Switch to the specified frame.
        Usage:
        driver.switch_to_frame(css = "id->kw")  or  driver.switch_to_frame(index=1)
        """
        start_time = time.time()
        try:
            if index == 'default' or css != 'default':
                css1 = css[0] + "->" + css[1]
                self.driver.switch_to.frame(self.get_element(css))
                self.my_print("{0}switch to frame element: <{1}>, Spend {2} seconds"
                              "".format(success, css1, "%.5f"%(time.time()-start_time)))
            elif index != 'default' or css == 'default':
                self.driver.switch_to.frame(index)
                self.my_print("{0}switch to index {1} frame, Spend {2} seconds"
                              "".format(success, index, "%.5f"%(time.time()-start_time)))
        except Exception:
            self.my_print("{0}unable switch to frame, Please re-enter the element "
                          "or index ->{1}".format(fail, self))
            raise

    # 返回上层(父)frame
    def switch_to_frame_out(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.
        Usage:
        driver.switch_to_frame_out()
        """
        start_time = time.time()
        self.driver.switch_to.default_content()
        self.my_print("{0}switch to frame out, Spend {1} seconds"
                      "".format(success, "%.5f"%(time.time()-start_time)))

    # 判断元素是否存在，返回布尔值
    def element_exist(self, css):
        """
        judge element is exist,The return result is true or false.
        Usage:
        driver.element_exist("id->kw")
        """
        start_time = time.time()
        css1 = css[0] + "->" + css[1]
        try:
            self.element_wait_display(css)
            self.my_print("{0}element: <{1}> is exist, Spend {2} seconds"
                          .format(success, css1, "%.5f"%(time.time()-start_time)))
            return True
        except TimeoutException:
            self.my_print("{0}element: <{1}> is not exist, Spend {2} seconds ->{3}"
                          .format(fail, css1, "%.5f"%(time.time()-start_time), self))
            self.fail_img()
            return False

    # 异常截图
    def fail_img(self):
        fail_name = '%s.png' % time.strftime('%Y_%m_%d_%H_%M_%S')
        fail_path = globalparam.exception_path + '\\' + fail_name
        self.driver.get_screenshot_as_file(fail_path)

    # 断言截图
    def assert_img(self):
        file_name = 'assert(%s).png' % time.strftime("%Y_%m_%d_%H_%M_%S")
        file_path = globalparam.exception_path + "\\" + file_name
        self.driver.get_screenshot_as_file(file_path)

    # 屏幕截图
    def take_screenshot(self, file_path):
        """
        Get the current window screenshot.
        Usage:
        driver.take_screenshot('c:\a1.png')
        """
        # fiel_name = '%s.png'%time.strftime('%Y_%m_%d_%H_%M_%S')
        start_time = time.time()
        try:
            self.driver.get_screenshot_as_file(file_path)
            self.my_print("{0}get the current window screenshot,path: {1}, Spend {2} seconds"
                          "".format(success, file_path, "%.5f"%(time.time()-start_time)))
        except Exception:
            self.my_print("{0}unable to get the current window screenshot,path: {1}, Spend {2} seconds"
                          " ->{3}".format(fail, file_path, "%.5f"%(time.time()-start_time), self))
            self.fail_img()
            raise

    # 点击按钮，打开打开新网页并切换到新网页窗口
    def open_new_window(self, css):
        """
        Open the new window and switch the handle to the newly opened window.
        Usage:
        driver.open_new_window("id->kw")
        """
        start_time = time.time()
        css1 = css[0] + "->" + css[1]
        try:
            original_windows = self.driver.window_handles
            element = self.get_element(css)
            element.click()
            all_handles = self.driver.window_handles
            for handle in all_handles:
                if handle != original_windows:
                    self.driver.switch_to.window(handle)
            self.my_print("{0}click element: <{1}> open a new window and swich into, Spend {2}"
                          " seconds".format(success, css1, "%.5f" % (time.time() - start_time)))
        except Exception:
            self.my_print("{0}click element: <{1}> open a new window and swich into, Spend {2} seconds"
                          " ->{3}".format(fail, css1, "%.5f" % (time.time() - start_time), self))
            raise

    # 切换到最后打开的窗口(窗口句柄按打开顺序形成列表)
    def into_finally_window(self):
        """
        Into the new window.
        Usage:
        dirver.into_new_window()
        """
        start_time = time.time()
        try:
            all_handles = self.driver.window_handles
            flag = 0
            while len(all_handles) < 2:
                time.sleep(1)
                all_handles = self.driver.window_handles
                flag += 1
                if flag == 5:
                    break
            self.driver.switch_to.window(all_handles[-1])
            self.my_print("{0}switch to the new window,new window's url: {1}, Spend {2} seconds"
                          "".format(success, self.driver.current_url, "%.5f"%(time.time()-start_time )))
        except Exception:
            self.my_print("{0}unable switch to the new window, Spend {1} seconds ->{2}"
                          "".format(fail, "%.5f"%(time.time()-start_time), self))
            self.fail_img()
            raise

    # 操作输入框，回车键提交
    def box_and_enter(self, css, text, secs=0.5):
        """
        Operation input box. 1、input message,sleep 0.5s;2、input ENTER.
        Usage:
        driver.type_css_keys('id->kw','beck')
        """
        start_time = time.time()
        css1= css[0] + "->" + css[1]
        try:
            self.element_wait_visible(css)
            ele = self.get_element(css)
            ele.send_keys(text)
            time.sleep(secs)
            ele.send_keys(Keys.ENTER)
            self.my_print("{0}element <{1}> type content: {2},and sleep {3} seconds,"
                          "input ENTER key, Spend {4} seconds".format(success, css1, text, secs,
                                                                      "%.5f"%(time.time()-start_time)))
        except Exception:
            self.my_print(
                "{0}unable element <{1}> type content: {2},and sleep {3} seconds,input"
                " ENTER key, Spend {4} seconds ->{5}".format(fail, css1, text, secs,
                                                       "%.5f"%(time.time()-start_time), self))
            self.fail_img()
            raise

    # 判断文本是否存在于元素中
    def is_text_in_element(self, locator, text, timeout=5):
        """
        判断文本在元素里,没定位到元素返回False，定位到返回判断结果布尔值
        Usage:
        result = driver.is_text_in_element(locator=(By.ID, 'su'), text='百度一下')
        """
        start_time = time.time()
        locator1 = locator[0] + "->" + locator[1]
        try:
            result = WebDriverWait(self.driver, timeout, 0.5).until\
                (EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            self.my_print("{0}element not positioned: <{1}> , Spend {2} seconds ->{3}"
                          "".format(fail, locator1, "%.5f"%(time.time()-start_time), self))
            self.fail_img()
            return False
        else:
            self.my_print("{0}positioned to element: <{1}> , Spend {2} seconds"
                          "".format(success, locator1, "%.5f"%(time.time()-start_time)))
            return result

    # 判断元素的value
    def is_text_in_value(self, locator, value, timeout=5):
        """
        判断元素的value值，没定位到元素返回false,定位到返回判断结果布尔值
        Usage:
        result = driver.text_in_element(locator=(By.ID, 'su', value='百度一下')
        """
        start_time = time.time()
        locator1 = locator[0] + "->" + locator[1]
        try:
            result = WebDriverWait(self.driver,timeout,0.5).until\
                (EC.text_to_be_present_in_element_value(locator, value))
        except TimeoutException:
            self.my_print("{0}element not positioned: <{1}> , Spend {2} seconds ->{3}"
                          .format(fail, locator1, "%.5f"%(time.time()-start_time), self))
            self.fail_img()
            return False
        else:
            self.my_print("{0}positioned to element: <{1}> , Spend {2} seconds"
                          .format(success, locator1, "%.5f"%(time.time()-start_time)))
            return result

    # 页面中查找一组元素
    def find_elements(self, *loc):
        try:
            if len(self.driver.find_elements(*loc)) >1:
                return self.driver.find_elements(*loc)
        except:
            print("%s cannot find  elements %s in page." %(self, loc))

    # 断言文本相等
    def assert_equal(self, loc, text):
        """
        say with certainty
        Usage:
        self.assertEqual(loc=self.get_title(),text='百度一下，你就知道')
        """
        start_time = time.time()
        try:
            self.assertEqual(loc, text)
            self.my_print("{0}say with certainty: {1} == {2}, Spend {3} seconds"
                          "".format(success, loc, text, "%.5f"%(time.time()-start_time)))
        except Exception:
            self.my_print("{0}say with certainty: {1} != {2}, Spend {3} seconds ->{4}"
                          "".format( fail, loc, text, "%.5f"%(time.time()-start_time), self))
            self.assert_img()
            raise

    # 断言文本
    def assert_notequal(self, loc, text):
        """
        say with certainty
        Usage:
        self.assert_notequal(loc=self.get_title(),text='百度一下，你就知道')
        """
        start_time = time.time()
        try:
            self.assertNotEqual(loc, text)
            self.my_print("{0}say with certainty: {1} != {2}, Spend {3} seconds"
                          .format(success, loc, text, "%.5f"%(time.time()-start_time)))
        except:
            self.my_print("{0}say with certainty: {1} == {2}, Spend {3} seconds ->{4}"
                          .format(fail, loc, text, "%.5f"%(time.time()-start_time), self))
            self.assert_img()
            raise


    # 执行js脚本
    def js(self, script):
        """
        Execute JavaScript scripts.
        Usage:
        driver.js("window.scrollTo(200,1000);")
        """
        t1 = time.time()
        try:
            self.driver.execute_script(script)
            self.my_print("{0}execute javascript scripts: {1}, Spend {2} seconds".format(success,script, time.time() - t1))
        except Exception:
            self.my_print("{0}unable to execute javascript scripts: {1}, Spend {2} seconds".format(fail,
                script, time.time() - t1))
            self.fail_img()
            raise


if __name__ == "__main__":
    print('succes')

