import React, { Component} from 'react';

const list = [{"id":1,"title":"Create api endpoint","body":"Configuration with URLs, views, serializers."},{"id":2,"title":"Consume API","body":"Call API endpoint to get a 200!"}]

class App extends Component{
  constructor(props) {
    super(props);
      this.state = {list};
    }
  render(){
    return(
      <div>
        {this.state.list.map(item => (
          <div key={item.id}>
            <h2>{item.id}.- {item.title}</h2>
              <p>{item.body}</p>
          </div>
        ))}
        </div>
    );
        }
  }


export default App;
