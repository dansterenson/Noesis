import React, {useState, useEffect} from 'react';
import './App.css';
import {Link} from 'react-router-dom'
import{ Component } from 'react';
import Chart from "./chart"
import {getSnapshotResult} from "./connect_api";

class Feelings extends Component{

    constructor() {
        super();
        this.state= {
            chartData: []
        }
    }

    componentWillMount = async () => {
        await this.fetchItems();
    }

    fetchItems = async () => {
        const {match} = this.props;
        const items = await getSnapshotResult(match.params.id, match.params.snapshot, "feelings")
        const labels = Object.keys(items[0])
        const chartData = {
                labels: ["Exhaustion", "Happiness", "Hunger", "Thirst"],
                datasets: [
                    {
                        label: '',
                        data: Object.values(items[0]),
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.6)',
                            'rgba(54, 162, 235, 0.6)',
                            'rgba(255, 206, 86, 0.6)',
                            'rgba(75, 192, 192, 0.6)',
                            'rgba(153, 102, 255, 0.6)',
                            'rgba(255, 159, 64, 0.6)',
                            'rgba(255, 99, 132, 0.6)'
                        ]
                    }
                ]
            }
        this.setState({chartData})
    };


    render() {
        return (
            <div>
                <h1 className={"titles"}>Feelings</h1>
                <Chart chartData={this.state.chartData}/>
            </div>
        );
    }
}


export default Feelings;