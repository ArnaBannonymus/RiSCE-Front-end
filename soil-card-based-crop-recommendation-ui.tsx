import React, { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Leaf, Upload, MapPin } from 'lucide-react';

// Simplified dataset (same as before)
const cropData = [
  { crop: 'rice', nitrogen: 80, phosphorus: 45, potassium: 40, ph: 6.5, temperature: 23, humidity: 80, rainfall: 200 },
  { crop: 'maize', nitrogen: 70, phosphorus: 45, potassium: 20, ph: 6.5, temperature: 22, humidity: 65, rainfall: 80 },
  { crop: 'chickpea', nitrogen: 40, phosphorus: 60, potassium: 80, ph: 7.0, temperature: 18, humidity: 15, rainfall: 80 },
  { crop: 'kidneybeans', nitrogen: 20, phosphorus: 60, potassium: 20, ph: 5.8, temperature: 19, humidity: 20, rainfall: 100 },
  { crop: 'pigeonpeas', nitrogen: 20, phosphorus: 60, potassium: 20, ph: 5.8, temperature: 28, humidity: 50, rainfall: 120 },
  { crop: 'mothbeans', nitrogen: 20, phosphorus: 40, potassium: 20, ph: 6.5, temperature: 28, humidity: 50, rainfall: 50 },
  { crop: 'mungbean', nitrogen: 20, phosphorus: 40, potassium: 20, ph: 6.5, temperature: 28, humidity: 80, rainfall: 50 },
  { crop: 'blackgram', nitrogen: 40, phosphorus: 60, potassium: 20, ph: 7.0, temperature: 28, humidity: 65, rainfall: 70 },
  { crop: 'lentil', nitrogen: 20, phosphorus: 60, potassium: 20, ph: 6.5, temperature: 22, humidity: 65, rainfall: 50 },
  { crop: 'pomegranate', nitrogen: 20, phosphorus: 10, potassium: 40, ph: 6.5, temperature: 22, humidity: 90, rainfall: 110 },
  { crop: 'banana', nitrogen: 100, phosphorus: 75, potassium: 50, ph: 6.5, temperature: 27, humidity: 80, rainfall: 100 },
  { crop: 'mango', nitrogen: 20, phosphorus: 20, potassium: 30, ph: 5.5, temperature: 30, humidity: 50, rainfall: 100 },
  { crop: 'grapes', nitrogen: 20, phosphorus: 125, potassium: 200, ph: 6.0, temperature: 25, humidity: 80, rainfall: 80 },
  { crop: 'watermelon', nitrogen: 100, phosphorus: 10, potassium: 50, ph: 6.5, temperature: 25, humidity: 90, rainfall: 50 },
  { crop: 'muskmelon', nitrogen: 100, phosphorus: 10, potassium: 50, ph: 6.5, temperature: 28, humidity: 90, rainfall: 50 },
  { crop: 'apple', nitrogen: 20, phosphorus: 125, potassium: 200, ph: 6.0, temperature: 22, humidity: 90, rainfall: 110 },
  { crop: 'orange', nitrogen: 20, phosphorus: 10, potassium: 10, ph: 6.5, temperature: 25, humidity: 90, rainfall: 110 },
  { crop: 'papaya', nitrogen: 50, phosphorus: 50, potassium: 50, ph: 6.5, temperature: 35, humidity: 90, rainfall: 150 },
  { crop: 'coconut', nitrogen: 20, phosphorus: 10, potassium: 30, ph: 6.0, temperature: 27, humidity: 95, rainfall: 150 },
  { crop: 'cotton', nitrogen: 120, phosphorus: 40, potassium: 20, ph: 6.5, temperature: 25, humidity: 80, rainfall: 80 },
  { crop: 'jute', nitrogen: 80, phosphorus: 40, potassium: 40, ph: 6.5, temperature: 25, humidity: 80, rainfall: 170 },
  { crop: 'coffee', nitrogen: 100, phosphorus: 20, potassium: 30, ph: 6.5, temperature: 25, humidity: 60, rainfall: 150 }
];

const CropRecommendationUI = () => {
  const [soilData, setSoilData] = useState(null);
  const [recommendation, setRecommendation] = useState([]);
  const [uploadedImage, setUploadedImage] = useState(null);

  const handleImageUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      setUploadedImage(URL.createObjectURL(file));
      // Simulating image processing and data extraction
      setTimeout(() => {
        setSoilData({
          ph: 6.10,
          nitrogen: 561,
          phosphorus: 19.71,
          potassium: 166.88,
          temperature: 24.88921174, // Average value
          humidity: 81.97927117, // Average value
          rainfall: 185.9461429, // Average value
          location: {
            address: "Dikling, Pakyong,Sikkim",
            coordinates: "88.5953259,27.2354343"
          }
        });
      }, 1000);
    }
  };

  const getRecommendation = () => {
    if (!soilData) return;

    const { nitrogen, phosphorus, potassium, ph, temperature, humidity, rainfall } = soilData;
    
    const distances = cropData.map(crop => {
      const distance = Math.sqrt(
        Math.pow((crop.nitrogen - nitrogen) / 100, 2) +
        Math.pow((crop.phosphorus - phosphorus) / 10, 2) +
        Math.pow((crop.potassium - potassium) / 100, 2) +
        Math.pow(crop.ph - ph, 2) +
        Math.pow((crop.temperature - temperature) / 10, 2) +
        Math.pow((crop.humidity - humidity) / 10, 2) +
        Math.pow((crop.rainfall - rainfall) / 100, 2)
      );
      return { crop: crop.crop, distance };
    });

    const sortedRecommendations = distances
      .sort((a, b) => a.distance - b.distance)
      .slice(0, 3)
      .map(item => item.crop);

    setRecommendation(sortedRecommendations);
  };

  return (
    <div className="p-4">
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center">
            <Leaf className="mr-2" />
            Soil Health Card Based Crop Recommendation
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <div className="flex items-center justify-center w-full">
              <Label htmlFor="soil-image" className="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100">
                <div className="flex flex-col items-center justify-center pt-5 pb-6">
                  <Upload className="w-8 h-8 mb-4 text-gray-500" />
                  <p className="mb-2 text-sm text-gray-500"><span className="font-semibold">Click to upload</span> or drag and drop</p>
                  <p className="text-xs text-gray-500">Upload your Soil Health Card image</p>
                </div>
                <Input id="soil-image" type="file" className="hidden" onChange={handleImageUpload} accept="image/*" />
              </Label>
            </div>
            {uploadedImage && (
              <div className="mt-4">
                <img src={uploadedImage} alt="Uploaded soil health card" className="w-full max-h-64 object-cover rounded" />
              </div>
            )}
            {soilData && (
              <div className="mt-4">
                <h3 className="font-semibold">Extracted Soil Data:</h3>
                <p>pH: {soilData.ph}</p>
                <p>Nitrogen: {soilData.nitrogen} kg/ha</p>
                <p>Phosphorus: {soilData.phosphorus} kg/ha</p>
                <p>Potassium: {soilData.potassium} kg/ha</p>
                <div className="mt-2">
                  <h4 className="font-semibold">Location:</h4>
                  <p>{soilData.location.address}</p>
                  <p>Coordinates: {soilData.location.coordinates}</p>
                  <div className="mt-2 bg-gray-200 h-48 flex items-center justify-center rounded">
                    <MapPin className="text-gray-400 w-8 h-8" />
                    <span className="ml-2 text-gray-600">Map placeholder</span>
                  </div>
                </div>
              </div>
            )}
            <Button onClick={getRecommendation} disabled={!soilData}>Get Recommendation</Button>
          </div>
          {recommendation.length > 0 && (
            <div className="mt-4">
              <h3 className="font-semibold">Recommended Crops:</h3>
              <ul>
                {recommendation.map((crop, index) => (
                  <li key={index}>{crop}</li>
                ))}
              </ul>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
};

export default CropRecommendationUI;
