import React, { useState, useEffect } from 'react';

// Main App component for the Hero Management GUI
const App = () => {
    // State to store the list of heroes
    const [heroes, setHeroes] = useState([]);
    // State for the new hero form inputs
    const [newHeroName, setNewHeroName] = useState('');
    const [newHeroClass, setNewHeroClass] = useState('Warrior'); // Default class
    const [newHeroStrength, setNewHeroStrength] = useState(10);
    const [newHeroDexterity, setNewHeroDexterity] = useState(10);
    const [newHeroIntelligence, setNewHeroIntelligence] = useState(10);
    // State for displaying messages to the user
    const [message, setMessage] = useState('');

    // Predefined classes for hero creation
    const heroClasses = ['Warrior', 'Mage', 'Rogue', 'Cleric'];

    /**
     * Handles the creation of a new hero.
     * Generates a unique ID and adds the hero to the list.
     */
    const handleCreateHero = () => {
        if (!newHeroName.trim()) {
            setMessage('Hero name cannot be empty!');
            return;
        }

        const newHero = {
            id: crypto.randomUUID(), // Generate a unique ID for the hero
            name: newHeroName.trim(),
            level: 1,
            class: newHeroClass,
            stats: {
                strength: parseInt(newHeroStrength),
                dexterity: parseInt(newHeroDexterity),
                intelligence: parseInt(newHeroIntelligence),
                health: 100, // Default starting health
                mana: 50,    // Default starting mana
            },
            skills: [], // New heroes start with no specific skills, can be added later
        };

        setHeroes((prevHeroes) => [...prevHeroes, newHero]);
        setMessage(`Hero "${newHero.name}" created successfully!`);

        // Reset form fields
        setNewHeroName('');
        setNewHeroClass('Warrior');
        setNewHeroStrength(10);
        setNewHeroDexterity(10);
        setNewHeroIntelligence(10);
    };

    /**
     * Handles the file selection and loads heroes from a JSON file.
     * @param {Object} event - The file input change event.
     */
    const handleLoadHeroes = (event) => {
        const file = event.target.files[0];
        if (!file) {
            setMessage('No file selected.');
            return;
        }

        const reader = new FileReader();
        reader.onload = (e) => {
            try {
                const loadedData = JSON.parse(e.target.result);
                // Basic validation for the loaded data
                if (Array.isArray(loadedData) && loadedData.every(item => 'name' in item && 'level' in item && 'class' in item)) {
                    // Ensure unique IDs for loaded heroes
                    const heroesWithIds = loadedData.map(hero => ({
                        ...hero,
                        id: hero.id || crypto.randomUUID() // Assign ID if not present
                    }));
                    setHeroes(heroesWithIds);
                    setMessage(`Successfully loaded ${heroesWithIds.length} heroes from file!`);
                } else {
                    setMessage('Invalid JSON file format. Please ensure it\'s an array of hero objects.');
                }
            } catch (error) {
                setMessage(`Error parsing JSON file: ${error.message}`);
            }
        };
        reader.onerror = () => {
            setMessage('Error reading file.');
        };
        reader.readAsText(file);
    };

    /**
     * Handles downloading the current list of heroes as a JSON file.
     */
    const handleSaveHeroes = () => {
        if (heroes.length === 0) {
            setMessage('No heroes to save!');
            return;
        }
        const json = JSON.stringify(heroes, null, 2);
        const blob = new Blob([json], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'heroes.json';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
        setMessage('Heroes saved to heroes.json!');
    };

    return (
        <div className="min-h-screen bg-gray-900 text-gray-100 p-4 font-inter">
            <style>
                {`
                @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
                .font-inter {
                    font-family: 'Inter', sans-serif;
                }
                `}
            </style>
            <h1 className="text-4xl font-bold text-center mb-8 text-indigo-400">Hero Management System</h1>

            {/* Message display area */}
            {message && (
                <div className="bg-blue-800 text-blue-100 p-3 rounded-lg mb-6 shadow-md text-center">
                    {message}
                </div>
            )}

            {/* Hero Creation Section */}
            <div className="bg-gray-800 p-6 rounded-xl shadow-lg mb-8 max-w-2xl mx-auto">
                <h2 className="text-2xl font-semibold mb-4 text-indigo-300">Create New Hero</h2>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div className="flex flex-col">
                        <label htmlFor="heroName" className="mb-1 text-sm text-gray-300">Hero Name:</label>
                        <input
                            type="text"
                            id="heroName"
                            className="p-2 rounded-md bg-gray-700 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                            value={newHeroName}
                            onChange={(e) => setNewHeroName(e.target.value)}
                            placeholder="Enter hero name"
                        />
                    </div>
                    <div className="flex flex-col">
                        <label htmlFor="heroClass" className="mb-1 text-sm text-gray-300">Class:</label>
                        <select
                            id="heroClass"
                            className="p-2 rounded-md bg-gray-700 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                            value={newHeroClass}
                            onChange={(e) => setNewHeroClass(e.target.value)}
                        >
                            {heroClasses.map((hClass) => (
                                <option key={hClass} value={hClass}>{hClass}</option>
                            ))}
                        </select>
                    </div>
                    <div className="flex flex-col">
                        <label htmlFor="strength" className="mb-1 text-sm text-gray-300">Strength (1-20):</label>
                        <input
                            type="number"
                            id="strength"
                            className="p-2 rounded-md bg-gray-700 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                            value={newHeroStrength}
                            onChange={(e) => setNewHeroStrength(Math.max(1, Math.min(20, parseInt(e.target.value) || 0)))}
                            min="1"
                            max="20"
                        />
                    </div>
                    <div className="flex flex-col">
                        <label htmlFor="dexterity" className="mb-1 text-sm text-gray-300">Dexterity (1-20):</label>
                        <input
                            type="number"
                            id="dexterity"
                            className="p-2 rounded-md bg-gray-700 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                            value={newHeroDexterity}
                            onChange={(e) => setNewHeroDexterity(Math.max(1, Math.min(20, parseInt(e.target.value) || 0)))}
                            min="1"
                            max="20"
                        />
                    </div>
                    <div className="flex flex-col">
                        <label htmlFor="intelligence" className="mb-1 text-sm text-gray-300">Intelligence (1-20):</label>
                        <input
                            type="number"
                            id="intelligence"
                            className="p-2 rounded-md bg-gray-700 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                            value={newHeroIntelligence}
                            onChange={(e) => setNewHeroIntelligence(Math.max(1, Math.min(20, parseInt(e.target.value) || 0)))}
                            min="1"
                            max="20"
                        />
                    </div>
                </div>
                <button
                    onClick={handleCreateHero}
                    className="mt-6 w-full bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded-md shadow-lg transition duration-300 ease-in-out transform hover:scale-105"
                >
                    Create Hero
                </button>
            </div>

            {/* File Operations Section */}
            <div className="bg-gray-800 p-6 rounded-xl shadow-lg mb-8 max-w-2xl mx-auto">
                <h2 className="text-2xl font-semibold mb-4 text-indigo-300">Load/Save Heroes</h2>
                <div className="flex flex-col md:flex-row gap-4 justify-between items-center">
                    <label htmlFor="jsonUpload" className="block text-sm text-gray-300 md:mb-0">Load from JSON:</label>
                    <input
                        type="file"
                        id="jsonUpload"
                        accept=".json"
                        onChange={handleLoadHeroes}
                        className="block w-full md:w-auto text-sm text-gray-400
                                file:mr-4 file:py-2 file:px-4
                                file:rounded-md file:border-0
                                file:text-sm file:font-semibold
                                file:bg-indigo-500 file:text-white
                                hover:file:bg-indigo-600 cursor-pointer"
                    />
                    <button
                        onClick={handleSaveHeroes}
                        className="w-full md:w-auto bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded-md shadow-lg transition duration-300 ease-in-out transform hover:scale-105"
                    >
                        Save Heroes to JSON
                    </button>
                </div>
            </div>

            {/* Display Heroes Section */}
            <div className="bg-gray-800 p-6 rounded-xl shadow-lg max-w-4xl mx-auto">
                <h2 className="text-2xl font-semibold mb-4 text-indigo-300">Your Heroes ({heroes.length})</h2>
                {heroes.length === 0 ? (
                    <p className="text-gray-400 text-center">No heroes created yet. Start by creating one above or loading from a file!</p>
                ) : (
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {heroes.map((hero) => (
                            <div key={hero.id} className="bg-gray-700 p-4 rounded-lg shadow-md border border-gray-600">
                                <h3 className="text-xl font-bold text-teal-400 mb-2">{hero.name}</h3>
                                <p className="text-gray-300"><span className="font-semibold">Level:</span> {hero.level}</p>
                                <p className="text-gray-300"><span className="font-semibold">Class:</span> {hero.class}</p>
                                <div className="mt-2">
                                    <p className="font-semibold text-gray-300">Stats:</p>
                                    <ul className="list-disc list-inside text-gray-400">
                                        <li>Strength: {hero.stats.strength}</li>
                                        <li>Dexterity: {hero.stats.dexterity}</li>
                                        <li>Intelligence: {hero.stats.intelligence}</li>
                                        <li>Health: {hero.stats.health}</li>
                                        <li>Mana: {hero.stats.mana}</li>
                                    </ul>
                                </div>
                                {hero.skills && hero.skills.length > 0 && (
                                    <div className="mt-2">
                                        <p className="font-semibold text-gray-300">Skills:</p>
                                        <ul className="list-disc list-inside text-gray-400">
                                            {hero.skills.map((skill, index) => (
                                                <li key={index}>{skill.name} (Lvl {skill.level})</li>
                                            ))}
                                        </ul>
                                    </div>
                                )}
                            </div>
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
};

export default App;
