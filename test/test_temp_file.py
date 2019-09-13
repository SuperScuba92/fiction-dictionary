from fict_dict.dataTempFile import dataFile
import unittest
import os

#TODO
'''
  Test implemented functions
'''
class test_temp_file(unittest.TestCase):

    test_temp=dataFile()
    testDict={"A": ["The quick brown fox jumps over the lazy dog"]}
    testDictTwo={"Abba": ["A Band"], "Abba-Kadabra" : ["A magical command"]}

    def setUp(self):
        self.test_temp.setNewDictionary(self.testDict, "A")


    def tearDown(self):
        #Remove any temp files remaining after testing
        if(os.path.isfile(self.test_temp.temp_abs)):
            os.remove(self.test_temp.temp_abs)
        self.test_temp.setNewDictionary({}, "")

    def test_setNewDictionary(self):
        self.test_temp.setNewDictionary(self.testDict, "testDict")
        self.assertEqual(self.test_temp.currentContext, self.testDict)

    def  test_createFile(self):
        try:
            result_dict=self.createFile_Helper()
            self.assertTrue(os.path.isfile(self.test_temp.temp_abs))
        except:
            self.fail("An unexpected FileError occured")

    def test_createFile_WithFile(self):
        try:
            result_dict=self.createFile_Helper()
            self.assertEqual(result_dict["currentContext"], self.testDict)
        except:
            self.fail("An unexpected FileError occured")

    def test_createFile_Errormessage(self):
        try:
            result_dict=self.test_temp.createFile()
            expectedErrorMsg="No default dictionary context was set create a populated dictionary first"
            self.assertEqual(result_dict["Error0"], expectedErrorMsg)
        except:
            self.fail("An unexpected FileError occured")

    #file should contain  second dictionary after update set up file with first dict
    #Then add second dict, and check for both
    def test_updateFile(self):
        self.fail()

    def test_dictionaryString(self):
        self.fail()

    def test_deleteFile(self):
        self.fail()

    def test_toStringSingle(self):
        expectedValue="Dictionary name: TestA\nA: The quick brown fox jumps over the lazy dog.\n"
        actualValue=test_temp.currentContext_toString()
        assertEqual(expectedValue, actualValue)

    def test_key_toString(self):
        self.test_temp.setNewDictionary(self.testDictTwo, "B")
        self.test_temp.setContext("A")
        expectedValue="Dictionary name: TestB\n \
        Abba: A Band\n Abba-Kadabra: A magical command\n"
        actualValue=test_temp.currentContext_toString("B")


    def  test_setContext(self):
        self.fail()

    def test_Contains(self):
        self.fail()

    def createFile_Helper(self):
        self.test_temp.setNewDictionary(self.testDictTwo, "B")
        result=self.test_temp.createFile()
        return result