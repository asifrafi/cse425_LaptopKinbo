const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');


const collectionName ='laptopKinbo'

const app = express();
const port = 5000;

app.use(express.json());
app.use(cors());

mongoose
  .connect('mongodb+srv://asiflogin:asif321@cluster0.scqzz.mongodb.net/CSE425', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => {
    console.log('MongoDB connected');
  })
  .catch((error) => {
    console.error('Error while connecting to MongoDB:', error);
  });//


const laptopSchema = new mongoose.Schema({
  name: String,
  price: Number,
});




// Create the Laptop model
const LaptopModel = mongoose.model('Laptop', laptopSchema,collectionName);


// API endpoint: GET /laptop/kinbo/api/
app.get('/laptop/kinbo/api/', async (req, res) => {
  try {
    const laptops = await LaptopModel.find();
    res.json(laptops);
  } catch (error) {
    res.status(500).send('Error retrieving laptops');
  }
});

// API endpoint: GET /laptopdetails/:pk/
app.get('/laptopdetails/:pk/', async (req, res) => {
  try {
    const laptop = await LaptopModel.findById(req.params.pk);
    if (laptop) {
      res.json(laptop);
    } else {
      res.status(404).send('Laptop not found');
    }
  } catch (error) {
    res.status(500).send('Error retrieving laptop details');
  }
});

// API endpoint: GET /laptopinrange/:l/:h/
app.get('/laptopinrange/:l/:h/', async (req, res) => {
  try {
    const laptops = await LaptopModel.find({
      price: { $gt: req.params.l, $lt: req.params.h },
    });
    res.json(laptops);
  } catch (error) {
    res.status(500).send('Error retrieving laptops');
  }
});

// API endpoint: GET /gaminglaptop/:l/:h/
app.get('/gaminglaptop/:l/:h/', async (req, res) => {
  try {
    const laptops = await LaptopModel.find({
      price: { $gt: req.params.l, $lt: req.params.h },
      name: { $regex: /RTX|GTX/i },
    });
    res.json(laptops);
  } catch (error) {
    res.status(500).send('Error retrieving gaming laptops');
  }
});

// API endpoint: GET /mac/:l/:h/
app.get('/mac/:l/:h/', async (req, res) => {
  try {
    const laptops = await LaptopModel.find({
      price: { $gt: req.params.l, $lt: req.params.h },
      name: { $regex: /MacBook/i },
    });
    res.json(laptops);
  } catch (error) {
    res.status(500).send('Error retrieving MacBooks');
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});