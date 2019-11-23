from com.ankit.books.books import Book

temp=[]
while True:
    print('--------------------------------')
    print('a. Enter book details.','b. View Book.','c. Search book.','d. Remove book.','e. Exit.',sep='\n')
    choice=input('Please enter your choice: ')
    
    if choice == 'a':
        bid=input('Enter book id: ')
        flag = True
        if len(temp)>0:
            temp=b.get_data()
            for i in temp:
                if i.bid == bid:
                    print('Id Already exists.')
                    flag = False
                    break
        if flag == True:
            title=input('Enter book title: ')
            pages=input('Enter book pages: ')
            price=input('Enter book price: ')
            b=Book(bid=bid,title=title,pages=pages,price=price)
            b.add_data()
            temp=b.get_data()

    elif choice == 'b':
        b=Book()
        temp=b.get_data()
        print('Book details are:\n')
        for i in temp:
            print('Book id: {0}, Book Title: {1}, Book Pages: {2} ,Book Price: {3}'.format(i.bid,i.title,i.price,i.pages))
        
    elif choice == 'c':
        bid=input('Enter book id :')
        temp=b.get_data()
        flag=True
        for i in temp:
            if i.bid == bid:
                print(i.get_details())
                flag=False
        if flag==True:
            print('Books details not found.')
        continue

    elif choice == 'd':
        bid=input('Enter book id :')
        temp=b.get_data()
        flag=True

        for i in temp:
            if i.bid == bid:
                i.remove_data()
                flag=False
        if flag==True:
            print('Book details not found.')
        continue

    elif choice == 'e':
        break
    else:
        print("Invalid option. Please try again.")




    
    

