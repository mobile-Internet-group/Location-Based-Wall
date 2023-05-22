// frontend/src/api/api.js
import axiosInstance from './index'

const axios = axiosInstance

export const getWalls = () => {return axios.get(`http://localhost:8000/api/walls/`)}

export const postWall = (wallName, wallAuthor) => {return axios.post(`http://localhost:8000/api/walls/`, {'name': wallName, 'author': wallAuthor})}