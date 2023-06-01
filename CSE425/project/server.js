const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;
const collectionName ='laptopKinbo'

mongoose
  .connect('mongodb+srv://simanta1:sm123@cluster0.cqstbgb.mongodb.net/CSE425', {
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


const Laptop = mongoose.model('Laptop', laptopSchema,collectionName);


app.use(bodyParser.json());

// api for fetching laptops
app.post('/api/things', async (req, res) => {
  try {
    const { price, type } = req.body;

    let laptops = [];

    if (type === 'type1') {
      laptops = await Laptop.find({ price: { $lte: price } });
    } else if (type === 'type2') {
      laptops = await Laptop.find({
        price: { $lte: price },
        name: { $regex: /GTX|RTX/i },
      });
    }

    res.json(laptops);
   // console.log(laptops)
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Error occurred while fetching' });
  }
});


app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
