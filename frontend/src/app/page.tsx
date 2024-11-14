"use client";

import { GridPattern } from "@/components/ui/animated-grid-pattern";
import Camera from "@/components/classifier-comps/camera-utils";
import React, { useState } from "react";

interface BookData {
    book_title:string;
    book_author:string;
    book_genre:string;
    book_description:string;
}

export default function Home() {
  const [imageData, setImageData] = useState<BookData | null>(null);

  return (
    <div className="relative bg-purple-500 min-h-screen flex items-center justify-center">
      <GridPattern className="absolute inset-0 z-0 w-full h-full" />
      <div className="relative z-10 p-5 text-center bg-black flex flex-col items-center">
        <h1 className="text-4xl font-bold text-white mb-4">Welcome to Bookly-Ai</h1>
        <p className="text-white mb-4">
          Not sure about buying that new book? Let us help you!
        </p>
        <Camera setImageData={setImageData} />
        {imageData ? (
          <div className="mt-8 p-4 bg-black text-white rounded-lg shadow-md w-full max-w-md">
            <h2 className="font-bold text-lg mb-2">Check this out:</h2>
            <p><strong>Title:</strong> {imageData.book_title}</p>
            <p><strong>Author:</strong> {imageData.book_author}</p>
            <p><strong>Genre:</strong> {imageData.book_genre}</p>
            <p><strong>Description:</strong> {imageData.book_description}</p>
          </div>
        ) : (
          <p className="mt-8 text-white">No data available. Please capture an image to classify.</p>
        )}
      </div>
    </div>
  );
}