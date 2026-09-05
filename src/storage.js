/**
 * Backward compatibility shim for Storage
 */
import { StorageService } from './services/storageService.js';

export const Storage = StorageService;
export default StorageService;
