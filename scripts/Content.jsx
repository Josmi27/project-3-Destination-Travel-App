import * as React from 'react';
import { Socket } from './Socket';
import { Chat } from './Chat';



export class Content extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'username' :[],
            'messages': [], 
            'message_array': []
        };
    }
    
    componentDidMount() {
        Socket.on('message received', (data) => {
            this.setState({
                'username_present': data['Username'],
                'message_received': data['Message']
            });
        
            
        });
    
        Socket.on('message array', (data) => {
            this.setState({
                'message_array': data['data']
            });
        });
        
        
    }
    

    render() {
        
        const listItems = this.state.message_array.map((a, index) =>
            <p className="number-item chatbubble" key={index}>{a}</p>
        );
        
        return (
            <html>
            <body>
                <div className="rcontainer">
                
                    <div className="container">
                        <h4 className="chat_title"> Welcome to the Relaxation Chat Room! </h4>
                        <div className="chat-page">
                    
                        <div className="msg-inbox">
                            <div className="chats">
                                <div className="msg-page">
                                <div className="received-msg">
                                <div className="received-msg-inbox">
                                {listItems}
                                        
                                </div>
                                </div>
                                </div>
                                </div>
                        </div>
                    </div>
                </div>
                <div className="msg-bottom">
                    <div> <Chat /> </div>
                </div>
                </div>
            </body>
            </html>
        );
    }
}







    