class Node{
  constructor(data){
    this.data = data
    this.next = null
  }
}

class LinkedList{
  constructor(data){
    if (data == null){
      this.head = null
      this.tail = null
      this.length =0
    }else{
      let new_node = new Node(data)
      this.head = new_node
      this.tail = new_node
      this.length = 1
    }
  }
}


l1 = new LinkedList(1)
console.log(l1.head.data)
