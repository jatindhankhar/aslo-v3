import aslo.api.i18n as i18n
import tempfile


class Test_i18n(object):

    def test_should_return_empty_dictionary_for_missing_po_files(self):
        mock_translations = i18n.get_translations(tempfile.mktemp())
        assert(not bool(mock_translations))

    def test_should_return_correct_language_code(self):
        target_file = "po/zh_TW.po"
        correct_language_code = "zh_TW"
        assert(i18n.get_language_code(target_file) == correct_language_code)
