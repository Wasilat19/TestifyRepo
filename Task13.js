// My Personal Library 2

const book = {
    title: 'The Impossible is Possible',
    description: 'Inspirational',
    numberOfPages: 60,
    author: 'John Mason',
    reading: false,
    toggleReadingStatus: function(){
        if(book.reading === true){
            book.reading = false
        }else{
            book.reading = true
        }
    }
}
book.toggleReadingStatus()
console.log(book.reading)