package com.amazon.amazonmq;


import org.apache.activemq.jms.pool.PooledConnectionFactory;
import org.apache.activemq.ActiveMQConnectionFactory;


import javax.jms.Connection;
import javax.jms.DeliveryMode;
import javax.jms.Destination;
import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.MessageConsumer;
import javax.jms.MessageProducer;
import javax.jms.Session;
import javax.jms.TextMessage;

/**
 * Hello world!
 * 
 *
 */
public class App 
{
    public static void main( String[] args ) throws JMSException
    {
        
        // Create a connection factory.
        ActiveMQConnectionFactory connectionFactory = new ActiveMQConnectionFactory("ssl://b-04b4eb30-c958-4da7-9e58-78e581a1eae1-1.mq.us-east-1.amazonaws.com:61617");

        
        // Specify the username and password.
        connectionFactory.setUserName("west0706");
        connectionFactory.setPassword("tkfkddmldhkd");

        // Create a pooled connection factory.
        PooledConnectionFactory pooledConnectionFactory = new PooledConnectionFactory();
        pooledConnectionFactory.setConnectionFactory(connectionFactory);
        pooledConnectionFactory.setMaxConnections(10);       
        
        // Establish a connection for the producer.
        Connection producerConnection = pooledConnectionFactory.createConnection();
        producerConnection.start();


        // Create a session.
        Session producerSession = producerConnection.createSession(false, Session.AUTO_ACKNOWLEDGE);

        // Create a queue named "MyQueue".
        Destination producerDestination = producerSession.createQueue("active01");

        // Create a producer from the session to the queue.
        MessageProducer producer = producerSession.createProducer(producerDestination);
        producer.setDeliveryMode(DeliveryMode.NON_PERSISTENT);




        // Create a message.
        String text = "Hello from Amazon MQ!";
        TextMessage producerMessage = producerSession.createTextMessage(text);


        for(int i=0; i<5000; i++) {
            producer.send(producerMessage);
            System.out.println(producerMessage);
            System.out.println(i);

            try {
                Thread.sleep(5000);
            } catch (Exception e) {
                //TODO: handle exception
            }
        }
        // Send the message.


        producer.close();
        producerSession.close();
        producerConnection.close();        
    }
}





