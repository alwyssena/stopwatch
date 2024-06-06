// App.js
import { useEffect, useState } from 'react';
import './App.css';

function StartButton({ isRunning, startTimer }) {
  return (
    <button onClick={startTimer} disabled={isRunning}>Start</button>
  );
}

function StopButton({ isRunning, stopTimer }) {
  return (
    <button onClick={stopTimer} disabled={!isRunning}>Stop</button>
  );
}

function ResetButton({ timer, resetTimer }) {
  return (
    <button onClick={resetTimer} disabled={timer.millisec === 0 && timer.sec === 0 && timer.min === 0 && timer.hr === 0}>Reset</button>
  );
}

function SplitButton({ timer,recordSplit }) {
  return (
    <button onClick={recordSplit} disabled={timer.millisec === 0 && timer.sec === 0 && timer.min === 0 && timer.hr === 0}>Split</button>
  );
}

function App() {
  const [timer, setTimer] = useState({ hr: 0, min: 0, sec: 0, millisec: 0 });
  const [isRunning, setIsRunning] = useState(false);
  const [showAlert, setShowAlert] = useState(false);
  const [splits, setSplits] = useState([]);

  useEffect(() => {
    let intervalId;
    if (isRunning) {
      intervalId = setInterval(() => {
        setTimer(prevTimer => {
          let { hr, min, sec, millisec } = prevTimer;

          millisec += 1;
          if (millisec === 100) {
            millisec = 0;
            sec += 1;
          }
          if (sec === 60) {
            sec = 0;
            min += 1;
          }
          if (min === 60) {
            min = 0;
            hr += 1;
          }

          return { hr, min, sec, millisec };
        });
      }, 10);
    }

    return () => clearInterval(intervalId);
  }, [isRunning]);

  const startTimer = () => setIsRunning(true);
  const stopTimer = () => setIsRunning(false);

  const resetTimer = () => {
    setShowAlert(true);
  };

  const handleConfirmReset = () => {
    setIsRunning(false);
    setTimer({ hr: 0, min: 0, sec: 0, millisec: 0 });
    setSplits([]);
    setShowAlert(false);
  };

  const handleCancelReset = () => {
    setShowAlert(false);
  };

  const recordSplit = () => {
    setSplits([...splits, `${timer.hr < 10 ? `0${timer.hr}` : timer.hr}:${timer.min < 10 ? `0${timer.min}` : timer.min}:${timer.sec < 10 ? `0${timer.sec}` : timer.sec}:${timer.millisec < 10 ? `0${timer.millisec}` : timer.millisec}`]);
  };

  return (
    <div className="bg">
      <div className="clock">
        {timer.hr < 10 ? `0${timer.hr}` : timer.hr}:
        {timer.min < 10 ? `0${timer.min}` : timer.min}:
        {timer.sec < 10 ? `0${timer.sec}` : timer.sec}:
        {timer.millisec < 10 ? `0${timer.millisec}` : timer.millisec}
      </div>
      <div className="buttons">
        <StartButton isRunning={isRunning} startTimer={startTimer} />
        <StopButton isRunning={isRunning} stopTimer={stopTimer} />
        <ResetButton timer={timer} resetTimer={resetTimer} />
        <SplitButton timer={timer} recordSplit={recordSplit} />
      </div>
      {showAlert && (
        <div className="custom-alert">
          <p>Are you sure you want to reset the timer?</p>
          <button onClick={handleConfirmReset}>Yes</button>
          <button onClick={handleCancelReset}>Cancel</button>
        </div>
      )}
      {splits.length > 0 && (
        <div className="splits">
          <h3>Splits</h3>
          <ul>
            {splits.map((split, index) => (
              <li key={index}>{split}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
