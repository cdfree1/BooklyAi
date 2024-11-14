"use client";

import React, {useRef, useState} from "react";
import Webcam from "react-webcam";

const videoConstraints = {
    width: 1080,
    height: 720,
    facingMode: "user"
};

interface BookData{
    book_title:string;
    book_author:string;
    book_genre:string;
    book_description:string;
  }

const Camera = ({setImageData}: {setImageData: (data: BookData) => void}) => {
    const webcamRef = useRef<Webcam>(null);

    const capture = React.useCallback(() => {
        if (webcamRef.current) {
            const imageSrc: String | null = webcamRef.current.getScreenshot();
            console.log(imageSrc);
            return imageSrc
        }
    },
        [webcamRef]
    );

    const getData = () => {
        const imageSrc: String | null | undefined = capture();
        if (imageSrc) {
            console.log(imageSrc);
            fetch('https://booklyai.onrender.com/classification/classify-book', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ image_path: imageSrc }),
            })
                .then(response => {
                    console.log(response.status)
                    return response.json();
                })
                .then(data => {
                    console.log(data);
                    setImageData(data);
                })
        }
    }

    return (
        <div className="flex flex-col items-center">
            <Webcam
                audio={false}
                height={720}
                ref={webcamRef}
                screenshotFormat="image/jpeg"
                width={1280}
                videoConstraints={videoConstraints}
                className="mb-4"
            />
            <button
                onClick={getData}
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
            >
                Capture
            </button>

        </div>
    );

}

export default Camera;

