const books = [
    {
        title: 'The Impossibe is Possible',
        description: 'Inspirational Book',
        numberOfPages: 60,
        author: 'John Mason',
        reading: true,
    },    
    {
        title: 'Programming',
        description: 'Fundamentals of Programming',
        numberOfPages: 100,
        author: 'Adetomiwa Aderinto',
        reading: true,
    },
    {
        title: 'Data Analysis',
        description: 'Inroduction to Data Analysis',
        numberOfPages: 150,
        author: 'Jamaal Braimah',
        reading: false,
    }
];

// console.log(books)
// log all books where the reading status is true to the console

for(let i=0; i<=books.length; i++){
    if(books[i].reading === true){
        console.log(books[i])
    }
}