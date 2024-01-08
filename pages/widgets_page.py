from locators.widgets_page_locators import AccordianPageLocators
from pages.base_page import BasePage

class AccordianPage(BasePage):

    locators = AccordianPageLocators()

    def check_accordian(self, accordian_number):
        accordian = {'first':
                         {'title': self.locators.SECTION_FIRST,
                          'content': self.locators.SECTION_CONTENT_FIRST},
                     'second':
                         {'title': self.locators.SECTION_SECOND,
                          'content': self.locators.SECTION_CONTENT_SECOND},
                     'third':
                         {'title': self.locators.SECTION_THIRD,
                          'content': self.locators.SECTION_CONTENT_THIRD}
                     }
        section_title = self.element_is_present(accordian[accordian_number]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_number]['content'])
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_number]['content'])
        return [section_title.text, len(section_content.text)]