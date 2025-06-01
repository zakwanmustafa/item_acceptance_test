{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red202\green202\blue202;}
{\*\expandedcolortbl;;\cssrgb\c83137\c83137\c83137;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import React, \{ useState, useEffect, useCallback \} from 'react';\
import \{ initializeApp \} from 'firebase/app';\
import \{ getAuth, signInAnonymously, signInWithCustomToken, onAuthStateChanged \} from 'firebase/auth';\
import \{ getFirestore, collection, addDoc, onSnapshot, query, serverTimestamp, doc, updateDoc, deleteDoc \} from 'firebase/firestore';\
import \{ CalendarDays, Clock, Package, FlaskConical, CheckCircle, XCircle, FileText, BarChart, PlusCircle, Trash2, Edit, Search, Download, Bell, User \} from 'lucide-react'; // Added User icon\
// import jsPDF from 'jspdf'; // For PDF export - REMOVED, loaded via CDN\
// import 'jspdf-autotable'; // For table generation in PDF - REMOVED, loaded via CDN\
import \{ BarChart as RechartsBarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer, CartesianGrid \} from 'recharts'; // For data visualization\
\
// Main App component\
const App = () => \{\
    // State variables for Firebase and user authentication\
    const [db, setDb] = useState(null);\
    const [auth, setAuth] = useState(null);\
    const [userId, setUserId] = useState('');\
    const [isAuthReady, setIsAuthReady] = useState(false); // Indicates if onAuthStateChanged has completed its initial check\
\
    // State for form inputs\
    const [itemName, setItemName] = useState('');\
    const [itemType, setItemType] = useState('');\
    const [manufacturer, setManufacturer] = useState('');\
    const [lotNumber, setLotNumber] = useState('');\
    const [expiryDate, setExpiryDate] = useState('');\
    const [receptionDate, setReceptionDate] = useState('');\
    const [receptionTime, setReceptionTime] = useState('');\
    const [conditionCheck, setConditionCheck] = useState('');\
    const [performanceCriteria, setPerformanceCriteria] = useState('');\
    const [performanceResult, setPerformanceResult] = useState('');\
    const [notes, setNotes] = useState('');\
    const [receivedBy, setReceivedBy] = useState(''); // This is the userId\
\
    // New fields for user name, performed by, and approved by\
    const [userName, setUserName] = useState('');\
    const [performedBy, setPerformedBy] = useState('');\
    const [approvedBy, setApprovedBy] = useState('');\
\
\
    // State for items displayed in the table\
    const [items, setItems] = useState([]);\
    const [editingItem, setEditingItem] = useState(null); // State to hold the item being edited\
\
    // State for filtering and searching\
    const [filterItemType, setFilterItemType] = useState('');\
    const [filterManufacturer, setFilterManufacturer] = useState('');\
    const [filterPerformanceResult, setFilterPerformanceResult] = useState('');\
    const [searchTerm, setSearchTerm] = useState('');\
    const [filteredItems, setFilteredItems] = useState([]); // State for filtered items\
\
    // State for report generation\
    const [reportPeriod, setReportPeriod] = useState('daily');\
    const [reportSummary, setReportSummary] = useState(null);\
    const [showReportModal, setShowReportModal] = useState(false);\
    const [message, setMessage] = useState(''); // For user feedback messages\
    const [showConfirmModal, setShowConfirmModal] = useState(false);\
    const [itemToDelete, setItemToDelete] = useState(null);\
\
    // State for notifications\
    const [expiringSoonItems, setExpiringSoonItems] = useState([]);\
    const [failedPerformanceItems, setFailedPerformanceItems] = useState([]);\
    const [expiryNotificationThresholdDays, setExpiryNotificationThresholdDays] = useState(30); // Default 30 days\
\
    // Initialize Firebase and set up authentication listener\
    useEffect(() => \{\
        try \{\
            const firebaseConfig = JSON.parse(typeof __firebase_config !== 'undefined' ? __firebase_config : '\{\}');\
            const app = initializeApp(firebaseConfig);\
            const firestoreDb = getFirestore(app);\
            const firebaseAuth = getAuth(app);\
\
            setDb(firestoreDb);\
            setAuth(firebaseAuth);\
\
            // Listen for auth state changes\
            const unsubscribeAuth = onAuthStateChanged(firebaseAuth, async (user) => \{\
                if (user) \{\
                    console.log("Auth state changed: User is authenticated.", user.uid);\
                    setUserId(user.uid);\
                    setReceivedBy(user.uid); // Set receivedBy to current user ID\
                    setPerformedBy(user.uid); // Default performedBy to current user ID\
                    setIsAuthReady(true);\
\
                    // Now that user is confirmed, set up Firestore listener\
                    const itemsCollectionRef = collection(firestoreDb, `artifacts/$\{typeof __app_id !== 'undefined' ? __app_id : 'default-app-id'\}/public/data/receptionItems`);\
                    const unsubscribeFirestore = onSnapshot(itemsCollectionRef, (snapshot) => \{\
                        console.log("Firestore snapshot received. Number of docs:", snapshot.docs.length);\
                        const fetchedItems = snapshot.docs.map(doc => (\{\
                            id: doc.id,\
                            ...doc.data()\
                        \}));\
                        // Sort items by receptionDate and receptionTime in descending order in memory\
                        fetchedItems.sort((a, b) => \{\
                            const dateA = new Date(`$\{a.receptionDate\}T$\{a.receptionTime || '00:00'\}`);\
                            const dateB = new Date(`$\{b.receptionDate\}T$\{b.receptionTime || '00:00'\}`);\
                            return dateB.getTime() - dateA.getTime();\
                        \});\
                        setItems(fetchedItems);\
                    \}, (error) => \{\
                        console.error("Error fetching items:", error);\
                        setMessage("Error fetching items. Please check console for details.");\
                    \});\
\
                    // Return cleanup for Firestore listener\
                    return () => unsubscribeFirestore();\
\
                \} else \{\
                    console.log("Auth state changed: User is NOT authenticated. Attempting anonymous sign-in if not already.");\
                    // Attempt anonymous sign-in if no user is present\
                    try \{\
                        await signInAnonymously(firebaseAuth);\
                        console.log("Signed in anonymously.");\
                    \} catch (error) \{\
                        console.error("Error signing in anonymously:", error);\
                        setMessage("Error signing in anonymously. Please check console for details.");\
                    \}\
                    setUserId(crypto.randomUUID()); // Fallback for unauthenticated or anonymous\
                    setIsAuthReady(true); // Mark as ready, even if anonymous, to allow Firestore attempts\
                    setItems([]); // Clear items if user logs out or fails to authenticate\
                \}\
            \});\
\
            // Sign in with custom token if available, when auth is ready\
            const initialAuthToken = typeof __initial_auth_token !== 'undefined' ? __initial_auth_token : null;\
            if (initialAuthToken) \{\
                signInWithCustomToken(firebaseAuth, initialAuthToken)\
                    .then(() => console.log('Signed in with custom token'))\
                    .catch(error => console.error('Error signing in with custom token:', error));\
            \}\
\
\
            // Return cleanup for auth listener\
            return () => unsubscribeAuth();\
        \} catch (error) \{\
            console.error("Failed to initialize Firebase:", error);\
            setMessage("Error initializing Firebase. Please check console for details.");\
        \}\
    \}, []); // Dependencies are just db and auth, as onAuthStateChanged handles user state\
\
    // Apply filtering and searching whenever items or filter criteria change\
    useEffect(() => \{\
        let currentFilteredItems = items;\
\
        // Filter by Item Type\
        if (filterItemType) \{\
            currentFilteredItems = currentFilteredItems.filter(item => item.itemType === filterItemType);\
        \}\
\
        // Filter by Manufacturer\
        if (filterManufacturer) \{\
            currentFilteredItems = currentFilteredItems.filter(item =>\
                item.manufacturer && item.manufacturer.toLowerCase().includes(filterManufacturer.toLowerCase())\
            );\
        \}\
\
        // Filter by Performance Result\
        if (filterPerformanceResult) \{\
            currentFilteredItems = currentFilteredItems.filter(item => item.performanceResult === filterPerformanceResult);\
        \}\
\
        // Search by Item Name or Lot Number\
        if (searchTerm) \{\
            currentFilteredItems = currentFilteredItems.filter(item =>\
                item.itemName.toLowerCase().includes(searchTerm.toLowerCase()) ||\
                (item.lotNumber && item.lotNumber.toLowerCase().includes(searchTerm.toLowerCase()))\
            );\
        \}\
\
        setFilteredItems(currentFilteredItems);\
    \}, [items, filterItemType, filterManufacturer, filterPerformanceResult, searchTerm]);\
\
    // Calculate notifications (expiring soon and failed performance)\
    useEffect(() => \{\
        const now = new Date();\
        const futureDateForExpiry = new Date();\
        futureDateForExpiry.setDate(now.getDate() + expiryNotificationThresholdDays);\
\
        const expiring = items.filter(item => \{\
            if (item.expiryDate) \{\
                const expiry = new Date(item.expiryDate);\
                // Check if expiry date is in the future but within the threshold\
                return expiry > now && expiry <= futureDateForExpiry;\
            \}\
            return false;\
        \});\
        setExpiringSoonItems(expiring);\
\
        const failed = items.filter(item => item.performanceResult === 'Fail');\
        setFailedPerformanceItems(failed);\
    \}, [items, expiryNotificationThresholdDays]); // Depend on threshold for recalculation\
\
    // Function to clear the form fields\
    const clearForm = () => \{\
        setItemName('');\
        setItemType('');\
        setManufacturer('');\
        setLotNumber('');\
        setExpiryDate('');\
        setReceptionDate('');\
        setReceptionTime('');\
        setConditionCheck('');\
        setPerformanceCriteria('');\
        setPerformanceResult('');\
        setNotes('');\
        setEditingItem(null); // Clear editing state\
        setMessage(''); // Clear any previous messages\
        setUserName('');\
        setPerformedBy('');\
        setApprovedBy('');\
    \};\
\
    // Function to handle adding or updating an item\
    const handleAddItem = async (e) => \{\
        e.preventDefault();\
        if (!db || !userId) \{\
            setMessage("Database not ready or user not authenticated. Please wait for authentication.");\
            return;\
        \}\
\
        if (!itemName || !itemType || !receptionDate || !conditionCheck || !performanceResult) \{\
            setMessage("Please fill in all required fields: Item Name, Item Type, Reception Date, Condition Check, Performance Result.");\
            return;\
        \}\
\
        const itemData = \{\
            itemName,\
            itemType,\
            manufacturer,\
            lotNumber,\
            expiryDate,\
            receptionDate,\
            receptionTime,\
            conditionCheck,\
            performanceCriteria,\
            performanceResult,\
            notes,\
            receivedBy: receivedBy || userId, // Ensure receivedBy is set\
            userName: userName, // New field\
            performedBy: performedBy, // New field\
            approvedBy: approvedBy, // New field\
        \};\
\
        try \{\
            if (editingItem) \{\
                // Update existing item\
                const itemDocRef = doc(db, `artifacts/$\{typeof __app_id !== 'undefined' ? __app_id : 'default-app-id'\}/public/data/receptionItems`, editingItem.id);\
                console.log("Updating item:", editingItem.id, itemData);\
                await updateDoc(itemDocRef, \{\
                    ...itemData,\
                    lastModifiedAt: serverTimestamp(), // Audit trail: last modified timestamp\
                    lastModifiedBy: userId,             // Audit trail: last modified by user\
                \});\
                setMessage('Item updated successfully!');\
            \} else \{\
                // Add new item\
                const itemsCollectionRef = collection(db, `artifacts/$\{typeof __app_id !== 'undefined' ? __app_id : 'default-app-id'\}/public/data/receptionItems`);\
                console.log("Adding new item:", itemData);\
                await addDoc(itemsCollectionRef, \{\
                    ...itemData,\
                    createdAt: serverTimestamp(), // Audit trail: creation timestamp\
                    createdBy: userId,            // Audit trail: created by user\
                \});\
                setMessage('Item added successfully!');\
            \}\
            clearForm();\
        \} catch (error) \{\
            console.error("Error adding/updating document:", error);\
            setMessage(`Error: $\{error.message\}`);\
        \}\
    \};\
\
    // Function to set form fields for editing\
    const handleEdit = (item) => \{\
        setEditingItem(item);\
        setItemName(item.itemName || '');\
        setItemType(item.itemType || '');\
        setManufacturer(item.manufacturer || '');\
        setLotNumber(item.lotNumber || '');\
        setExpiryDate(item.expiryDate || '');\
        setReceptionDate(item.receptionDate || '');\
        setReceptionTime(item.receptionTime || '');\
        setConditionCheck(item.conditionCheck || '');\
        setPerformanceCriteria(item.performanceCriteria || '');\
        setPerformanceResult(item.performanceResult || '');\
        setNotes(item.notes || '');\
        setReceivedBy(item.receivedBy || userId);\
        setUserName(item.userName || ''); // Set new field\
        setPerformedBy(item.performedBy || ''); // Set new field\
        setApprovedBy(item.approvedBy || ''); // Set new field\
        setMessage(''); // Clear any previous messages\
        // Scroll to top to make sure form is visible\
        window.scrollTo(\{ top: 0, behavior: 'smooth' \});\
    \};\
\
    // Function to confirm deletion\
    const confirmDelete = (item) => \{\
        setItemToDelete(item);\
        setShowConfirmModal(true);\
    \};\
\
    // Function to handle deleting an item\
    const handleDelete = async () => \{\
        if (!db || !itemToDelete) \{\
            setMessage("Database not ready or no item selected for deletion.");\
            return;\
        \}\
        try \{\
            const itemDocRef = doc(db, `artifacts/$\{typeof __app_id !== 'undefined' ? __app_id : 'default-app-id'\}/public/data/receptionItems`, itemToDelete.id);\
            console.log("Deleting item:", itemToDelete.id);\
            await deleteDoc(itemDocRef);\
            setMessage('Item deleted successfully!');\
            setShowConfirmModal(false);\
            setItemToDelete(null);\
        \} catch (error) \{\
            console.error("Error deleting document:", error);\
            setMessage(`Error: $\{error.message\}`);\
        \}\
    \};\
\
    // Function to generate report summary\
    const generateReport = useCallback(() => \{\
        const now = new Date();\
        let reportItems = [];\
\
        if (reportPeriod === 'daily') \{\
            const today = now.toISOString().split('T')[0];\
            reportItems = items.filter(item => item.receptionDate === today);\
        \} else if (reportPeriod === 'weekly') \{\
            const oneWeekAgo = new Date(now.getFullYear(), now.getMonth(), now.getDate() - 7);\
            reportItems = items.filter(item => \{\
                const itemDate = new Date(item.receptionDate);\
                return itemDate >= oneWeekAgo;\
            \});\
        \} else if (reportPeriod === 'monthly') \{\
            const oneMonthAgo = new Date(now.getFullYear(), now.getMonth() - 1, now.getDate());\
            reportItems = items.filter(item => \{\
                const itemDate = new Date(item.receptionDate);\
                return itemDate >= oneMonthAgo;\
            \});\
        \} else if (reportPeriod === 'yearly') \{\
            const oneYearAgo = new Date(now.getFullYear() - 1, now.getMonth(), now.getDate());\
            reportItems = items.filter(item => \{\
                const itemDate = new Date(item.receptionDate);\
                return itemDate >= oneYearAgo;\
            \});\
        \}\
\
        const totalItems = reportItems.length;\
        const passedItems = reportItems.filter(item => item.performanceResult === 'Pass').length;\
        const failedItems = reportItems.filter(item => item.performanceResult === 'Fail').length;\
        const pendingItems = reportItems.filter(item => item.performanceResult === 'Pending').length;\
\
\
        setReportSummary(\{\
            totalItems,\
            passedItems,\
            failedItems,\
            pendingItems, // Include pending items in summary\
            period: reportPeriod,\
            data: reportItems, // Include data for export\
        \});\
        setShowReportModal(true);\
    \}, [items, reportPeriod]);\
\
    // Function to export report data to CSV\
    const exportReportToCSV = () => \{\
        if (!reportSummary || reportSummary.data.length === 0) \{\
            setMessage("No data to export for the selected report period.");\
            return;\
        \}\
\
        const headers = [\
            "Item Name", "Item Type", "Manufacturer", "Lot Number", "Expiry Date",\
            "Reception Date", "Reception Time", "Physical Condition", "Performance Criteria",\
            "Performance Result", "Notes", "Received By (ID)", "User Name", "Performed By", "Approved By",\
            "Created At", "Created By (ID)", "Last Modified At", "Last Modified By (ID)"\
        ];\
\
        const csvRows = [];\
        csvRows.push(headers.join(',')); // Add headers\
\
        reportSummary.data.forEach(item => \{\
            const row = [\
                `"$\{item.itemName || ''\}"`,\
                `"$\{item.itemType || ''\}"`,\
                `"$\{item.manufacturer || ''\}"`,\
                `"$\{item.lotNumber || ''\}"`,\
                `"$\{item.expiryDate || ''\}"`,\
                `"$\{item.receptionDate || ''\}"`,\
                `"$\{item.receptionTime || ''\}"`,\
                `"$\{item.conditionCheck || ''\}"`,\
                `"$\{(item.performanceCriteria || '').replace(/"/g, '""')\}"`, // Escape quotes for CSV\
                `"$\{item.performanceResult || ''\}"`,\
                `"$\{(item.notes || '').replace(/"/g, '""')\}"`, // Escape quotes for CSV\
                `"$\{item.receivedBy || ''\}"`,\
                `"$\{item.userName || ''\}"`, // New field\
                `"$\{item.performedBy || ''\}"`, // New field\
                `"$\{item.approvedBy || ''\}"`, // New field\
                `"$\{item.createdAt ? new Date(item.createdAt.toDate()).toLocaleString() : ''\}"`,\
                `"$\{item.createdBy || ''\}"`,\
                `"$\{item.lastModifiedAt ? new Date(item.lastModifiedAt.toDate()).toLocaleString() : ''\}"`,\
                `"$\{item.lastModifiedBy || ''\}"`\
            ];\
            csvRows.push(row.join(','));\
        \});\
\
        const csvString = csvRows.join('\\n');\
        const blob = new Blob([csvString], \{ type: 'text/csv;charset=utf-8;' \});\
        const link = document.createElement('a');\
        link.href = URL.createObjectURL(blob);\
        link.setAttribute('download', `reception_report_$\{reportSummary.period\}_$\{new Date().toISOString().split('T')[0]\}.csv`);\
        document.body.appendChild(link);\
        link.click();\
        document.body.removeChild(link);\
        setMessage("Report exported successfully!");\
    \};\
\
    // Function to export report data to PDF\
    const exportReportToPDF = () => \{\
        if (!reportSummary || reportSummary.data.length === 0) \{\
            setMessage("No data to export for the selected report period.");\
            return;\
        \}\
\
        // Ensure jsPDF and jspdf-autotable are available globally\
        if (typeof window.jspdf === 'undefined' || typeof window.jspdf.AcroForm === 'undefined') \{ // Check for jspdf and autotable plugin\
            setMessage("PDF library not loaded. Please try again.");\
            console.error("jsPDF or jspdf-autotable not loaded.");\
            return;\
        \}\
\
        const doc = new window.jspdf.jsPDF(); // Use window.jspdf.jsPDF\
        doc.setFontSize(18);\
        doc.text(`Reception Report ($\{reportSummary.period\})`, 14, 22);\
\
        doc.setFontSize(12);\
        doc.text(`Total Items Received: $\{reportSummary.totalItems\}`, 14, 32);\
        doc.setTextColor(34, 139, 34); // Forest Green\
        doc.text(`Items Passed: $\{reportSummary.passedItems\}`, 14, 39);\
        doc.setTextColor(220, 20, 60); // Crimson\
        doc.text(`Items Failed: $\{reportSummary.failedItems\}`, 14, 46);\
        doc.setTextColor(255, 165, 0); // Orange\
        doc.text(`Items Pending: $\{reportSummary.pendingItems\}`, 14, 53);\
        doc.setTextColor(0, 0, 0); // Black for subsequent text\
\
        const tableColumn = [\
            "Item Name", "Type", "Manufacturer", "Lot No.", "Expiry Date",\
            "Reception Date", "Time", "Condition", "Performance", "Received By (ID)",\
            "User Name", "Performed By", "Approved By", "Created At", "Created By (ID)",\
            "Last Modified At", "Last Modified By (ID)"\
        ];\
        const tableRows = [];\
\
        reportSummary.data.forEach(item => \{\
            const itemData = [\
                item.itemName || '',\
                item.itemType || '',\
                item.manufacturer || '',\
                item.lotNumber || '',\
                item.expiryDate || '',\
                item.receptionDate || '',\
                item.receptionTime || '',\
                item.conditionCheck || '',\
                item.performanceResult || '',\
                item.receivedBy || '',\
                item.userName || '', // New field\
                item.performedBy || '', // New field\
                item.approvedBy || '', // New field\
                item.createdAt ? new Date(item.createdAt.toDate()).toLocaleString() : '',\
                item.createdBy || '',\
                item.lastModifiedAt ? new Date(item.lastModifiedAt.toDate()).toLocaleString() : '',\
                item.lastModifiedBy || ''\
            ];\
            tableRows.push(itemData);\
        \});\
\
        doc.autoTable(\{ // autoTable is a plugin method, available on the doc object\
            startY: 65,\
            head: [tableColumn],\
            body: tableRows,\
            styles: \{ fontSize: 8, cellPadding: 2, overflow: 'linebreak' \},\
            headStyles: \{ fillColor: [248, 250, 252], textColor: [74, 85, 104], fontStyle: 'bold' \},\
            alternateRowStyles: \{ fillColor: [255, 255, 255] \},\
            didDrawPage: function (data) \{\
                // Footer\
                let str = "Page " + doc.internal.getNumberOfPages();\
                doc.setFontSize(10);\
                doc.text(str, data.settings.margin.left, doc.internal.pageSize.height - 10);\
            \}\
        \});\
\
        doc.save(`reception_report_$\{reportSummary.period\}_$\{new Date().toISOString().split('T')[0]\}.pdf`);\
        setMessage("Report exported to PDF successfully!");\
    \};\
\
\
    // Set default reception date and time to current date/time on component mount\
    useEffect(() => \{\
        const today = new Date();\
        const yyyy = today.getFullYear(); // Fixed: Correctly define yyyy\
        const mm = String(today.getMonth() + 1).padStart(2, '0'); // Months are 0-indexed\
        const dd = String(today.getDate()).padStart(2, '0');\
        const hh = String(today.getHours()).padStart(2, '0');\
        const min = String(today.getMinutes()).padStart(2, '0');\
\
        setReceptionDate(`$\{yyyy\}-$\{mm\}-$\{dd\}`);\
        setReceptionTime(`$\{hh\}:$\{min\}`);\
    \}, []);\
\
    // Prepare data for performance trend chart\
    const performanceChartData = useCallback(() => \{\
        const passCount = items.filter(item => item.performanceResult === 'Pass').length;\
        const failCount = items.filter(item => item.performanceResult === 'Fail').length;\
        const pendingCount = items.filter(item => item.performanceResult === 'Pending').length;\
\
        return [\
            \{ name: 'Pass', count: passCount, fill: '#22c55e' \}, // Tailwind green-500\
            \{ name: 'Fail', count: failCount, fill: '#ef4444' \}, // Tailwind red-500\
            \{ name: 'Pending', count: pendingCount, fill: '#f59e0b' \}, // Tailwind amber-500\
        ];\
    \}, [items]);\
\
\
    // Tailwind CSS classes for consistent styling\
    const inputClass = "p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 w-full";\
    const buttonClass = "px-4 py-2 rounded-md font-semibold transition duration-200 ease-in-out";\
    const primaryButtonClass = `$\{buttonClass\} bg-blue-600 text-white hover:bg-blue-700 shadow-md flex items-center justify-center space-x-2`;\
    const secondaryButtonClass = `$\{buttonClass\} bg-gray-300 text-gray-800 hover:bg-gray-400 shadow-md flex items-center justify-center space-x-2`;\
    const dangerButtonClass = `$\{buttonClass\} bg-red-600 text-white hover:bg-red-700 shadow-md flex items-center justify-center space-x-2`;\
    const iconClass = "w-5 h-5";\
\
    return (\
        <div className="min-h-screen bg-gray-100 p-4 font-sans text-gray-800 flex flex-col items-center">\
            <script src="https://cdn.tailwindcss.com"></script>\
            <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet" />\
            \{/* jsPDF and jspdf-autotable CDN links */\}\
            <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>\
            <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.5.23/jspdf.plugin.autotable.min.js"></script>\
            <style>\
                \{`\
                body \{\
                    font-family: 'Inter', sans-serif;\
                \}\
                .modal-overlay \{\
                    position: fixed;\
                    top: 0;\
                    left: 0;\
                    right: 0;\
                    bottom: 0;\
                    background-color: rgba(0, 0, 0, 0.6);\
                    display: flex;\
                    justify-content: center;\
                    align-items: center;\
                    z-index: 1000;\
                \}\
                .modal-content \{\
                    background: white;\
                    padding: 2rem;\
                    border-radius: 12px;\
                    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);\
                    max-width: 500px;\
                    width: 90%;\
                    transform: translateY(-20px);\
                    opacity: 0;\
                    animation: fadeInDown 0.3s forwards;\
                \}\
                @keyframes fadeInDown \{\
                    to \{\
                        transform: translateY(0);\
                        opacity: 1;\
                    \}\
                \}\
                .table-container \{\
                    overflow-x: auto;\
                    width: 100%;\
                \}\
                table \{\
                    min-width: 1500px; /* Adjusted min-width for new columns */\
                \}\
                th, td \{\
                    padding: 0.75rem;\
                    text-align: left;\
                    border-bottom: 1px solid #e2e8f0;\
                \}\
                th \{\
                    background-color: #f8fafc;\
                    font-weight: 600;\
                    color: #4a5568;\
                \}\
                tr:hover \{\
                    background-color: #f0f4f8;\
                \}\
                .notification-card \{\
                    background-color: #fff;\
                    padding: 1.5rem;\
                    border-radius: 12px;\
                    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);\
                    margin-bottom: 1rem;\
                    border-left: 5px solid;\
                \}\
                .notification-card.expiring \{\
                    border-color: #f59e0b; /* Amber */\
                \}\
                .notification-card.failed \{\
                    border-color: #ef4444; /* Red */\
                \}\
                .chart-container \{\
                    width: 100%;\
                    height: 300px; /* Fixed height for the chart */\
                \}\
                `\}\
            </style>\
\
            <header className="w-full max-w-6xl bg-white shadow-lg rounded-xl p-6 mb-8 text-center">\
                <h1 className="text-4xl font-extrabold text-blue-800 mb-2">Reception Item Acceptance Testing</h1>\
                <p className="text-lg text-gray-600">Complying with MS ISO 15189 Medical Testing Requirements</p>\
                <div className="mt-4 text-sm text-gray-500">\
                    Your User ID: <span className="font-mono text-blue-700 break-all">\{userId || 'Loading...'\}</span>\
                </div>\
            </header>\
\
            \{/* Message display */\}\
            \{message && (\
                <div className="w-full max-w-6xl p-3 mb-4 text-center text-sm font-medium text-white bg-blue-500 rounded-lg shadow-md">\
                    \{message\}\
                </div>\
            )\}\
\
            \{/* Notifications Section */\}\
            <section className="w-full max-w-6xl mb-8">\
                <h2 className="text-2xl font-bold text-gray-800 mb-4 flex items-center space-x-2">\
                    <Bell className=\{iconClass\} /> Notifications\
                </h2>\
                <div className="bg-white shadow-lg rounded-xl p-6 mb-4">\
                    <label htmlFor="expiryThreshold" className="block text-sm font-medium text-gray-700 mb-2">\
                        Notify for expiry within (days):\
                    </label>\
                    <input\
                        type="number"\
                        id="expiryThreshold"\
                        value=\{expiryNotificationThresholdDays\}\
                        onChange=\{(e) => setExpiryNotificationThresholdDays(Math.max(0, parseInt(e.target.value) || 0))\}\
                        className=\{inputClass\}\
                        min="0"\
                    />\
                </div>\
                \{expiringSoonItems.length === 0 && failedPerformanceItems.length === 0 ? (\
                    <div className="bg-white shadow-lg rounded-xl p-6 text-center text-gray-500">\
                        No new notifications. All clear!\
                    </div>\
                ) : (\
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">\
                        \{expiringSoonItems.length > 0 && (\
                            <div className="notification-card expiring">\
                                <h3 className="text-xl font-semibold text-amber-700 mb-2">Expiring Soon (\{expiringSoonItems.length\})</h3>\
                                <ul className="list-disc list-inside text-gray-700">\
                                    \{expiringSoonItems.map(item => (\
                                        <li key=\{item.id\} className="mb-1">\
                                            <span className="font-medium">\{item.itemName\}</span> (Lot: \{item.lotNumber || 'N/A'\}) - Expires: \{item.expiryDate\}\
                                        </li>\
                                    ))\}\
                                </ul>\
                            </div>\
                        )\}\
                        \{failedPerformanceItems.length > 0 && (\
                            <div className="notification-card failed">\
                                <h3 className="text-xl font-semibold text-red-700 mb-2">Failed Performance (\{failedPerformanceItems.length\})</h3>\
                                <ul className="list-disc list-inside text-gray-700">\
                                    \{failedPerformanceItems.map(item => (\
                                        <li key=\{item.id\} className="mb-1">\
                                            <span className="font-medium">\{item.itemName\}</span> (Lot: \{item.lotNumber || 'N/A'\}) - Reception Date: \{item.receptionDate\}\
                                        </li>\
                                    ))\}\
                                </ul>\
                            </div>\
                        )\}\
                    </div>\
                )\}\
            </section>\
\
\
            \{/* Item Entry Form */\}\
            <section className="w-full max-w-6xl bg-white shadow-lg rounded-xl p-8 mb-8">\
                <h2 className="text-2xl font-bold text-gray-800 mb-6">\{editingItem ? 'Edit Reception Item' : 'Add New Reception Item'\}</h2>\
                <form onSubmit=\{handleAddItem\} className="grid grid-cols-1 md:grid-cols-2 gap-6">\
                    \{/* Item Name */\}\
                    <div>\
                        <label htmlFor="itemName" className="block text-sm font-medium text-gray-700 mb-1">Item Name <span className="text-red-500">*</span></label>\
                        <input\
                            type="text"\
                            id="itemName"\
                            value=\{itemName\}\
                            onChange=\{(e) => setItemName(e.target.value)\}\
                            className=\{inputClass\}\
                            placeholder="e.g., Glucose Reagent"\
                            required\
                        />\
                    </div>\
\
                    \{/* Item Type */\}\
                    <div>\
                        <label htmlFor="itemType" className="block text-sm font-medium text-gray-700 mb-1">Item Type <span className="text-red-500">*</span></label>\
                        <select\
                            id="itemType"\
                            value=\{itemType\}\
                            onChange=\{(e) => setItemType(e.target.value)\}\
                            className=\{inputClass\}\
                            required\
                        >\
                            <option value="">Select Type</option>\
                            <option value="Reagent">Reagent</option>\
                            <option value="Kit">Kit</option>\
                            <option value="Chemical">Chemical</option>\
                            <option value="Consumable">Consumable</option>\
                            <option value="Other">Other</option>\
                        </select>\
                    </div>\
\
                    \{/* Manufacturer */\}\
                    <div>\
                        <label htmlFor="manufacturer" className="block text-sm font-medium text-gray-700 mb-1">Manufacturer</label>\
                        <input\
                            type="text"\
                            id="manufacturer"\
                            value=\{manufacturer\}\
                            onChange=\{(e) => setManufacturer(e.target.value)\}\
                            className=\{inputClass\}\
                            placeholder="e.g., Roche Diagnostics"\
                        />\
                    </div>\
\
                    \{/* Lot Number */\}\
                    <div>\
                        <label htmlFor="lotNumber" className="block text-sm font-medium text-gray-700 mb-1">Lot Number</label>\
                        <input\
                            type="text"\
                            id="lotNumber"\
                            value=\{lotNumber\}\
                            onChange=\{(e) => setLotNumber(e.target.value)\}\
                            className=\{inputClass\}\
                            placeholder="e.g., 123456789"\
                        />\
                    </div>\
\
                    \{/* Expiry Date */\}\
                    <div>\
                        <label htmlFor="expiryDate" className="block text-sm font-medium text-gray-700 mb-1">Expiry Date</label>\
                        <input\
                            type="date"\
                            id="expiryDate"\
                            value=\{expiryDate\}\
                            onChange=\{(e) => setExpiryDate(e.target.value)\}\
                            className=\{inputClass\}\
                        />\
                    </div>\
\
                    \{/* Reception Date */\}\
                    <div>\
                        <label htmlFor="receptionDate" className="block text-sm font-medium text-gray-700 mb-1">Reception Date <span className="text-red-500">*</span></label>\
                        <input\
                            type="date"\
                            id="receptionDate"\
                            value=\{receptionDate\}\
                            onChange=\{(e) => setReceptionDate(e.target.value)\}\
                            className=\{inputClass\}\
                            required\
                        />\
                    </div>\
\
                    \{/* Reception Time */\}\
                    <div>\
                        <label htmlFor="receptionTime" className="block text-sm font-medium text-gray-700 mb-1">Reception Time</label>\
                        <input\
                            type="time"\
                            id="receptionTime"\
                            value=\{receptionTime\}\
                            onChange=\{(e) => setReceptionTime(e.target.value)\}\
                            className=\{inputClass\}\
                        />\
                    </div>\
\
                    \{/* Condition Check */\}\
                    <div>\
                        <label htmlFor="conditionCheck" className="block text-sm font-medium text-gray-700 mb-1">Physical Condition Check <span className="text-red-500">*</span></label>\
                        <select\
                            id="conditionCheck"\
                            value=\{conditionCheck\}\
                            onChange=\{(e) => setConditionCheck(e.target.value)\}\
                            className=\{inputClass\}\
                            required\
                        >\
                            <option value="">Select Condition</option>\
                            <option value="Good">Good</option>\
                            <option value="Damaged">Damaged</option>\
                            <option value="Expired">Expired</option>\
                            <option value="Incorrect">Incorrect Item</option>\
                        </select>\
                    </div>\
\
                    \{/* Performance Criteria */\}\
                    <div className="md:col-span-2">\
                        <label htmlFor="performanceCriteria" className="block text-sm font-medium text-gray-700 mb-1">Performance Criteria (Manufacturer's Specs)</label>\
                        <textarea\
                            id="performanceCriteria"\
                            value=\{performanceCriteria\}\
                            onChange=\{(e) => setPerformanceCriteria(e.target.value)\}\
                            className=\{`$\{inputClass\} h-24`\}\
                            placeholder="e.g., QC values within +/- 2SD, expected linearity, etc."\
                        ></textarea>\
                    </div>\
\
                    \{/* Performance Result */\}\
                    <div>\
                        <label htmlFor="performanceResult" className="block text-sm font-medium text-gray-700 mb-1">Performance Result <span className="text-red-500">*</span></label>\
                        <select\
                            id="performanceResult"\
                            value=\{performanceResult\}\
                            onChange=\{(e) => setPerformanceResult(e.target.value)\}\
                            className=\{inputClass\}\
                            required\
                        >\
                            <option value="">Select Result</option>\
                            <option value="Pass">Pass</option>\
                            <option value="Pending">Pending</option> \{/* Added Pending option */\}\
                            <option value="Fail">Fail</option>\
                        </select>\
                    </div>\
\
                    \{/* Notes */\}\
                    <div className="md:col-span-2">\
                        <label htmlFor="notes" className="block text-sm font-medium text-gray-700 mb-1">Notes</label>\
                        <textarea\
                            id="notes"\
                            value=\{notes\}\
                            onChange=\{(e) => setNotes(e.target.value)\}\
                            className=\{`$\{inputClass\} h-24`\}\
                            placeholder="Any additional observations or comments."\
                        ></textarea>\
                    </div>\
\
                    \{/* User Name */\}\
                    <div>\
                        <label htmlFor="userName" className="block text-sm font-medium text-gray-700 mb-1">User Name</label>\
                        <input\
                            type="text"\
                            id="userName"\
                            value=\{userName\}\
                            onChange=\{(e) => setUserName(e.target.value)\}\
                            className=\{inputClass\}\
                            placeholder="e.g., John Doe"\
                        />\
                    </div>\
\
                    \{/* Performed By */\}\
                    <div>\
                        <label htmlFor="performedBy" className="block text-sm font-medium text-gray-700 mb-1">Performance Test Performed By</label>\
                        <input\
                            type="text"\
                            id="performedBy"\
                            value=\{performedBy\}\
                            onChange=\{(e) => setPerformedBy(e.target.value)\}\
                            className=\{inputClass\}\
                            placeholder="e.g., Jane Smith"\
                        />\
                    </div>\
\
                    \{/* Approved By */\}\
                    <div>\
                        <label htmlFor="approvedBy" className="block text-sm font-medium text-gray-700 mb-1">Approved By</label>\
                        <input\
                            type="text"\
                            id="approvedBy"\
                            value=\{approvedBy\}\
                            onChange=\{(e) => setApprovedBy(e.target.value)\}\
                            className=\{inputClass\}\
                            placeholder="e.g., Dr. Alice Brown"\
                        />\
                    </div>\
\
                    \{/* Received By (Read-only, shows current user ID) */\}\
                    <div>\
                        <label htmlFor="receivedBy" className="block text-sm font-medium text-gray-700 mb-1">Received By (User ID)</label>\
                        <input\
                            type="text"\
                            id="receivedBy"\
                            value=\{receivedBy || userId\}\
                            className=\{`$\{inputClass\} bg-gray-50 text-gray-500`\}\
                            readOnly\
                        />\
                    </div>\
\
\
                    \{/* Form Actions */\}\
                    <div className="md:col-span-2 flex justify-end space-x-4 mt-4">\
                        <button type="button" onClick=\{clearForm\} className=\{secondaryButtonClass\}>\
                            Clear Form\
                        </button>\
                        <button type="submit" className=\{primaryButtonClass\}>\
                            \{editingItem ? (\
                                <>\
                                    <Edit className=\{iconClass\} /> Update Item\
                                </>\
                            ) : (\
                                <>\
                                    <PlusCircle className=\{iconClass\} /> Add Item\
                                </>\
                            )\}\
                        </button>\
                    </div>\
                </form>\
            </section>\
\
            \{/* Filtering and Search Section */\}\
            <section className="w-full max-w-6xl bg-white shadow-lg rounded-xl p-8 mb-8">\
                <h2 className="text-2xl font-bold text-gray-800 mb-6 flex items-center space-x-2">\
                    <Search className=\{iconClass\} /> Filter & Search Items\
                </h2>\
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">\
                    \{/* Search Term */\}\
                    <div>\
                        <label htmlFor="searchTerm" className="block text-sm font-medium text-gray-700 mb-1">Search (Name/Lot No.)</label>\
                        <input\
                            type="text"\
                            id="searchTerm"\
                            value=\{searchTerm\}\
                            onChange=\{(e) => setSearchTerm(e.target.value)\}\
                            className=\{inputClass\}\
                            placeholder="Search by item name or lot number"\
                        />\
                    </div>\
\
                    \{/* Filter by Item Type */\}\
                    <div>\
                        <label htmlFor="filterItemType" className="block text-sm font-medium text-gray-700 mb-1">Filter by Item Type</label>\
                        <select\
                            id="filterItemType"\
                            value=\{filterItemType\}\
                            onChange=\{(e) => setFilterItemType(e.target.value)\}\
                            className=\{inputClass\}\
                        >\
                            <option value="">All Types</option>\
                            <option value="Reagent">Reagent</option>\
                            <option value="Kit">Kit</option>\
                            <option value="Chemical">Chemical</option>\
                            <option value="Consumable">Consumable</option>\
                            <option value="Other">Other</option>\
                        </select>\
                    </div>\
\
                    \{/* Filter by Performance Result */\}\
                    <div>\
                        <label htmlFor="filterPerformanceResult" className="block text-sm font-medium text-gray-700 mb-1">Filter by Performance</label>\
                        <select\
                            id="filterPerformanceResult"\
                            value=\{filterPerformanceResult\}\
                            onChange=\{(e) => setFilterPerformanceResult(e.target.value)\}\
                            className=\{inputClass\}\
                        >\
                            <option value="">All Results</option>\
                            <option value="Pass">Pass</option>\
                            <option value="Pending">Pending</option>\
                            <option value="Fail">Fail</option>\
                        </select>\
                    </div>\
                    \{/* Filter by Manufacturer (text input for partial match) */\}\
                    <div className="md:col-span-3">\
                        <label htmlFor="filterManufacturer" className="block text-sm font-medium text-gray-700 mb-1">Filter by Manufacturer</label>\
                        <input\
                            type="text"\
                            id="filterManufacturer"\
                            value=\{filterManufacturer\}\
                            onChange=\{(e) => setFilterManufacturer(e.target.value)\}\
                            className=\{inputClass\}\
                            placeholder="Enter manufacturer name"\
                        />\
                    </div>\
                </div>\
            </section>\
\
            \{/* Performance Trend Chart */\}\
            <section className="w-full max-w-6xl bg-white shadow-lg rounded-xl p-8 mb-8">\
                <h2 className="text-2xl font-bold text-gray-800 mb-6 flex items-center space-x-2">\
                    <BarChart className=\{iconClass\} /> Performance Trend\
                </h2>\
                <div className="chart-container">\
                    <ResponsiveContainer width="100%" height="100%">\
                        <RechartsBarChart\
                            data=\{performanceChartData()\}\
                            margin=\{\{ top: 5, right: 30, left: 20, bottom: 5 \}\}\
                        >\
                            <CartesianGrid strokeDasharray="3 3" />\
                            <XAxis dataKey="name" />\
                            <YAxis />\
                            <Tooltip />\
                            <Legend />\
                            <Bar dataKey="count" />\
                        </RechartsBarChart>\
                    </ResponsiveContainer>\
                </div>\
            </section>\
\
            \{/* Item List */\}\
            <section className="w-full max-w-6xl bg-white shadow-lg rounded-xl p-8 mb-8">\
                <h2 className="text-2xl font-bold text-gray-800 mb-6">Recorded Reception Items</h2>\
                <div className="table-container">\
                    <table className="w-full border-collapse rounded-lg overflow-hidden">\
                        <thead>\
                            <tr>\
                                <th>Item Name</th><th>Type</th><th>Manufacturer</th><th>Lot No.</th><th>Expiry Date</th><th>Reception Date</th><th>Time</th><th>Condition</th><th>Performance</th><th>User Name</th><th>Performed By</th><th>Approved By</th><th>Received By (ID)</th><th>Created At</th><th>Created By (ID)</th><th>Last Modified At</th><th>Last Modified By (ID)</th><th>Actions</th>\
                            </tr>\
                        </thead>\
                        <tbody>\
                            \{filteredItems.length === 0 ? (\
                                <tr>\
                                    <td colSpan="18" className="text-center py-4 text-gray-500">No items found matching your criteria.</td>\
                                </tr>\
                            ) : (\
                                filteredItems.map(item => (\
                                    <tr key=\{item.id\}>\
                                        <td>\{item.itemName\}</td><td>\{item.itemType\}</td><td>\{item.manufacturer || '-'\}</td><td>\{item.lotNumber || '-'\}</td><td>\{item.expiryDate || '-'\}</td><td>\{item.receptionDate\}</td><td>\{item.receptionTime || '-'\}</td><td>\{item.conditionCheck\}</td><td>\
                                            \{item.performanceResult === 'Pass' ? (\
                                                <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800">\
                                                    <CheckCircle className="w-3 h-3 mr-1" /> Pass\
                                                </span>\
                                            ) : item.performanceResult === 'Fail' ? (\
                                                <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800">\
                                                    <XCircle className="w-3 h-3 mr-1" /> Fail\
                                                </span>\
                                            ) : (\
                                                <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-amber-100 text-amber-800">\
                                                    <Clock className="w-3 h-3 mr-1" /> Pending\
                                                </span>\
                                            )\}\
                                        </td><td>\{item.userName || '-'\}</td><td>\{item.performedBy || '-'\}</td><td>\{item.approvedBy || '-'\}</td><td className="text-sm font-mono break-all">\{item.receivedBy\}</td><td className="text-sm">\{item.createdAt ? new Date(item.createdAt.toDate()).toLocaleString() : '-'\}</td><td className="text-sm font-mono break-all">\{item.createdBy || '-'\}</td><td className="text-sm">\{item.lastModifiedAt ? new Date(item.lastModifiedAt.toDate()).toLocaleString() : '-'\}</td><td className="text-sm font-mono break-all">\{item.lastModifiedBy || '-'\}</td><td className="flex space-x-2">\
                                            <button\
                                                onClick=\{() => handleEdit(item)\}\
                                                className=\{`$\{secondaryButtonClass\} p-2 text-sm`\}\
                                                title="Edit Item"\
                                            >\
                                                <Edit className=\{iconClass\} />\
                                            </button>\
                                            <button\
                                                onClick=\{() => confirmDelete(item)\}\
                                                className=\{`$\{dangerButtonClass\} p-2 text-sm`\}\
                                                title="Delete Item"\
                                            >\
                                                <Trash2 className=\{iconClass\} />\
                                            </button>\
                                        </td>\
                                    </tr>\
                                ))\
                            )\}\
                        </tbody>\
                    </table>\
                </div>\
            </section>\
\
            \{/* Report Generation Section */\}\
            <section className="w-full max-w-6xl bg-white shadow-lg rounded-xl p-8 mb-8">\
                <h2 className="text-2xl font-bold text-gray-800 mb-6 flex items-center space-x-2">\
                    <BarChart className=\{iconClass\} /> Generate Reports\
                </h2>\
                <div className="flex flex-col sm:flex-row items-center space-y-4 sm:space-y-0 sm:space-x-4">\
                    <label htmlFor="reportPeriod" className="block text-sm font-medium text-gray-700">Select Report Period:</label>\
                    <select\
                        id="reportPeriod"\
                        value=\{reportPeriod\}\
                        onChange=\{(e) => setReportPeriod(e.target.value)\}\
                        className=\{inputClass\}\
                    >\
                        <option value="daily">Daily</option>\
                        <option value="weekly">Weekly</option>\
                        <option value="monthly">Monthly</option>\
                        <option value="yearly">Yearly</option>\
                    </select>\
                    <button onClick=\{generateReport\} className=\{primaryButtonClass\}>\
                        <FileText className=\{iconClass\} /> Generate Report\
                    </button>\
                </div>\
            </section>\
\
            \{/* Report Modal */\}\
            \{showReportModal && reportSummary && (\
                <div className="modal-overlay">\
                    <div className="modal-content">\
                        <h3 className="text-2xl font-bold text-gray-800 mb-4">Reception Report (\{reportSummary.period\})</h3>\
                        <p className="text-lg mb-2">Total Items Received: <span className="font-semibold">\{reportSummary.totalItems\}</span></p>\
                        <p className="text-lg mb-2 text-green-700">Items Passed: <span className="font-semibold">\{reportSummary.passedItems\}</span></p>\
                        <p className="text-lg mb-2 text-red-700">Items Failed: <span className="font-semibold">\{reportSummary.failedItems\}</span></p>\
                        <p className="text-lg mb-4 text-amber-700">Items Pending: <span className="font-semibold">\{reportSummary.pendingItems\}</span></p>\
                        <div className="flex justify-end space-x-4">\
                            <button onClick=\{exportReportToCSV\} className=\{primaryButtonClass\}>\
                                <Download className=\{iconClass\} /> Export to CSV\
                            </button>\
                            <button onClick=\{exportReportToPDF\} className=\{primaryButtonClass\}>\
                                <Download className=\{iconClass\} /> Export to PDF\
                            </button>\
                            <button onClick=\{() => setShowReportModal(false)\} className=\{secondaryButtonClass\}>\
                                Close\
                            </button>\
                        </div>\
                    </div>\
                </div>\
            )\}\
\
            \{/* Confirmation Modal for Deletion */\}\
            \{showConfirmModal && itemToDelete && (\
                <div className="modal-overlay">\
                    <div className="modal-content">\
                        <h3 className="text-xl font-bold text-gray-800 mb-4">Confirm Deletion</h3>\
                        <p className="mb-6">Are you sure you want to delete the item: <span className="font-semibold">\{itemToDelete.itemName\}</span> (Lot: \{itemToDelete.lotNumber || 'N/A'\})?</p>\
                        <div className="flex justify-end space-x-4">\
                            <button onClick=\{() => setShowConfirmModal(false)\} className=\{secondaryButtonClass\}>\
                                Cancel\
                            </button>\
                            <button onClick=\{handleDelete\} className=\{dangerButtonClass\}>\
                                <Trash2 className=\{iconClass\} /> Delete\
                            </button>\
                        </div>\
                    </div>\
                </div>\
            )\}\
        </div>\
    );\
\};\
\
export default App;\
}