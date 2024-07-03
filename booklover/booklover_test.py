import unittest
from booklover import BookLover
class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        self.assertTrue(test_object.has_read("War of the Worlds"))
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_object = BookLover("Muscleman", "mymom@mymom.com", "science fiction")
        test_object.add_book("Muscle Man's Guide To Life", 5)
        test_object.add_book("Muscle Man's Guide To Life", 5)
        self.assertEqual(len(test_object.book_list[test_object.book_list['book_name'] == "Muscle Man's Guide To Life"]), 1)        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_object = BookLover("Muscleman", "mymom@mymom.com", "science fiction")
        test_object.add_book("Muscle Man's Guide To Life", 5)
        self.assertTrue(test_object.has_read("Muscle Man's Guide To Life"))
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_object = BookLover("Muscleman", "mymom@mymom.com", "science fiction")
        test_object.add_book("Muscle Man's Guide To Life", 5)
        self.assertFalse(test_object.has_read("Best My Mom Jokes"))
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test_object = BookLover("Brennan Thompson", "nunyabiz@nunyabiz.com", "Non-fiction")
        test_object.add_book("Dummies Guide to Coding", 1)
        test_object.add_book("How to Code for Idiots", 1)
        test_object.add_book("Recognizing When You're In Over Your Head", 2)
        self.assertEqual(test_object.num_books_read(), 3)
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test_object = BookLover("Brennan Thompson", "nunyabiz@nunyabiz.com", "Non-fiction")
        test_object.add_book("Charlie Wilson's War", 5)
        test_object.add_book("Tuntematon Sotilas", 5)
        test_object.add_book("Education of a Wandering Man", 4) 
        self.assertTrue((test_object.fav_books()['book_rating'] > 3).all())
if __name__ == '__main__':
    unittest.main(verbosity=3)